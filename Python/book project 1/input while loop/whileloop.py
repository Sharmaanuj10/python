message = ''

# you can use this for game to run as long as user want
while message != 'quit': 
    
    message = input('hi : ')
    # in her i use user input and store to number and pass through the loop Again
    
    if message != 'quit':
        print(message)
    
    elif message == 'quit':
        print('quiting...')
        print('Quited')