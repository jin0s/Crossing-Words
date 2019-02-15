var http = require('http');

var fs = require('fs');
var htmlFile;
var cssFile;
var jsFile;

fs.readFile('./index.html', function(err, data) {
    if (err){
        throw err;
    }
    htmlFile = data;
});

fs.readFile('./index.css', function(err, data) {
    if (err){
        throw err;
    }
    cssFile = data;
});

fs.readFile('./index.js', function(err, data) {
    if (err){
        throw err;
    }
    jsFile = data;
});

var server = http.createServer(function (request, response) {
    switch (request.url) {
        case "/index.css" :
            response.writeHead(200, {"Content-Type": "text/css"});
            response.write(cssFile);
            break;
       case "/index.js" :
            response.writeHead(200, {"Content-Type": "text/js"});
            response.write(jsFile);
            break;
        default :    
            response.writeHead(200, {"Content-Type": "text/html"});
            response.write(htmlFile);
    }
        response.end();
});



//Listen on port 8000, IP defaults to 127.0.0.1
server.listen(8000);


console.log("Server running at http://127.0.0.1:8000/");
