var searchState = []; //搜索状态
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
   $("#state").multiselect({});
});

$("#btnSearch").click(function () {
    var c = $("#cust_name").val();
    var no = $("#sg_no").val();
    var d = $("#sg_datetime").val();

    var s = [];
    $("#state option:selected").each(function () {
        s.push(this.value);
    });
    queryParams = {
        customer: c,
        no: no,
        sgDate: d,
        sgState: s
    };
    $("#collectTable").bootstrapTable('refreshOptions',{
        queryParams:queryParams,
        ajaxOptions:{traditional:true}
    });
    //$("#collectTable").bootstrapTable('refresh');
});

var tableFormatter = {
    custFormatter: function (value) {
        if(value==null || value==undefined ) return '-';
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
        /**
        html = "";
        if(row.state == 1 || row.state==2) html += "<a href='/raw/collect/pay?id="+row.id+"' data-permission='pay'>结算</a>";
        if(row.state==0) html += "<a href='/raw/collect/create?id="+row.id+"' data-permission='weight'>称重</a>";
        html += ' <a>打印</a>'
        if (row.state < 2 ) html += "<a data-permission='eidt'>编辑</a> <a data-permission='delete'>删除</a> " ;
        */
        html = $("#rowButtons").tmpl(row); //.prop('outerHTML');
        if (row.state == 0){
            html.find("#a2").remove()
            html.find("#a3").remove()
        } else if(row.state == 1){
            html.find("#a1").remove()
        } else{
            html.find("#a1").remove()
            html.find("#a4").remove()
            html.find("#a5").remove()
        }
        return html.prop("outerHTML");
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
