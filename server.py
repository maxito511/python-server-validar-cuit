import socket
from socket import * 
from time import ctime


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR =(HOST, PORT)

tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(ADDR)
tcpsersock.listen(5)

def esCUITValida(cuit):
    """
    Funcion destinada a la validacion de CUIT
    """
    # Convertimos el valor a una cadena
    cuit = str(cuit)
    # Aca removemos guiones, espacios y puntos para poder trabajar
    cuit = cuit.replace("-", "") # Borramos los guiones
    cuit = cuit.replace(" ", "") # Borramos los espacios
    cuit = cuit.replace(".", "") # Borramos los puntos
    # Si no tiene 11 caracteres lo descartamos
    if len(cuit) != 11:
        return False, cuit
    # Solo resta analizar si todos los caracteres son numeros
    if not cuit.isdigit():
        return False, cuit
    # Despues de estas validaciones podemos afirmar
    #   que contamos con 11 numeros
    # Aca comienza la magia
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    elif aux == 10:
        aux = 9
    if int(cuit[10]) == aux:
        return True, cuit
    else:
        return False, cuit

while True:
    print("Experando por una conexion")
    tcpclisock, addr = tcpsersock.accept()
    print("Conectado con: "),addr

    while True:
        data = tcpclisock.recv(BUFSIZ)
        demo = esCUITValida(data)
        if not demo[0]:
            tcpclisock.send('[%s] %s' %(ctime(), 'No parece ser un CUIT valido, por favor vuelva a ingresarlo'))  
        else:
            tcpclisock.send('[%s] %s' %(ctime(), 'Es un numero de CUIT valido'))
            break

    tcpclisock.close()

