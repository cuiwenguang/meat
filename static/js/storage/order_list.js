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
        html = $("#rowButtons").tmpl({id:value}).prop('outerHTML');
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

function showPrint(id) {
    $("#tbody").html("")
    $.ajax({
            url: "/storage/order/getorderlist",
            method: "get",
            async: false,
            data: {id:id},
            success: function (res) {
                console.log(res.data)
                var dataList = res.data,sum_number=0,sum_price=0;
                for (var i =0; i<dataList.length;i++){
                    html = "<tr><td>"+dataList[i].code+"</td><td>"+dataList[i].name+"</td><td>kg</td>" +
                        "<td>"+dataList[i].price+"</td><td>"+dataList[i].number+"</td><td>"+dataList[i].money+"</td></tr>"
                    $("#tbody").append(html)
                    sum_number += dataList[i].number;
                    sum_price += dataList[i].money;
                }
                count="<tr>\n" +
                    "                                    <td>合计</td>\n" +
                    "                                    <td colspan=\"3\" style=\"text-align: center\">\n" +
                    "                                        <span style=\"letter-spacing: 25px\">\n" +
                    "                                            <span>拾</span>\n" +
                    "                                            <span>万</span>\n" +
                    "                                            <span>千</span>\n" +
                    "                                            <span>百</span>\n" +
                    "                                            <span>拾</span>\n" +
                    "                                            <span>元</span>\n" +
                    "                                        </span>\n" +
                    "                                    </td>\n" +
                    "                                    <td>"+sum_number+"</td>\n" +
                    "                                    <td>"+sum_price+"</td>\n" +
                    "                                </tr>"
                $("#tbody").append(count)
            }
        });
    $(".today").html(getToday(3));
    $("#orderId").html("X20181234"+id)
    $("#frmCreate").modal();
}

function printOrder() {
    document.body.innerHTML=document.getElementById('print-block').innerHTML;
    window.print();
    window.location.href='/storage/order'

}