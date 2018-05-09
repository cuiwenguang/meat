
$(function () {
    // 类别和价格关联
    $("#category").change(selCategory);
    $("#price").val($("#category").find("option:selected").data("price"));

    // 根据数量初始化皮重
    var pz = parseInt($("#number").val()) * parseFloat($("#p_weight").data("single"));
    $("#p_weight").val(pz)
    $("#number").blur(changeNumber);

    //根据毛重和皮重计算净重，测试代码，以后回通过传感器自动获取
    var jz = parseFloat($("#m_weight").val()) - parseFloat($("#p_weight").val());
    if(jz<0) jz=0;
    $("#weight").val(jz.toFixed(2));
    $("#m_weight").blur(changeWeight);

    // 绑定表格
    tableBind();

});

var selCategory = function () {
    $("#price").val($(this).find("option:selected").data("price"));
};

var changeNumber = function () {
    if($("#number").val()=="") $("#number").val(1);
    var pz = parseInt($("#number").val()) * parseFloat($("#p_weight").data("single"));
    $("#p_weight").val(pz.toFixed(2));
    changeWeight();
};

var changeWeight = function () {
    var jz = parseFloat($("#m_weight").val()) - parseFloat($("#p_weight").val());
    if (jz < 0) jz=0;
    $("#weight").val(jz.toFixed(2));
};

$("#btnWeight").click(function () {
    $("#seq").val($("#tabDetails").find('tbody tr').length+1);
    $.post("/raw/postcollect", $("#frmCreate").serialize(), function (ret) {
        showMessage(ret);
        if(ret.code==200){
            initForm(ret.data);
            tableBind();
        }
    })
});

$("#btnSave").click(function () {
    if($("#tabDetails").find('tbody tr').length == 0){
        alert('没有任何称重记录，不允许提交');
        return;
    }
    if($("#id_card").val()=="" || $("#cust_name").val()==""){
        alert('交货人信息不完成，生份证和姓名不允许为空');
        return;
    }
    $.post("/raw/submitcollect", $("#frmCreate").serialize(), function (ret) {
        showMessage(ret)
        if (ret.code==200){
            initForm(ret.data);
            tableBind();
        }
    })
});

function tableBind() {
    var id = $("#id").val()
    if(parseInt(id)>0){
        $("#tabDetails").bootstrapTable({
            "url": "/raw/collect/details?id="+id
        });
    }
    $("#tabDetails").bootstrapTable('refresh');
}

function initForm(data) {
    $("#id").val(data.id);
    $("#sg_no").val(data.sg_no);
    $("#sg_datetime").val(data.sg_datetime);
    $("#total_number").val(data.total_number);
    $("#total_weight").val(parseFloat(data.total_weight).toFixed(2));
    $("#total_price").val(parseFloat(data.total_price).toFixed(2));
    if(data.customer){
        $("#id_card").val(data.customer.id_card);
        $("#cust_name").val(data.customer.cust_name);
        $("#mobile").val(data.customer.mobile);
        $("#address").val(data.customer.address);
    } else {
        $("#id_card").val('');
        $("#cust_name").val('');
        $("#mobile").val('');
        $("#address").val('');
    };

}

var tableFormatter = {
    category: function (value) {
        return value.name;
    },
    options: function (value) {
        return '<a onclick="del('+value+')">删除</a>'
    }
};
