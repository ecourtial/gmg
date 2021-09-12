/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
 define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            /**
             * Add or edit a trading history entry
             */
            diplayData: function (data, context) {
                $('#contentTitle').html(this.getTitle(context));
                $('#content').empty().html(data.form);
            },

            getTitle: function(context) {
                if (context === 'add') {
                    return "Ajouter une entrée dans l'historique commercial";
                } else {
                    return '???';
                }
            }
        };
    }
);
