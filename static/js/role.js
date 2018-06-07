$(function () {
    $("#tableUser").bootstrapTable({
        "url": "/system/role/getrole",
        "pagination": true,
        "pageList": [10, 15, 20, 25, 30],
    });
    validate();
    $("#btnSave").click(save);
});

function showEdit(id) {
    if (id > 0) {
        $("#id").val(id);
        var name = $("#name").val()
        $.ajax({
            url: "/system/role/edit",
            method: "get",
            data: {id: id,name:name},
            success: function (res) {
                if (res.code == 200) {
                    $("#name").val(res.data)
                }
            }
        });
    }else {
        $("#id").val(id)
        $("#name").val("")
    }
    $("#frmCreate").modal();
}

var save = function() {
    $("#frmRole").bootstrapValidator('validate');
    if($("#frmRole").data('bootstrapValidator').isValid()){
       $.post('/system/role/create', $("#frmRole").serialize(), function (res) {
           if (res.code == 200){
               $("#frmRole").bootstrapTable('refresh');
               window.location.href = '/system/role'
           }
           if(res.code == 300){
               $("#frmRole").bootstrapTable("refresh");
               window.location.href = '/system/role'
           }
       },"json");
    }
}

function delUser(id){
    alert(id)
     $.ajax({
        url: "/system/role/delete",
        method: "get",
        data:{id:id},
        success: function (res) {
            if (res.code == 200) {
                $("#frmRole").bootstrapTable("refresh");
                window.location.href = '/system/role'
            }
        }
    });
}

function validate() {
    $("#frmRole").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields: {
            name: {
                message: "输入的信息不正确",
                validators: {
                    notEmpty: {
                        message: "角色不能为空"
                    }
                }
            }
        }
    });
}

var fmt = {
    optFormatter: function (value) {
        html = "<a href='javascript:showEdit("+value+")'> 编辑 </a>" +
            "<a href='javascript:delUser("+value+")'> 删除 </a>" +
        "<a href='/system/power/resp?id="+value+"'> 权限分配 </a>";
        return html;
    }
}