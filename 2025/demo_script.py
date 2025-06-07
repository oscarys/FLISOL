#!/usr/bin/python

import os, json

DIRECTORIO = '/home/oys/FLISOL/2025/experimento'

clave = dict()

carpetas = os.listdir(DIRECTORIO)

for carpeta in carpetas:

    archivo = os.listdir(f'{DIRECTORIO}/{carpeta}')[0]
    nombre = archivo.split('-')[0].strip()

    with open(f'{DIRECTORIO}/{carpeta}/{archivo}', 'rt', encoding='windows-1250') as f:
        lineas = f.readlines()
        num_id = lineas[2].split(':')[1].strip()
        clave[num_id] = nombre
        lineas.pop(1)

    with open(f'{DIRECTORIO}/{carpeta}/{num_id}-Events.txt', 'wt', encoding='utf-8') as f:
        f.writelines(lineas)

    os.remove(f'{DIRECTORIO}/{carpeta}/{archivo}')
    os.rename(f'{DIRECTORIO}/{carpeta}', f'{DIRECTORIO}/{num_id}')

with open('clave_flisol.json', 'wt') as f:
    f.write(json.dumps(clave))
