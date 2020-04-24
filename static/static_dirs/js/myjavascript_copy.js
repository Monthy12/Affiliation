function myBusinessFunction() {
    
    var x = document.getElementById("business").value;
    if (x == "RGD"){
        document.getElementById("agency_all").style.visibility = "hidden";
        $('#agency_all').css("margin-bottom",'-100px')
    }else{
        document.getElementById("agency_all").style.visibility = "visible";
        $('#agency_all').css("margin-bottom",'0.1px')
    }    
}

function specifyProgramme() {
    var programme = document.getElementById("programme").value;

    document.getElementById("programme_name_hidden").style.visibility = "hidden";

    alert("Testing")
}

$(document).ready(function(){

    document.getElementById("programme_name_hidden").style.visibility = "hidden";
})

$(document).ready(function(){

    document.getElementById("doc_name_all").style.visibility = "hidden";
    $('.modal_reduce').css("margin-bottom",'-10px')
})


function myDocumentFunction(){

    var documentValue = document.getElementById("documents_name").value;

    if(documentValue == 'referred'){
        document.getElementById("doc_name_all").style.visibility = "visible";
        $('.modal_reduce').css("margin-bottom",'0.1px')
    }else{
        document.getElementById("doc_name_all").style.visibility = "hidden";
        $('.modal_reduce').css("margin-bottom",'-10px')
    }
}


function deletefile(){
    // var x = document.getElementById("registration_number").value;
    
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
          )
        }
      })
}


//////////////

$(document).ready(function (){
    // var postURL 
    var ii = 1;

    $("#add_mentor").click(function(){
        $("#dynamic_fields").append(''+
            '<tr id="row'+ii+'" class="dynamic-added">'+
                '<td>'+
                    '<div class="margin-bottom-small">'+
                    '<input type="text" name="mentor" placeholder="Name of Mentor Institution" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<input type="text" name="mentor_programme" placeholder="Programmes run by Mentor Institution" class="form-control name_list" required/>'+
                '</td>'+

                '<td>'+
                    '<select class="form-control" id="level" name="level" required>'+
                        '<option value="">--- Please Select Level ---</option>'+
                        '<option value="Bachelor">Bachelor</option>'+
                        '<option value="Masters">Masters</option>'+
                        '<option value="PHD">PHD</option>'+
                    '</select>'+
                '</td>'+

                '<td>'+
                    '<button type="button" name="remove" id="'+ii+'" class="btn btn-danger btn_removes">X</button>'+
                '</td>'+
            '</tr>');

    });

    $(document).on('click', '.btn_removes', function(){
   
        var button_id = $(this).attr("id");
        $('#row'+button_id+'').remove()
    });


    $('#submit_mentor').click(function(){
        $.ajax({
            url: '{% url "mentor" %}',
            method: 'POST',
            data: $('#add_name').serialize(),
            type: 'json',
            success: function(data){
                alert("Working")
            }
        });
    });
 
});


$(document).ready(function (){
    // var postURL 
    var i = 1;

    $("#add_facility").click(function(){

        $("#dynamic_facility").append(''+
            '<tr id="row'+i+'" class="dynamic-added">'+
                '<td>'+
                    '<div class="margin-bottom-small">'+
                    '<input type="text" name="facility" placeholder="Name of Facility" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<button type="button" name="remove" id="'+i+'" class="btn btn-danger btn_remove_facility">X</button>'+
                '</td>'+
            '</tr>'
        );
        

    });

    $(document).on('click', '.btn_remove_facility', function(){
        var button_id = $(this).attr("id");
        $('#row'+button_id+'').remove()
        alert('hy')

    });


    $('#submit_facility').click(function(){
        $.ajax({
            url: '{% url "room_detail" %}',
            method: 'POST',
            data: $('#add_facility').serialize(),
            type: 'json',
            success: function(data){
                alert("Working")
            }
        });
    });


    // $('#submit_institution').click(function(){
    //     $.ajax({
    //         url: '{% url "institution" %}',
    //         method: 'POST',
    //         data: $('#add_inst').serialize(),
    //         type: 'json',
    //         success: function(data){
    //             alert("Working")
    //         }
    //     });
    // });
    
});



