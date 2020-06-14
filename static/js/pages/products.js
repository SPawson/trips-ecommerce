$(document).on('load', function () {




})

$("#show-filters").click(function () {
    let icon = '  <i class="fas fa-sort"></i>'
    $("#filters").toggle();

    if ($("#filters").is(":visible")){
        console.log("Filter visible");
        $("#show-filters").html("Hide Filters" + icon);
    }
    else{
        
        $("#show-filters").html("Show Filters" + icon);
    }
});

//used to initialise the datepicker on the product listing
$(function () {
    $('.dates #datepicker').datepicker({
        'format': 'yyyy-mm-dd',
        'autoclose': true
    });
});