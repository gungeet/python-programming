'''
no_of_students = 10
if no_of_students > 5:
    print ('Good class size.')
else: 
    print ('Class size not ideal.')

grade = 12
if grade >= 80:
    print ('A')
elif grade >= 60:
    print ('B')
else:
    print ('C')

'''
from random import randint

ans = randint (1, 10)
print (ans)
guess = int(input())
print (type (guess))

if guess == ans:
    print ('correct')
else: 
    print ('try again')


