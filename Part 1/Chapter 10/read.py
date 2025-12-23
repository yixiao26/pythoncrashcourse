filename = './Chapter 10/learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C')
    print(contents.rstrip())
    
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())
    