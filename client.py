import socket

cliente = socket.socket()
cliente.connect(('localhost', 21567))

cuit = input('Ingrese la CUIT:\t')
try:
    cliente.send(cuit.encode())
    respuesta = cliente.recv(1024).decode()

    print (respuesta)
    
finally:
    print('Fin de conexion')
    cliente.close()