import socket
import sys
 
HOST = '127.0.0.1'   
PORT = 9998
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created' 

s.connect((HOST, PORT))
try:    
    message = 'This is the message.  It will be repeated.'
    print  'sending' + message 
    data = s.recv(16)   
    print 'received' + data
    s.sendall(data)

except socket.error:   
    print 'Send failed'
    sys.exit()
    
s.close()
