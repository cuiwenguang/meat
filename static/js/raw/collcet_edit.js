function updateTab(did) {
    $("#frmCreate").modal();
    $("#detailId").val(did);
    $.ajax({
        url: "/raw/collect/update",
        method: "get",
        async: false,
        data: {id: did},
        success: function (res) {
            if (res.code == 200) {
                console.log(res.data)
                $("#number").val(res.data.number);
                $("#price").val(res.data.price);
                $("#m_weight").val(res.data.m_weight);
                $("#p_weight").val(res.data.p_weight);
                $("#weight").val(res.data.weight);
            }
        }
    });
}

$("#dataSave").click(function () {
    var collect_info_id = $("#collect_info_id").val()
    var number = $("#number").val();
    var price = $("#price").val();
    var m_weight = $("#m_weight").val();
    var p_weight = $("#p_weight").val();
    var weight = $("#weight").val();
    var cg_name = $("#cg_name").val();
    var did = $("#detailId").val();



    if (p_weight == "") {
        alert("请输入皮重");
        return
    }
    if (weight == "") {
        alert("请输入净重");
        return
    }
    if (m_weight == "") {
        alert("请输入毛重");
        return
    }
    if (price == "") {
        alert("请输入价格");
        return
    }
    if (number == "") {
        alert("请输入数量");
        return
    }
    data = {
        "number": number,
        "price": price,
        "m_weight": m_weight,
        "p_weight": p_weight,
        "weight": weight,
        "cg_name": cg_name,
        "did": did
    }
    $.ajax({
        url: "/raw/collect/updateInfo",
        method: "get",
        async: false,
        data: data,
        success: function (res) {
            if (res.code == 200) {
                window.location.href = "/raw/collect/edit?id=" + collect_info_id
            }
        }
    });
})

$("#saveCus").click(function () {
    var sgDatetime = $("#sg_datetime").val();
    var idCard = $("#id_card").val();
    var custName = $("#cust_name").val();
    var mobile = $("#mobile").val();
    var address = $("#address").val();
    var collect_info_id = $("#collect_info_id").val()

    data = {
        "sgDatetime": sgDatetime,
        "idCard": idCard,
        "custName": custName,
        "mobile": mobile,
        "address": address,
        'collect_info_id': collect_info_id
    }

    $.ajax({
        url: "/raw/collect/updatecustomer",
        method: "get",
        async: false,
        data: data,
        success: function (res) {
            if (res.code == 200) {
                alert("修改成功")
                window.location.href = "/raw/collect/edit?id=" + collect_info_id
            }
        }
    });
})

function delData(did) {
    data = {"did": did}
    var collect_info_id = $("#collect_info_id").val()
    $.ajax({
        url: "/raw/collect/delcollectinfo",
        method: "get",
        async: false,
        data: data,
        success: function (res) {
            if (res.code == 200) {
                window.location.href = "/raw/collect/edit?id=" + collect_info_id
            }
        }
    });
}