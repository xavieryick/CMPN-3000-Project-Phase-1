from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    message = input('Enter a sentence here (type exit to exit): ')
    clientSocket.send(sentence.encode())
    if sentence.lower() == 'exit':
        print('Exiting...')
        clientSocket.close()
        break
    else: 
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())