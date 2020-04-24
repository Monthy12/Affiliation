// $(function () {
//     $('#datetimepicker1').datetimepicker();
// });

$(document).ready(function(){
    $('#datetimepicker1').datetimepicker();
    
})


function myFunction() {
    var x = document.getElementById("bussiness").value;
    document.getElementById("demo").innerHTML = "You selected: " + x;
  }