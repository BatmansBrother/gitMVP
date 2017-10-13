import socket
import sys
import select
import time
import base64
import struct
#import cv2
#import picamera


my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(("10.0.0.2",5000))
my_socket.send("FeildCam")
#sys.stdout.write('your message: ')
time.sleep(1)
my_socket.send("\r\n")
#sys.stdout.flush()
#camera = picamera.PiCamera()

def txt():
            confirm = ''
            print "requesting file transfer..."
            while True:
                  confirm = my_socket.recv(4096)
                  if "ack" in confirm:
                    break
            print "request permitted!"
            with open("foo.txt") as f:
                  #line = f.read()
                  line = f.read()
                  f.close()
                  print str(line)
                  #send_msg(my_socket,line)
                  my_socket.send(str(line)+"\r")
                  my_socket.send("[END]" + "\r")
                  #send_msg(my_socket,line)
                  #my_socket.send(line+'\r\n')
            print "File sent"
            time.sleep(1)
            #my_socket.send('\r\n')
            #send_msg(my_socket,'\n\r')

def getPic():

            
            t0 = 0
            t = 5
            while t0 < t:
                        print(t)
                        time.sleep(1)
                        t = t-1
            camera.capture(course.jpg)
            print('done')

            
def jpeg():
           # getPic() # iiiiiiii
            
            confirm = ''
            print "requesting image transfer..."
            while True:
                  confirm = my_socket.recv(4096)
                  if "ack" in confirm:
                    break
            print "request permitted"
            with open('spsuIn.jpg','rb') as image:
                with open('encoded.txt','wb') as efw:
                  imageRead = image.read()
                  encodedImage = base64.encodestring(imageRead)
                  efw.write(encodedImage)
                  efw.close()
                  image.close()
                  send_msg(my_socket,encodedImage)
                  
            print "Image sent"

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
        if not raw_msglen:
                return None
        msglen = struct.unpack('>I',raw_msglen)[0]
        # Read data
        #lock.release()
        return recvall(sock,msglen)

def recvall(sock,n):
        data = ''
        while len(data) < n:
                packet = sock.recv(n - len(data))
                if not packet:
                        return None
                data = data + packet
        return data
            
while True:
            r, w, x = select.select([sys.stdin, my_socket], [], [])
            if not r:
                continue
            if r[0] is sys.stdin:
                message = raw_input()
                if message == "quit":
                    my_socket.close()
                    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    my_socket.connect(("192.168.1.14",5000))
                    my_socket.send("FeildCam")
                    my_socket.close()
                    break
                if message == "txt":
                    my_socket.send(message)
                    txt()
                    sys.stdout.flush()
                if message == "jpeg":
                    my_socket.send(message)
                    jpeg()
                    sys.stdout.flush()
                else:    
                    my_socket.send(message)
                sys.stdout.write('your message: ')
                sys.stdout.flush()
            '''else:
              try:
                data = my_socket.recv(4096)
                print data
                sys.stdout.flush()
              except:
                continue
            '''
