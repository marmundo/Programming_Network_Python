import socket

#Creates socket tcp
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Set the socket to reuse the same address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#Sets ip and port
server_socket.bind(("127.0.0.1",1060))
#Sets how many clients to listen at the same time
server_socket.listen(1)


#Procedure to receive the file
while True:
	#Tcp handshaking
	sc_data,sockname=server_socket.accept()
	print("Receiving from ",sockname[0]," ,",sockname[1])
	file_name=""
	while True:
		#receives 1024 bytes each
		file_n=sc_data.recv(123)
		
		#in case to processed all the file break while
		if not file_n:
			break
		file_name=file_name+file_n.decode("utf-8")
	file_name=file_name+".bak"
	print(file_name)
	#Open file in append and byte mode
	file=open(file_name+".bak","ab")
	

	#while True:
	#	print("Receiving file content")
		#receives 1024 bytes each
	#	data=sc_data.recv(1024)
		#write received data in file
	#	file.write(data)
		#in case to processed all the file break while
	#	if not data:
	#		break
	#print("Closing File")		
	file.close()