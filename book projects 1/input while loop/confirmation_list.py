# Start with users that need to be verified and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candice']

confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # here the pop user store in the current user
 
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    # and now the poped user added to the list using the append method

# to dsplay all confirmed users.
print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    # title to capatilize the first letter