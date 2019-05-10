marvel_movies = ['Captain America, The First Avenger', 'Iron Man', 'Iron Man II',
'Thor', 'Thor, The Dark World', 'The Amazing Spiderman', 'Dr Strange']

'''
create a new list with all the movies without the word 'The' in their title
'''
new_movies = []
for movie in marvel_movies:
    if "The" not in movie:
        new_movies.append(movie)

print(new_movies)

# list comprehension



# copy old list
fruits = ['apple', 'mango', 'banana']
               #result
copy_fruits = [fruit for fruit in fruits] #new thing in thing in things
                     #iteration_________

numbers = [2, 34, 43, 10]
new_numbers = [num**2 for num in numbers]

print(new_numbers)

vals = [1,2,3,4,11]
odds = [val for val in vals if val % 2 == 1]

print(odds)

nice_fruit = ['apple', 'grapes', 'mango', 'banana', 'peaches']

new_fruit = [fruit if fruit[0] == 'p' else fruit[0] for fruit in nice_fruit]
print(new_fruit)