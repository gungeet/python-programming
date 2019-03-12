'''
#my solution

num = 4
num_list= [34, 23, 11, 22]

for numbers in num_list:
    print (numbers * num)

'''

#the problem with my solution is that it doesn't update the list or number
#goal is to change numbers not simple multiplication

factor = 4
my_nums = [22, 32, 45, 3, 1]

for idx in range(len(my_nums)): #get idx for all numbers in my_nums
    my_nums[idx] = my_nums[idx] * factor #updating the idx's with equation

print(my_nums)