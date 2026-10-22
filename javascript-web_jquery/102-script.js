#!/usr/bin/node
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const language = $('#language_code').val();

    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${language}`)
      .done((data) => {
        $('#hello').text(data.hello);
      })
      .fail((error) => {
        console.error(error);
      });
  });
});
