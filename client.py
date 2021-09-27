import socket
import threading

nickNameBros = ""

def receiveMessages(client):
    global nickNameBros
    while True:
        messageReceived = client.recv(1024).decode("utf-8")
        if messageReceived == "Nickname-ul tau este : ": 
            nickNameBros = input(messageReceived)
            client.send(nickNameBros.encode("utf-8"))
        else :
            print(messageReceived)

def sendMessages(client):
    while True:
        message = nickNameBros + " : " + input("your message = \n")
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