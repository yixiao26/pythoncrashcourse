yixiao = {
    'first_name':'Yixiao',
    'last_name':'Hu',
    'age':16,
    'city':'Canberra',
}

print(yixiao['first_name'])
print(yixiao['last_name'])
print(yixiao['age'])
print(yixiao['city'])

numbers = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}

print(f"a's favourite number is {numbers['a']}")
print(f"b's favourite number is {numbers['b']}")
print(f"c's favourite number is {numbers['c']}")
print(f"d's favourite number is {numbers['d']}")
print(f"e's favourite number is {numbers['e']}")


glossary = {
    'list': 'a collection of elements with order',
    'tuple':'an immutable list',
    'dictionary':'a collection of key-value pairs',
    'list comprehension': 'simplified expression for a rule in a list',
    'if statement': 'conditional statement that only executes if value is True',
}

print('list' +
      ':' +
      '\n\t' +
      glossary['list'] +
      '\n'
)

print('tuple' +
      ':' +
      '\n\t' +
      glossary['tuple'] +
      '\n'
)

print('dictionary' +
      ':' +
      '\n\t' +
      glossary['dictionary'] +
      '\n'
)

print('list comprehension' +
      ':' +
      '\n\t' +
      glossary['list comprehension'] +
      '\n'
)

print('if statement' +
      ':' +
      '\n\t' +
      glossary['if statement'] +
      '\n'
)
