$(function () {
    $("#configForm").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields:{
            'unit_of_weight': {
                message: "重量计量单位输入不正确",
                validators: {
                    notEmpty: {
                        message: "重量计量单位不能为空"
                    }
                }
            },

            'unit_of_number': {
                message: "数量计量单位输入不正确",
                validators: {
                    notEmpty: {
                        message: "数量计量单位不能为空"
                    }
                }
            },
            'default_tare': {
                message: "酮体默认皮重输入值不正确",
                validators: {
                    notEmpty: {
                        message: "酮体默认皮重不能为空"
                    },
                    numeric: {
                        message: "酮体默认皮重只能输入整数"
                    }
                }
            },
            'default_number': {
                message: "酮体默认每次可称重数量输入值不正确",
                validators: {
                    notEmpty: {
                        message: "酮体默认每次可称重数量不能为空"
                    },
                    digits: {
                        message: "酮体默认每次可称重数量只能输入整数"
                    }
                }
            }
        }
    });
});

$("#btnSave").click(function () {
    $("#configForm").bootstrapValidator('validate');
    if ($("#configForm").data('bootstrapValidator').isValid()) {
        $.post("/raw/postonfig",
            $("#configForm").serialize(),
            function (data) {
                $("#alertContainer").html('');
                if(data.code == 200){
                    $('<div class="alert alert-success" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                    $("#configForm").data('bootstrapValidator').resetForm();
                } else {
                    $('<div class="alert alert-warning" role="alert">' +
                        '<strong>'+data.message+'</strong>' +
                    '</div>').appendTo("#alertContainer").show(300).delay(1000).hide(300);
                }
            });
    }
})