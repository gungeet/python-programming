'''
user_input = (input('What calculation would you like to do? (add, sub, mult ,div): '))
num_one = (int(input('Choose first number: ')))
num_two = (int(input('Choose second number: ')))


if user_input == 'add':
    print('your result is {}' .format(num_one + num_two))

if user_input == 'sub':
    print('your result is {}' .format(num_one - num_two))

if user_input == 'mult':
    print('your result is {}' .format(num_one * num_two))

if user_input == 'div':
    print('your result is {}' .format(num_one / num_two))

user_input = (input('What calculation would you like to do? (add, sub, mult ,div): '))
num_one = (int(input('Choose first number: ')))
num_two = (int(input('Choose second number: ')))
'''

#got it right!!! woot!
#reducing duplicate code, refactoring!

user_input = (input('What calculation would you like to do? (add, sub, mult ,div): '))
num_one = (int(input('Choose first number: ')))
num_two = (int(input('Choose second number: ')))


if user_input == 'add':
    ans = num_one + num_two

if user_input == 'sub':
    ans = num_one - num_two

if user_input == 'mult':
    ans = num_one * num_two

if user_input == 'div':
    ans = num_one / num_two

print('Your result is {}. Calc u later!' .format(ans))

user_input = (input('What calculation would you like to do? (add, sub, mult ,div): '))
num_one = (int(input('Choose first number: ')))
num_two = (int(input('Choose second number: ')))