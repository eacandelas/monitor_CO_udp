import SocketServer
import shelve

FILE = '/tmp/CO_log'
HOST = ""
PORT = 2323

class cologger(SocketServer.BaseRequestHandler):

    def handle(self):
        reading = '0'
        data = self.request[0].strip().split(":")
        print "monitor: " + data[1]
        print "reading: " + data[0]
        db = shelve.open(FILE)
        if not 'readings' in db:
            db['readings'] = []
        readings = db['readings']

        if data[0] >= 0 and len(data) > 1:
            readings.append((data[1],data[0]))
	    
        db['readings'] = readings
        db.close()
       
        response= data[1] + ":" + data[0]
        socket = self.request[1]
        socket.sendto(response, self.client_address)

if __name__ == "__main__":
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), cologger)
    server.serve_forever()