$(document).ready(function (){
    // var postURL 
    var a = 1;

    $("#add_library").click(function(){
        $("#dynamic_book").append(''+
            '<tr id="row'+a+'" class="dynamic_book">'+
                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="subject" placeholder="Name of Subject Area" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="number_of_books" placeholder="eg. 20" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="number_of_reference" placeholder="eg. 20" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="number_of_ebooks" placeholder="eg. 20" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="number_of_audio_visuals" placeholder="eg. 20" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="number_of_others" placeholder="eg. 20" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<button type="button" name="remove" id="'+a+'" class="btn btn-danger btn_remove_library">X</button>'+
                '</td>'+

            '</tr>'
        );

    });

    $(document).on('click', '.btn_remove_library', function(){
        var button_id = $(this).attr("id");
        $('#row'+button_id+'').remove()
    });


    $('#submit_library').click(function(){
        $.ajax({
            url: '{% url "library" %}',
            method: 'POST',
            data: $('#add_library').serialize(),
            type: 'json',
            success: function(data){
                alert("Working")
            }
        });
    });

});


$(document).ready(function (){
    // var postURL 
    var b = 1;

    $("#add_lab").click(function(){
        $("#dynamic_workshop").append(''+
            '<tr id="row'+b+'" class="dynamic_lab">'+
                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="lab_type" placeholder="Type of Laborary" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="fixed_item" placeholder="Name of Fixed Item" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="quantity_of_fixed_item" placeholder="eg. 5" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="consummable" placeholder="Name of Consummable" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+

                '<td>'+
                    '<div class="margin-bottom-small">'+
                        '<input type="text" name="quantity_of_consummable" placeholder="eg. 5" class="form-control name_list" required/>'+
                    '</div>'+
                '</td>'+


                '<td>'+
                    '<button type="button" name="remove" id="'+b+'" class="btn btn-danger btn_remove_workshop">X</button>'+
                '</td>'+

            '</tr>'
        );

    });

    $(document).on('click', '.btn_remove_workshop', function(){
        var button_id = $(this).attr("id");
        $('#row'+button_id+'').remove()
    });


    $('#submit_library').click(function(){
        $.ajax({
            url: '{% url "laboratory" %}',
            method: 'POST',
            data: $('#add_workshop').serialize(),
            type: 'json',
            success: function(data){
                alert("Working")
            }
        });
    });

});


$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
  });



$('#public').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("private").disabled = true;
    }else{
        document.getElementById("private").disabled = false;
    }
})

$('#private').click(function(){
    if ($(this).is(":checked")){ 
        document.getElementById("public").disabled = true;
    }else{
        document.getElementById("public").disabled = false;
    }
})


// $(document).ready(function(){
//     $("#yes").click(function(){
//         $("#no").prop("checked", false);
//         $("#yes").prop("checked", true);
//     });
//     $("#no").click(function(){
//         $("#yes").prop("checked", false);
//         $("#no").prop("checked", true);
//     });
// });

// $(document).ready(function(){
//     $("#yes1").click(function(){
//         $("#no1").prop("checked", false);
//         $("#yes1").prop("checked", true);
//     });
//     $("#no1").click(function(){
//         $("#yes1").prop("checked", false);
//         $("#no1").prop("checked", true);
//     });
// });


$('#yes').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity").disabled = false;
    }else{
        document.getElementById("exam_quantity").disabled = true;
    }
})

$('#no').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity").disabled = true;
    }else{
        document.getElementById("exam_quantity").disabled = false;
    }
})

$('#yes1').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity1").disabled = false;
    }else{
        document.getElementById("exam_quantity1").disabled = true;
    }
})

$('#no1').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity1").disabled = true;
    }else{
        document.getElementById("exam_quantity1").disabled = false;
    }
})


$(document).ready(function(){
    $("#yes2").click(function(){
        $("#no2").prop("checked", false);
        $("#yes2").prop("checked", true);
    });
    $("#no2").click(function(){
        $("#yes2").prop("checked", false);
        $("#no2").prop("checked", true);
    });
});

$('#yes2').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity2").disabled = false;
    }else{
        document.getElementById("exam_quantity2").disabled = true;
    }
})

$('#no2').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity2").disabled = true;
    }else{
        document.getElementById("exam_quantity2").disabled = false;
    }
})



$(document).ready(function(){
    $("#yes3").click(function(){
        $("#no3").prop("checked", false);
        $("#yes3").prop("checked", true);
    });
    $("#no3").click(function(){
        $("#yes3").prop("checked", false);
        $("#no3").prop("checked", true);
    });
});

$('#yes3').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity3").disabled = false;
    }else{
        document.getElementById("exam_quantity3").disabled = true;
    }
})

$('#no3').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity3").disabled = true;
    }else{
        document.getElementById("exam_quantity3").disabled = false;
    }
})


$(document).ready(function(){
    $("#yes4").click(function(){
        $("#no4").prop("checked", false);
        $("#yes4").prop("checked", true);
    });
    $("#no4").click(function(){
        $("#yes4").prop("checked", false);
        $("#no4").prop("checked", true);
    });
});

