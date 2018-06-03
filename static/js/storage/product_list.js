$(function () {
    $("#productTable").bootstrapTable({
        "url": "/storage/getproducts",
        "checkbox": true
    });
    $("#btnEdit").click(function () {
        $("#frmCreate").modal({});
    });
});

function showEdit(id) {
    if (id == 0) {
        return false;
    } else {
        $("#id").val(id);
        $.post("/storage/showproduct", $("#frmProduct").serialize(), function (ret) {
            if (ret.code == 200) {
                $("#code").val(ret.data.code),
                    $("#name").val(ret.data.name),
                    $("#standard").val(ret.data.standard),
                    $("#packing").val(ret.data.packing),
                    $("#price").val(ret.data.price),
                    $("#remark").val(ret.data.remark)
            }
        }, "json");
        $("#frmCreate").modal({});
    }
}


$(function () {
    $("#frmProduct").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {
            /*input状态样式图片*/
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excuded: "disabled",

        fields: {
            'code': {
                message: "编号输入不正确",
                validators: {
                    notEmpty: {
                        message: "编号不能为空"
                    },
                    stringLength: {
                        min: 4,
                        max: 4,
                        message: '编号长度为4'
                    },
                    regexp: {
                        regexp: /^[0-9]+$/,
                        message: '请输入数字..'
                    }
                },
            },
            name: {
                validators: {
                    notEmpty: {
                        message: '名称不能为空'
                    },
                    // threshold: 2, //有6字符以上才发送ajax请求，（input中输入一个字符，插件会向服务器发送一次，设置限制，6字符以上才开始）
                    // remote: {//ajax验证。server result:{"valid",true or false} 向服务发送当前input name值，获得一个json数据。例表示正确：{"valid",true}
                    //     url: '/storage/cheekdata',//验证地址
                    //     message: '名称已存在',//提示消息
                    //     delay: 2000,//每输入一个字符，就发ajax请求，服务器压力还是太大，设置2秒发送一次ajax（默认输入一个字符，提交一次，服务器压力太大）
                    //     type: 'get',//请求方式
                    //     // 自定义提交数据，默认值提交当前input value
                    //     data: function (validator) {
                    //         return {
                    //             name: $('[name="name"]').val(),
                    //         }
                    //     },
                    // }
                }
            },
            'standard': {
                validators: {
                    notEmpty: {
                        message: "规格不能为空"
                    }
                }
            },
            'packing': {
                validators: {
                    notEmpty: {
                        message: "包装不能为空"
                    }
                }
            },
            'price': {
                validators: {
                    notEmpty: {
                        message: "价格不能为空"
                    }
                }
            },

        }
    });
})

$("#btnSave").click(function () {
    $("#frmProduct").bootstrapValidator('validate');
    if ($("#frmProduct").data('bootstrapValidator').isValid()) {
        $.post("/storage/postproduct", $("#frmProduct").serialize(), function (ret) {
            if (ret.code == 200) {
                $(".productTable").bootstrapTable("refresh");
                window.location.href = "/storage/product/list"
            }
            if (ret.code == 300) {
                $(".productTable").bootstrapTable("refresh");
                window.location.href = "/storage/product/list"
            }
        }, "json");
    }
});

function delProduct(id) {
    data = {"id": id}
    $.ajax({
        url: "/storage/delproduct",
        method: "get",
        async: false,
        data: data,
        success: function (res) {
            if (res.code == 200) {
                window.location.href = "/storage/product/list"
            }
        }
    });
}

var formatter = {
    optFormatter: function (value) {
        html = $('#rowButtons').tmpl({id:value}).prop("outerHTML");
        return html;
    }
}