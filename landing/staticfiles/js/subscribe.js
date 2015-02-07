var csrftoken = $.cookie('csrftoken');


$(document).ready(function() {
  $("#message").css('visibility', 'hidden');
});

$("#button").unbind('click').click(function() {
  var client = $("#client").val();
  var account = $("#account").val();
  var data = {
    "client": client,
    "account": account,
  };

  $.ajax({
      url: '/api/subscribe/',
      type: 'POST',
      data: data,
      dataType: 'json',
    })
    .done(function(data) {
      console.log(data);

      var message = "";
      var type_alert = "";

      switch (data.code) {
        case 200:
          message = '<p><i class="fa fa-check-circle"></i> Cliente válido! Aún puede user esta cuenta movistar ' + data.lifetime + ' veces más. <strong>Invita a tus amigos o familiares!</strong></p>'
          type_alert = "alert alert-success";
          break;
        case 500:
          message = '<p><i class="fa fa-thumbs-down"></i> Cliente no válido.</p>'
          type_alert = "alert alert-danger";
          break;
        case 403:
          message = '<p><i class="fa fa-lock"></i> Código movistar no valido.</p>'
          type_alert = "alert alert-warning";
          break;
        default: //400
          message = '<p><i class="fa fa-times"></i> Sintaxis no válida.</p>'
          type_alert = "alert alert-danger";
          break;
      }

      $('#message').html(message);
      $("#message").css('visibility', 'visible');
      $("#message").attr("class", type_alert);

      // Redirect.
      if (data.code == 200) {
        setTimeout(function() {
          window.location.replace("/thanks/");
        }, 3000);
      }
    })
    .fail(function(object, msg) {
      console.log('error enviando data: ' + object.responseText);
    });
});


function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
