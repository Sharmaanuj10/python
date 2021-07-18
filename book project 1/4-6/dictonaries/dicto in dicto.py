cities = {
    'NYC' : {
        'country' : 'america',
        'population' : '333'
            },
    'tokyo' : {
        'country' : 'japan',
        'population' : '98379'

    }
    }
        
for city, data in cities.items():
   #  her i get the key and value form the dictonary and print key first
    print(f'{city}:')
    
# her now i get data from the dictonary's dictonary and print it

    for key,value in data.items():

        print(f'\t{key}: {value}')