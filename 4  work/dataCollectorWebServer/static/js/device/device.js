/**
 * Created by chenbiren on 2014/9/4.
 */
var Global = {};
var showInfo = {
    'alias': "设备别名",
    'deviceType': "设备类别",
    'deviceModel': "设备型号",
    'deviceHwVer': '设备版本'
};
var Dev = {
    getDevicesInfo: function (_url, _data) {
        var result = {};
        $.ajax({
            type: "POST",
            url: Utils.rootPath() + "/" + _url,
            contentType: "application/x-www-ui-urlencoded",
            data: _data,
            async: false,
            dataType: "json",
            error: function (data) {
                result['success'] = false;
                result['errorCode'] = 0;
                result['errorMsg'] = "Can not send ajax request.";
            },
            success: function (data) {
                if (data['success'] != true) {
                    result = data;
                    return;
                }
                result['success'] = true;
                result['map'] = {};
                for (var i = 0; i < data['deviceList'].length; i++) {
                    var device = data['deviceList'][i];
                    result['map'][device['deviceId']] = device;
                }
            }
        });
        Global['devices'] = result['map'];
        Global['success'] = true;
        return result;
    },

    showDeviceList : function(deviceMap) {
        var ul = $("<ul></ul>");
        for (var k in deviceMap) {
            var li = $("<li></li>");
            var device = deviceMap[k];
            li.attr('name', k);
            if (device['online'] == true) {
                li.addClass("online");
            }
            var deviceName = device['deviceName'];
            if (device['alias']) {
                deviceName = device['alias'];
            }
            li.html(deviceName + "<b>> </b>");
            ul.append(li);
        }

        return ul;
    },

    showDeviceInfo : function(device) {
        var titleDiv = $("<div><p>设备的基本信息</p></div>").addClass('show_device_title');
        var detailDiv = $("<div></div>").addClass("productDetail");
        var img = this.createImg("product.png");
        var imageDiv = $("<div></div>").append(img).addClass('productImage');
        var infoDiv = $("<div></div>").append(imageDiv);
        console.log(JSON.stringify(device));
        for (var k in showInfo) {
            var p = $("<p></p>");
            console.log("[info]" + " " + k + " " +device[k]);
            p.html(showInfo[k] + ": " + device[k]);
            detailDiv.append(p);
        }
        infoDiv.append(detailDiv).addClass('show_device_info');
        $(".operation label").html();
        if (device['online'] == true) {
            $("#getFwList").show();
            return titleDiv.add(infoDiv).add(this.getOnlineInfo(device));
        }
        $("#getFwList").hide();
        return titleDiv.add(infoDiv).add(this.getOfflineInfo(device));
    },

    setAlias : function(_deviceId, _alias) {
        var params = {deviceId: _deviceId, alias: _alias};
        var result = Ajax.ajaxDevice("device/setAlias", params);
        return result;
    },

    getOnlineInfo : function(device) {
        var div = $('<div></div>').addClass("online_info");

        function getLanInfo(lanInfo, wanInfo) {
            var lantr = "<tr><td width='110' height='34'>{0}</td><td width='116'>{1}</td></tr>";
            var lantable = $("<table width='226' border='0' cellspacing='0' cellpadding='0'></table>");
            var lanDiv = $("<div></div>").addClass("lan_info");
            lantable.append($(lantr.format(['WAN IP:', wanInfo['wanIp']])));
            lantable.append($(lantr.format(['LAN IP:', lanInfo['lanIp']])));
            lantable.append($(lantr.format(['WAN MASK:', wanInfo['wanMask']])));
            lanDiv.append(Dev.createImg("lan.png").addClass("tb")).append(lantable);
            return lanDiv;
        }

        function getWifiInfo(wifiInfo) {
            var wifitr = "<tr><td width='104' height='50'>Wifi {0}G: </td>" +
                "<td width='118'><a href='#'><img src='" + Utils.rootPath() + "/images/{1}" +"' alt></a></td>" +
                "<td width='135'>名称：{2}</td>" +
                "<td width='55'><a href='#'><img src='" + Utils.rootPath() + "/images/edit.png" +"' alt></a></td></tr>";
            var wifitable = $("<table width='412' border='0' cellspacing='0' cellpadding='0'></table>");
            var wifiDiv = $("<div></div>").addClass("wifi_info");
            wifitable.append($(wifitr.format(['2.4','btn-on.png','SSID-2.4G'])));
            wifitable.append($(wifitr.format(['5.0','btn-off.png','SSID-5.0G'])));
            wifiDiv.append(Dev.createImg("wifi.png").addClass("tb")).append(wifitable);
            return wifiDiv;
        }
        //TODO show the info of lan, wan and wifi
        div.append(getLanInfo(device['lanInfo'], device['wanInfo'])).append(getWifiInfo(device['wifiBasic']));
        return div;
    },

    getOfflineInfo : function(device) {
        var div = $('<div></div>').addClass("offline_info");
        var offlineDiv = $("<div></div>").addClass("not_online");
        offlineDiv.append(this.createImg("update-1.png"));
        offlineDiv.append($("<p></p>").html("亲，你的设备不在线哦！"))
        return div.append(offlineDiv);
    },

    createImg : function(img) {
        return $("<img alt>").attr('src', Utils.rootPath() + "/images/" + img);
    },

    startInterval : function(updateTime) {
        var interval;
        var falseCount = 0, maxFalseCount = 20;
        $(".operation label").first().html("软件预计升级时间：" + updateTime + "s");
        interval = setInterval(function() {
            var result = Ajax.ajaxDevice("device/getFwDownloadProgress", {
                deviceId: $('.selected').attr('name')
            });
            if (result['success'] == true) {
                var progress = result['progress'];
                $(".operation label").eq(1).html("下载进度：" + progress + "%");
                if (progress > 99) {
                    clearInterval(interval);
                    location.href = Utils.rootPath() + "/device/index";
                }
            } else {
                falseCount++;
                if (falseCount > maxFalseCount) {
                    $(".operation label").eq(1).html("下载失败");
                    clearInterval(interval);
                }
            }

        }, 1000);
    }
};

