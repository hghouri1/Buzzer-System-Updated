################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer


myRequest = None
myflag = True
teamName = "No Team"
class RequestHandler_httpd(BaseHTTPRequestHandler):

  def do_GET(self):
    global myRequest
    global myflag
    global teamName
    

    
    if (myflag):
        myRequest = self.requestline
        myRequest = myRequest[5 : int(len(myRequest) - 9)]
        if (myRequest == "TeamA"):
            print(myRequest)
            teamName = "Team1"
            print(self.client_address)
            string = 'on'
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)
            myflag = False
        elif (myRequest == "teamB"):
            teamName = "Team2"
            print(myRequest)
            print(self.client_address)
            string = 'on'
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)
            myflag = False
        elif (myRequest == "teamC"):
            teamName = "Team3"
            print(myRequest)
            print(self.client_address)
            string = 'on'
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)
            myflag = False
        else :
            print(myRequest)
            print(self.client_address)
            string = teamName
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)
    else:
        myRequest = self.requestline
        myRequest = myRequest[5 : int(len(myRequest) - 9)]
        if (myRequest == "changeFlag"):
            myflag = True
            teamName = "No team"
            string = 'Changed flag successfully'
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)
        else:
            print(myRequest)
            print(self.client_address)
            string = teamName
            messagetosend = bytes(string,"utf")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(messagetosend))
            self.end_headers()
            self.wfile.write(messagetosend)

    return


server_address_httpd = ('192.168.0.108',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Server Started')
httpd.serve_forever()


