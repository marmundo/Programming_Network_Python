import socket,os

path=os.getcwd()
print("Você está na pasta ",path)
answer=input("Você deseja fazer o backup desta pasta? (s/n)")

if answer=='n':
	path=input("Digite o caminho da pasta")
	os.chdir(path)


#Creates TCP socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connects with server
#sock.connect(("127.0.0.1",1060))

list_files = os.listdir(path)	

for file in list_files:
	sock.connect(("127.0.0.1",1060))
	if os.path.isfile(file) and 	file!=".DS_Store":
		#Opens the file in read and byte mode
		file_acess=open(file,"r+b")
		file_name=file_acess.name
		print(file_name)
		sock.sendall(file_name.encode("utf-8"))
		sock.close()
		#read file
		#file_data=file_acess.read()
		#send file to server
		#sock.sendall(file_data)
#closes socket
print("Arquivo enviado")
sock.close()