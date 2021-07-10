guest = ['Ashish', 'Archit', 'Devesh']
# firstly add the guest list
print(
    f'\n\tHi! {guest[0]},{ guest[1]}, { guest[2]} you are invited in dinner with me.')

# now devesh said no so del the devesh and add ritesh to list
del guest[2]
guest.insert(2, 'ritesh')
# print the new guest list
print(
    f'\n\tHi! {guest[0]},{ guest[1]}, { guest[2]} you are invited in dinner with me.\n')

print(
    f'\n\tHi! {guest[0]},{ guest[1]}, { guest[2]} I found a new big dinning chair so i am invinting more.')
# Now i found a bigger so let invite some more friend using the insert to add the friend

guest.insert(0, 'rohit')
guest.insert(2, 'luchika')
# here i use append as i need to add it at last and not want to write more😁
guest.append('nitesh')

# at last print the final list
print(
    f'\nThe new list is: \n\t{guest[0]},\n\t{ guest[1]},\n\t{guest[2]},\n\t{guest[3]} ,\n\t{guest[4]},\n\t{guest[5]}')

# but now my dinner table not going ot arrive so lets remove some of them
# i am going to remove the person using the pop method

# make sure to pop the item in descending order other wise you are pop main item
# as if you pop one the 2 one become 1 so if you pop 2 that mean you pop '3'😱😒
# i use pop so i can also get what i removed so print the message to them only
guest3_pop = guest.pop(5)
print(f'sorry i am not able to invite you {guest3_pop}')

guest2_pop = guest.pop(2)
print(f'sorry i am not able to invite you {guest2_pop}')

guest1_pop = guest.pop(0)
print(f'sorry i am not able to invite you {guest1_pop}')

guest0_pop = guest.pop(2)
print(f'sorry i am not able to invite you {guest1_pop}')

print(f"\n\t{guest[0]} {guest[1]}  you are still invited")
# so now i invited Archit and Ashish


# but at end moment my wife said no dont invite any we invite every one not two of our friend
# so i agreee and now i use remove method
# guest0 = 'Ashish'
# guest1 = 'Archit'
# guest.remove(guest0)
# guest.remove(guest1)

### you can use both upper remove or lower remove
## guest.remove('Ashish')
## guest.remove('Archit')
#print(f'\n\t{guest} are invited i mean none')

# but now i going use the method del
del guest[1]
del guest[0]
print(f'\n\t{guest} are invited I mean none of you invited\n')
