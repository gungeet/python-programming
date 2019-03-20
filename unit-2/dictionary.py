my_list = []

#add to list
#append(), insert()

#remove from list
#pop(), remove()

#ordered, mutable


#dictionaries
students = {}

#add to dictionary
students['name'] = 'John'
print(students)

#name gets updated
students['name'] = 'Martha'
print(students)

#another key added with a list
students['courses'] = ['Python programming', 'Data science', 'UX', 'Social media marketing']
print(students)

print('------------------------------')
#append the list
students['courses'].append('UI design')
print(students)


#two ways to create a dictionary
print('------------two ways to create a dictionary------------------')
my_dictionary = {
    'puppy': 'Furry, energetic animal',
    'pineapple': 'Acidic tropical fruit',
    'tea' : 'herb-infused drink'
}
print(my_dictionary)


print('------------------------------')
my_dictionary = {} #starting with empty dictionary
my_dictionary['puppy'] = 'Furry, energetic animal'
my_dictionary['pineapple'] = 'Acidic tropical fruit'
my_dictionary['tea'] = 'herb-infused drink'

print(my_dictionary)

print('------------------------------')
collection_2 = {"three": 3, "five": 5, 9:"nine"}
print(collection_2)

#model a playlist
print('********* model a playlist **************')

my_playlist = []

#each song on the playlist
#genre - list
#artist - list
#album - string
#release_year - string
#title - string
#playback_length - string
# -dictionary

my_song = {
    'genres' : ['Pop', 'Hip Hop'],
    'artists' : ['Cardi B', 'Ari', 'Riri'],
    'album' : 'NA',
    'release_year' : '2019',
    'title' : 'something somethin',
    'playback_length' : '2:15'
}

my_playlist.append(my_song)
print(my_playlist)


#sorting/shuffling-----------------------------

def swap_first_two(my_list):
    temp = a_list[0] #store a temp value 
    a_list[0] = a_list[1] #change the second value to first
    a_list[1] = temp #use temp for second value
    return my_list

a_list = [1, 2, 15, 20]
swap_first_two(a_list)
print(a_list)

#can also do it^ in pythonic way
def swap_first_two(my_list):
    my_list[0], my_list[1] = my_list[1], my_list[0]

a_list = [1, 2, 15, 20]

swap_first_two(a_list)
print(a_list)
#[2, 1, 15, 20]