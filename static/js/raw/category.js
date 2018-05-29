$(function () {
   $("#categoryTable").bootstrapTable({
       "url": "/raw/categories"
   });
});

function showEdit(id) {
    if(id!=0){
        $("#id").val(id);
        $.get("/raw/category/"+id, function (ret) {
            if(ret.code == 200){
                $("#name").val(ret.data.name);
                $("#price").val(ret.data.default_price);
            }
        });
    }
    $("#frmCreate").modal();
}

function opratorFormatter(value) {
    /**
    html = "<button type='button' class='btn-sm btn-default' id='btnEdit' onclick='showEdit("+ value +")'>编辑</button> " +
        "<button type='button' class='btn-sm btn-default' id='btnEdit' onclick='del("+ value +")'>删除</button>"
    */
    var html = $('#rowButtons').tmpl({id:value}).prop("outerHTML");
    return html
}

$("#btnSave").click(function save() {
    $.post("/raw/postcategory", $("#frmCategory").serialize(), function (ret) {
        if (ret.code==200){
            $("#categoryTable").bootstrapTable('refresh');
            $("#frmCreate").modal('hide');
            $("#name").val("");
            $("#price").val("");
            $("#id").val(0);
        }
    });
});

function del(id) {
    $.post("/raw/delcategory", {"id": id}, function (ret) {
        showMessage(ret);
        $("#categoryTable").bootstrapTable('refresh');
    })
}