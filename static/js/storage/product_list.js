$(function () {
   $("#productTable").bootstrapTable({
       "url": "/storage/getproducts",
       "checkbox":true
   });
   $("#btnEdit").click(function () { 
      $("#frmCreate").modal({});
   });
});

function showEdit(id) {
    $("#id").val(id);
    $("#frmCreate").modal({});
}

$("#btnSave").click(function () {
    $.post("/storage/postproduct", $("#frmProduct").serialize(), function (ret) {
        $("#productTable").bootstrapTable("refresh");
    });
});

var formatter = {
    optFormatter: function (value) {
        html ="<a href='javascript:showEdit("+value+")'> 编辑 </a>"+
            "<a > 删除 </a>"
        return html;
    }
}