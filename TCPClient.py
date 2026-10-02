from socket import *
serverName = '127.0.0.1' # defining server name/ip
serverPort = 12000 # defining server port
clientSocket = socket(AF_INET, SOCK_STREAM) # creating client side socket
clientSocket.connect((serverName,serverPort)) # connecting the client side socket to the server
while True:
    message = input('Enter a sentence here (type exit to exit): ') # wait for inputs
    clientSocket.send(message.encode()) # send the encoded inputs
    if message.lower() == 'exit': # check for the word 'exit'
        print('Exiting...') # display that the program is exiting
        clientSocket.close() # closing client side socket
        break # breaks out of loop
    else: # message is not 'exit'
        modifiedMessage = clientSocket.recv(2048) # receive message with max size of 2048
        print('From server: ', modifiedMessage.decode()) # print message received