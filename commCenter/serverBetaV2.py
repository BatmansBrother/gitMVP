import socket, select
import multiprocessing
import time
import base64
import struct
import guiBETAV2


#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, userID, message):
        global CONNECTION_LIST
        global server_socket
    #Do not send the message to master socket and the client who has send us the message
        #lock.acquire()
    #for socket in CONNECTION_LIST:
        #if socket != server_socket and socket != sock :
        #print userID + message

        if 'FeildCam' in userID and 'txt' in message:
            message = ''
            try :
                sock.send('ack'+'\r') #tell feildCam it can now send the file
                #time.sleep(1)
                #print "Retreiving data..."
                write2file("Retrieving Data...")
                content = ''
                #time.sleep(1)

                while 1:
                    #print str(content)
                    content = sock.recv(1024)
                    if "[END]" in content:
                        break  #handshake flag
                time.sleep(1) ## NEED THIS HERE !!!! full one second
                #content = recv_msg(sock)  # file transfer
                #print str(content)
                f = open("/home/mccoll/gitMVP/commCenter/data/sessionData.txt","w")
                    #print "File opened..."
                write2file("File opened...")
                f.write(content)
                f.close()
                
                #print "File received!"
                write2file("File Recieved!")
                time.sleep(0.5) #NEED THIS HERE!!!
                #return None
            except :
                # broken socket connection maybe, chat client pressed ctrl+c for example
                sock.close() #socket.close()
                CONNECTION_LIST.remove(sock)#socket

        if 'FeildCam' in userID and 'jpeg' in message:
            
            try :
                sock.send('ack'+'\r') #tell feildCam it can now send the file
                time.sleep(0.1)
                t0 = time.time()
                print "Receiving encoded image..."
                content = ''
                content = recv_msg(sock)        
                decodedImage = base64.decodestring(content)
                with open("spsuOut.jpg","wb") as f:
                    #print "File opened..."
                    f.write(decodedImage)
                #f.close()
                print "File recieved..." + str(time.time()-t0)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                sock.close() #socket.close()
                CONNECTION_LIST.remove(sock)#socket
        else:
                return None
             #try :
                #sock.send(message+'\r')
             #except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                #sock.close()
                #CONNECTION_LIST.remove(sock)#socket
        #lock.release()

# send files
def send_msg(sock,msg):#,lock):
        #lock.acquire()
        # Prefix each message with a 4-byte length
        msg = struct.pack('>I',len(msg)) + msg
        sock.sendall(msg)
        #lock.release()
        
# recieve files
def recv_msg(sock):#,lock):
        #lock.acquire()
        # Read package length and unpack it into an integer
        raw_msglen = recvall(sock, 4)
        #print str(raw_msglen) + 'raw'
        if not raw_msglen:
                return None
        msglen = struct.unpack('>I',raw_msglen)[0]
        # Read data
        #lock.release()
        return recvall(sock,msglen)

def recvall(sock,n):
        data = ''
        while len(data) < n:
                #print str(len(data))
                packet = sock.recv(n - len(data))
                #print str(packet)
                if not packet:
                        return None
                data = data + packet
        return data


        
        
# serv() defined variables
CONNECTION_LIST = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def serv():
    # List to keep track of socket descriptors
    global CONNECTION_LIST
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000
    global server_socket
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("10.0.0.10", PORT))
    server_socket.listen(10)
    server_socket.settimeout(1)
    # List of client usernames

    # Add server socket to the list of readable connections
    
    #print "Communications server started on port: " + str(PORT)
    write2file("Communications server started on port: " + str(PORT))

    clientList = ['FeildCam', 'MobileMouse']
    # Authentifiaction ID list
    userDict = {}
    connections = len(CONNECTION_LIST)
    CONNECTION_LIST.append(server_socket)
    # Get the list sockets which are ready to be read through select
    while True:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        
        for sock in read_sockets:
        #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "\nCleint requesting connection..."
                broadcast_data(sock, "[%s:%s] awaiting request...\n" % addr,'')#,lock) #sockfd
            #Some incoming message from a client
            elif connections < len(CONNECTION_LIST) :
            # If there is a new client request check if there are on the list         
            # Data recieved from client, process it
                    authenticate = sock.recv(RECV_BUFFER)
                    
                    if authenticate in clientList:
                        print str(authenticate) + " Connected!"
                        #save client address to username
                        userDict[str(sock.getpeername())] = clientList[clientList.index(authenticate)]
                        connections=len(CONNECTION_LIST)
                    # reject client if userneame is inncorrect
                    else :
                        print "Client rejected: inncorrect key\n"
                        sock.close()
                        CONNECTION_LIST.remove(sock) #sock
                                 
            else:
                try:       
            # When a TCP program closes abruptly,
            # a "Connection reset by peer" exception will be thrown
                    
                    data = sock.recv(8)
                    
                    time.sleep(1)
                    if data:
                        broadcast_data(sock, '<' +  userDict[str(sock.getpeername())] + '>' ,  data)#,lock)
                    else:
                        data = ''

                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr,'')#,lock)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock) #sock
                    connections = len(CONNECTION_LIST)
                    continue

    server_socket.close()

def write2file(data):
    
    f = open("/home/mccoll/gitMVP/commCenter/data/serverData.txt","a")
    f.write(data +"\r\n")
    f.close()
    time.sleep(1)   



if __name__ == "__main__":


    lock = multiprocessing.Lock()
 

    guiProcess = multiprocessing.Process(target=guiBETAV2.guiProc)
    serverProcess = multiprocessing.Process(target=serv)
    guiProcess.start()
    serverProcess.start()
    
    '''
    while True:

        continue
    '''
    serverProcess.join()
    print 'fatal error'
    


       
