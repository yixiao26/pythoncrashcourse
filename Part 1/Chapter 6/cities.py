cities = {
    'Canberra': {
        'country':'australia',
        'population':'340000',
        'fact':'national capital',
    },
    'Xian': {
        'country':'china',
        'population':'11000000',
        'fact':'long history',
    }
}

for place, information in cities.items():
    print(f"{place}'s Statistics:")
    for keys in information.keys():
        print(f"\t{keys}: {information[keys]}")
    print("\n")