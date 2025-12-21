cats = 'cats.txt'
dogs = 'dogs.txt'

def read_file(filename):
    try:
        with open(filename) as file_object:
            for object in file_object:
                print(object.rstrip())

    except FileNotFoundError:
        pass

read_file(cats)
read_file(dogs)