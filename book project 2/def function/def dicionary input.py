def make_album(artist , album ): 

    album = {'artist': artist, 'album' : album  }
    
    return album


while True:
    print("\npress 'q' to quite")
    
    artists = input('Enter Artist name : ')
    
    if artists == 'q':
        break
    
    albums =  input("Enter the album name : ")

    if albums == 'q':
        break
        
    musicians = make_album(artists, albums)
    print(musicians)


