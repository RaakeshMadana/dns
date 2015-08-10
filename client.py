import socket
import time

ip="127.0.0.1"
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.settimeout(5)
url=raw_input("Enter the URL\n")
while True:
    try:
        s.sendto(url,(ip,port))
        ipaddr,servaddr=s.recvfrom(1024)
        print ipaddr
        url=raw_input("Enter the URL")
    except:
        print "Retransmitting request"
        continue
