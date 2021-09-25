/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            // Used to filter content from JS injection
            filterContent: function(content) {
                return $('#extraP').text(content).html()
            },

            getMonthName: function(monthId) {
                var correspondence = {
                    1: "Janvier",
                    2: "Février",
                    3: "Mars",
                    4: "Avril",
                    5: "Mai",
                    6: "Juin",
                    7: "Juillet",
                    8: "Août",
                    9: "Septembre",
                    10: "Octobre",
                    11: "Novembre",
                    12: "Décembre",
                };

                if (!(monthId in correspondence)) {
                    return "Mois inconnu";
                }

                return correspondence[monthId];
            }
        };
    }
);
        