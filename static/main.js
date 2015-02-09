var make_games_table = function() {
  var games;
  var users;
  var post_game = function(e) {
    $.ajax({
      url: Amazing.url + '/game/',
      method: 'post',
      contentType: 'application/json',
      data: JSON.stringify({
        name: $('[name="name"]').val(),
        owner_id: Amazing.user.id
      }),
      success: function(r) {
        Amazing.game = r;
      }
    });
  };
  var delete_game = function(e) {
    e.preventDefault();
    var
      $el = $(e.currentTarget),
      id = $el.data('id');

    $.ajax({
      url: Amazing.url + '/game/' + id,
      method: 'delete',
      contentType: 'application/json',
      success: function() { location.reload(); }
    });
  };
  var render_new_game_form = function(e) {
    e.preventDefault();

    $('section.body')
      .off()
      .html(
        'User Name: ' +
        '<input name="name" class="form-control">' +
        '<button class="btn btn-default" data-action="submit">Submit</button>'
      )
      .on('click', '[data-action="submit"]', function(e) {
        $.ajax({
          url: Amazing.url + '/user/',
          method: 'post',
          contentType: 'application/json',
          data: JSON.stringify({ name: $('[name="name"]').val() }),
          success: function(r) {
            Amazing.user = r;
            $('section.body')
              .off()
              .html(
                'Game Name: ' +
                '<input name="name" class="form-control">' +
                '<button class="btn btn-default" data-action="submit">Submit</button>'
              )
              .on('click', '[data-action="submit"]', post_new_game);
          }
        });
      });
  };
  var render = _.after(2, function() {
    var html = '<h2>Games</h2>' +
      '<table class="table table-striped">';

    _.each(games, function(game) {
      game.user = _.findWhere(users, function(user) {
        return user.id == game.owner_id;
      });

      html += '<tr>' +
        '<td>' + game.name + '</td>' +
        '<td>' + game.user.name + '</td>' +
        '<td>' +
        '<a href="#!" data-id="' + game.id + '" data-action="delete">delete</a> ' +
        '<a href="#!" data-id="' + game.id + '" data-action="join">join</a>' +
        '</td>' +
        '</tr>';
    });

    html += '<tr><td colspan="3">' +
      '<a href="#!" data-action="add-new-game">Add New Game</a>' +
      '</td></tr>' +
      '</tbody></table>';

    $('section.body')
      .off()
      .html(html)
      .on('click', '[data-action="add-new-game"]', render_new_game_form)
      .on('click', '[data-action="delete"]', delete_game);
  });

  $.ajax({
    url: Amazing.url + '/game/',
    success: function(r) {
      games = r.data;
      render();
    }
  });

  $.ajax({
    url: Amazing.url + '/user/',
    success: function(r) {
      users = r.data;
      render();
    }
  });
};

make_games_table();
