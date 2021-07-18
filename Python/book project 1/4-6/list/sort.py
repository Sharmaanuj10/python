# i want sort my car name temporaryly so lets sort using sorted  method
cars = ['mercedes', 'audi', 'koienseg', 'devil16']
print("\n")
print(sorted(cars))

# lets check my cars order a sorted temporarly or not
print(cars)


# In this i printed the cars in reverse order
# but i want to check how many cars i have so use len method

print(len(cars))

# now i can sort the name permanantly
cars.sort()
print(cars)

# its easy way is
cars.reverse()
print(cars)

# now lets sort in reverse order(hard method)
# we now sort our list
cars.sort(reverse=True)
print(cars)
