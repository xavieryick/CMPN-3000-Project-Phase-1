from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The TCP server is ready to receive!')
connectionSocket, addr = serverSocket.accept()
while True:
    message = connectionSocket.recv(1024).decode()
    if message.lower() == 'exit':
        print('Exiting...')
        connectionSocket.close()
        break
    else:
        print('From client:', message)
        modifiedMessage = message.upper()
        print('To client:', modifiedMessage)
        connectionSocket.send(modifiedMessage.encode())