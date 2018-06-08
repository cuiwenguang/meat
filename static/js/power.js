$(function () {
    $.ajax({
        url: "/system/power/getperms",
        method: "get",
        success: function (res) {
            if (res.code == 200) {
                $("#permissions").html("");
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    var values = "<option  value=" + data[i].id + ">" + data[i].name + "</option>";
                    $("#permissions").append(values)
                }

                $('#permissions').dblclick(function () {
                    id = $("#permissions").val();
                    $("#permissions option[value=" + id + "]").remove(); //删除Select中Value='3'的Option
                    for (var i = 0; i < data.length; i++) {
                        if (data[i].id == id) {
                            $("#id_perm").append("<option value=" + id + ">" + data[i].name + "</option>"); //为Select追加一个Option(下拉项)
                        }
                    }
                })

                $('#id_perm').dblclick(function () {
                    id = $("#id_perm").val();
                    $("#id_perm option[value=" + id + "]").remove(); //删除Select中Value='3'的Option
                    for (var i = 0; i < data.length; i++) {
                        if (data[i].id == id) {
                            $("#permissions").append("<option value=" + id + ">" + data[i].name + "</option>"); //为Select追加一个Option(下拉项)
                        }
                    }
                })
            }
        }
    });
});


function Update(id) {
    var array = new Array();  //定义数组
    $("#id_perm option").each(function () {  //遍历所有option
        var txt = $(this).val();   //获取option值
        if (txt != '') {
            array.push(txt);  //添加到数组中
        }
    });
    var data = {"perm":array}
    $.ajax({
        url: "/system/power/updateperms?id="+id,
        method: "get",
        data:data,
        success: function (res) {
            if (res.code == 200) {
                alert("添加成功")
            }
        }
    });


}