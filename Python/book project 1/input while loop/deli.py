user_want = {}
# fistly define a dictonairy empty

poll_active = True

while poll_active:

    name = input('Enter your name: ')
    want = input('if you visit one place in the world where you visit? ')
    repeat = input('waant to know others wnats (yes,no)? ')

    # after input store the data at dictionary user_want    
    user_want[name] = want
    
    # but user dont want to know about other if he/she type no so to stop the loop we can do:
    if repeat == 'no':
        poll_active = False


# at last we take keys and values form the user_want dictionary and just print them 
   
for names,wants in user_want.items():
    print(f'\tHi! {names} you want to visit {wants}')    