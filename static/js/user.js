$(function () {
    $("#tableUser").bootstrapTable({
        "url": "/system/getusers",
        "pagination": true,
        "pageList": [10, 15, 20, 25, 30],
    });
    validate();
    $("#btnSave").click(save);
});

function showEdit(id) {
    if(id>0){
        $("#id").val(id);
        $.post("/system/user/edit", $("#frmUser").serialize(), function (ret) {
            if (ret.code == 200) {
                var user = ret.data;
                console.log(user[0].username);
                $("#username").val(user[0].username);
                $("#email").val(user[0].email);
                $("#start-psd").css("display","none");
                $("#first_name").val(user[0].first_name)
            }
        }, "json");
    }else {
        $("#id").val(id)
        $("#username").val("");
        $("#first_name").val("");
        $("#password").val("");
        $("#email").val("");
        $("#start-psd").css("display","block");
        $("#group").val("1");

    }
    $("#frmCreate").modal();
}

var save = function() {
    $("#frmUser").bootstrapValidator('validate');
    if($("#frmUser").data('bootstrapValidator').isValid()){
       $.post('/system/user/create', $("#frmUser").serialize(), function (res) {
           if (res.code == 200){
               $("#tableUser").bootstrapTable('refresh');
               window.location.href = '/system/user'
           }
           if(res.code == 300){
               $("#tableUser").bootstrapTable("refresh");
               window.location.href = '/system/user'
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
                $("#tableUser").bootstrapTable("refresh");
            }
        }
    });
}

function validate() {
    $("#frmUser").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields: {
            username: {
                message: "输入的信息不正确",
                validators: {
                    notEmpty: {
                        message: "工号不能为空"
                    }
                }
            },
            email: {
                message: "输入的信息不正确",
                validators: {
                    message: "邮箱输入不正确",
                    notEmpty: {
                        message: "邮箱不能为空"
                    },
                    emailAddress: {
                        message: "邮箱格式不正确"
                    }
                }
            },
            password: {
                message: "输入的信息不正确",
                validators: {
                    message: "密码错误",
                    notEmpty: {
                        message: "密码不能为空"
                    }
                }
            }
        }
    });
}

var fmt = {
    optFormatter: function (value) {
        html = "<a href='javascript:showEdit("+value+")'> 编辑 </a>" +
            "<a href='javascript:delUser("+value+")'> 删除 </a>";
        return html;
    }
}