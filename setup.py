#!usr/bin/env python

##################################################################
# setup.py                                                       #
# description: for running the web server honeypot               #
# author: @shipcod3                                              #
# greetz: ROOTCON goons                                          #
##################################################################

import SimpleHTTPServer, SocketServer

print """  
  _  _                   ___      
 | || |___ _ _  ___ _  _| _ \_  _ 
 | __ / _ \ ' \/ -_) || |  _/ || |
 |_||_\___/_||_\___|\_, |_|  \_, |
                    |__/     |__/  by @shipcod3
"""
def usage():
    print("USAGE: python setup.py <port>")  

def dnsmisconfig(argv):
    if len(argv) < 2:
        return usage()

    PORT = sys.argv[1]
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "HoneyPy running on", PORT
    httpd.serve_forever()

if __name__ == "__main__":
    main(sys.argv)
