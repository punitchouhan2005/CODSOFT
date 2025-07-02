import random
import string
#different strings format 
p1 = string.ascii_lowercase
p2 = string.ascii_uppercase
p3 = string.digits
p4 = string.punctuation

#taking password length input from user
#length should be greater then or equal to digit
#plength = int(input("ENTER PASSWORD LENGTH (LENGTH>=8):"))
while (True) :
    plength = int(input("ENTER PASSWORD LENGTH (LENGTH>=8):"))
    if plength < 8 : 
     print("enter correct length") 
    else :
         break
         #use of list to store password(string format)
Password=[]
Password.extend(list(p1))
Password.extend(list(p2))
Password.extend(list(p3))
Password.extend(list(p4))
random.shuffle(Password)
print("YOUR STRONG PASSWORD IS :")
print("".join(Password[0:plength]))