$('#yes4').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity4").disabled = false;
    }else{
        document.getElementById("exam_quantity4").disabled = true;
    }
})

$('#no4').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity4").disabled = true;
    }else{
        document.getElementById("exam_quantity4").disabled = false;
    }
})



$(document).ready(function(){
    $("#yes5").click(function(){
        $("#no5").prop("checked", false);
        $("#yes5").prop("checked", true);
    });
    $("#no5").click(function(){
        $("#yes5").prop("checked", false);
        $("#no5").prop("checked", true);
    });
});

$('#yes5').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity5").disabled = false;
    }else{
        document.getElementById("exam_quantity5").disabled = true;
    }
})

$('#no5').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity5").disabled = true;
    }else{
        document.getElementById("exam_quantity5").disabled = false;
    }
})



$(document).ready(function(){
    $("#yes6").click(function(){
        $("#no6").prop("checked", false);
        $("#yes6").prop("checked", true);
    });
    $("#no6").click(function(){
        $("#yes6").prop("checked", false);
        $("#no6").prop("checked", true);
    });
});

$('#yes6').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity6").disabled = false;
    }else{
        document.getElementById("exam_quantity6").disabled = true;
    }
})

$('#no6').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity6").disabled = true;
    }else{
        document.getElementById("exam_quantity6").disabled = false;
    }
})


$(document).ready(function(){
    $("#yes7").click(function(){
        $("#no7").prop("checked", false);
        $("#yes7").prop("checked", true);
    });
    $("#no7").click(function(){
        $("#yes7").prop("checked", false);
        $("#no7").prop("checked", true);
    });
});

$('#yes7').click(function(){
    if ($(this).is(":checked")){
        // alert("true")
        document.getElementById("exam_quantity7").disabled = false;
    }else{
        document.getElementById("exam_quantity7").disabled = true;
    }
})

$('#no7').click(function(){
    if ($(this).is(":checked")){
        // alert('false')
        document.getElementById("exam_quantity7").disabled = true;
    }else{
        document.getElementById("exam_quantity7").disabled = false;
    }
})


$(function () {
  $("#datepicker").datepicker({ 
        'autoclose': true, 
        'format': 'yyyy-mm-dd',
        'todayHighlight': true
  }).datepicker('update', new Date());
});



$('#bologna-list a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
})




function myMultiple(){

    var a = document.getElementById("input").value;


    if(a === 'HND'){
        var array = ["Accountancy","Accounting with Computing","Actuarial Science",
        "Architectural Wood Technology and Furniture Production (CBT)","Agricultural Engineering","Agro- Enterprise Development","Automotive Engineering","Banking and Finance","Bilingual Secretaryship and Management Studies",
        "Biomedical Engineering Technology","Building Technology","Business Administration","Chemical Engineering","Civil Engineering","Commercial Art","Computer Engineering","Computer Network Management","Computer Science",
        "Computerised Accounting","Construction Engineering and Management","Dispensing Technology","Ecological Agriculture","Electrical/Electronics Engineering","Entrepreneurship and Finance","Environmental Management Technology",
        "Estate Management","Event Management","Fashion Design and Technology","Fashion Design and Textiles","Food Technology","Furniture Design and Production","General (Ecological) Agriculture","Hospitality Management",
        "Hotel Catering and Institutional Management","Health Information Management","Industrial Art","Information Communication Technology","Information Management and Technology","Interior Architecture and Furniture Production",
        "Interior Design and Technology (CBT)","Marketing","Materials Engineering","Mechanical Engineering","Media and Mass Communication","Media and Communication Studies","Medical Laboratary Technology","Post Harvest Technology",
        "Procurement and Logistics Management","Production Engineering","Purchasing and Supply","Plumbing and Gas Technology","Renewable Energy Systems Engineering","Science and Industrial Laboratary Technology","Secretaryship and Management Studies",
        "Statistics","Statistics and Mathematics","Surveying and Geoinformatics","Tourism","Other (Please Specify)"];
    }
    else if(a === 'DIPLOMA'){
        var array = ["Agribusiness and Finance", "Banking Technology and Accounting", "Business Administration","Computerised Accounting","Engineering","Fashion Design","E- Marketing","Environment, Health and Safety",
        "Procurement and Supply Chain Management","Professional Certificate in Garment Construction and Fashion Illustration","Public Administration","Public Relations","Other (Please Specify)"];
    }
    else{
        var array = ["Choose a Level"]
    }

    var string = "";
    for(i=0;i<array.length;i++){

        string = string +"<option value='"+array[i]+"'>"+array[i]+"</option>"
    }


    console.log(string)
    string ="<select name='programme'>"+string+"</select>";
    document.getElementById('output').innerHTML = string

}
