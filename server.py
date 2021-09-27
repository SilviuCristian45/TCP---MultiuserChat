import socket
import threading


#input : message - string - the client's mesage which is sent to all other clients
#        otherClients - list - the list of other clients connected sockets stored 
def broadcast(message, otherClients, sender):
    msgToSend = message.encode("utf-8")
    for otherClient in otherClients:
        if otherClient != sender: #sender-ului nu-i mai trimitem mesajul
            otherClient.send(msgToSend)
        

#input : clientSock - socket - the client's socket which is used to receive data from that particular user 
def handleClient(clientSock, clients):
    while True:
        try:
            message = clientSock.recv(1024).decode("utf-8")
            broadcast(message, clients, clientSock)
        except:
            print("error handling client ")


def main():
    IPserver = socket.gethostbyname(socket.gethostname()) #adresa ip de pe pc-ul meu 
    maxConnections = 10 #maxim 10 useri 
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket-ul server-ului 
    PORT = 1026
    serverIsRunning = True
    clientsIP = []
    clientsNickNames = []

    serverSocket.bind( (IPserver,PORT) )
    serverSocket.listen(maxConnections)

    print("server is running ...")

    while serverIsRunning:
        clientSock,clientAddr = serverSocket.accept()
        print(f"Client with the ip {clientAddr} has connected to the server !!!")
        clientsIP.append(clientSock)
        
        clientSock.send("Nickname-ul tau este : ".encode("utf-8"))
        nickName = clientSock.recv(1024).decode("utf-8")

        clientsNickNames.append(nickName)
        
        broadcast(f" {nickName} a intrat pe chat. Bun venit !!! ", clientsIP, clientSock)

        thread = threading.Thread(target=handleClient, args=(clientSock, clientsIP))
        thread.start()
            

    return


if __name__ == "__main__":
    main()