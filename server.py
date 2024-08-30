import http.server
import socketserver
from urllib.parse import unquote

PORT = 8080
FILENAME = "plaid_client.html"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/" + FILENAME
        elif self.path.startswith('/'):
            self.path = unquote(self.path)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = CustomHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
