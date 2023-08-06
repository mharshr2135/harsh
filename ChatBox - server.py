import socket

s = socket.socket()
print("socket created")
s.bind(('localhost',9999))
s.listen(3)

while True:
    c,addr = s.accept()
    mes1 = c.recv(1024).decode()
    print("Connected with", addr,mes1)

    c.send(bytes("welcome",'utf-8'))
    c.close()
