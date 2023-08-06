import socket

s1 = socket.socket()
print("connected to client1")
s1.bind(('localhost',9999))
s1.listen(3)

s2 = socket.socket()
print("connected to client2")
s2.bind(('localhost',9998))
s2.listen(3)

while True:
    c1,addr1 = s1.accept()
    mes1 = c1.recv(1024).decode()
    print("Connected with", addr2,mes2)

    c2,addr2 = s2.accept()
    mes2 = c2.recv(1024).decode()
    print("Connected with", addr1,mes1)
    
    #c.send(bytes("welcome",'utf-8'))
    c.close()
