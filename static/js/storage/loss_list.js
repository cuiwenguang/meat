$(function () {
    $("#lossList").bootstrapTable({
        "url": '/storage/get/loss/list'
    });
})
function showEdit(id) {
        $("#frmCreate").modal({});
}
$("#btnSave").click(function () {
    $.post('/storage/loss/add', $("#frmProduct").serialize(), function (res) {
        window.location.href = '/storage/loss/list';
    });

});
var fmt = {
    optFormatter: function (value) {
       html = $('#rowButtons').tmpl({id:value}).prop("outerHTML");
        return html;
    },
    };

