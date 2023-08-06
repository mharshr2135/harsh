import socket

c = socket.socket()
c.connect(('localhost',9999))
print("Start Texting")
while True
  mes = input()
  c.send(bytes(mes,'utf-8'))
  print(c.recv(1024).decode())
