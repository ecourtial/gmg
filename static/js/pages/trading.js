/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
 define(
    ["jquery", "tools"],
    function ($, tools) {
        "use strict";

        return {
            /**
             * Diplay the list of games trading history
             */
            diplayData: function (data, context) {
                $('#contentTitle').html("Historique commercial");
                var content = '<p id="subtitle">Jeux vendus ou achetés</p>';
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

                    var gameEntry = that.getBadges(value) + tools.filterContent(value.game_id) 
                        + "- " + tools.filterContent(value.title) + " (" + tools.filterContent(value.platform) + ")";
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

            getBadges: function(value) {
                if (value.type === 0) {
                    return  '<img title="J\'y ai vendu" src="' + outImageUrl + '"/> '
                }

                if (value.type === 1) {
                    return ' <img title="Je l\'ai acheté" src="' + inImageUrl + '"/> '
                }

                return "";
            }
        };
    }
);
