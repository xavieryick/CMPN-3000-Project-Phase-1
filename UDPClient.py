from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Enter a sentence here (type exit to exit): ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    if message.lower() == 'exit':
        print('Exiting...')
        clientSocket.close()
        break
    else: 
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print('From server: ', modifiedMessage.decode())
