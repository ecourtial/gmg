/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            /**
             * Diplay the details of a game
             */
            diplayData: function (data, context) {
                $('#contentTitle').html(data.game.title + ' (' + data.game.platform + ')');
                var content = $('#gameDetailContent').html();

                // Badges
                var badges = this.getBadges(data.game);
                if (badges === '') {
                    badges = 'Aucun';
                }
                content = content.replace("@BADGES@", badges);

                // Main content
                content = content.replace("@ID@", data.game.game_id);
                content = content.replace("@IS_SOLO_RECCURING@", this.boolToYesNoConverter(data.game.singleplayer_recurring));
                content = content.replace("@IS_MULTI_RECCURING@", this.boolToYesNoConverter(data.game.singleplayer_recurring));
                content = content.replace("@IS_TO_DO@", this.boolToYesNoConverter(data.game.to_do));
                content = content.replace("@IS_TO_PLAY_SOLO_SOMETIMES@", this.boolToYesNoConverter(data.game.todo_solo_sometimes));
                content = content.replace("@IS_TO_PLAY_MULTI_SOMETIMES@", this.boolToYesNoConverter(data.game.todo_multiplayer_sometimes));
                content = content.replace("@ORIGINAL_VERSION@", this.boolToYesNoConverter(data.game.original));
                content = content.replace("@IS_TO_BUY@", this.boolToYesNoConverter(data.game.to_buy));
                content = content.replace("@IS_TO_WATCH_BACKGROUND@", this.boolToYesNoConverter(data.game.to_watch_background));
                content = content.replace("@IS_TO_WATCH_SERIOUS@", this.boolToYesNoConverter(data.game.to_watch_serious));
                content = content.replace("@IS_TO_WATCH_AGAIN@", this.boolToYesNoConverter(data.game.to_rewatch));
                content = content.replace("@IS_ONE_COPY@", this.boolToYesNoConverter(data.game.copy));
                content = content.replace("@IS_MANY@", this.boolToYesNoConverter(data.game.many));
                content = content.replace("@IS_TOP@", this.boolToYesNoConverter(data.game.top_game));
                content = content.replace("@IS_PLAYED_OFTEN@", this.boolToYesNoConverter(data.game.played_it_often));

                // Hall of fames
                if (data.game.all_of_fames === 0) {
                    var hofYear = 'N/A';
                    var hofPosition = hofYear;
                } else {
                    var hofYear = data.game.all_of_fames_year;
                    var hofPosition = data.game.all_of_fames_position;
                }
                content = content.replace("@HALL_YEAR@", hofYear);
                content = content.replace("@HALL_POSITION@", hofPosition);
                
                // Comments
                if (data.game.comments === '' || data.game.comments === null) {
                    var comments = 'Aucun';
                } else {
                    var comments = data.game.comments;
                }
                content = content.replace("@COMMENTS@", comments);

                $('#content').empty().html(content);
            },

            boolToYesNoConverter: function (value) {
                return value === 1 ? "Oui" : "Non";
            },

            getBadges: function(value) {
                var gameEntry = '';

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
