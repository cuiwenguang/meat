$(function () {
   $("#tableEnter").bootstrapTable({
       "url": '/storage/exchange/all',
       "pagination": true,
       "sidePagination": "server",
       "pageList": [10, 15, 20, 25, 30],
       "detailView": true,
       "detailFormatter": fmt.detailformatter
    });
   $("#state").multiselect({});
   datepickerInit("#create_at");
   $("#btnSearch").click(function () {
        var c = $("#customer").val();
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
        $("#tableEnter").bootstrapTable('refreshOptions', {
            queryParams: queryParams,
            ajaxOptions: {traditional: true}
        });
    });
   $("#frmProduct").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {
            /*input状态样式图片*/
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excuded: "disabled",

        fields: {
            'check_desc': {
                validators: {
                    notEmpty: {
                        message: "审核描述不能为空"
                    }
                }
            },

        }
    });
});
var fmt = {
    customerFormatter: function (value) {
        return ret = value ? value.customer_name : "-";
    },
    stateFormatter: function (value) {
       switch(value){
            case 0:
                return "<label style='color: orange'>申请</label>";
            case 1:
                return "<label style='color: green'>审核通过</label>";
            case 2:
                return "<label style='color: red'>不通过</label>";
           default:
              return "暂存";
        }
    },
    optFormatter: function (value,row) {
        html = $('#rowButtons').tmpl(row);
        if(row.state==-1){
           html.find("#a2").remove()
        }
        if(row.state==1){
           html.find("#a1").remove();
           html.find("#a3").remove();
        }
        return html.prop("outerHTML");
    },
    detailformatter: function (index, row) {
        var html = "";
        $.ajax({
            url: "/storage/exchange/detail/list",
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
function showPrint(id) {
    $("#code").val(id);
    $("#frmCreate").modal({});
    $("#btnCheck").click(function () {
        $("#frmProduct").bootstrapValidator('validate');
        if ($("#frmProduct").data('bootstrapValidator').isValid()) {
            $.post('/storage/exchange/check', $("#frmProduct").serialize(), function (res) {
                window.location.href = '/storage/exchange/list';
            });
        }
    });
}
function deleteOrder(id) {
    $.post("/storage/exchange/delete", {"id": id}, function (res) {
        if (res.code == 200) {
            $("#tableEnter").bootstrapTable("refresh");
        }
    });
}