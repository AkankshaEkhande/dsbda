import socket
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")    
print("RSA Server Side \n")
while True:
    c, address = s.accept()
    n, e = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    print("Recieved public key from client is n=%d,e=%d\n", (n,e))
    m=int(input("enter your message "))
    if int(m):
        k=(m**e)%n

    print("Encrypted data send is=  ", k)
    c.send(bytes(str(k), 'utf8'))
    M, S = [int(i) for i in c.recv(2048).decode('utf-8').split('\n')]
    M1=(S**e)%n
    if M == M1:
        print("As M = M1, Accept the sent by Alice")
    else:
        print("As M not equal to M1,Do not accept the message sent by Alice ")
    
    c.close()
