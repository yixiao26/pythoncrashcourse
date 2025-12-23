def make_shirt(size="large", text="I love Python"):
    print("The size of your shirt is", size, "and the text will be", "'" + text + "'")


make_shirt("small", "I love Python")
make_shirt(size="small", text="I love Python")

make_shirt("medium")
make_shirt("medium", "Another message")


def describe_city(country="Australia", name="Canberra"):
    print(name.title(), "is in", country.title())


describe_city("China", "Beijing")
describe_city("Russia", "Moscow")
describe_city(country="Germany")
