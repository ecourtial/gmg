/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            /**
             * Add or edit a game
             */
            diplayData: function (data, context) {
                $('#contentTitle').html(this.getTitle(context));
                $('#content').empty().html(data);
            },

            getTitle: function(context) {
                if (context === 'add') {
                    return 'Ajouter un jeu';
                } else {
                    return '???';
                }
            }
        };
    }
);
