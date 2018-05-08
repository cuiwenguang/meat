$(function () {
   $("#collectTable").bootstrapTable({
       "url": "/raw/getcollectlist",
       "pagination": true,
       "sidePagination": "server",
       "pageList": [10, 15, 20, 25, 30],
       "detailView":true,
       "detailFormatter": tableFormatter.detailFormatter
   });
   datepickerInit("#sg_datetime");
   $("#state").multiselect();
});

var tableFormatter = {
    custFormatter: function (value) {
        if(value==null || value ==undefined ) return '-';
        return value.cust_name
    },
    weightFormatter: function (value) {
        return value.toFixed(2);
    },
    moneyFormatter: function (value) {
        return "￥" + value.toFixed(2);
    },
    stateFormatter: function (value) {
        switch(value){
            case 0:
                return "暂存";
            case 1:
                return "<label style='color: red'>未结算</label>";
            case 2:
                return "<label style='color: orange'>结算中</label>";
            case 3:
                return "<label style='color: green'>完成</label>";
        }
    },
    optFormatter: function (value, row) {
        html = "";
        if ($("#action").val() == "pay"){
            if(row.state == 1) html += "<a href='#'>结算</a>";

        }else {
            if(row.state==0) html += "<a href='/raw/collect/create?id="+row.id+"'>称重</a>";
            html += ' <a>打印</a>'
            if (row.state < 2 ) html += ' <a>编辑</a> <a>删除</a> ';
            return html
        }
    },
    detailFormatter: function (index, row) {
        var html = "";
        $.ajax({
            url: "/raw/getsubdetail",
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
