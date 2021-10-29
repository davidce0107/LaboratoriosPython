# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:26:52 2021

@author: David Campos Espinoza
"""

def piramid(char, value):
    fila = 0
    contador = 1
    while fila < value:
        print(contador * str(char))
        contador +=1
        fila += 1
    
   
piramid('F', 5)