#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: emersoncrp

import sys
import requests
import hashlib
from termcolor import cprint

def generar_hash_sha1(texto):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(texto.encode('utf-8'))
    convertidor_api(sha1_hash.hexdigest(), texto)

def convertidor_api(conver_password, texto):
    passwork_valor = conver_password[:5]
    passwork_busqueda = conver_password[5:]
    api_password(passwork_valor, passwork_busqueda, texto)

def api_password(password, busqueda, texto):
    password = password.upper()
    url = f"https://api.pwnedpasswords.com/range/{password}"
    response = requests.get(url)
    if response.ok:
        cadena = response.text
        array_datos = [linea.split(':') for linea in cadena.split('\n') if linea]
        busqueda = busqueda.upper()
        comparacion(array_datos, busqueda, texto)
    else:
        print(f"Error en la solicitud: {response.status_code}")

def comparacion(separado, busqueda, texto):
    for i in separado:
        if i[0] == busqueda and int(i[1]) >= 1:
            cprint(f"[-] Password: {texto} Coincidencia: {i[1]}" , "red", attrs=["bold"], file=sys.stderr)
            return
    cprint(f"[+] Password: {texto} Coincidencia: 0", "green", attrs=["bold"], file=sys.stderr)    


def main():
    """Función principal"""
    with open("../src/password.txt") as archivo:
        for linea in archivo:
            password = linea.strip()
            generar_hash_sha1(password)

if __name__ == "__main__":
    main()
