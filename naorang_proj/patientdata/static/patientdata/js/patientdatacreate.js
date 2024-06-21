$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientvitals").modal("show");
      },
      success: function (data) {
        $("#modal-patientvitals .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm1 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patienthistory").modal("show");
      },
      success: function (data) {
        $("#modal-patienthistory .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm2 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientsystemic").modal("show");
      },
      success: function (data) {
        $("#modal-patientsystemic .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm3 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientobstetric").modal("show");
      },
      success: function (data) {
        $("#modal-patientobstetric .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm4 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientgeneral").modal("show");
      },
      success: function (data) {
        $("#modal-patientgeneral .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm5 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientinvestigations").modal("show");
      },
      success: function (data) {
        $("#modal-patientinvestigations .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm6 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientprovisional").modal("show");
      },
      success: function (data) {
        $("#modal-patientprovisional .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm7 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientdiagnosis").modal("show");
      },
      success: function (data) {
        $("#modal-patientdiagnosis .modal-content").html(data.html_form);
      }
    });
  };

  var loadForm8 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patientadvice").modal("show");
      },
      success: function (data) {
        $("#modal-patientadvice .modal-content").html(data.html_form);
      }
    });
  };


  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientvital-table ").html(data.html_partial_patientvitals_detail);
          $("#modal-patientvitals").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientvitals .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveForm1 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patienthistory-table ").html(data.html_patientreg_detail);
          $("#modal-patienthistory").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patienthistory .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveForm2 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientsystemic-table ").html(data.html_partial_patientsystrmic_detail);
          $("#modal-patientsystemic").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientsystemic .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveForm3 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientobstetric-table ").html(data.html_patientreg_detail);
          $("#modal-patientobstetric").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientobstetric .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveForm4 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientgeneral-table ").html(data.html_patientreg_detail);
          $("#modal-patientgeneral").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientgeneral .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  var saveForm5 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientinvestigations-table ").html(data.html_patientreg_detail);
          $("#modal-patientinvestigations").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientinvestigations .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  var saveForm6 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientprovisional-table ").html(data.html_patientreg_detail);
          $("#modal-patientprovisional").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientprovisional .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveForm7 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientdiagnosis-table ").html(data.html_patientreg_detail);
          $("#modal-patientdiagnosis").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientdiagnosis .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  var saveForm8 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',

      success: function (data) {

        if (data.form_is_valid) {
          $("#patientadvice-table ").html(data.html_patientreg_detail);
          $("#modal-patientadvice").modal("hide");
          location.reload('patientreg-detail')
        }
        else {
          $("#modal-patientadvice .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Binding */

  // Create patientvitals
  $(".js-create-patientvitals").click(loadForm);
  $("#modal-patientvitals").on("submit", ".js-patientvitals-create-form", saveForm);

  // Update patientvitals
  $("#patientvitals-table ").on("click", ".js-update-patientvitals", loadForm);
  $("#modal-patientvitals").on("submit", ".js-patientvitals-update-form", saveForm);

  //delete patientvitals
  $("#patientvitals-table ").on("click", ".js-delete-patientvitals", loadForm);
  $("#modal-patientvitals").on("submit", ".js-patientvitals-delete-form", saveForm);

  // update patient history

  $("#patienthistory-table").on("click", ".js-update-patienthistory", loadForm1);
  $("#modal-patienthistory").on("submit", ".js-patienthistory-update-form", saveForm1);

  // create systemin

  $(".js-create-patientsystemic").click(loadForm2);
  $("#modal-patientsystemic").on("submit", ".js-patientsystemic-create-form", saveForm2);

  // Update patientsystemic

  $("#patientsystemic-table ").on("click", ".js-update-patientsystemic", loadForm2);
  $("#modal-patientsystemic").on("submit", ".js-patientsystemic-update-form", saveForm2);

  //delete patientsystemic
  $("#patientsystemic-table ").on("click", ".js-delete-patientsystemic", loadForm2);
  $("#modal-patientsystemic").on("submit", ".js-patientsystemic-delete-form", saveForm2);

  // update patient obstetric

  $("#patientobstetric-table").on("click", ".js-update-patientobstetric", loadForm3);
  $("#modal-patientobstetric").on("submit", ".js-patientobstetric-update-form", saveForm3);

  // update patient GENERAL

  $("#patientgeneral-table").on("click", ".js-update-patientgeneral", loadForm4);
  $("#modal-patientgeneral").on("submit", ".js-patientgeneral-update-form", saveForm4);


  // update patient investigations

  $("#patientinvestigations-table").on("click", ".js-update-patientinvestigations", loadForm5);
  $("#modal-patientinvestigations").on("submit", ".js-patientinvestigations-update-form", saveForm5);

// update patient provisional

  $("#patientprovisional-table").on("click", ".js-update-patientprovisional", loadForm6);
  $("#modal-patientprovisional").on("submit", ".js-patientprovisional-update-form", saveForm6);

// update patient diagnosis

  $("#patientdiagnosis-table").on("click", ".js-update-patientdiagnosis", loadForm7);
  $("#modal-patientdiagnosis").on("submit", ".js-patientdiagnosis-update-form", saveForm7);

// update patient advice

  $("#patientadvice-table").on("click", ".js-update-patientadvice", loadForm8);
  $("#modal-patientadvice").on("submit", ".js-patientadvice-update-form", saveForm8);

  // create patientadvice
  $(".js-create-patientadvice").click(loadForm8);
  $("#modal-patientadvice").on("submit", ".js-patientadvice-create-form", saveForm8);

//delete patientadvice
  $("#patientadvice-table ").on("click", ".js-delete-patientadvice", loadForm8);
  $("#modal-patientadvice").on("submit", ".js-patientadvice-delete-form", saveForm8);


});

/* Date time picker experiment


$(function () {
        $('.datetime-input').datetimepicker({
            format:'YYYY-MM-DD HH:mm:ss'
        });
    });*/
