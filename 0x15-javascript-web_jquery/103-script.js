$(document).ready(function() {
    $('#btn_translate').click(function() {
      translateHello();
    });
  
    $('#language_code').keypress(function(event) {
      if (event.which === 13) {
        translateHello();
      }
    });
  
    function translateHello() {
      const languageCode = $('#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
        $('#hello').text(data.hello);
      });
    }
  });  