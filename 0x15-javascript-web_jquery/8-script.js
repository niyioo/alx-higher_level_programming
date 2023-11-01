$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      const movies = data.results;
      const $list = $('#list_movies');
      movies.forEach(function(movie) {
        $list.append($('<li>' + movie.title + '</li>'));
      });
    });
  });  