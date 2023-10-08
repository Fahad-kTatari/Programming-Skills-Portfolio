#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:30:02 2023

@author: FAHAD TATARI
Chapter 7 Ex5 Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.


"""

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")


describe_city("Islamabad", "Pakistan")
describe_city("Dubai", "UAE")
describe_city("Doha" , "Qatar")
