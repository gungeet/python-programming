my_name = {'g': 2, 'u':1, 'n':1, 'e':2, 't':1}

#for item in my_name.keys():
    #print('The letter {} appears in my name {} times' .format(item, my_name[item]))


for letter, val in my_name.items():
    print('The letter {} appears in my name {} times' .format(letter, val))

#--------hw — use dictionary to solve this problem -----------

#word frequency generator

my_sentence = 'There is a woman with a plan. The woman has a plan in hand'
'''
for words in my_sentence:
    dict_keys = my_sentence.split(' ')
for counts in my_sentence:
    dict_values = my_sentence.count(' ')

dict_items = {'words': 'counts'}
print (dict_items)



def frequency_generator(my_sentence):
    dict_keys = my_sentence.split(' ')
    dict_values = my_sentence.count(' ')
    dict_items = {'words': 'counts'}
    pass

print(frequency_generator)


word_list = my_sentence.split()
each_word = set(word_list)

for words in each_word:
    print ('{}: {}' .format(word_list, each_word))
'''
dict_keys = {}
#generate a list from words 
#get unique words as keys

list_of_words = my_sentence.split()

for word in list_of_words:
    if word in dict_keys.keys():
        dict_keys[word] += 1
    else:
        dict_keys[word] = 1

print (dict_keys)
#counts the frequnecy of each word to get val
# for word in my_sentence:
#     dict_val = my_sentence.count(dict_keys)
# #print key and val
# print(dict_val)



#my_sentence = 'There is a woman with a plan. The woman has a plan in hand.'
#frequency_generator(my_sentence)
#There: 1
#is: 1
#a: 3
#woman : 2
#with: 1
#plan: 2
#... 

