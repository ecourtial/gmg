/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery"],
    function ($) {
        "use strict";

        /**
         * Declaring the object.
         */
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
                        self.showTempMsg(false);
                        self.displayData(data);
                        self.showAnotherGameButton(showAnotherButton);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        self.showTempMsg(false);
                        self.displayErrorMsg();
                    }
                });
            };

            /**
             * Display the result
             * @param data
             */
            this.displayData = function (data) {
                $("#mainTitle").html(data.game.name);
                var contentExample = $('#contentExample').html();

                contentExample = contentExample.replace("@SUPPORT@", data.game.platform);
                contentExample = contentExample.replace("@IS_SOLO@", self.boolToYesNoConverter(data.game.toPlaySolo));
                contentExample = contentExample.replace("@IS_MULTI@", self.boolToYesNoConverter(data.game.toPlayMulti));
                contentExample = contentExample.replace("@IS_PRIO@", self.boolToYesNoConverter(data.game.toDo));
                contentExample = contentExample.replace("@IS_ONE_COPY@", self.boolToYesNoConverter(data.game.copy));
                contentExample = contentExample.replace("@IS_MANY@", self.boolToYesNoConverter(data.game.many));
                contentExample = contentExample.replace("@IS_TOP@", self.boolToYesNoConverter(data.game.topGame));
                contentExample = contentExample.replace("@IS_PLAYED_OFTEN@", self.boolToYesNoConverter(data.game.played_it_often));
                contentExample = contentExample.replace("@RECURING_SOLO@", self.boolToYesNoConverter(data.game.todo_recurring));

                var allFameYear = "N/A";
                var allFamePosition = "N/A";
                if (data.game.allOfFame) {
                    allFameYear = data.game.allOfFameYear;
                    allFamePosition = data.game.allOfFamePosition;
                }
                contentExample = contentExample.replace("@HALL_YEAR@", allFameYear);
                contentExample = contentExample.replace("@HALL_POSITION@", allFamePosition);

                var gameComments = "";
                if (data.game.comments) {
                    gameComments = this.nl2br(data.game.comments);
                }
                contentExample = contentExample.replace("@COMMENTS@", gameComments);
                contentExample = contentExample.replace("@GAME-ID@", data.game.id);

                $("#gameContent").empty().html(contentExample);
                $("#hallOfFameCriteria").show();
                var deleteButton = $("#deleteGameForm");
                if (deleteButton) {
                    deleteButton.show();
                }
            };

            /**
             * @param str
             *
             * @returns {string}
             */
            this.nl2br = function (str) {
                return str.replace(/(?:\r\n|\r|\n)/g, '<br>');
            };

            /**
             * @param value
             *
             * @returns {string}
             */
            this.boolToYesNoConverter = function (value) {
                return value === true ? "Oui" : "Non";
            };

            /**
             * Display generic error msg
             */
            this.displayErrorMsg = function () {
                $("#content").append("Impossible de contacter le serveur");
            };

            /**
             * Show / Hide the temporary msg "Please wait..."
             */
            this.showTempMsg = function(status) {
                if (status) {
                    $("#tempMsg").show();
                } else {
                    $("#tempMsg").hide();
                }
            };

            /**
             * Show / Hide the another game button
             */
            this.showAnotherGameButton = function (status) {
                if (status) {
                    $('#anotherGame').show();
                } else {
                    $('#anotherGame').hide();
                }
            };
        };

        /**
         * Function which control the data processing
         */
        function launchDataProcessing() {
            $("#mainTitle").html(temporaryTitle);
            $("#gameContent").empty();
            dataReader.showTempMsg(true);
            dataReader.showAnotherGameButton(false);
            dataReader.getData();
        }

        // On startup : run a first instance
        var temporaryTitle = $("#mainTitle").html();
        var dataReader = new dataGetter();

        $(document).ready(function() {
            launchDataProcessing();
        });

        // Click to get another random game
        $("#anotherGame").click(function () {
            launchDataProcessing();
        });
    }
);
