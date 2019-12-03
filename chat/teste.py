'''
import RSA as RSA
dicti = {53330: '1271,947', 53332: '1271,947', 53334: '1271,947'}


def converter_chave(x):
    chave = x.split(',')
    e = int(chave[0])
    n= int(chave[1])
    return e,n



def broadcast_cifrado(msg,dicionario):
    for clients in dicionario:
        e,n =converter_chave(dicionario[clients])
        msg_cifrada = RSA.cipher(msg,e,n)
        msg_cifrada = ','.join(str(x) for x in msg_cifrada) 
        print(msg_cifrada)

msg='oi'
broadcast_cifrado(msg,dicti)
'''
lista = ['key:1691,1027', 'key:817,641', 'key:1147,1051']
publicForeignKey = filter(lambda x: 'key' in x, lista)
print(publicForeignKey)
