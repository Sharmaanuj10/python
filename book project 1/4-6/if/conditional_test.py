# saga 1
car = 'subaru'

print("\nIs car == 'subaru'? I predict True.")
# In  this firstly define car by = to subaru 
# but later now i want to check whether car is subaru so i use ==
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
# but now check wheteher car is audi (really no) by using  ==

print(car == 'audi')

# saga 2
name = 'Anuj'
# In  this firstly define namer (by =) as anuj 
# but later now i want to check whether name is jack so i use ==
print(name == 'jack')
# now i want to check whether name is is anuj or not
print(name == 'Anuj')

print(name.lower() == 'anuj')
# lower is used for lowercase and ################### makes sure  to use  == to check

# Saga 3
digit = 21

print( digit>21 and digit<21)
#  here i use is to check the statemt is true or not

print( digit>=21 and digit<=21)

print( digit>= 21 or digit<= 21)
# or check whether only one is correct from any one

# Saga 4
digits = [1,2,3,4,5,6,7,8,9]
print( 1 in digits)
print( 10 in digits)
# here i use  to check  wheter the digit i want is in list or not 
# now at last test whether the item is not in list

print( 1 not in digits)
print( 10 not in digits)
