#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:53:11 2023

@author: FAHAD TATARI
Chapter 3 Ex 4 Guest List
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d

like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.


"""
invitees = ["Ahmed", "Ali", "Khalid"]

invitation_message = "Dear {},\n i would appreciate if you would accept my invitation and come to dinner

for person in invitees:
    print(invitation_message.format(person))
