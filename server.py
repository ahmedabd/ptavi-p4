#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc = {}
    ultimadireccionSIP = ''
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            linea = line.decode('utf-8')
            linea_lista = linea.split()            
            print("El cliente nos manda " + linea)
            # Si no hay más líneas salimos del bucle infinito
            if not linea or  len(linea.split()) != 5 :
                break
            if len(linea.split()) == 5:
                if linea_lista[4] == '0':
                    (registro, self.ultimadireccionSIP, mensaje, expires, tiempo) = linea_lista
                    del self.dicc[self.ultimadireccionSIP]
                    print(self.dicc)
                elif linea_lista[4] > '0':
                    ip = self.client_address[0]
                    #print(ip)
                    (registro, self.ultimadireccionSIP, mensaje, expires, tiempo) = linea_lista
                    self.dicc[self.ultimadireccionSIP] = ip
                    print(self.dicc)

            
                

            

if __name__ == "__main__":
    PORT = int(sys.argv[1])
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
