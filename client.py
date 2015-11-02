#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = sys.argv[1]
PORT = int(sys.argv[2])

# Contenido que vamos a enviar
REGISTER = sys.argv[3].upper()
USER = sys.argv[4]
EXPIRES = int(sys.argv[5])


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))


if sys.argv[3] == 'register':
    print("Enviando: " + REGISTER)
    print("Enviando: " + USER)
    my_socket.send((bytes(REGISTER + ' ' + 'sip:' + USER + ' ', 'utf-8') + b'SIP/2.0\r\n' + bytes('Expires:' + ' ' + str(EXPIRES), 'utf-8') + b'\r\n\r\n'))
    data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
