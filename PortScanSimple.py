#!/usr/bin/env python3

import socket
import sys
from termcolor import colored


host = input('Dime la ip a escanear: ')
startport = int(input('Dime el puerto inicial: '))
finishport = int(input('Dime el puerto final: '))

puertos_abiertos = []

for puerto in range (startport, finishport + 1):
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.settimeout(0.5)
    resultado = conexion.connect_ex ((host, puerto))
    if resultado == 0:
        puertos_abiertos.append(puerto)
        print (colored(f'El puerto {puerto} está abierto.', 'red'))
        conexion.close()
    else:
        print (colored(f'El puerto {puerto} está cerrado.', 'green'))

print (colored(f'Los puertos abiertos son: {puertos_abiertos}', 'yellow'))




