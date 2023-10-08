#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:24:05 2023

@author: FAHAD TATARI
Chapter 3 Ex 5 Change guest list
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""

invitees = ["Ahmed", "Ali", "Khalid"]

invitation_message = "Dear {},\n,I would appreciate if you would accept my invitation and come to dinner"

guest_cant_make_it = "Ali"

print("Ali can't make it to the dinner.")

invitees.remove(guest_cant_make_it)
new_invitee = "Zahid"
invitees.append(new_invitee)

for person in invitees:
    print(invitation_message.format(person))
