$(function () {
    initCusotmerInput();
    validateForm();
    $("#btnAddDetail").click(function () {
        $.post("/storage/postorder", $("#formOrder").serialize(), function (res) {
            if (res.code == 200) {
                initForm(res.data);
                tableBind(true);
                showMessage(res);
            }
        })
    });
    $("#btnSave").click(function () {
        if ($("#tableDetail").find('tbody tr').length == 0) {
            showMessage({code: 403, message: "没有任何出库信息，不允许提交"})
            return;
        }
        $("#formOrder").bootstrapValidator('validate');
        if ($("#formOrder").data('bootstrapValidator').isValid()) {
            $("#state").val(1);
            $.post("/storage/postorder", $("#formOrder").serialize(), function (res) {
                if (res.code == 200) {
                    clearForm();
                    $("#tableDetail").bootstrapTable('removeAll');
                    showMessage(res);
                }
            })
        }
    });
    $("#product").change(computeMoney);
    $("#number").keyup(computeMoney);
    tableBind(false);
});


function initCusotmerInput() {
    $("#customer").typeahead({
        minLength: 0,
        showHintOnFocus: true,
        fitToElement: true,
        items: 5,
        source: function (query, process) {
            var param = {query: query}
            $.get("/storage/customer/search", param, function (res) {
                process(res.data);
            });
        },
        autoSelect: true
    });
}

function validateForm() {
    $("#formOrder").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {
            /*input状态样式图片*/
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excuded: "disabled",
        fields: {
            'customer': {
                message: "客户信息输入不正确",
                validators: {
                    notEmpty: {
                        message: "客户信息不能为空"
                    }
                }
            },

            'create_at': {
                message: "时间格式不正确",
                validators: {
                    notEmpty: {
                        message: "数量计量单位不能为空"
                    },
                    date: {
                        format: 'YYYY-MM-DD hh:mm:ss',
                        message: '日期格式不正确'
                    }
                }
            },
            'money': {
                message: "金额输入值不正确",
                validators: {
                    notEmpty: {
                        message: "金额不能为空"
                    },
                    numeric: {
                        message: "金额只能输入整数"
                    }
                }
            },
            'number':{
                validators:{
                    notEmpty:{
                        message:"数量不能为空"
                    },
                    between:{
                        message:"数量不能为0",
                        min:1,
                        max:Number.MAX_VALUE,
                    },
                    remote:{
                        url: "../check/number",
                        data: {'product': function () {
                                return $("#product").val();
                            }, 'number': $("#number").val()},
                        message: "所选数量大于库存",
                        delay: 2000,
                        type: 'POST'
                    }
                }
            }
        }
    });
}


function initForm(form) {
    $("#id").val(form.id);
    $("#customer").val(form.customer.customer_name);
    $("#create_at").val(form.create_at);
    $("#hand_user").val(form.hand_user);
    $("#money").val(form.money);
    $("#remark").val(form.remark);
}
function clearForm() {
    $("#id").val(0);
    $("#customer").val("");
    $("#hand_user").val("");
    $("#money").val(0);
    $("#state").val(0);
    $("#remark").val('');
}

function tableBind(isPostBack) {
    var id = $("#id").val();
    $("#tableDetail").bootstrapTable({
            "url": "/storage/order/details"
        });
    if(isPostBack) {
        queryParams = {id: id};
        $("#tableDetail").bootstrapTable('refreshOptions', {
            queryParams: queryParams,
            ajaxOptions: {traditional: true}
        });
    }
}

var computeMoney = function () {
    var number = parseInt($("#number").val());
    if ($("#number").val() == "") number = 0;
    var money = parseFloat($("#product").find("option:selected").data("price")) * number;
    money = parseFloat($("#money").data("value")) + money;
    $("#money").val(money.toFixed(2));
}

var fmt = {
    codeFormatter: function (value) {
        return value.code;
    },
    nameFormatter: function (value) {
        return value.name;
    },
    standardFormatter: function (value) {
        return value.standard;
    },
    priceFormatter: function (value) {
        return value.price;
    },
    optFormatter: function (value) {
        html = "<a>删除</a>"
        return html;
    }
}