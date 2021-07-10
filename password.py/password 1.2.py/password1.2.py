# now in this we going to import directly and efficently 
# so lets imprt the data and reduce the file

from data_2 import password as ps   #ps meant passowrd in short
from data_2 import username as us   #us meant username in short

# Now lets user input now

Username = input("Enter username: ")
Username = Username.rstrip()

# rstrip is used to remove the spacing from after warth 
# .title is used to capitalize the data

password = input("Enter Passowrd :")
 
if us == Username and ps == password:
    
    # now lets make a place where all the password are going to save
    # now we need to imprort the data where i make the storage
    # we can also write the code here also which we are importing

    import passworddata

else:
    print("Incorrect Username or Password ")


