#SERVER

import socket
import RPi.GPIO as GPIO
import time

UDP_IP = "192.168.43.95"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:
       data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

       print "\nGot connection from", addr
       print "\nConnection successfull"
       print "\nReceived URL : ", data

       print"\nLED ON"

       def blink(pin):
                GPIO.output(pin,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pin,GPIO.LOW)
                time.sleep(0.2)
                return

       GPIO.setmode(GPIO.BCM)
       GPIO.setwarnings(False)
       GPIO.setup(25, GPIO.OUT)

       for i in range(0,10):
                blink(25)

       print"\nLED OFF\n"

       GPIO.cleanup()

	   
	   

