names = input("Enter your username: ")

from userdata_3 import usernames
from userdata_3 import passwords

for username in usernames:
        
    if username == names:                       
        passcode = input("Enter Password : ") 

        for password in passwords:
            if password == passcode:
                import passworddata

# make sure to not put the else statement in the loop other wise 
# it print the n times till it break

