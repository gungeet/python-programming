import stories as st

print(st.get_story())

story = {'title': 'The Catcher in the Rye', 'author': 'Somebody'} 
st.add_story (story)

rect = st.Rectangle(10, 5)
print (rect.area())