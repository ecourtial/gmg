/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery", "tools"],
    function ($, tools) {
        "use strict";

        return {
            /**
             * Diplay the hall of fames
             */
            diplayData: function (data, context) {   
                $('#contentTitle').html('Bienvenue sur Games!');     
                var content = "";

                content += "Bonjour.";
                content += "<ul>";
                content += "<li>Il y a actuellement <strong>" + tools.filterContent(data.gameCount) + "</strong> jeux enregistrés dans l'application, pour <strong>" + tools.filterContent(data.platformCount) + "</strong> plateformes.</li>";
                content += "<li>Il y a actuellement <strong>" + tools.filterContent(data.toDoSoloOrToWatch) + "</strong> jeux à jouer en solo ou à regarder.</li>";
                content += "</ul>";
                content += $('#hallOfFameCriteria').html();
                content += this.displayHallOfFame(data);

                $('#content').empty().html(content);
            },

            displayHallOfFame: function (data) {
                if (data.hallOfFameGames.length == 0) {
                    return '';
                }

                var content = "";
                content += "<br>Il y a <strong>" + tools.filterContent(data.hallOfFameGames.length) + "</strong> jeux dans le Hall of Fames (année où on y a joués pour la première fois, pas année de leur sortie) ..."
                content += "<br/><br/>";
                content += "<ul>";

                var previousYear = 0;
                var currentYear = 0;
                var currentYearGameCount = 0;
                var currentYearContent = "";
                var liOpened = false;
                var that = this;

                $.each(data.hallOfFameGames, function (index, value) {
                    if (previousYear != value.meta.hall_of_fame_year) {
                        if (previousYear != 0) {
                            content += that.getHallOfFameClosure(previousYear, currentYearContent, currentYearGameCount);
                            currentYearContent = "";
                            currentYearGameCount = 0;
                            liOpened = false;
                        }
                        currentYearGameCount = 0;
                        previousYear = value.meta.hall_of_fame_year;
                        currentYearContent += ": <ul>";
                        liOpened = true;
                    }
                    currentYear = value.meta.hall_of_fame_year;
                    currentYearGameCount++
                    currentYearContent += "<li><i>" + tools.filterContent(value.title) + "</i> (" + tools.filterContent(value.platform_name) + ")</li>";
                });

                if (liOpened) {
                    content += this.getHallOfFameClosure(currentYear, currentYearContent, currentYearGameCount);
                }
                content += "</ul>";

                return content;
            },

            getHallOfFameClosure: function(year, currentYearContent, currentYearGameCount) {
                currentYearContent += "</ul></li>";
                var output = (currentYearGameCount > 1 ? 'entrées' : 'entrée');
                currentYearContent = "<li><strong>" + tools.filterContent(year) + "</strong> (" + currentYearGameCount + " " + output + ")" + currentYearContent;

                return currentYearContent;
            }
        }
    }
);    