# pizza saga 😂
pizzas = ['pepporini', 'cheese', 'veg']
for pizza in pizzas:

    print(f'DEliever a {pizza}')

print('make sure to delever fast')

# now lets associate the my pizza list to pizza
mypizzas = pizzas
myfriendslist = mypizzas[:]
# i gave my list to him but if i add something in my list it doesnt change the friends list

mypizzas.append("butter")
myfriendslist.append("waffer")

print(myfriendslist)
print("\t\nsee!\n")
print(mypizzas)

