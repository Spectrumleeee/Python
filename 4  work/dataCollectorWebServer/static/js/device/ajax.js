/**
 * Created by chenbiren on 2014/9/26.
 */

var $Devices = {
    init : ajaxGetDevices
};
//DMap == Device Map
var $DMap = {

};

function ajaxGetDevices(func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/info",
        contentType: "application/x-www-ui-urlencoded",
        async: false,
        dataType: "json",
        error: function (data) {
            $Devices['success'] = false;
            console.log("[ERROR] GetDevices", data);
        },
        success: function (data) {
            if (data['success'] != true) {
                $Devices['success'] = false;
                $Devices['errorMsg'] = data['errorMsg'];
            } else {
                $Devices['success'] = true;
                $Devices['size'] = data['deviceList'].length;
                if ($Devices['size'] > 0) {
                    $Devices['current'] = data['deviceList'][0];
                }
                for (var id in data["deviceList"]) {
                    var device = data['deviceList'][id];
                    var deviceId = device['deviceId'];
                    $DMap[deviceId] = device;
                }
            }

            func(data['success'], data['deviceList']);
        }
    });
}

function ajaxSetAlias(deviceId, alias, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/setAlias",
        data:{deviceId: deviceId, alias: alias},
        dataType: "json",
        error: function(data) {
            console.log("[ERROR] SetAlias", data);
        },
        success: function(data) {
            func(data['success'], data);
        }
    });
}

function ajaxGetFwList(fwId, hwId, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/getFwList",
        data:{fwId: fwId, hwId: hwId},
        dataType: "json",
        error: function(data) {
            console.log("[ERROR] GetFwList", data);
        },
        success: function(data) {
            func(data["success"], data);
        }
    });
}

function ajaxUnbindDevice(deviceId, cloudPassword, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/unbindDevice",
        data: {deviceId: deviceId, cloudPassword: cloudPassword},
        dataType: 'json',
        error: function(data) {
            console.log("[ERROR] UnbindDevice", data);
        },
        success: function(data) {
            func(data['success'], data);
        }
    });
}

function ajaxUpdateFw(deviceId, fwId, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/updateFw",
        data: {deviceId: deviceId, fwId: fwId},
        dataType: "json",
        error: function(data) {
            console.log("[ERROR] UpdataFw", data);
        },
        success: function(data) {
            func(data['success'], data);
        }
    });
}

function ajaxGetFwDownloadProgress(deviceId, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/getFwDownloadProgress",
        data: {deviceId: deviceId},
        dataType: "json",
        error: function(data) {
            console.log("[ERROR] GetFwDownloadProgress", data);
        },
        success: function(data) {
            func(data["success"], data);
        }
    });
}

function ajaxPassthrough(deviceId, requestData, func) {
    $.ajax({
        type: "POST",
        url: Utils.rootPath() + "/device/passthrough",
        data:{deviceId: deviceId, requestData: requestData},
        dataType: "json",
        error: function(data) {
            console.log("[ERROR] Passthrough", data);
        },
        success: function(data) {
            func(data['success'], data);
        }
    });
}

