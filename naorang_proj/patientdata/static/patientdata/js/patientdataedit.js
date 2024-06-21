$('#div_id_passport_no').hide()
$("#div_id_country").hide()
$("#div_id_passport_of_country").hide()


$(document).ready(
  function(){
    $("select#id_foreigner_NRI").change(function(){

      if ($(this).val()=='NRI'){

        $('#div_id_passport_no').show()
        $("#div_id_country").show()
        $("#div_id_passport_of_country").show()
      }
      else{
          $('#div_id_passport_no').hide()
          $("#div_id_country").hide()
          $("#div_id_passport_of_country").hide()

      }

    })


  })


