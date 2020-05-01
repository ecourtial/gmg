/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";
        var dataGetter = function () {
            /**
             * Constructor
             */
            var self = this;

            /**
             * Contact the server to extract data
             */
            this.getData = function () {
                $.ajax({
                    type: "GET",
                    url: targetUrl,
                    success: function (data, textStatus, jqXHR) {
                        self.cleanTempMsg();
                        self.displayData(data);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        self.cleanTempMsg();
                        self.displayErrorMsg();
                    }
                });
            };

            /**
             * Display the result
             * @param data
             */
            this.displayData = function (data) {
                if (data.msg === "") {
                    var content = "";

                    content += "Bonjour.";
                    content += "<ul>";
                    content += "<li>Il y a actuellement <strong>" + data.ownedCount + "</strong> jeux possédés enregistrés dans l'application.</li>";
                    content += "<li>Il y a actuellement <strong>" + data.toBuyCount + "</strong> jeux à acheter enregistrés dans l'application.</li>";
                    content += "<li>Il y a actuellement <strong>" + data.hardwareToBuyCount + "</strong> éléments de matériel à acheter enregistrés dans l'application.</li>";
                    content += "</ul>";
                    $("#content").append(content);
                    self.displayHallOfFame(data);
                } else {
                    $("#content").append(data.msg);
                }
            };

            /**
             * Display the hall of fame content
             * @param data
             */
            this.displayHallOfFame = function (data) {
                if (data.allOfFameGames.length == 0) {
                    return;
                }

                var content = "";
                content += "<br>Il y a <strong>" + data.allOfFameGames.length + "</strong> jeux dans le Hall of Fames (année où ils ont été 'découverts', pas année de leur sortie) ..."
                content += "<br>";
                content += "<ul>";
                var previousYear = 0;
                var liOpened = false;

                $.each(data.allOfFameGames, function (index, value) {
                    if (previousYear != value.all_of_fame_year) {
                        if (previousYear != 0) {
                            content = content.substr(0, content.length - 2);
                            content += "</li>";
                            liOpened = false;
                        }
                        previousYear = value.all_of_fame_year;
                        content += "<li>" + value.all_of_fame_year + ": ";
                        liOpened = true;
                    }
                    content += "<i>" + value.name + "</i> (" + value.platform + "), ";
                });
                if (liOpened) {
                    content = content.substr(0, content.length - 2);
                    content += "</li>";
                }
                content += "</ul>";
                var allOfFameCriteria = $("#hallOfFameCriteria").remove();
                $("#content").append(content);
                $("#content").append(allOfFameCriteria);
                $("#hallOfFameCriteria").show();
            };

            /**
             * Display generic error msg
             */
            this.displayErrorMsg = function() {
                $("#content").append("Impossible de contacter le serveur");
            };

            /**
             * Remove the temporary msg "Please wait..."
             */
            this.cleanTempMsg = function() {
                $("#tempMsg").remove();
            };
        };

        var dataReader = new dataGetter();
        dataReader.getData();
    }
);
