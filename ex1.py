from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
    <head>
        <title>sample

        </title>
    </head>
    <body>
        <center><font color="blue" face="Lucida Handwriting" size="100">
        <b>List of Protocols in TCP/IP Model</b>
        </font></center>
        <font color="red">
        <h2>
            Application Layer - HTTP,FTP,DNS,Telnet<br>
            Transport Layer - TCP & UPD<br>
            Network Layer - IPV4/IPV6<br>
            Link Layer - Ethernet
        </h2>
        </font>
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