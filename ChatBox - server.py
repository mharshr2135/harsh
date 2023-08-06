import socket

s1 = socket.socket()
print("socket created")
s1.bind(('localhost',9999))
s1.listen(3)

while True:
    c1,addr1 = s1.accept()
    mes1 = c1.recv(1024).decode()
    print("Connected with", addr1,mes1)

    #c.send(bytes("welcome",'utf-8'))
    c.close()
