user_input = (input('Type a word: '))


for words in range(len(user_input)-1, -1, -1):
    print(user_input[words], end=" ")