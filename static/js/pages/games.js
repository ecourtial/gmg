/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            /**
             * Diplay the list of games for the given context
             */
            diplayData: function (data, context) {
                $('#contentTitle').html(this.getTitle(data, context));
                var that = this;
                var content = '<ul>';

                $.each(data.games, function (index, value) {
                    var gameEntry = value.title;

                    if (context !== 'gamePerPlatform') {
                        gameEntry += ' (' + value.platform + ')';
                    }

                    gameEntry = that.getBadges(gameEntry, value);
                    gameEntry += ' - <a data-link-type="gameDetails" id="entry' + value.game_id + '" href="">Détails</a>';
                    content += '<li>' + gameEntry + '</li>'
                });

                content += '</ul>';

                $('#content').empty().html(content);
            },

            getTitle: function(data, context) {
                var output = (data.games.length > 1 ? 'entrées' : 'entrée');
                var countTitle = ' (' + data.games.length + ' ' + output + ')';

                var correspondence = {
                    "singleplayer_recurring": "A jouer régulièrement en solo",
                    'multiplayer_recurring': 'A jouer régulièrement en multijoueur',
                    'todo_solo_sometimes': "A jouer parfois en solo",
                    'todo_multiplayer_sometimes':  "A jouer parfois en multijoueur",
                    'original': "Version originale - non copiée",
                    'to_do': "A faire",
                    'to_buy': "A acheter",
                    'to_watch_background': "A regarder en fond",
                    'to_watch_serious': "A regarder sérieusement",
                    'to_rewatch': "A regarder à nouveau parfois",
                };

                if (context in correspondence) {
                    return correspondence[context] + countTitle;
                }

                if (context === 'gamePerPlatform') {
                    var platform = data.platform;
                    var title = platform.platform_name + countTitle;
                } else if(context === 'gameSearch') {
                    var title = "Recherche '" + $('#extraP').text($('#gameSearch').val()).html() + "'" + countTitle;
                } else {
                    console.log("Unknown game context '" + context + "'");
                    var title = '???';
                }

                return title;
            },

            getBadges: function(gameEntry, value) {
                if (value.all_of_fames === 1) {
                    gameEntry += ' <img title="Dans le hall of fames" src="' + allOfFamesImageUrl + '"/>'
                }

                if (value.top_game === 1) {
                    gameEntry += ' <img title="Top jeu" src="' + topImageUrl + '"/>'
                }

                if (value.played_it_often === 1) {
                    gameEntry += ' <img title="Beaucoup joué" src="' + playedOftenImageUrl + '"/>'
                }

                if (value.to_buy === 1) {
                    gameEntry += ' <img title="À acheter" src="' + toBuyImageUrl + '"/>'
                }

                return gameEntry;
            }
        };
    }
);
