
#  firstly we are going to make sure the security
#  for that lets make a login portal for this

# firstly we need to import our only file here

userfile = open('username.txt')
Userdata = userfile.read()


passwordfile = open("password.txt")
secretpassword = passwordfile.read()

# Now lets user input now
Username = input("Enter username: ")
password = input("Enter Passowrd :")

Username = Username.capitalize()
# if we capitalize the user name error are solved easily

if (Username == Userdata and password == secretpassword):
    print("Hi")

    # now lets make a place where all the password are going to save
    # now we need to imprort the data where i make the storage
    # we can also write the code here also 

    import passworddata

else:
    print("Incorrect Username or Password ")



# quite complicated check out the versions after the 1.5
