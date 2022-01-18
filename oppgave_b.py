# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:04:05 2021

@author: Erlend Tøssebro
"""

alder = int(input("Alder: "))
if alder < 18 or alder >= 67:
    print("Pris: 20 kr.")
else:
    print("Pris: 40 kr.")

