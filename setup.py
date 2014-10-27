#!usr/bin/env python

##################################################################
# setup.py                                                       #
# description: for running the web server honeypot               #
# author: @shipcod3                                              #
# greetz: ROOTCON goons                                          #
##################################################################

import sys, SimpleHTTPServer, SocketServer

print """  
  _  _                   ___      
 | || |___ _ _  ___ _  _| _ \_  _ 
 | __ / _ \ ' \/ -_) || |  _/ || |
 |_||_\___/_||_\___|\_, |_|  \_, |
                    |__/     |__/  by @shipcod3
"""
class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def usage():
    print("USAGE: python setup.py <port>")  

def main(argv):
    if len(argv) < 2:
        return usage()

    PORT = int(sys.argv[1])
    Handler = ServerHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()

if __name__ == "__main__":
    main(sys.argv)
