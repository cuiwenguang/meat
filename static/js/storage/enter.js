$(function () {
    datepickerInit("#rangeDate");
    $("#mulSelProduct").multiselect({});
    $("#formEnter").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {/*input状态样式图片*/
                 valid: 'glyphicon glyphicon-ok',
                 invalid: 'glyphicon glyphicon-remove',
                 validating: 'glyphicon glyphicon-refresh'
             },
        excuded: "disabled",
        fields:{
            'number': {
                message: "入库数量输入不正确",
                validators: {
                    notEmpty: {
                        message: "数量不能为空"
                    },
                    digits: {
                        message: "数量只能输入整数"
                    }
                }
            },

            'code': {
                message: "产品编号格式不对",
                validators: {
                    notEmpty: {
                        message: "产品编号不能为空"
                    }
                }
            }
        }
    });

    $("#tableEnter").bootstrapTable({
        "url": "/storage/getenterdata",
        "pagination": true,
        "sidePagination": "server",
        "pageList": [10, 15, 20, 25, 30]
    });
});

$("#btnSubmit").click(function () {
    $("#formEnter").bootstrapValidator('validate');
    if ($("#formEnter").data('bootstrapValidator').isValid()) {
        $.post("/storage/post_enter",
            $("#formEnter").serialize(),
            function (ret) {
                if(ret.code==200){
                    $("#tableEnter").bootstrapTable('refresh');
                }
            });
    }
});

$("#btnSearch").click(function () {
    var d = $("#rangeDate").val();
    var s = [];
    $("#mulSelProduct option:selected").each(function () {
        s.push(this.value);
    });
    queryParams = {
        rangeDate: d,
        products: s
    };
    $("#tableEnter").bootstrapTable('refreshOptions', {
        queryParams: queryParams,
        ajaxOptions: {traditional: true}
    });
});


$("#code").keyup(function () {
    if ($("#code").val().length == 4) {
        $.get("/storage/getproductbycode?code=" + $("#code").val(), function (res) {
            if (res.code == 200) {
                $("#id").val(res.data.id);
                $("#name").val(res.data.name);
                $("#standard").val(res.data.standard);
                $("#packing").val(res.data.packing);
            } else {
                $("#id").val(0);
                $("#name").val('');
                $("#standard").val('');
                $("#packing").val('');
                alert("产品不存在");
            }
        });
    }
});

var formatter = {
    codeFormatter: function (value) { return value.code },
    nameFormatter: function (value) { return value.name },
    standardFormatter: function (value) { return value.standard },
    packingFormatter: function (value) { return value.packing },
    optFormatter: function (value) {
        html = "<a href='javascript:del("+value+")'>删除</a>"
        return html;
    }
};

function del(id) {
    $.post('/storage/enter/delete', {id:id}, function (res) {
        if (res.code == 200){
            $("#tableEnter").bootstrapTable('refresh');
        }
    })
}