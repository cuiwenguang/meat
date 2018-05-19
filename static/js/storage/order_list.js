$(function () {
    $("#tableOrder").bootstrapTable({
        "url": "/storage/getorders",
        "pagination": true,
        "sidePagination": "server",
        "pageList": [10, 15, 20, 25, 30],
        "detailView": true,
        "detailFormatter": fmt.detailformatter
    });
    datepickerInit("#create_at");
    $("#state").multiselect({});
    $("#btnSearch").click(function () {
        var c = $("#cust_name").val();
        var d = $("#create_at").val();
        var s = [];
        $("#state option:selected").each(function () {
            s.push(this.value);
        });
        var queryParams = {
            customer: c,
            create_at: d,
            state: s
        };
        $("#tableOrder").bootstrapTable('refreshOptions', {
            queryParams: queryParams,
            ajaxOptions: {traditional: true}
        });
    });
});
var fmt = {
    customerFormatter: function (value) {
        return ret = value ? value.customer_name : "-";
    },
    stateFormatter: function (value) {
        return value == 0 ? "暂存" : "<label style='color:green'>完成</label>";
    },
    optFormatter: function (value) {
        html = "<a href='/storage/order/edit?id=" + value + "'> 编辑 </a>" +
            "<a href='javascript:print(" + value + ")'> 打印 </a>" +
            "<a href='javascript:deleteOrder(" + value + ")'> 删除 </a>";
        return html
    },
    detailformatter: function (index, row) {
        var html = "";
        $.ajax({
            url: "/storage/order/detail/list",
            method: "get",
            async: false,
            data: {id: row.id},
            success: function (res) {
                html = res;
            }
        });
        return html;
    }
};

function deleteOrder(id) {
    $.post("/storage/order/delete", {id: id}, function (res) {
        if (res.code == 200) {
            $("#tableOrder").bootstrapTable("refresh");
        }
    });
}