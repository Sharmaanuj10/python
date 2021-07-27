class Restaurant:

    # after definig the class we just create its method  as like this: 
    def __init__(self,restaurant_name , cuision_type):
        self.restaurant_name = restaurant_name
        self.cuision_type= cuision_type
        self.number_served = 0

    # in her the '''''self'''' is mean the my_rest which used to get the name or the attribute (restaurant_name)


    def describe_restaurant():
        print(f'{self.restaurant_name} have great serivice ')
        print(f'{self.restaurant_name} also great room with great hygein ')


    def open_restaurnt(self):
        print(f'{self.restaurant_name} is already open')
    
          
    
    

my_rest = Restaurant('kingfisher' , 'beared')
# create our restarant we give  the name and the type and call the name of restarant or type
print(my_rest.restaurant_name)
# call the method to check that my_rest is open or not 
my_rest.open_restaurnt()



restaurant = Restaurant('Royal Palace', 'delight')

# here we assign the value to 3 

restaurant.number_served = 3
print(restaurant.number_served)


