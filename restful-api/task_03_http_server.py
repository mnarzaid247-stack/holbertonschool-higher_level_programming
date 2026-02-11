#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class my_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain"; "charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain"; "charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            return
        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json"; "charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            body = json.dumps(info).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json"; "charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_response(404)
        self.send_header("Content-Type", "text/plain"; "charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

    def run(server_class=HTTPServer, handler_class=my_server, port=8000):
        server_address = ("", port)
        httpd = server_class(server_address, handler_class)
        print(f"Server running on http://localhost:{port}")
        httpd.serve_forever()
    if __name__ == '__main__':
        run()
