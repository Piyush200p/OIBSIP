import random
import string
character=input("Enter (y/n) if you wwant to use character :")
digit=input("Enter (y/n) if you wwant to use digit :")
symbole=input("Enter (y/n) if you wwant to use symbole :")
k = int(input("Enter the length of password :"))
pp=''
if(character=="y"):
    pp+=string.ascii_letters
if(digit=="y"):
    pp+=string.digits
if(symbole=="y"):
    pp+=string.punctuation
if(pp==""):
    print("No Choice selected")
password="".join(random.choices(pp, k=k ))
print("Generated Password :",password)