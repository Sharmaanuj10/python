active = True
print("if you want to quit type quit")
while active:
    
    message = input("Enter your message: ")
    if message == 'quit':
       # break # to break the loop here
        active = False
        #comtinue # to execute left over code exiting the if 
    else:
        print(message)
    
    