#reversing a string

'''
user_input = (input('Type a word: '))


for words in range(len(user_input)-1, -1, -1):
    print(user_input[words], end=" ")
'''

'''
#class solution 1
sentence = input('Enter a sentence: ')

res = ''
last_idx = len(sentence) - 1

while last_idx >= 0:
    res += sentence[last_idx]
    last_idx -= 1

print(res)
'''

#class solution 2
sentence = input('Enter a sentence: ')
print (''.join(reversed(sentence)))
