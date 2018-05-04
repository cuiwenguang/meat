$(function () {
    $("#category").change(selCategory);
    $("#price").val($("#category").find("option:selected").data("price"));
    var pz = parseInt($("#number").val()) * parseFloat($("#p_weight").data("single"));
    $("#p_weight").val(pz)
    $("#number").blur(changeNumber);
    var jz = parseFloat($("#m_weight").val()) - parseFloat($("#p_weight").val());
    if(jz<0) jz=0;
    $("#weight").val(jz);
    $("#m_weight").blur(changeWeight);
})

var selCategory = function () {
    $("#price").val($(this).find("option:selected").data("price"));
}

var changeNumber = function () {
    var pz = parseInt($("#number").val()) * parseFloat($("#p_weight").data("single"));
    $("#p_weight").val(pz);
    changeWeight();
}

var changeWeight = function () {
    var jz = parseFloat($("#m_weight").val()) - parseFloat($("#p_weight").val());
    if (jz < 0) jz=0;
    $("#weight").val(jz);
}