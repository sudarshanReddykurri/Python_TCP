import socket
import sys
from thread import *
 
HOST = '127.0.0.1'   
PORT = 9998 
 
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'
s.bind((HOST, PORT))   
print 'Socket bind complete'
s.listen(4)
print 'Socket now listening on port'+' '+ str(PORT)
def clientthread(conn):   
    conn.send('Value')    
    while True:       
        data = conn.recv(1024)                  
        conn.sendall(data)    
    conn.close() 

while 1:    
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])    
    start_new_thread(clientthread ,(conn,))
 
s.close()
