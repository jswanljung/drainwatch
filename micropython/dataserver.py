import socket

HOST =  ""
PORT = 50007

def listen():
    s =  socket.socket() 
    s.bind((HOST,  PORT))
    s.listen(1)
    conn,  addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
            
