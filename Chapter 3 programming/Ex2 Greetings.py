#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:40:16 2023

@author: rzakir
"""

names = ["Sumaima", "Ahmed", "Ali", "Khalid", "Amir"]

message = "Hello {},you are an amazing person!"

for name in names:
    print(message.format(name))