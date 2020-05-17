/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        return {
            /**
             * Diplay the list of platforms
             */
            diplayData: function (data, context) {
                $('#contentTitle').html('Par support');
                var content = '<ul>';

                $.each(data.platforms, function (index, value) {
                    content += '<li>' + value.platform_name + ' (' + value.game_count + ') - <a data-link-type="gamePerPlatform" id="entry' + value.platform_id + '" href="">Voir la liste</a></li>'
                });

                content += '</ul>';

                $('#content').empty().html(content);
            }
        };
    }
);
