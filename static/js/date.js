function getToday(type) {
    var date = new Date();
    var seperator1 = "-";
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    if (type == 0) {
        var currentdate = year + seperator1 + month + seperator1 + strDate + " 00:00:00";
        return currentdate;
    }
    if (type == 1) {
        var currentdate = year + seperator1 + month + seperator1 + strDate + " 23:59:59";
        return currentdate;
    }
}

function getWeek(i) {
    var now = new Date();
    var firstDay = new Date(now - (now.getDay() - 1) * 86400000);
    firstDay.setDate(firstDay.getDate() + i);
    var mon = Number(firstDay.getMonth()) + 1;
    var day = firstDay.getDate()
    if(mon>=1 && mon<=9){
        mon = "0" + mon;
    }
    if(day>=0 && day<=9){
        day = "0" + day
    }
    return now.getFullYear() + "-" + mon + "-" + day+" 00:00:00";
}

function getMouth(day){
    var date = new Date();
    var year = date.getFullYear() + "";
    var month = date.getMonth() + 1;
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if(day==0){
        var begin = year + "-" + month + "-01 00:00:00"
        return begin;
    }
    if(day==1){
        var lastDateOfCurrentMonth = new Date(year,month,0);
        var end = year + "-" + month + "-" + lastDateOfCurrentMonth.getDate() + " 23:59:59";
        return end;
    }
}

function getLastWeek(i) {
    var now = new Date();
    var firstDay = new Date(now - (now.getDay() - 1) * 86400000);
    firstDay.setDate(firstDay.getDate() + i);
    var mon = Number(firstDay.getMonth()) + 1;
    var day = firstDay.getDate() - 7;
    if (mon >= 1 && mon <= 9) {
        mon = "0" + mon;
    }
    if (day >= 0 && day <= 9) {
        day = "0" + day
    }
    return now.getFullYear() + "-" + mon + "-" + day + " 00:00:00";
}

function getLastMouth(day){
    var date = new Date();
    var year = date.getFullYear() + "";
    var month = date.getMonth();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if(day==0){
        var begin = year + "-" + month + "-01 00:00:00"
        return begin;
    }
    if(day==1){
        var lastDateOfCurrentMonth = new Date(year,month,0);
        var end = year + "-" + month + "-" + lastDateOfCurrentMonth.getDate() + " 23:59:59";
        return end;
    }
}

// arr = "2018-05-06";
// function date_week(arr) {
//     var n;
//     arr.substring(8,10)
//     var str = "星期"+ n
//     return str;
// }
//
// date_week(arr)