console.log($);
$(function(){
    $.get('/color/result/', function(res) {

        console.log(res);
    });
});
