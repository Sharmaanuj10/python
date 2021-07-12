# lets use duple now as the duple have pranthesis() not square bracket[]
menus = ('hotdog', 'burger','cherrybrown','chasingd','savitar:)')
for menu in menus:
    print(menu)

# menus[1] = 'carrot'
# in this you going to see the error as the tuple in not changable

# but i can redefine it as
menus = ('hotdog', ' chicken', 'cherrybrown', 'chasin', 'savitar:)')
for menu in menus:
    print(f'\n {menu}')