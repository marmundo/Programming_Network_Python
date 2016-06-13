import socket

#Creates TCP socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connects with server
sock.connect(("127.0.0.1",1060))

#Opens the file in read and byte mode
file=open("teste.txt","r+b")
#read file
file_data=file.read()
#send file to server
sock.sendall(file_data)
#closes socket
sock.close()