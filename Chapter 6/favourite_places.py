favourite_places = {
    'alice':'australia',
    'bob':'brazil',
    'charlie':'china',
}
for person, place in favourite_places.items():
    print(f"{person.title()} wants to go to {place.title()}")