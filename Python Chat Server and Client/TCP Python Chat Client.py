#~~~~ PYTHON CHAT CLIENT
#~~~~ SOPHIE M. MAXWELL
#~~~~ 30153698
#~~~~ 14/05/2017

import socket, threading
#set variables
board = []#the board to store the message data
tLock = threading.Lock()#set the threading lock

#get the socket data
def getData(socket):

    tLock.acquire() #get the threading lock
    data = socket.recv(1024) #get a buffer of 1024 bytes
    print data # print the data
    board.append(data) # add the data to the board
    tLock.release() #release the threading lock
#main function of cha client 
def Main():
    #set the host and the port
    host = '127.0.0.1'#host ip
    port = 5000#port number

#if connecion successful, print message
    s = socket.socket() 
    s.connect((host, port)) #connect to the server
    print"You are connected to the server" #output a message
    while True:#while the user is connected to the server...

        rT = threading.Thread(target=getData, args=(s,))
        rT.start()
        rT.join()

        message = raw_input(" Please enter a message-> ")#ask user for message
        if message in ["quit","Q","q"]: #close the program if user inputs Q, q or quit
            s.close()
            break
        
        s.send(message)#send the message

        print board #print the message through displaying the board

if __name__ == '__main__':#run main
    Main()
