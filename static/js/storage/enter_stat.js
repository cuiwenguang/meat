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
            beginWeek = getWeek(0);
            endWeek = getWeek(7);
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
        url: "/raw/getstatdata",
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
        $("#tbody").append("<tr><td>" + list[i].category + "</td><td>" + list[i].number + "</td><td>" +
            list[i].weight + "</td><td>" + list[i].price + "</td></tr>");
        sumNumber += list[i].number;
        sumPrice += list[i].price;
        sumWeight += list[i].weight;
        number.push(list[i].number);
        price.push(list[i].price);
        weight.push(list[i].weight);
        name.push(list[i].category);
    }
    $("#tbody").append("<tr><td>合计</td><td>" + sumNumber + "</td><td>" +
        sumWeight + "</td><td>" + sumPrice + "</td></tr>");

    //初始化饼图图
    var ctx, data = [], myLineChart;
    Chart.defaults.global.responsive = true;
    ctx = $('#pie-chart').get(0).getContext('2d');
    var colors = ["#FA13E4", "#FA2A00", "#1ABC9C", "#4A12F0", "#B134FA", "#FAE51C", "#FA0E8F"];
    for (var i = 0; i < name.length; i++) {
        data.push(
            {
                value: number[i],
                color: colors[i],
                highlight: colors[i],
                label: name[i]
            }
        )
    }
    myLineChart = new Chart(ctx).Pie(data);

    //初始化柱状图
    var ctx, data, myBarChart;
    Chart.defaults.global.responsive = true;
    ctx = $('#bar-chart').get(0).getContext('2d');
    data = {
        labels: name,
        datasets: [
            {
                label: "My First dataset",
                fillColor: "rgba(26, 188, 156,0.6)",
                strokeColor: "#1ABC9C",
                pointColor: "#1ABC9C",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "#1ABC9C",
                data: price
            }
        ]
    };
    myBarChart = new Chart(ctx).Bar(data);
}
