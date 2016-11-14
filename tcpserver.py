import socket
import sys
 
HOST = '127.0.0.1'   
PORT = 4000

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created' 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening on port' + ' ' +str(PORT)
 
while 1:   
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])     
    data = conn.recv(4096)       
    print data      
    conn.sendall(data) 
    conn.close()
    
s.close()
