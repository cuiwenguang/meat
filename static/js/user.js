$(function () {
    $("#tableUser").bootstrapTable({
        "url": "/system/getusers"
    });

});

function showEdit(id) {
    if(id>0){
        //
    }
    $("#frmCreate").modal();
}

function save() {
    
}

function validate() {
    $("#frmCreate").bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        excluded: [':disbled', ':hidden'],
        fields: {

        }
    });
}