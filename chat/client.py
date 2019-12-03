# Python program to implement client side of chat room. 
import socket,pickle
import select 
import sys 
import RSA as RSA



dict_chaves ={}

#gerando a chave publica do servidor
n,e, toti,p ,q= RSA.keygen()
sendPublic =  str(n) + ',' + str(e)

#gera chave privada
d = RSA.calculate_private_key(toti,e)
print("A chave publica  gerada:{}".format(sendPublic))
print("A chave privada gerada: {} ,{},{} ".format(p,q,d))

def broadcast_cifrado(msg,dicionario):
    for clients in dicionario:
        e,n =converter_chave(dicionario[clients])
        msg_cifrada = RSA.cipher(msg,e,n)
        msg_cifrada = ','.join(str(x) for x in msg_cifrada)
        user = int(clients)
        server.sendto('>>'+ msg_cifrada,("127.0.0.1",user))



def RSA_decifra(word,n,d):

    msg_descifrada = '\r   '
    return msg_descifrada

def converter_chave(x):
    chave = x.split(',')
    e = int(chave[0])
    n= int(chave[1])
    return e,n


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))
key = 'key:'+sendPublic
print('enviando a minha chave publica ({}) para o outro cliente'.format(sendPublic))
server.send(key) 
print(server)





lista = []
while True: 

    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 


    """ There are two possible input situations. Either the 
    user wants to give manual input to send to other people, 
    or the server is sending a message to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048)

            lista.append(message)
           
            #print(publicForeignKey)
            if(type(message==type(server))):
                print('entrou')
                d = pickle.loads(message)
                print(type(d))
                #message = message.replace('key','')
                #dict_chaves = eval(message)
                #print(dict_chaves)

                
            else:
                msg_descifrada = RSA_decifra(message,n,d)
                print(message)
                sys.stdout.flush()
                print (msg_descifrada)
        else: 
            message = sys.stdin.readline()
            broadcast_cifrado(message,dict_chaves)
            #server.send(message)
            sys.stdout.write("<You>") 
            sys.stdout.write(message) 
            sys.stdout.flush()
            
server.close() 
