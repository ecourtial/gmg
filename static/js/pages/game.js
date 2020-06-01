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
                content = content.replace("@ID@", data.game.meta.game_id);
                content = content.replace("@IS_SOLO_RECCURING@", this.boolToYesNoConverter(data.game.meta.singleplayer_recurring));
                content = content.replace("@IS_MULTI_RECCURING@", this.boolToYesNoConverter(data.game.meta.singleplayer_recurring));
                content = content.replace("@IS_TO_DO@", this.boolToYesNoConverter(data.game.meta.to_do));
                content = content.replace("@IS_TO_PLAY_SOLO_SOMETIMES@", this.boolToYesNoConverter(data.game.meta.todo_solo_sometimes));
                content = content.replace("@IS_TO_PLAY_MULTI_SOMETIMES@", this.boolToYesNoConverter(data.game.meta.todo_multiplayer_sometimes));
                content = content.replace("@ORIGINAL_VERSION@", this.boolToYesNoConverter(data.game.meta.original));
                content = content.replace("@IS_TO_BUY@", this.boolToYesNoConverter(data.game.meta.to_buy));
                content = content.replace("@IS_TO_WATCH_BACKGROUND@", this.boolToYesNoConverter(data.game.meta.to_watch_background));
                content = content.replace("@IS_TO_WATCH_SERIOUS@", this.boolToYesNoConverter(data.game.meta.to_watch_serious));
                content = content.replace("@IS_TO_WATCH_AGAIN@", this.boolToYesNoConverter(data.game.meta.to_rewatch));
                content = content.replace("@IS_ONE_COPY@", this.boolToYesNoConverter(data.game.meta.copy));
                content = content.replace("@IS_MANY@", this.boolToYesNoConverter(data.game.meta.many));
                content = content.replace("@IS_TOP@", this.boolToYesNoConverter(data.game.meta.top_game));
                content = content.replace("@IS_PLAYED_OFTEN@", this.boolToYesNoConverter(data.game.meta.played_it_often));

                // Hall of fame
                if (data.game.meta.hall_of_fame === 0) {
                    var hofYear = 'N/A';
                    var hofPosition = hofYear;
                } else {
                    var hofYear = data.game.meta.hall_of_fame_year;
                    var hofPosition = data.game.meta.hall_of_fame_position;
                }
                content = content.replace("@HALL_YEAR@", hofYear);
                content = content.replace("@HALL_POSITION@", hofPosition);
                
                // Comments
                if (data.game.meta.comments === '' || data.game.meta.comments === null) {
                    var comments = 'Aucun';
                } else {
                    var comments = data.game.meta.comments;
                }
                content = content.replace("@COMMENTS@", comments);

                $('#content').empty().html(content);
            },

            boolToYesNoConverter: function (value) {
                return value === 1 ? "Oui" : "Non";
            },

            getBadges: function(value) {
                var gameEntry = '';

                if (value.meta.hall_of_fame === 1) {
                    gameEntry += ' <img title="Dans le hall of fame" src="' + hallOfFameImageUrl + '"/>'
                }

                if (value.meta.top_game === 1) {
                    gameEntry += ' <img title="Top jeu" src="' + topImageUrl + '"/>'
                }

                if (value.meta.played_it_often === 1) {
                    gameEntry += ' <img title="Beaucoup joué" src="' + playedOftenImageUrl + '"/>'
                }

                if (value.meta.to_buy === 1) {
                    gameEntry += ' <img title="À acheter" src="' + toBuyImageUrl + '"/>'
                }

                return gameEntry;
            }
        };
    }
);
