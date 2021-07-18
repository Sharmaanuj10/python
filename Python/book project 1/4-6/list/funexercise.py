#3 for values in range(1,1000001):
##    print(values)
##     # if your computer not able to hold than press ctrl+c or kill the terminal

# digit = []
# for value in range(1,21,2):
#     digit.append(value)
    
# print(digit)

##now lets calculate the sum of 1 to 1million digits

# digits = []
# for numbers in range(1,1000001):
#     digits.append(numbers)

# ##sum method summed max give max value and min gave min value
# print(sum(digits))
# print(max(digits))
# print(min(digits))

# # now lets make the list of mutiple of 3 from 1 to 3
# multiple = list(range(0,31,3))
# print(multiple)
# # its easy man


# number = [value**3 for value in range(1,11)]
# print(number)



## Now lets do slicing in dividig into the ratio

guess = [1,2,3,4,5,6,7,8,9]
print("The first three item of the list are :")
print(guess[0:3])

# in slicing we have to use the ocrrect order that we see not the list attribute
 
print("The middle items are : ")
print(guess [3:6])
# The first one of the slicing is not counted like in 3 the 4 digit is typed
 
print(" The last three digit are: ")
print(guess[-3:])
# instead of -3 i can also use 6:9 so i get 789
# is you notice that use -3! instead of -4 digit removed from + side 
# as if i type -3:-1 i got 78
