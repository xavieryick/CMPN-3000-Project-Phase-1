from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('The UDP server is ready to receive!')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    receivedMessage = message.decode()
    if receivedMessage.lower() == 'exit':
        print('Exiting...')
        serverSocket.close()
        break
    else:
        print('From client:', receivedMessage)
        modifiedMessage = message.decode().upper()
        print('To client:', modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)