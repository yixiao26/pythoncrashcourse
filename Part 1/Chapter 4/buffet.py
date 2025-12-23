foods = ('apple', 'orange', 'banana', 'mango', 'pineapple')
menu = []
menu = list(foods)

menu.append('pear')
menu.append('watermelon')
print(menu)


new_menu_tuple = tuple(menu)
print(new_menu_tuple)

power = (x**2 for x in range(0, 5))
for x in power:
    print(x)