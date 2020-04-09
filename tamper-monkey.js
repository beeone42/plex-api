// ==UserScript==
// @name         Plex Api
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Add "auto-update" link on plex web interface when server update is available !
// @author       You
// @match        https://my-plex-server-url/web/index.html
// @grant        none
// @require http://code.jquery.com/jquery-3.4.1.min.js
// ==/UserScript==

(function() {
    'use strict';

    setTimeout(function(){
	$("div.server-update-alert-bar a.skip-version-link").after(
	    "<a class='link' href='https://my-plex-server-url/api/plex-api-key-please-change-me/update' target='_blank'>auto-update</a>"
	);
    }, 1000);

})();
