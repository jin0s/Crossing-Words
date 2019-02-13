// Load the http module to create an http server.
var http = require('http');

// Configure our HTTP server to respond with a glorious centaur with wings to all requests.
var server = http.createServer(function (request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("                 | __\n--==/////////////[})))==*\n                 / | '          ,|\n                    `|`|      //|                             ,|\n                      | `|  //,/'                           -~ |\n   )             _-~~~|  |/ / |'|                       _-~  / ,\n  ((            /' )   | | / /'/                    _-~   _/_-~|\n (((            ;  /`  ' )/ /''                 _ -~     _-~ ,/'\n ) ))           `~~|   `||/'/|'           __--~~__--| _-~  _/, \n((( ))            / ~~    | /~      __--~~  --~~  __/~  _-~ /\n ((|~|           |    )   | '      /        __--~~  |-~~ _-~\n    `|(|    __--(   _/    |'|     /     --~~   __--~' _-~ ~|\n     (  ((~~   __-~        |~|   /     ___---~~  ~~|~~__--~ \n      ~~|~~~~~~   `|-~      |~| /           __--~~~'~~/\n                   ;| __.-~  ~-/      ~~~~~__|__---~~ _..--._\n                   ;;;;;;;;'  /      ---~~~/_.-----.-~  _.._ ~|     \n                  ;;;;;;;'   /      ----~~/         `|,~    `| |        \n                  ;;;;'     (      ---~~/         `:::|       `||.      \n                  |'  _      `----~~~~'      /      `:|        ()))),      \n            ______/|/~    |                 /        /         (((((())  \n          /~;;.____/;;'  /          ___.---(   `;;;/             )))'`))\n         / //  _;______;'------~~~~~    |;;/|    /                ((   ( \n        //  | |                        /  |  |;;,|                 `   \n       (<_    | |                    /',/-----'  _> \n        |_|     ||_                 //~;~~~~~~~~~ \n                 |_|               (,~~ \n                                    |~|\n                                     ~~\n");
});

// Listen on port 8000, IP defaults to 127.0.0.1
server.listen(8000);

// Put a friendly message on the terminal
console.log("Server running at http://127.0.0.1:8000/");
