import http.server
import socketserver
port =55555
ip ="127.0.0.1"
karim=http.server.SimpleHTTPRequestHandler
server =socketserver.TCPServer((ip,port),karim)
def run():
    print("serving at port",port)
    server.serve_forever()
run()

