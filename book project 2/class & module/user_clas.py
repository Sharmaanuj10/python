class User_Profile:

    def __init__(self,first_name, last_name):
        self.first_name = first_name # to acess attirute we need to probvide them  self or Aditya
        self.last_name = last_name
    
    def describe_user(self):
        print(f'Hi!{self.first_name} {self.last_name} The football couch')
    
    def greet_user(self):
        print(f'Hi! {self.first_name} How are you?')



User1 = User_Profile('Aditya','Sharma')                                                         
print(User1.first_name, User1.last_name)              # see line 4 and 5 or method __init__
User1.describe_user()
User1.greet_user()

User2 = User_Profile('Anuj' , 'Sharma')
print(User2.first_name, User2.last_name)
User2.describe_user()
User2.greet_user()