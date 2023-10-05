#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:40:16 2023

@author: rzakir
Chapter3 Ex 2 Greetings 
"""

names = ["Sumaima", "Ahmed", "Ali", "Khalid", "Amir"]

message = "Hello {},you are an amazing person!"

for name in names:
    print(message.format(name))
