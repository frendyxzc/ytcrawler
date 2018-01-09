"use strict"
var system = require("system");

if(system.args.length < 2){
    console.log("Usage : phantomjs search.js <youtube-keyword in quotation marks>");
    phantom.exit();
} else{
    var query = system.args[1];
    var url = "https://www.youtube.com/results?search_query="+ encodeURI(query);
    console.log(query);
    var pagex = require("webpage").create();
    pagex.open(url, function(status){
        //console.log("Test : "+status);
        var x = pagex.evaluate(function() {
           console.log("Evaluate");
           return [].map.call(document.querySelectorAll('img'), function(link) {
            var y = {
              href : link.getAttribute('src'),
            };
            return y;
           });
        });
        
        for(var i in x){
	        if(x[i].href.indexOf('ggpht') != -1) {
				console.log(x[i].href);
	        }
        }
        
        console.log('#####');
        phantom.exit();        
    });
}