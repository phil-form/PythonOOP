import http.server as srv

server = srv.HTTPServer
handler = srv.CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']

srvAddr = ("", 8080)
httpd = server(srvAddr, handler)

httpd.serve_forever()