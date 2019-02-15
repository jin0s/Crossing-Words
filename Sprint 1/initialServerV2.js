var http = require('http');

var fs = require('fs');
var htmlFile;
var cssFile;

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

var server = http.createServer(function (request, response) {
    switch (request.url) {
        case "/index.css" :
            response.writeHead(200, {"Content-Type": "text/css"});
            response.write(cssFile);
            break;
        default :    
            response.writeHead(200, {"Content-Type": "text/html"});
            response.write(htmlFile);
    }
    });
    response.end();


//Listen on port 8000, IP defaults to 127.0.0.1
server.listen(8000);


console.log("Server running at http://127.0.0.1:8000/");
