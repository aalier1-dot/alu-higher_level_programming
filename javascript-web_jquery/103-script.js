#!/usr/bin/node
$(document).ready(() => {
  const translate = () => {
    const language = $('#language_code').val();

    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${language}`)
      .done((data) => {
        $('#hello').text(data.hello);
      })
      .fail((error) => {
        console.error(error);
      });
  };

  $('#btn_translate').click(translate);
  $('#language_code').keypress((event) => {
    if (event.which === 13) {
      translate();
    }
  });
});
