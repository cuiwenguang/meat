$(function () {
    $("#productTable").bootstrapTable({
        "url": "/storage/getproducts",
        "checkbox": true,
        "pageList": [10, 15, 20, 25, 30],
        "pagination": true,
    });
    $("#btnEdit").click(function () {
        $("#frmCreate").modal({});
    });
});

function showEdit(id) {
    if (id == 0) {
        $("#code").val(""),
        $("#name").val(""),
            $("#standard").val(""),
            $("#packing").val(""),
            $("#price").val(""),
            $("#remark").val("")

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
                    },
                    threshold: 8,

                    remote: {//例表示正确：{"valid",true}
                        url: '/storage/product/cheek/code',//验证地址
                        data: {"code": $('#code').val()}
                    }, message: '产品编号已被注册',//提示消息
                    delay: 2000,
                    type: 'POST'

                },
                name: {
                    validators: {
                        notEmpty: {
                            message: '名称不能为空'
                        },
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
        }
    });
});

// $("#code").keyup(function () {
//     if ($("#code").val().length == 4) {
//         $.get("/storage/product/cheek/code?code=" + $("#code").val(), function (res) {
//             if (res.code == 200) {
//                 alert(res.mess);
//             }
//         });
//     }
// });

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


$("#printBarCode").click(function () {
    $("#bar-code").html("")
    $.ajax({
        url: "/storage/product/getcode",
        success: function (res) {
            if (res.code == 200) {
                var list =res.data;
                for (var i=0;i<list.length;i++){
                    console.log(list[i].name)
                    html = "<div class=\"bar-code\" style=\"width: 170px;text-align: center;float:left;\">\n" +
                        "                        <img style=\"width: 160px;height: 60px;\" src=\"../../../static/barcode/69012345"+list[i].code+".png\">\n" +
                        "                        <p style='font-size: 12px'>产品编号："+list[i].code+"</p>\n" +
                        "                        <p style='font-size: 12px'>产品名："+list[i].name+"</p>\n" +
                        "                    </div>";
                    $("#bar-code").append(html)
                }
                $("#frmPrint").modal()
            }
        }
    });
})

$("#btnPrint").click(function () {

    document.body.innerHTML = document.getElementById('print-block').innerHTML;
    window.print();
    window.location.href = '/storage/product/list'
})


$("#toggleView").click(function () {
    html = "<tr><td>编号</td><td>名称</td><td>条码</td></tr>"
    $("#thead").html(html);
    $("#tbody").html("");

    $.ajax({
        url: "/storage/product/getcode",
        success: function (res) {
            if (res.code == 200) {
                var list =res.data;
                for (var i=0;i<list.length;i++){
                    message = "<tr><td>"+list[i].code+"</td><td>"+list[i].name+"</td><td>" +
                        "<img style='width: 160px;height: 60px' src='../../../static/barcode/69012345"+list[i].code+".png'>" +
                        "</td></tr>"
                    $("#tbody").append(message)
                }

            }
        }
    });
});


$("#dataView").click(function () {
    window.location.href="/storage/product/list"
})