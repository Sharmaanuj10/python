def profile_maker(name,password,**username):
   
   
   username[name] = password

   return username


print(profile_maker('anuj','shoab', kanan = 'six' , kasio = 'tim'))
