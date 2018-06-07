$(function () {
   initCusotmerInput();
   validateForm();
   $("#btnAddDetail").click(function () {
       computeMoney();
      $.post("/storage/exchange/post", $("#formOrder").serialize(), function (res) {
         if (res.code == 200) {
            initForm(res.data);
            tableBind(true);
            showMessage(res);
         }
      });
   });

   tableBind(true);
   $("#directState").change(function () {
      $("#direct").val($("#directState").val());
   });
   $("#btnSave").click(function () {
      if ($("#tableDetail").find('tbody tr').length == 0) {
         showMessage({code: 403, message: "没有任何退换货信息，不允许提交"})
          return;
      }
      $("#formOrder").bootstrapValidator('validate');
      if ($("#formOrder").data('bootstrapValidator').isValid()) {
         $("#state").val(0);
         $.post("/storage/exchange/post", $("#formOrder").serialize(), function (res) {
                if (res.code == 200) {
                    window.location.href = '/storage/exchange/list';
                }
         });
      }
   });
});
function initCusotmerInput() {
    $("#customer").typeahead({
        minLength: 0,
        showHintOnFocus: true,
        fitToElement: true,
        items: 5,
        source: function (query, process) {
            var param = {query: query}
            $.get("/storage/customer/search", param, function (res) {
                process(res.data);
            });
        },
        autoSelect: true
    });
}
function validateForm() {
    $("#formOrder").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {
            /*input状态样式图片*/
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excuded: "disabled",
        fields: {
            'customer': {
                message: "客户信息输入不正确",
                validators: {
                    notEmpty: {
                        message: "客户信息不能为空"
                    }
                }
            },

            'create_at': {
                message: "时间格式不正确",
                validators: {
                    notEmpty: {
                        message: "数量计量单位不能为空"
                    },
                    date: {
                        format: 'YYYY-MM-DD hh:mm:ss',
                        message: '日期格式不正确'
                    }
                }
            },
            'money': {
                message: "金额输入值不正确",
                validators: {
                    notEmpty: {
                        message: "金额不能为空"
                    },
                    numeric: {
                        message: "金额只能输入整数"
                    }
                }
            },
            'remark':{
                validators:{
                  notEmpty:{
                     message:"退货原因不能为空"
                  }
                }
            }
        }
    });
}
function initForm(form) {
    $("#id").val(form.id);
    $("#customer").val(form.cusotmer.customer_name);
    $("#create_at").val(form.create_at);
    $("#money").val(form.money);
    $("#remark").val(form.remark);
}
function tableBind(isPostBack) {
    var id = $("#id").val();
    if (parseInt(id) > 0) {
        $("#tableDetail").bootstrapTable({
            "url": "/storage/exchange/get/details?id=" + id
        });
    }
    ;
    if (isPostBack) {
        $("#tableDetail").bootstrapTable('refresh');
    }
}
var computeMoney = function () {
   var totalmoney = parseFloat($("#money").val());
    var money = parseInt($("#number").val()) * parseFloat($("#product").find('option:selected').data('price'));
    if($("#directState").val() == '0'){
        money = -money;
    }
    if($("#directState").val() == '1'){
        money = money;
    }
    $("#money").val((totalmoney+money).toFixed(2));
}
var fmt = {
    codeFormatter: function (value) {
        return value.code;
    },
    nameFormatter: function (value) {
        return value.name;
    },
    standardFormatter: function (value) {
        return value.standard;
    },
    priceFormatter: function (value) {
        return value.price;
    },
    optFormatter: function (value) {
        html = "<a>删除</a>"
        return html;
    },
    directFormatter: function(value){
       html = "";
       if(value == 0){
          html = "退货";
       }else{
          html = "换货";
       }
       return html;
    }
}