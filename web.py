from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>

    <table border=5>
        <tr>
            <th>Configuration</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>Processor</td>
            <td>I5</td>
        </tr>
        <tr>
            <td>Primary Memory</td>
            <td>16 GB RAM</td>
        </tr>
        
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()