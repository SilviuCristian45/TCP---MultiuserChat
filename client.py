import socket
import threading


def receiveMessages(client):
    while True:
        messageReceived = client.recv(1024).decode("utf-8")
        print(messageReceived)

def sendMessages(client):
    while True:
        message = input("your message = \n")
        client.send(message.encode("utf-8"))

def main():
    IP = socket.gethostbyname(socket.gethostname()) #adresa ip de pe pc-ul meu 
    PORT = 1026
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect( (IP,PORT) )

    tRecv = threading.Thread(target= receiveMessages, args= (clientSocket,))
    tSend = threading.Thread(target= sendMessages, args= (clientSocket,))

    tRecv.start()
    tSend.start()

    return



if __name__ == "__main__":
    main() 