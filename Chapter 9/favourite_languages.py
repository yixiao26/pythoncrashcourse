from collections import OrderedDict

languages = OrderedDict()
languages['jen'] = 'python'
languages['sarah'] = 'c'
languages['edward'] = 'ruby'
languages['mike'] = 'javascript'

for name, language in languages.items():
    print(name.title() + 
        "'s favorite language is " + 
        language.title()
    )