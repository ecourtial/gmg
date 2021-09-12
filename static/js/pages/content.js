/**
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
define(
    ["jquery", "platforms", "games", "game", "home", "platformEditor", "gameEditor", "historyEditor", "history", "trading"],
    function ($, platforms, games, game, home, platformEditor, gameEditor, historyEditor, history, trading) {
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
             * Contact the server to extract or POST data
             */
            this.request = function (targetUrl, displayObject, context = null, persist = false, payload = null, requestType = "GET", callback = null) {
                if (persist === true) {
                    previousUrl = targetUrl;
                    previousDisplayer = displayObject;
                    previousContext = context;
                }
                
                $.ajax({
                    type: requestType,
                    url: targetUrl,
                    data: payload,
                    success: function (data, textStatus, jqXHR) {
                        self.showTempMsg(false);
                        if (data && data.message) {
                            self.displayMsg(data.message);
                        } else if (displayObject) {
                            displayObject.diplayData(data, context);
                        } else if (callback) {
                            callback();
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

        // Function to display home content
        function displayHomeContent() {
            dataManager.showTempMsg(true);
            dataManager.request(hallOfFameUrl, home);
        }

        function deleteGame(gameId) {
            if (confirm("Etes-vous sûr de vouloir supprimer ce jeu?") === false) {
                return false;
            }

            dataManager.showTempMsg(true);

            if (previousDisplayer === null || previousDisplayer === game) {
                previousContext = 'home';
                previousDisplayer = home;
                previousUrl = hallOfFameUrl;
            }

            var callback = function() {
                $( "#extraP").trigger( "gameEditDone", [gameId]);
            };

            dataManager.request(deleteGameUrl+gameId, null, null, false, {'_token': $('#tokenCSRF').html()}, 'DELETE', callback)
        }

        function deleteHistory(id) {
            if (confirm("Etes-vous sûr de vouloir supprimer cette entrée ?") === false) {
                return false;
            }

            var callback = function() {
                $("#history").trigger("click");
            };
            
            dataManager.showTempMsg(true);
            dataManager.request(deleteHistoryUrl + id, null, null, false, {'_token': $('#tokenCSRF').html()}, 'DELETE', callback);
        }

        function deleteTradingHistory(id) {
            if (confirm("Etes-vous sûr de vouloir supprimer cette entrée ?") === false) {
                return false;
            }

            var callback = function() {
                $("#trading_history").trigger("click");
            };
            
            dataManager.showTempMsg(true);
            dataManager.request(deleteTradeHistoryUrl + id, null, null, false, {'_token': $('#tokenCSRF').html()}, 'DELETE', callback);
        }

        /**
         * Event listeners
         */

        // Game after edition
        $( "#extraP" ).on( "gameEditDone", function(event, gameId) {
            dataManager.showTempMsg(true);

            if (previousContext !== null) {
                dataManager.request(previousUrl, previousDisplayer, previousContext);
            } else {
                dataManager.request(gameDetailsUrl + gameId, game, 'gameEdit', true);
            }
        });

        // Return to game list
        $( "#extraP" ).on( "returnToGameListForThisPlaftorm", function(event, supportId) {
            dataManager.showTempMsg(true);
            dataManager.request(gameListByPlatformUrl + supportId, games, 'gamePerPlatform', true);
        });

        /** 
         * On startup
         */
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
            dataManager.request(platformListUrl, platforms, null);

            return false;
        });

        // Click on the various menu items listing games
        $('[id^="special-list"]').click(function() {
            var request = $(this).attr('id').substring(13);
            dataManager.showTempMsg(true);
            dataManager.request(gamesSpecialListUrl + request, games, request, true);

            return false;
        });

        // Click on the random menu
        $('[id^="random"]').click(function() {
            var request = $(this).attr('id').substring(7);
            dataManager.showTempMsg(true);
            dataManager.request(randomgameUrl + request, game, request, false);

            previousUrl = null;
            previousContext = null;
            previousDisplayer = null;

            return false;
        });

        // Click on the platform menu
        $('#history').click(function() {
            dataManager.showTempMsg(true);
            dataManager.request(getHistoryUrl, history, null);

            return false;
        });

        // Click on the trading menu
        $('#trading_history').click(function() {
            dataManager.showTempMsg(true);
            dataManager.request(getTradingHistoryUrl, trading, null);

            return false;
        });

        // Search form
        $('#searchForm').submit(function() {
            var url = gamesSpecialListUrl + 'search?query=' + $('#gameSearch').val();
            dataManager.showTempMsg(true);
            dataManager.request(url, games, 'gameSearch', true);

            return false;
        });

        // Add platform form
        $('#addPlatform').click(function() {
            dataManager.showTempMsg(true);
            dataManager.request(addPlatformUrl, platformEditor, 'add');

            return false;
        });

        // Add game form
        $('#addGame').click(function() {
            dataManager.showTempMsg(true);
            dataManager.request(addGameUrl, gameEditor, 'add');

            return false;
        });

        // Add history entry form
        $('#addHistory').click(function() {
            dataManager.showTempMsg(true);
            dataManager.request(addHistoryUrl, historyEditor, 'add');

            return false;
        });
        
        /** Content listeners */

        // Handle clicks on dynamically added links
        $("#content").on("click", "a", function(){
            var linkType = $(this).data('link-type');
            var id = $(this).attr('id').substring(6);

            if (linkType === 'gamePerPlatform') {
                var url = gameListByPlatformUrl + id
                var displayObject = games;
                var persist = true;
            } else if (linkType === 'gameDetails') {
                var url = gameDetailsUrl + id
                var displayObject = game;
                var persist = true;
            } else if (linkType === 'gameEdit') {
                var url = editGameUrl + id
                var displayObject = gameEditor;
                var persist = false;
            } else if (linkType === 'gameDelete') {
                // Specific use case since we do a DELETE instead of a GET
                deleteGame(id);

                return false;
            } else if(linkType === 'historyDelete') {
                deleteHistory(id);
                return false;
            } else if(linkType === 'tradingHistoryDelete') {
                deleteTradingHistory(id);
                return false;
            }else {
                return false;
            }

            dataManager.showTempMsg(true);
            dataManager.request(url, displayObject, linkType, persist);

            return false;
        });
    }
);
