def city_country(name, country):
    name_country = name + ", " + country
    return name_country


print(city_country("Canberra", "Australia"))


def make_album(artist, album, tracks=""):
    music = {"artist": "", "album": ""}

    music["artist"] = artist
    music["album"] = album

    if tracks:
        music["tracks"] = tracks

    return music


information = make_album("abc", "xyz")
print(information)

while True:
    print("Enter q at any time to quit")
    artist = input("Artist: ")
    if artist == "q":
        break
    album = input("Album: ")
    if album == "q":
        break
    information = make_album(artist, album)
    print(information)
