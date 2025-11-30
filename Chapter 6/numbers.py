numbers = {
    'alice': [1, 2, 3],
    'bob': [3, 4],
    'charlie':[100, 49531],
    'dave': [1],
    'egg': 1,
}


for key, value in numbers.items():
    if isinstance(value, list):
        if len(value)>1:
            print(f"{key} likes the numbers")
            for x in value:
                print(x)
        else:
            print(f"{key} likes the number {value}")
    else:
        number = []
        number.append(value)
        if len(number)>1:
            print(f"{key} likes the numbers")
            for x in number:
                print(x)
        else:
            print(f"{key} likes the number {number}")