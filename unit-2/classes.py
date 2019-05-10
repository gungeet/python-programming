from random import randint

class Student:
    def __init__(self, name, address):
        self.name = name   #self.class means we are going to have variable named name for the class, self
        self.address = address

    def name_and_address(self):
        return self.name + ' lives in ' + self.address
        
student_1 = Student('Flavio', 'Toronto')
student_2 = Student('Marcus', 'Guelph')

print(student_1.name) 
print(student_1.name_and_address())

print ('--------------------------------')

#classes can be imported into other python files

class Playlist:
    def __init__(self): #python syntax for a class; python looks for __init__(self)- initializes data
        self.playlist = []

    def add_to_playlist (self, song): #adding thigs to the playlist
        self.playlist.append(song) #playlist is an instance variable

    def remove_from_playlist (self, id):
        #we have find the index of the id(song) to remove it from the playlist
        for idx, song in enumerate(self.playlist):
            if song ['id'] == id: 
                self.playlist.pop(idx)

    def get_songs(self):
        for song in self.playlist:
                print ('{} by {}' .format(song['title'], song['artist']))
    
    def size(self):
        return len(self.playlist)

    def shuffle(self):
        for idx, song in enumerate(self.playlist):
            temp = randint(0, len(self.playlist)-1)
            self.playlist[idx], self.playlist[temp] =  self.playlist[temp], self.playlist[idx]  


my_songs = Playlist()
my_songs.add_to_playlist({'id': 10, 'title': 'I don\'t know', 'artist': 'Cardi B'})
my_songs.add_to_playlist({'id': 13, 'title': 'Kites', 'artist': 'Unknown'})
my_songs.add_to_playlist({'id': 1, 'title': 'I like it like that', 'artist': 'Cardi B'})
my_songs.add_to_playlist({'id': 14, 'title': 'Paperplanes', 'artist': 'Someone'})
my_songs.add_to_playlist({'id': 3, 'title': 'Faces', 'artist': 'Hands'})

my_songs.remove_from_playlist(10)

print(my_songs.size())


my_songs.shuffle()
my_songs.get_songs()

print('-----------------------------')


