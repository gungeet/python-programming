'''
fruits = ['apple', 'pear', 'mango']

print (fruits[4])
#index error is when you try to access something beyond the list

name = 'Python'
print (names)
#names doesn't exist- hasn't been defines

rapper = {
    'name': 'young thug',
    'address' : 'don\'t know ',
    'hits': 'none'
}
print (rapper['telephone'])
#acessing a key that doesn't exist

class Student:
    def __init__ (self, name):
        self.name = name

a = Student('John')
print(a.grade)
#accessing an attribute that doesn't exist

a.grade = 50
print(a.grade)

try:
    val = int(input('enter a number: '))
except ValueError as ve:
    print('You did not enter an interger', ve)
'''


class Phone:
    def __init__ (self, phone_number):
        self.number = phone_number

    def call (self, other_number):
        print("Calling from", self.number, "to", other_number)
    
    def text(self, other_number, msg):
        print('sending text from', self.number, 'to', other_number)
        print(msg)

new_phone = Phone(54321)
test_phone = Phone(1099000)
test_phone.call(515)
test_phone.text(int('141'), 'Hi')

