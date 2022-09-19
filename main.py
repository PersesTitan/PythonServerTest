from http.server import HTTPServer, BaseHTTPRequestHandler
import read_file


class HTTPRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(read_file.op("index.html").encode('UTF-16'))

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_len)
        value = post_data.decode("UTF-16")


http = HTTPServer(("localhost", 8080), HTTPRequest)
http.serve_forever()
