$(function () {
    $("#tableLoss").bootstrapTable({
        "url": '/storage/loss/get/list',
        "pagination": true,
        "sidePagination": "server",
        "pageList": [10, 15, 20, 25, 30],
        "clickToSelect": true,
    });
    datepickerInit("#create_at");
    $("#state").multiselect({});
    $("#btnSearch").click(function () {
        var c = $("#user_name").val();
        var d = $("#create_at").val();
        var s = [];
        $("#state option:selected").each(function () {
            s.push(this.value);
        });
        var queryParams = {
            user_name: c,
            create_at: d,
            state: s
        };
        $("#tableLoss").bootstrapTable('refreshOptions', {
            queryParams: queryParams,
            ajaxOptions: {traditional: true}
        });
    });
});

function showEdit(id) {
    if (id == 0) {
        $("#number").val('');
        $("#desc").val('');
    } else {
        $("#id").val(id);
        $.post("/storage/loss/get", $("#frmProduct").serialize(), function (ret) {
            if(ret.code==200){
                $("#product").val(ret.data.product.id);
                $("#number").val(ret.data.number);
                $("#desc").val(ret.data.desc);
            };
        });
    }
    $("#frmCreate").modal({});
}
$("#btnSave").click(function () {
    $("#frmProduct").bootstrapValidator('validate');
    if ($("#frmProduct").data('bootstrapValidator').isValid()) {
        $.post('/storage/loss/post', $("#frmProduct").serialize(), function (res) {
            window.location.href = '/storage/loss/list';
        });
    }
});
//审核
function checkEdit(id) {
    var getSelectRows = $("#tableLoss").bootstrapTable('getSelections', function (row) {
        return row;
    });
    if(getSelectRows.length == 0){
        showMessage({code: 403, message: "没有选择任何信息，无法进行批量审核"})
    }else{
        if(id == 0){
            var ids = new Array();
            for(var i=0;i<getSelectRows.length;i++){
                ids[i] = getSelectRows[i].id;
            }
            $("#code").val(ids);
        }else{
            $("#code").val(id);
        }
        $("#frmCheck").modal({});
    }
    $("#btnCheck").click(function () {
        $("#frmChecks").bootstrapValidator('validate');
        if ($("#frmChecks").data('bootstrapValidator').isValid()) {
            $.post('/storage/loss/check', $("#frmChecks").serialize(), function (res) {
                if (res.code == 200) {
                    window.location.href = '/storage/loss/list';
                }
            });
        }
    });
}
var fmt = {
    optFormatter: function (value,row) {
       html = $('#rowButtons').tmpl(row);
       if(row.state==1){
           html.find("#a2").remove()
       }
       return html.prop("outerHTML");
    },
    stateFormatter: function (value) {
        switch(value){
            case 0:
                return "申请";
            case 1:
                return "<label style='color: green'>审核通过</label>";
            case 2:
                return "<label style='color: red'>不通过</label>";
        }
    },
    productFormatter: function (value) {
        return ret = value ? value.name : "-";
    },
};
$(function () {
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
            'number': {
                message: "数量输入不正确",
                validators: {
                    notEmpty: {
                        message: "数量不能为空"
                    },
                    regexp: {
                        regexp: /^[0-9]+$/,
                        message: '请输入数字..'
                    },
                    between:{
                        message:"数量不能为0",
                        min:1,
                        max:Number.MAX_VALUE,
                    },
                    remote:{
                        url: "../check/number",
                        data: {'product': function () {
                                return $("#product").val();
                            }, 'number': $("#number").val()},
                        message: "所选数量大于库存",
                        delay: 2000,
                        type: 'POST'
                    }

                },
            },
            'desc': {
                validators: {
                    notEmpty: {
                        message: "损耗原因不能为空"
                    }
                }
            },

        }
    });
});
