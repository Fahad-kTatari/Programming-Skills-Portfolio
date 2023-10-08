#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:48:59 2023

@author: FAHAD TATARI
Chapter 5 Ex 1 person
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

   
"""

person_info = {
    'first_name': 'Fahad',
    'last_name': 'Ali',
    'age': 36,
    'city': 'Germanay'}


print("First Name: " + person_info['first_name'])
print("Last Name: " + person_info['last_name'])
print("Age: " + str(person_info['age']))
print("City: " + person_info['city'])
