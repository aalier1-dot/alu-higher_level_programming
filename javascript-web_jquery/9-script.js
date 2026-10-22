#!/usr/bin/node
$(document).ready(() => {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr')
    .done((data) => {
      $('#hello').text(data.hello);
    })
    .fail((error) => {
      console.error(error);
    });
});
