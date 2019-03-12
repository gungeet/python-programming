#if there is too much repetition in code, wrtie a function
#can have ifs, whiles, etc but can't define a function within a function but can call a function
'''
def high_low():
    my_variable = 23
    if my_variable > 10:
        print('HIGH')
    else:
        print('LOW')

high_low()
'''

#adding arguments in functions can allow you to call functions multiple times and get variable results
'''
def high_low(my_var):
    if my_var > 10:
        print('HIGH')
    else:
        print('LOW')

high_low(5)
high_low(33)
high_low(1)
'''

#fizzbuzz
'''
def fizzbuzz():
    for i in range(1, 102):
        if i % 15 == 0:
            print('FizzBuzz') 
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
   
fizzbuzz()
'''       

#capitalizing words

'''
def capitalize(my_name):
    #convert to uppercase
    return my_name.upper()

print (capitalize('gungeet')) #have to write print here because we didn't mention it in the function like the previous function
'''

'''
def add_two(number):
    total = number + 2
    print (total)
    return total

add_two(10)
'''

#global and local scopes
'''
my_age = 41 

def print_age(): #inside the funtion is local scope 
    prtin(my_age)
    my_address = 'Brampton'

def print_address():
    print(my_address)

print(my_address) #won't get printed because my_adress isn't defined outside the function above- there is no value
'''

def cap_first_letter(sentence):
    new_sentence = '' #because trying to add new sentence
    for word in sentence.split(' '): #splits the given sentence into words
        new_word = word[0].upper() + word[1:] #changes each word
        #create new sentence with new words 
        new_sentence += new_word + ' ' # putting together the new sentence but all of it is compressed with no spaces so add ' ' to add a space between each word
    return new_sentence


print(cap_first_letter('Split this up.'))




