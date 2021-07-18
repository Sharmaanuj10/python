names = input("Enter your username: ")

from userdata_3 import usernames , passwords

for username in usernames:

     # here if the username and the names value are smae just ask for passowrd       

    if username == names:                       
        passcode = input("Enter Password : ") 
    
    #  after getting the passcode check wether the passowrd and passocde are equal
    
        for password in passwords:
            if password == passcode:
                
                # now just import the passowrd data where all the passowrd are in.
                import passworddata


# make sure to not put the else statement in the loop other wise 
# it print the n times till it break




# quite complicated check out the versions after the 1.5