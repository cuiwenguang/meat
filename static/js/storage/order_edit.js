$(function () {
    initCusotmerInput();
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
    $("#btnAddDetail").click(function () {
       $.post("/storage/postorder", $("#formOrder").serialize(), function (res) {
           if(res.code==200){
               initForm(res.data);
               tableBind();
           }
       })
    });
    $("#product").change(computeMoney);
    $("#number").keyup(computeMoney);
    tableBind();
}

function initForm(form) {
    $("#id").val(form.id);
    $("#customer").val(form.customer.customer_name);
    $("#create_at").val(form.create_at);
    $("#hand_user").val(form.hand_user);
    $("#money").val(form.money);
    $("#remark").val(form.remark);
}

function tableBind() {
    var id = $("#id").val();
    $("#tableDetail").bootstrapTable({
        "url": "/storage/order/details?id="+id
    });
}

var computeMoney = function () {
    var number = parseInt($("#number").val());
    if($("#number").val() == "") number = 0;
    var money = parseFloat($("#product").find("option:selected").data("price")) * number;
    money = parseFloat($("#money").data("value")) + money;
    $("#money").val(money.toFixed(2));
}

var fmt = {
    codeFormatter: function (value) {return value.code;},
    nameFormatter: function (value) {return value.name;},
    standardFormatter: function (value) {return value.standard;},
    priceFormatter: function (value) {return value.price;},
    optFormatter: function (value) {
        html = "<a>删除</a>"
        return html;
    }
}