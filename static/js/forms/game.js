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
                $('#contentTitle').html(data.title);
                $('#content').empty().html(data.form);
            }
        };
    }
);
