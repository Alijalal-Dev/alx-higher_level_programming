.ready(function () {
  .click(translate);
  .focus(function () {
    .keydown(function (e) {
      if (e.keyCode === 13) translate();
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: .val() }), function (data) {
    .html(data.hello);
  });
}