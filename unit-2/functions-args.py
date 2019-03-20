#functions that returns the sum of
#any number of numbers passed in
'''
def add(a,b): #this only add print(add(1,2))
    return a + b
'''

'''
def add(*args): #this allows to add all sata sets; args is a reserved by python— have to use it for arguments (*args)
    sum = 0
    for val in args:
        sum += val
    return sum

print(add(1,2))

print(add(1,2,3,4,5))
'''

#message ('Bob', 'Python')
#hello bob, you're doing Python!
'''
def message(name, prog): #something I tried
    return ('Hello {}, you are doing {}' .format(name, prog))

print (message('Alice', 'python'))
'''

'''
def message(*args):
   
    message = '' # when there is no argument
    num_args = len(args) #check how many arguments are there- get the indexes
    if num_args == 2: #if there are two arguments
        message = 'Hello {}, you are doing {}.' .format(args[0], args[1])
    elif num_args == 1: #if there is one argument
        message = 'Hello {}.' .format(args[0])
    else:
        pass
    
    print (message)


message('Kali', 'Python')
message('Pathan', 'Biology')
message('Shergil', 'Kabaddi')
message('Papu')
'''


#keyword arguments
#print('This', 'is', 'an', 'awesome', 'Python', 'course', sep='--') #sep is a keyword argument- uses'--' instead of spaces
'''
def say_hi(name, job='Instructor'): #instructor is the default job
    print('Hello {}, you\'re an {}.' .format(name, job))

say_hi('Jagga', job='cliff-climber') #override default
'''

#making multiple args 
#if anything prints with curly brackets means its a library

#define a dictionary
#dictionary is always two things- key and value
'''
people = {'Buca': 'Scooper', 'Laddu': 'Halwai'}

print(people.keys()) #want keys? call dictionary and keys in such format
print(people.values())
print(people.items()) #print twoples in the dictionary
'''

def say_hello(**kwargs):
    #hello {name}, It's gread that you're a {job}.
    for key, val in kwargs.items():
        print ('Hello {}, it\'s good that you\'re a {}.' .format(key, val))

say_hello(Balu= 'Honey Eater', Katta = 'Farmer')

print('--------------------------------------')

def car_type(**kwargs):
    #car_type(make='Subaru', color='black')
        #Your Subaru is black.
    #car_type(make='Honda', color='red', year='2017')
        #Your 2017 Honda is red.
    num_args = len(kwargs)
    msg = ''
    if num_args == 3:
        msg = 'Your {} {} is {}.' .format(kwargs['year'], kwargs['make'], kwargs['color'])
    elif num_args == 2:
        msg = 'Your {} is {}.' .format(kwargs['make'], kwargs['color'])
    else:
        pass
    print (msg)

car_type(make='Subaru', year='2017', color='black')
car_type(make='Viper', year='2019', color='blue')
car_type(make='Honda',  color='red')