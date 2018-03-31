#!/usr/local/bin/python
import socket

#change this to the other port number assigned to you
serverPort = 15004

#add your chat server code

def main():
   serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   serverSocket.bind((socket.gethostname(), serverPort))
   serverSocket.listen(5)

   print("The chat server is ready to receive. Listening on port: ", serverPort)
   while 1:
      (connectionSocket, addr) = serverSocket.accept()
      print("Connection accepted.\n")
      connectionSocket.close()


main();
