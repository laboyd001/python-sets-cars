# In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

# nums = range(10)
# small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

# words = ['big', 'red', 'dog', 'ate', 'his', 'food']
# three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript

# define a set that contains tuples.  Each tuple should contain two strings: 1. the name of the artist 2. song by artist
# Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'), 
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }

songs = {
    ('Nickelback', 'How you remind me'),
    ('Radiohead', 'Karma Police'),
    ('Foo Fighters', 'Stacked Actors'),
    ('Nickelback', 'Animals')
}

# using a set comprehension, create a new set that contains all the songs not performed by Nickelback

no_nickelback = [song for song in songs if song[0] != 'Nickelback']
print("These are the non-Nickelback songs:",no_nickelback)