$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  .append(...data.results.map(movie => `<li>${movie.title}</li>`));
});