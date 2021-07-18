name = {
    'Siren' : 'blue',
    'Anuj' : 'red',
    'Adi' : 'blue',
    'dream' : 'green',
    'sam' : 'purple'
}
# lets talk about the attribute of list like


# sorted, del, get, set , to acess key and value attribute


# del is used to delete ny pair of item in the list:

del name['Adi']
print(f'\n {name} \n')

# sorted is used to sort item temporarly

print(sorted(name))

# we add what we wan(t to sort key or value as follow

# in here it print all values of 'keys' or first set
print(sorted(name.keys()))

# in here it will print all the values of 'values'
print(sorted(name.values() ) )

# get is used to get item from list
# it is used to resolve conflict if we define a unknown key we can print message for it as:

print(name.get('jack' , 'no name found'))
# in here jack is not defined so it will print no name found the alternative value

# you can also store value in any variable 

actual_value = set(name.values())
print(actual_value)
# it going to remove every single repeat value

# for names in name:
#     print(names) # only key value printed

# for key , value in name.items():
#     print(key)
#     print(value)

# or
for names in name.keys(): # you can also use values attribute in here
    print(names)