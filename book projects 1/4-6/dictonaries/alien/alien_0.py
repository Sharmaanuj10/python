aliens = []

# now lets make 15 alien
for alien_no in range(1,16):
    new_alien = {'color' : 'red' , 'speed' : 'slow' , 'point' : '5'}
    aliens.append(new_alien)


# alien = aliens[:4] 
# print(f'{alien}\n') 

# you can also use this too

for alien in aliens[:4]:
    print(alien)

print('...')
