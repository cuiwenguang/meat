$(function() {
  if (localStorage.menuState=="0"){
    $(".app-container").addClass("expanded");
  } else {
    $(".app-container").removeClass("expanded");
  }
  $(".navbar-expand-toggle").click(function() {
    if (localStorage.menuState=="0"){
      localStorage.menuState = "1";
    } else {
      localStorage.menuState = "0";
    }
    $(".app-container").toggleClass("expanded");
    return $(".navbar-expand-toggle").toggleClass("fa-rotate-90");
  });
  return $(".navbar-right-expand-toggle").click(function() {
    $(".navbar-right").toggleClass("expanded");
    return $(".navbar-right-expand-toggle").toggleClass("fa-rotate-90");
  });
});

$(function() {
  return $('.toggle-checkbox').bootstrapSwitch({
    size: "small"
  });
});

$(function() {
  return $('.match-height').matchHeight();
});

$(function() {
  return $(".side-menu .nav .dropdown").on('show.bs.collapse', function() {
    return $(".side-menu .nav .dropdown .collapse").collapse('hide');
  });
});

$("#updatePsd").click(function () {
    $("#frmPassword").modal({});
});

$(function () {
    $("#frmPsd").bootstrapValidator({
        message: "无效的值",
        feedbackIcons: {
            /*input状态样式图片*/
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excuded: "disabled",

        fields: {
            rePsd: {
                validators: {
                    notEmpty: {
                        message: '用户新密码不能为空'
                    },
                    identical: {
                        field: 'cheekPsd',
                        message: '用户新密码与确认密码不一致！'
                    },
                    stringLength: {
                        min: 6,
                        max: 19,
                        message: '用户新密码长度大于5小于20'
                    },
                    regexp: {
                        regexp: /^[^ ]+$/,
                        message: '用户新密码不能有空格'
                    }

                }
            },
            cheekPsd: {
                validators: {
                    identical: {
                        field: 'rePsd',
                        message: '用户新密码与确认密码不一致！'
                    },
                    notEmpty: {
                        message: '用户确认密码不能为空'
                    },
                    stringLength: {
                        min: 6,
                        max: 19,
                        message: '用户确认密码长度大于5小于20'
                    },

                }
            },
            psd: {
                validators: {
                    notEmpty: {
                        message: '密码不能为空'
                    },
                }
            },
        }
    });
});

$("#btnSubmit").click(function () {
    $("#frmPsd").bootstrapValidator('validate');
    if ($("#frmPsd").data('bootstrapValidator').isValid()) {
        $.post("/changepsd", $("#frmPsd").serialize(), function (ret) {
            if (ret.code == 200) {
                window.location.href = 'logout';
            } else {
                alert(ret.mess)
            }
        })
    }
});