$(function () {
    $("#tableUser").bootstrapTable({
        "url": "/system/getusers"
    });
    validate();
    $("#btnSave").click(save);
});

function showEdit(id) {
    if(id>0){
        //
    }
    $("#frmCreate").modal();
}

var save = function() {
    $("#frmUser").bootstrapValidator('validate');
    if($("#frmUser").data('bootstrapValidator').isValid()){
       $.post('', $("#frmUser").serialize(), function (res) {
           if (res.code == 200){
               $("#tableUser").bootstrapTable('refresh');
           }
       });
    }
}

function validate() {
    $("#frmCreate").bootstrapValidator({
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