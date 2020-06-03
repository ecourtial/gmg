/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery", "tools"],
    function ($, tools) {
        "use strict";

        return {
            /**
             * Diplay the list of platforms
             */
            diplayData: function (data, context) {
                $('#contentTitle').html('Par support');
                var content = '<ul>';

                $.each(data.platforms, function (index, value) {
                    content += '<li>' + tools.filterContent(value.platform_name) + ' (' + value.game_count + ') - <a data-link-type="gamePerPlatform" id="entry' + tools.filterContent(value.platform_id) + '" href="">Voir la liste</a></li>'
                });

                content += '</ul>';

                $('#content').empty().html(content);
            }
        };
    }
);
