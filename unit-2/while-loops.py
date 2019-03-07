#print  a message 10 times
'''
count = 0
while count < 10:
    print("inside while loop")
    #this limits how many times the loop will run otherwise it run infinitely
    count +=1 
'''

#search for value in list
#idx    0  1   2  3  4
'''
nums = ['a', 84, 6, 8, 10]
found = False
key = 6
'''
'''
while not found:
    if key in nums:
        found = True
        break
'''
'''
for idx, item in enumerate(nums):
    if nums[idx] == key:
        print('Found {} at position {}' .format(key, idx)
        #if i don't break, it'll keep on checking the whole list
        break
'''
'''
#continue
my_nums = [1, 3,15, 8]
for num in my_nums:
    if num % 2 == 0:
        continue
    print ('{} is odd!' .format(num))
'''
'''
answer = 7

#input a number
#loop while that number is not equal to your answer
#if input is bigger, print too big
#if input is smaller, print too small
#if equal, break and print you've got it

guess = int(input('enter a number: '))

while True:
    if guess > answer:
        print('Too Big')
    if guess < answer:
        print('too small')
    if guess == answer:
        print('you\'ve got it')
        break
    guess = int(input('enter a number: '))

#notes: in - to check if a value is in a list of values
'''

#find the sum of a list of numbers

ages = [25, 39, 45, 41, 27, 18, 33]
total_ages = 0

for age in ages:
    total_ages += age #sum = sum + age

print ('total age is {}' .format(total_ages))