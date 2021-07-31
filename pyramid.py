print("\nchoose height between '1' to '74' otherwise output are unsatisfiying\n")
height = int(input('Enter the height of the pyramid: '))
brick = input('Choose Brick of the pyramid: ')


def pyramind_creator(height,brick,variable=1):
    
    while 0<height:
        print(' '*height + brick*variable) #python consider input as string so we can multiply it.
        height-=1
        variable+=2

pyramind_creator(height,brick)