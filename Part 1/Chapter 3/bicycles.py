bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

bike = bicycles[0].title()
message = ("My first bicycle was a " + bike + ".")
print(message)
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

bicycles[0] = 'bigw'
print(bicycles)