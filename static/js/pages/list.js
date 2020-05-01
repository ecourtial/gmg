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
                var gameListNode = $("#gameList");
                var contentExample = $('#contentExample').html();

                $("#mainTitle").append(" (" + data.length + " entrées)");

                $.each(data, function (index, value) {
                    var gameInfo = contentExample;
                    gameInfo = gameInfo.replace("@GAME_NAME@", value.name);
                    gameInfo = gameInfo.replace("@GAME_URL@", gameDetailUrl + value.id);
                    gameInfo = gameInfo.replace("@GAME-ID@", value.id);
                    gameInfo = gameInfo.replace("@GAME_ICON@", self.getIcons(value));
                    gameListNode.append(gameInfo);
                });
            };

            this.getIcons = function (game) {
                var iconString = "";

                if (game.all_of_fame == 1) {
                    iconString += '<img title="Hall of fame" src="' + imageUrl + 'hall-of-fame.png"/>';
                }
                if (game.top_game == 1) {
                    iconString += '<img title="Top jeu" src="' + imageUrl + 'top.png"/>';
                }
                if (game.played_it_often == 1) {
                    iconString += '<img title="Beaucoup joué" src="' + imageUrl + 'time.png"/>';
                }

                console.log(iconString);

                return iconString;
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
        };

        var dataReader = new dataGetter();
        dataReader.getData();
    }
);
