/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery", "tools"],
    function ($, tools) {
        "use strict";

        return {
            /**
             * Diplay the list of games history
             */
            diplayData: function (data, context) {
                $('#contentTitle').html("Historique");
                var content = '<p id="subtitle">Jeux vus ou joués</p>';
                var currentYear = 0;
                var that = this;

                $.each(data.games, function (index, value) {
                    var gameYear = parseInt(value.year);
                    var yearString = '<strong>' + gameYear + '</strong>';

                    if (currentYear === 0) {
                        content += yearString + '<ul>';
                        currentYear = gameYear;
                    } else {
                        if (currentYear != gameYear) {
                            content += '</ul>' + yearString + '<ul>';
                            currentYear = gameYear;
                        }
                    }

                    var gameEntry = value.position + "- " + tools.filterContent(value.title);
                    gameEntry = that.getBadges(gameEntry, value);
                    gameEntry += ' - <a data-link-type="gameDetails" id="entryD' + tools.filterContent(value.game_id) + '" href="">Détails</a>';

                    if (logged) {
                        gameEntry += ' - <a data-link-type="gameEdit" id="entryE' + tools.filterContent(value.game_id) + '" href="">Editer</a>';
                        gameEntry += ' - <a data-link-type="gameDelete" id="entryR' + tools.filterContent(value.game_id) + '" href="">Supprimer</a>';
                        gameEntry += ' - <a data-link-type="historyDelete" id="entryH' + tools.filterContent(value.id) + '" href="">Supprimer entrée historique</a>';
                    }

                    content += '<li>' + gameEntry + '</li>'
                });

                content += '</ul></ul>';

                $('#content').empty().html(content);
            },

            getBadges: function(gameEntry, value) {
                if (value.watched === 1) {
                    gameEntry += ' <img title="Je l\'ai regardé" src="' + watchedImageUrl + '"/>'
                }

                if (value.played === 1) {
                    gameEntry += ' <img title="J\'y ai joué" src="' + playedImageUrl + '"/>'
                }

                return gameEntry;
            }
        };
    }
);
