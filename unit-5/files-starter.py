import re

#reading a file
'''
story = open('short-story.txt', 'r') #this is file pointer; does not print; 'r' is for reading
print(story) #printing will not print the story
'''

'''
f = open('short-story.txt', 'r') # point to file
data = f.read() # read the file

print(data) # print the file

# always close file after reading
f.close() #close the file

# write to a file
f = open('short-story.txt', 'w') # w doesn't append to a file, it overwrites it
f.write('This is now a new story\n') 
f.write('And this is the second line\n')
f.close()

# append to a file
f = open('short-story.txt', 'a') #this will create a file if it doesn't exist and 'a' will append
f.write('This is a new line in my new story\n')
f.write('The end.\n')
f.close() 

# seek to specific positions and overwrite - for adding lines to a specific positon in the file
f = open('short-story.txt', 'r+')
f.seek(11)
f.write('this new line has been added here with r+\n')
f.close()

# so we don't have to close wach time we open
with open('short-story.txt', 'w') as f:
    f.write('This is a short story.\n')
    f.write('Because it is only 3 lines, it is short.\n')
    f.write('The story ends here.\n')

'''

# point to the file and read it
# split all the lines into a list
# if word == short
# replace with good

# index word and once first instace is found replace with new
# store the search words position
# pop that word
# replace the word with new word

line = 'This is a short story.'
find_what = 'short'
replace_with = 'good'
find_idx = line.find('sh')

print(find_idx)

part_before = line[:find_idx] #copy from start of line to the found position
part_after = line[find_idx + len(find_what):] #copy from found potiion + length of and search string to the end of the line

print(part_before)
print (part_after)

new_line = ''
new_line = part_before + replace_with + part_after

print(new_line)


#with regular expression
def find_and_replace(file_name, find_what, replace_with):
    with open(file_name, 'r') as f:
        old_story = f.read()

    new_story = re.sub(find_what, replace_with, old_story)
    print(new_story)