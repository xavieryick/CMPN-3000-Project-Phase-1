from socket import *
serverPort = 12000 # define server port
serverSocket = socket(AF_INET, SOCK_DGRAM) # create server socket
serverSocket.bind(('', serverPort)) # bind the socket to the port

print('The UDP server is ready to receive!') # print when connection is found
while True:
    message, clientAddress = serverSocket.recvfrom(2048) # receive message from client
    receivedMessage = message.decode() # decode received message
    if receivedMessage.lower() == 'exit': # check for 'exit'
        print('Exiting...') # print that program is closing
        serverSocket.close() # closes socket
        break
    else: # message is not 'exit'
        print('From client:', receivedMessage) # print incoming message
        modifiedMessage = message.decode().upper() # modify message to be uppercase
        print('To client:', modifiedMessage) # print modified message
        serverSocket.sendto(modifiedMessage.encode(), clientAddress) # send modified message