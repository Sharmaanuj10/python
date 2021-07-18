aliens = [] # <---- list to define dictonary

# now lets make 15 alien

for alien_no in range(1,16):
    new_alien = {'color' : 'red' , 'speed' : 'slow' , 'point' : '5'}
    aliens.append(new_alien)

# here firtly the 'aliens' for value are copied in the 'alien' variable

for alien in aliens[:4]: # we call alien which are present in the list 'aliens'
   
    # now we take first four alien to modify them using if statement
    # if the alien color is red we change its value in first four copied value

    if alien['color'] == 'red':
        alien['color'] = 'green'
        alien['speed'] = 'medium'
        alien['point'] = '10'
   
   
for alien in aliens[:6]:
    
    # we again use the alien attribute to store the first 6 alien data and print (try another variable too) 
    
    print(alien)
