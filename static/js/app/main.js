/**
 * Main Require JS File
 * @author Eric COURTIAL <e.courtial30@gmail.com>
 */
requirejs.config({
    // Define variable like main URL, libraries
    baseUrl: "/js",
    paths: {
        "jquery": "vendor/jquery-3.2.1.min",
        "bootstrap": "vendor/bootstrap",
        "content": "pages/content",
        "platforms": "pages/platforms",
        "games": "pages/games",
        "game": "pages/game",
        "home": "pages/home",
        "tools": "app/tools",
        "platformEditor": "forms/platform"
    },
    // Define dependencies between modules and libraries, and the order of loading
    shim: {
        "bootstrap": {
            deps: ["jquery"], // Require jQuery
            exports: "$" // Alias
        },
    }
});

// Load modules and libraries required on the whole website
require(["jquery", "bootstrap"]);
