def location(city , country):
    print(f'The {city} , {country}')



while True: #while only work when the block is true so we already define it as True
    
    print("\nEnter 'q' to pause")
    city = input('Enter the city: ')

    if city=='q':
        break

    country = input('Enter the country : ')

    if country=='q':
        break
    location(city,country)    



