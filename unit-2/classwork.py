classmates = ['Ros', 'Marcus', 'Flavio',
 'Joseph', 'Maham', 'Vinay', 'Gungeet', 'Faris']
'''
#prints number of items in list
print(len(classmates))

#prints the first item in the list
print(classmates[0])

#prints last element in list
print(classmates[-1])

#adds element to list
classmates.append('John')
print(classmates[-1])

#inserts element in list
classmates.insert(1, 'Mishoo')
print(classmates[1])

#remove elemnet from end of the list
classmates.pop()
print(classmates[-1])

#print all elements in the list
for name in classmates:
    print(name)

#search for item in list
for name in classmates:
    if name == 'Maham':
        print('Maham found in the list')
'''

if 'Maham' in classmates:
    print('Found Maham in the list!')

#using indices in for loop
for idx, name in enumerate(classmates):
    print(idx, name)

name = 'Gungeet'

for x in range(len(name)-1, -1, -1):
    print(name[x])

#shortest way
print(name[::-1])

print(name[1:3])