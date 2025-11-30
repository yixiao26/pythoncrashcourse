languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jen': 'javascript',
}

print(languages['jen'])
for name, language in languages.items():
    print(name.title() + 
        "'s favorite language is " + 
        language.title()
    )
    
for name in sorted(languages):
    print(name.title() + ', thank you for taking the poll.')

for a in "hello":
    print(a)