def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for x in range(0, len(magicians)):
        magicians[x] = f"{magicians[x]} the Great"
    return magicians


magicians = ["a", "b", "c"]
copy = magicians[:]

make_great(copy)
show_magicians(copy)

show_magicians(magicians)
