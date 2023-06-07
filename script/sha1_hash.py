#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: emersoncrp

import hashlib

def generar_hash_sha1(texto):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(texto.encode('utf-8'))
    return sha1_hash.hexdigest()

# Ejemplo de uso
texto = "1234"
hash_sha1 = generar_hash_sha1(texto)
print("Texto original:", texto)
print("Hash SHA1:", hash_sha1)
