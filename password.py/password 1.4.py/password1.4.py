names = input("Enter your username: ")

from userdata_4 import usernames , passwords


def webdata():
    webdata= input("Enter the key word : ")
    names = {
        'youtube' : 'subscribe', # here now you can  save  infinte number of password 
        'twitter' : 'qwerty',
        # '' : '',
        # I created many string to store the data
        
    }

    print(names.get(webdata))
    # here the attribute '.get' get the data from the names;


for username in usernames:

   if username == names:                       
        passcode = input("Enter Password : ") 
    
      
        for password in passwords:
            if password == passcode:
                
               # now get the webdata function .
               webdata()


# make sure to not put the else statement in the loop other wise 
# it print the n times till it break


