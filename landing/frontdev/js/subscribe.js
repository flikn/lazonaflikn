var csrftoken = $.cookie('csrftoken');

$("#button").unbind('click').click(function() {
  event.preventDefault();

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

      switch (data.code) {
        case 200:
          message = '<p><i class="fa fa-check-circle"></i> Cliente válido</p>'
          break;
        case 500:
          message = '<p><i class="fa fa-thumbs-down"></i> Cliente NO válido</p>'
          break;
        case 403:
          message = '<p><i class="fa fa-lock"></i> Este Cliente ya fue validado</p>'
          break;
        default: //400
          message = '<p><i class="fa fa-times"></i> Sintaxis no válida</p>'
          break;
      }

      $('#message').html(message);

      // Redirect.
      if (data.code == 200) {
        window.location.replace("http://onlineclass.pythonindia.com/welcome-page1/");
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
