/**
 * Created by chenbiren on 2014/10/10.
 */

$(document).ready(function() {
    $Devices.init(function(success, data) {
        if (success == false) {
            location.href = Utils.rootPath() + "/device/error";
        }
        if ($Devices.size < 1) {
            location.href = Utils.rootPath() + "/device/none";
        }
        $("#device_list").html(showDeviceList($DMap));
    });
    $(".show_device_info").html(showLeftDevice($Devices.current));
    $("#alias").live('click', function() {
        console.log("[CLICK]", this);
        $("#alias").hide();
        $("#alias_form input").show();
    });

    $("#alias_form input[type='image']").live('click', setAlias);

    $("#device_list ul li").live('click', function() {
        var deviceId = $(this).attr('name');
        $Devices.current = $DMap[deviceId];
        $(this).addClass("selected").siblings().removeClass("selected");
        $("#content_menu ul li a").removeClass("selected");
        $("#content_menu ul li a:first").addClass("selected");
        $(".show_device_info").html(showLeftDevice($Devices.current));
    });

    $("#content_menu ul li a").live('click', function() {
        var index = $(this).parent().index();
        $("#content_menu ul li a").removeClass("selected");
        $(this).addClass("selected");
        if (index == 0) {
            $(".show_device_info").html(showLeftDevice($Devices.current));
        }else if (index == 2) {
            $(".show_device_info").html(showMidDevice($Devices.current));
        }else if (index == 4) {
            $(".show_device_info").html(showRightDevice($Devices.current));
        }
    });
});

function setAlias() {
    //forbid submit
    $("ui").submit(function() {return false});
    console.log("[CLICK]", this);
    var alias = $("#alias_form input[type='text']").val();
    ajaxSetAlias($Devices.current['deviceId'], alias, function(success, data) {
        if (success == false) {
            alert("can not set alias");
        } else {
            $Devices.current['alias'] = alias;
            $("#device_list").html(showDeviceList($DMap));
            $(".show_device_info").html(showLeftDevice($Devices.current));
            $("#alias_form input[type='image']").on('click', setAlias);
        }
    })
}