var Ajax = {
    ajaxDevice : function (_url, _params) {
        var result = {};
        var params = {};

        $.ajax({
            type : "POST",
            url : Utils.rootPath() + "/" + _url,
            data : _params,
            contentType : "application/x-www-ui-urlencoded",
            dataType :"json",
            async: false,
            error : function(data) {
                result['success'] = false;
                result['errorCode'] = 0;
                result['errorMsg'] = "Can not send ajax request.";
            },
            success : function(data) {
                result = data;
            }
        });
        console.log(JSON.stringify(result));
        return result;
    }
};

var Dialog = {
    setAlias : function() {
        var selector = $("#dialog-setAlias");
        var buttons = {
            "确定修改" : function() {
                var alias = $("#alias").val();
                var deviceId = $("#device_list ul li.selected").attr('name');
                var result = Dev.setAlias(deviceId, alias);
                if (result.success == true) {
                    var devices = Global['devices'];
                    devices[deviceId]['alias'] = alias;
                    $("#device_info").html(Dev.showDeviceInfo(devices[deviceId]));
                    $(".selected").html(alias + "<b>> </b>")
                }
                selector.dialog("close");
            },
            "取消": function() {
                selector.dialog("close");
            }
        };
        return cg_dialog(selector, buttons);
    },
    getFwList : function() {
        var selector = $("#dialog-getFwList");
        var buttons = {
            "取消": function() {
                selector.dialog("close");
            }
        };
        var dialog = cg_dialog(selector, buttons);
        selector.bind('dialogopen', function() {
            var device= Global['devices'][$(".selected").attr('name')];
            console.log(JSON.stringify(device));
            var result = Ajax.ajaxDevice("device/getFwList",{
                hwId: device['hwId'],
                fwId: device['fwId']
            });
            console.log(result);
            if (result.success == true) {
                if (result['fwList'].length == 0) {
                    selector.dialog("option", "buttons", [
                        {text: "取消", click: function () {
                            selector.dialog("close");
                        }}
                    ]);
                    selector.html($("<p></p>").html("你的固件版本已经是最新，不用更新！"));
                } else {
                    selector.dialog("option", "buttons", [{
                            text:"更新",
                            click: function() {
                                var device= Global['devices'][$(".selected").attr('name')];
                                var result = Ajax.ajaxDevice("device/updateFw",{
                                    deviceId: device['deviceId'],
                                    fwId: device['fwId']
                                });
                                if (result.success == true) {
                                    Dev.startInterval(result['updateTime']);
                                } else {
                                    alert(result['errorMsg']);
                                }
                                selector.dialog("close");
                            }
                        },
                        {
                            text: "取消",
                            click:function() {
                                selector.dialog("close");
                            }
                        }
                    ]);
                    var fwInfo = $("<div></div>");
                    var fwShowInfo = "Version: {0}, Date: {1}, Log: {2}";
                    for (var i = 0; i < result['fwList'].length; i++) {
                        var fw = result['fwList'][i];
                        fwInfo.append($("<p></p>").html(fwShowInfo.format([fw['fwVer'], fw['fwReleaseDate'], fw['fwReleaseLog']])));
                        fwInfo.append($("<br/>"))
                    }
                    selector.html(fwInfo);
                }
            } else {
                selector.dialog("option", "buttons", [{text: "取消", click:function() {
                    selector.dialog("close");
                }}]);
                selector.html($("<p></p>").html("网络连接出现问题，请稍后再试！"));
            }
        });
        return dialog;
    },
    unbindDevice : function() {
        var selector = $("#dialog-unbindDevice");
        var buttons = {
            "确定删除" : function() {
                var result = Ajax.ajaxDevice("device/unbindDevice",
                    {
                        cloudPassword:$("input#cloudPassword").val(),
                        deviceId: $(".selected").attr("name")
                    });
                if (result.success == true) {
                    location.href = Utils.rootPath() + "/" + "device/index";
                    selector.dialog("close");
                } else {
                    alert(result['errorMsg']);
                    selector.dialog("close");
                }
            },
            "取消": function() {
                selector.dialog("close");
            }
        };
        return cg_dialog(selector, buttons);
    }
};

var cg_dialog = function(selector, buttons) {
    return selector.dialog({
        autoOpen : false,
        modal: true,
        buttons: buttons,
        close: function() {console.log(selector.attr('id') + " Dialog Closed.")}
    });
};