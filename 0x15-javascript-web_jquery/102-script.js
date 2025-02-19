.ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  .click(function () {
    $.get(url + $.param({ lang: .val() }), function (data) {
      .html(data.hello);
    });
  });
});