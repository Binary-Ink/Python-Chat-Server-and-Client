#~~~~ CHAT SERVER
#~~~~ SOPHIE M. MAXWELL
#~~~~ 30153698
#~~~~14/05/2017

#import the socket
import socket, select

#send messages to all connected clients, do not send data to server or client who sent message
def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:#for each person
        if socket != server_socket and socket != sock :#if other users attempt to send the message
            try :
                socket.send(message)#try and send the message
            except :
                # socket connection may be broken, remove socket
                socket.close()#close the socket
                CONNECTION_LIST.remove(socket)#remove the connection
 
if __name__ == "__main__": #run main
    
    CONNECTION_LIST = []#list containing sockets
    PORT = 5000#port number
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.setblocking(0)
    server_socket.listen(10)
    
    CONNECTION_LIST.append(server_socket)#add the server socket to list of connections
    #display port number
    print "Chat server started on port " + str(PORT)
      # list sockets which are ready to be read 
    while True:
    
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[]) 
        for sock in read_sockets:
            # recieve new connection through server_socket
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr                 
                broadcast_data(sockfd, "Player 1")             
            #incoming messages from client
            else:
                try:
                    data = sock.recv(4096)
                    if data:
                        broadcast_data(sock, data)                
                 #display if client offline
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    #remove the socket
                    CONNECTION_LIST.remove(sock)
                    continue
     #close server socket
    server_socket.close()


