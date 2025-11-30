# Name Cases and String Manipulation
#lower, upper, title, lstrip, rstrip, strip
name = 'Eric'
print("Hello " + name + ", would you like to learn some Python today?")

name = name.lower()
print(name)
name = name.upper()
print(name)
name = name.title()
print(name)

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_person = 'Albert Einstein'
print(famous_person, 'once said, "A person who never made a mistake never tried anything new."')

message = "A person who never made a mistake never tried anything new."
print(famous_person + ' once said, "' + message + '"')

name = " \t\n Eric \n\t "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())