$(function () {
    var timeSpan;

    $("#day").click(function () {
            todaBeginDate = getToday(0);
            todaEndDate = getToday(1);
            timeSpan = {"beginDate": todaBeginDate, "endDate": todaEndDate}
            $("#tbody").html("");
            var data = request(timeSpan)
            updateGUI(data)
        }
    );

    $("#weekday").click(function () {
            // beginWeek = getWeek(0);
            // endWeek = getWeek(7);
            beginWeek = '2018-06-04 00:00:00';
            endWeek = '2018-06-10 23:59:59';
            console.log(beginWeek, endWeek)
            timeSpan = {"beginDate": beginWeek, "endDate": endWeek}
            $("#tbody").html("");
            var data = request(timeSpan)
            updateGUI(data)
        }
    );

    $("#mouth").click(function () {
        beginMouth = getMouth(0);
        endMouth = getMouth(1);
        console.log(beginMouth, endMouth)
        timeSpan = {"beginDate": beginMouth, "endDate": endMouth}
        $("#tbody").html("");
        var data = request(timeSpan)
        updateGUI(data)
    });

    $("#day").trigger("click");
});


function request(timeSpan) {
    var respData;
    $.ajax({
        url: "/storage/out/stat/data",
        method: "get",
        async: false,
        data: timeSpan,
        success: function (res) {
            if (res.code == 200) {
                console.log(res.data)
                respData = res.data
            }
        }
    });
    return respData
}


function updateGUI(data) {
    var list = data, number = [], price = [], weight = [], name = [];
    var sumNumber = 0, sumPrice = 0, sumWeight = 0;
    // if(list=" "){$(".card-body").html("亲，今日还未收购哦..."); return}
    for (var i = 0; i < list.length; i++) {
        $("#tbody").append("<tr><td>" + list[i].name + "</td><td>" + list[i].total_number + "</td><td>" +
            list[i].total_price + "</td></tr>");
        sumNumber += list[i].total_number;
        sumPrice += list[i].total_price;
        number.push(list[i].total_number);
        price.push(list[i].total_price);
        name.push(list[i].name);
    }
    $("#tbody").append("<tr><td>合计</td><td>" + sumNumber + "</td><td>" + sumPrice + "</td></tr>");

    //初始化饼图图
    var ctx, data = [], myLineChart;
    Chart.defaults.global.responsive = true;
    ctx = $('#pie-chart').get(0).getContext('2d');
    var colors = ["#FA13E4", "#FA2A00", "#1ABC9C", "#4A12F0", "#B134FA", "#FAE51C", "#FA0E8F"];
    data = {
        datasets: [{
            data: number,
            backgroundColor:colors
        }],
        labels:name

    };

    myLineChart = new Chart(ctx,{
        type:"pie",
        data:data,
    });

    //初始化柱状图
    var ctx, data, myBarChart;
    //Chart.defaults.global.responsive = true;
    ctx = $('#bar-chart').get(0).getContext('2d');
    data = {
        labels: name,
        datasets: [
            {
                label: "金额",
                backgroundColor:"#1ABC9C",
                data: price
            }
        ]
    };
    options = {
                legend: {
                    display: true,
                    labels: {
                        fontColor: 'rgb(255, 99, 132)'
                    }
                }
            }

    myBarChart = new Chart(ctx,{
        type:"bar",
        data:data,
        options:options

    });
}
