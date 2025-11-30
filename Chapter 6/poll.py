languages = {
    'a': 'python',
    'b': 'ruby',
    'c': 'javascript',
    'd': 'c'
}

people = ['a', 'b', 'x', 'y', 'z']

for x in people:
    if x in languages.keys():
        print(f"Thank you for selecting {languages[x]}")
    else:
        print(f"{x} Please take the poll")