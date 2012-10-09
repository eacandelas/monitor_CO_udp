import SocketServer
import shelve
import os


FILE = '/home/eden/CO_log'
HOST = '192.168.100.122'
PORT = 2323

class cologger(SocketServer.BaseRequestHandler):

    def handle(self):
        reading = '0'
        data = self.request[0].strip().split(":")
        print data[0]
        print data[1]
        reading = data[0]
        db = shelve.open(FILE)
        db['readings'] = reading
        db.close()
        
        response = data[0]+ ":" + data[1]  
        socket = self.request[1]
        socket.sendto(response, self.client_address)

if __name__ == "__main__":
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), cologger)
    print HOST
    print PORT
    server.serve_forever()
