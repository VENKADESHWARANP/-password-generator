import random
  
length=int(input("enter the length of the password:"))

small="abcdefghijklmnopqrstuvwxyz"

big="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers="1234567890"

symbols="@#$%&*!?~^+=<>"


all=big+small+numbers+symbols

password="".join(random.sample(all,length))

output=print("The password is=",password)