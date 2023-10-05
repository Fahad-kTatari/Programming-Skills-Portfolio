#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:25:11 2023

@author: rzakir
chapter 1 Ex 5 computer area of circle
"""

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print(f"The area of the circle with radius {radius} is {area:.2f}")
