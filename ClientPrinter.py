#CLIENT

import socket

UDP_IP = "192.168.43.95"
UDP_PORT = 5005
MESSAGE = "www.google.com"
   
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
   
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))	   
	   
	   