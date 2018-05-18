$(function () {
    $("#tableOrder").bootstrapTable({
        "url": "/storage/getorders",
        "pagination": true,
        "sidePagination": "server",
        "pageList": [10, 15, 20, 25, 30],
        "detailView":true,
        "detailFormatter": fmt.detailformatter
    });
});
var fmt = {
    optFormatter: function (value) {
        html = "<a> 出库 </a>" +
            "<a> 删除 </a>";
        return html
    },
    detailformatter: function (index, row) {
        var html = "";
        $.ajax({
            url: "/storage/order/detail/list",
            method: "get",
            async: false,
            data: {id:row.id},
            success: function (res) {
                html = res;
            }
        });
        return html;
    }
}