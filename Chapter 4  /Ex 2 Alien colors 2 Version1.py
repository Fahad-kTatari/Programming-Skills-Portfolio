#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:35:53 2023

@author: FAHAD TATARI
Chapter 4 Ex 2 Alien colors Version 1
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.


"""
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the green alien.")
else:
    print("You just earned 10 points for shooting the non-green alien.")
