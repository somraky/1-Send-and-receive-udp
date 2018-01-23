import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    recv, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", recv
    data = int(recv)
    factorial = 1
    while data>1:
        factorial *= data
        data = data-1
    print "send result:",factorial
    sock.sendto(str(factorial),addr)
    
