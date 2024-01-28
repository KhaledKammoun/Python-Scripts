import http.server
import ssl
import os

server_address = ('localhost', 8000)
current_directory = os.path.dirname(os.path.abspath(__file__))
certfile_path = os.path.join(current_directory, 'C:\Windows\System32\server.pem')

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=certfile_path)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket)

print("Serving directory '{}' on https://{}:{}".format(current_directory, server_address[0], server_address[1]))
httpd.serve_forever()