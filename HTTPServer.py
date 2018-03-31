#!/usr/local/bin/python
import socket

#change this to the port provided for you
serverPort = 15003

#add your web server code from the last assignment
#modify it to handle the chatroom
      
def main():
   serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   serverSocket.bind((socket.gethostname(), serverPort))
   serverSocket.listen(5)
   print("The server is ready to receive. Listening on port: ", serverPort)
   while 1:
      (connectionSocket, addr) = serverSocket.accept()
      print("Connection accepted.\n");

main();
