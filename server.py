import SocketServer
import shelve

FILE = '/tmp/CO_log'
HOST = ""
PORT = 2323

class cologger(SocketServer.BaseRequestHandler):

    def handle(self):
        tx = 'error'
        data = self.request[0].strip().split(":")
        db = shelve.open(FILE)
        if not 'readings' in db:
            db['readings'] = []
        readings = db['readings']

        if data[0] == "store" and len(data) > 3:
            readings.append(data[2], data[1])
            tx = 'stored'
        elif data[0] == 'read':
            tx = reading.pop() 
	    
        db['readings'] = readings
        db.close()

        socket = self.request[1]
        socket.sendto(tx, self.client_address)

if __name__ == "__main__":
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), cologger)
    server.serve_forever()
