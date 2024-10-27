#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(4):
    print("Sending request %s …" % request)
    socket.send_string("This is a message from CS361")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))