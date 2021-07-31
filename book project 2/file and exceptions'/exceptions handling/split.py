def filecount(filename):
    try:
        with open(filename) as a:
            file = a.read()
        
    except Exception:
       pass
        
        
    else:
        words = file.split() # split seprate the string where it find the space
        print(len(words))


# filename = 'alice.txt' # you want to check for multiple files use list filename = ['alice.txt','except.py']

filenames = ['alice.txt','except.py']
filenames = 'alice.txt'


try:
    for filename in filenames:
       filecount(filename)
       
except:
    filecount(filenames)
else:
    filecount(filenames)




#title = 'Now I am Happy'
#print(title.split())