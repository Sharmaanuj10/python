class Pet:

    def __init__(self, name , age):
        self.name = name
        self.age = age


class cat(Pet): # cat inherite Pet class
    
    # if we want to add another attribute to initialize we use the super method 
    def __init__(self , name, age,color):
        super().__init__(name ,age)
        self.color = color


    def speak(self):
        return 'meow'


class dog(Pet):

    def speak(self):
        return 'bark'


p1 = cat('misty', 16 , 'white')
p2 = dog('bob',6)
print(p2.speak()) # or # print(dog.speak(p1))
print(p1.name, p1.color) 





# the dog and cat have some simialrity so define a class and the cat and the dog will inherit them
# if define something in the sub class(dog or cat) and also in sup class sub class have the priority