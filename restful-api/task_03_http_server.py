#!/usr/bin/python3

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """simple API"""
    
    def do_GET(self):
        """take request of GET path"""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(port=8000):
    """start HTTP server on port 8000"""
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Serveur démarré sur http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server(8000)