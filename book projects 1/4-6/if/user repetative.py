# now lets check whether the username are not repetative
# so current user are

current_users = ['ashish','lokesh','maria','george','dream']

# new users are which are new sign in:
new_users = ['George', 'kinda','dream', 'mosh','aditya'] 

upper_current_user = current_users[:]
# now i copy the current user data at the upper current user

for users in current_users: # dont use the upper current user other wise it became infinte loop

     # now capitalize and store so i can add them to list of user
    capitalize_user = users.title()
    uppercase_users = users.upper()
    
    # add both list attribute in the list

    upper_current_user.append(uppercase_users)
    upper_current_user.append(capitalize_user)

# now lets take one user at a time from new user to check
for user in new_users:
        
     # here the user from new users if present 'in' upper current users it undergo this
    
    if  user in upper_current_user:
        print(f'\n{user} username is not available')

    else:
        print(f'\n{user} username is  available')