#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:25:11 2023

@author: FAHAD TATARI
chapter 1 Ex 5 computer area of circle
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print(f"The area of the circle with radius {radius} is {area:.2f}")
