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
            }
        };
    }
);
        