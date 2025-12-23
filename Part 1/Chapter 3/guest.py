guests = ['Alice', 'Bob', 'Charlie']
print(guests[0] + ", you are invited to dinner.")
print(guests[1] + ", you are invited to dinner.")
print(guests[2] + ", you are invited to dinner.")

guests = ['Alice', 'Bob', 'Charlie']
print("Bob cannot make it to dinner.")
guests[1] = 'David'
print(guests[0] + ", you are invited to dinner.")
print(guests[1] + ", you are invited to dinner.")
print(guests[2] + ", you are invited to dinner.")

print("I have found a bigger dinner table!")
guests.insert(0, 'Eve')
guests.insert(2, 'Frank')
guests.append('Grace')
print(guests[0] + ", you are invited to dinner.")
print(guests[1] + ", you are invited to dinner.")
print(guests[2] + ", you are invited to dinner.")
print(guests[3] + ", you are invited to dinner.")
print(guests[4] + ", you are invited to dinner.")
print(guests[5] + ", you are invited to dinner.")

number = len(guests)
print("Total number of guests invited: " + str(number))

removed = guests.pop()
print("Sorry " + removed + ", I can't invite you to dinner.")
removed = guests.pop()
print("Sorry " + removed + ", I can't invite you to dinner.")
removed = guests.pop()
print("Sorry " + removed + ", I can't invite you to dinner.")
removed = guests.pop()
print("Sorry " + removed + ", I can't invite you to dinner.")

print(guests[0] + ", you are still invited to dinner.")
print(guests[1] + ", you are still invited to dinner.")

print(guests)

del guests[0]
del guests[0]

print(guests)