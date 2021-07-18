name = input("Enter your username: ")
passcode = input("Enter you password: ")

#  upper is used to capatilize  the latter
name = name.upper()

#  all the password saved 
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

# username and their passwords 
userdata = {
    'ANUJ' : 'lol',
    'ANUJ SHARMA' : 'use',
    '' : ''
}

# now we looped the dictonairy and get the keys and values or username and password to check
for username , password in userdata.items():
   
#    In this case if the name == username we enter so it check wether passcode is equal or not
    if name == username:
    
        if passcode == password:
     
     # now the user is verified so we import the webdata or passowords data
            webdata()

# in this the the username and passowrd are linked so they are not going to mess with each other like older have


# Note : still it have a problem can you find out what??🧐🧐