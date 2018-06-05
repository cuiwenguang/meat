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

function getTime(n) {
    var now = new Date();
    var year = now.getFullYear();
//因为月份是从0开始的,所以获取这个月的月份数要加1才行
    var month = now.getMonth() + 1;
    var date = now.getDate();
    var day = now.getDay();
    console.log(date);
//判断是否为周日,如果不是的话,就让今天的day-1(例如星期二就是2-1)
    if (day !== 0) {
        n = n + (day - 1);
    }
    else {
        n = n + day;
    }
    if (day) {
//这个判断是为了解决跨年的问题
        if (month > 1) {
            month = month;
        }
//这个判断是为了解决跨年的问题,月份是从0开始的
        else {
            year = year - 1;
            month = 12;
        }
    }
    now.setDate(now.getDate() - n);
    year = now.getFullYear();
    month = now.getMonth() + 1;
    date = now.getDate();
    console.log(n);
    s = year + "年" + (month < 10 ? ('0' + month) : month) + "月" + (date < 10 ? ('0' + date) : date) + "日";
    return s;
}

/***参数都是以周一为基准的***/
//上周的开始时间
console.log(getTime(7));
//上周的结束时间
console.log(getTime(1));
//本周的开始时间
console.log(getTime(0));
//本周的结束时间
console.log(getTime(-6));