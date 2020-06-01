/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery", "platforms", "games", "game", "home"],
    function ($, platforms, games, game, home) {
        "use strict";

        /**
         * Object handling the Ajax call
         */
        var dataManager = function () {
            /**
             * Constructor
             */
            var self = this;

            /**
             * Contact the server to extract data
             */
            this.getData = function (targetUrl, displayObject, context) {
                $.ajax({
                    type: "GET",
                    url: targetUrl,
                    success: function (data, textStatus, jqXHR) {
                        self.showTempMsg(false);
                        if (data.message) {
                            self.displayMsg(data.message);
                        } else {
                            displayObject.diplayData(data, context);
                        }
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        self.showTempMsg(false);
                        self.displayMsg(jqXHR.responseJSON, true);
                    }
                });
            };

            /**
             * Display generic msg
             */
            this.displayMsg = function (message, error = false) {
                if (error) {
                    var intro = "Une erreur est survenue : ";
                } else {
                    var intro = "Information : "
                }
                $("#content").append(intro + message);
            };

            /**
             * Show / Hide the temporary msg "Please wait..."
             */
            this.showTempMsg = function(status) {
                if (status) {
                    $("#content").empty();
                    $("#tempMsg").show();
                } else {
                    $("#tempMsg").hide();
                }
            };
        }; // End of the data getter object

        function displayHomeContent() {
            dataManager.showTempMsg(true);
            dataManager.getData(hallOfFameUrl, home, null);
        }

        /** On startup */
        var dataManager = new dataManager();
        dataManager.showTempMsg(true);
        displayHomeContent();

        /** Main Menu listeners */

        // Click on the home menu
        $('#homeMenu').click(function() {
            displayHomeContent();

            return false;
        });

        // Click on the platform menu
        $('#platforms').click(function() {
            dataManager.showTempMsg(true);
            dataManager.getData(platformListUrl, platforms, null);

            return false;
        });

        // Click on the various menu items listing games
        $('[id^="special-list"]').click(function() {
            var request = $(this).attr('id').substring(13);
            dataManager.showTempMsg(true);
            dataManager.getData(gamesSpecialListUrl + request, games, request);

            return false;
        });

        // Click on the random menu
        $('[id^="random"]').click(function() {
            var request = $(this).attr('id').substring(7);
            dataManager.showTempMsg(true);
            dataManager.getData(randomgameUrl + request, game, request);

            return false;
        });

        // Search form
        $('#searchForm').submit(function() {
            var url = gamesSpecialListUrl + 'search?query=' + $('#gameSearch').val();
            dataManager.showTempMsg(true);
            dataManager.getData(url, games, 'gameSearch');

            return false;
        });
        
        /** Content listeners */

        // Handle clicks on dynamically added links
        $("#content").on("click", "a", function(){
            var linkType = $(this).data('link-type');
            var id = $(this).attr('id').substring(5);

            if (linkType === 'gamePerPlatform') {
                var url = gameListByPlatformUrl + id
                var displayObject = games;
            } else if (linkType === 'gameDetails') {
                var url = gameDetailsUrl + id
                var displayObject = game;
            } else {
                return false;
            }

            dataManager.showTempMsg(true);
            dataManager.getData(url, displayObject, linkType);

            return false;
        });      
    }
);
