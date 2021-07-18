topping = ''
toppings = []
print('if you want to stop type quit')

while topping != 'quit':

    topping = input("enter the topping : ")
    
    # toppings.append(topping)
    # you can also use this
    toppings.insert(1,topping)
    
    if topping != 'quit':
        print(topping)
        
print(f' Your toppings are:')
for toppin in toppings:
    print(f'\t\t{toppin}')
    