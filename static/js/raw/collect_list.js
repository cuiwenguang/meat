$(function () {
   $("#collectTable").bootstrapTable({
       "url": "/raw/getcollectlist",
       "pagination": true,
       "sidePagination": "server",
       "pageList": [10, 15, 20, 25, 30]
   });
});