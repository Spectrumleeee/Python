/**
 * Created by chenbiren on 2014/10/9.
 */
var allow_show = {
    'deviceType': "设备类别",
    'deviceModel': "设备型号",
    'fwVer': "固件版本",
    'deviceHwVer': '设备版本'
};

function showDeviceList(devices) {
    var ul = $("<ul></ul>");
    for (var k in devices) {
        var li = $("<li></li>");
        var device = devices[k];
        li.attr('name', k);
        if (device['online'] == true) {
            li.addClass("online");
        }
        if (k == $Devices.current['deviceId']) {
            li.addClass("selected");
        }
        var deviceName = device['deviceName'];
        if (device['alias']) {
            deviceName = device['alias'];
        }
        li.html(deviceName + "<b>> </b>");
        ul.append(li);
    }

    return ul;
}

function showLeftDevice(device) {
    var productDetail = html.div().addClass("productDetail").append(showAliasForm(device));
    for (var k in allow_show) {
        productDetail.append(html.p(allow_show[k] + "：" + device[k]));
    }
    return productDetail;
}

function showMidDevice(device) {
    var div1 = html.div().addClass("setupContent");
    div1.append(html.img('update-5.png'));
    div1.append(html.p('请输入账户密码删除设备').addClass("_p1"));
    div1.append(html.p('删除设备后，你将不能通过云服务对设备进行管理').addClass("_p2"));
    div1.append(html.p('重新添加设备，需要进入设备重新输入云账号进行再次绑定').addClass("_p2"));
    var input = html.input('password').attr('style', "color: rgb(156, 159, 172);")
                                      .addClass("password setupInput");
    var div2 = html.div().addClass("passwordInput").append(input);
    var div3 = html.div().addClass("setupBtns");
    div3.append(html.a().addClass("cancle").html("取消"));
    div3.append(html.a().html("删除设备"));
    return div1.append(div2).append(div3);
}

function showRightDevice(device) {
    return "";
}

function showAliasForm(device) {
    var a = html.a().attr("id", "alias").html(device['alias']);
    var label = html.label().html("设备别名：").append(a);
    var input = html.input('text').attr('style', "display:none;height:17px");
    var image = html.input('image').attr('style', "display: none;height: 19px")
                                   .attr('src', Utils.rootPath() + "/images/edit.png");
    return html.form().attr("id", "alias_form").append(label, input, image);
}

var html = {
    div: function() {
        return $("<div></div>");
    },
    img: function(name) {
        return $("<img alt>").attr('src', Utils.rootPath() + "/images/" + name);
    },
    p: function(data) {
        return $("<p></p>").html(data);
    },
    a: function() {
        return $('<a href="#"></a>');
    },
    form: function() {
        return $("<ui></ui>")
    },
    input: function(type) {
        return $("<input/>").attr('type', type);
    },
    label: function() {
        return $("<label></label>")
    }
};
