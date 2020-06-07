# Strings and Text

# Here I'm defining the variable for how many types of people there are, while also setting up a great joke
types_of_people = 10
# Now I'm going to define a formatted string that contains the variable I just defined
x = f"There are {types_of_people} types of people"

# Here I'm defining a few variabls as strings
binary = "binary"
do_not = "don't"

# Now I'm defining another formatted string with strings inside of it.
y = f"Those who know {binary} and those who {do_not}."

# And finally, here I output those strings that I defined
print(x)
print(y)

# Now I'm putting those strings, which had strings within them, within another string to really draw this joke out
print(f"I said: {x}")
print(f"I also said: '{y}'")

# This next part sounds like my life
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#Personally I think the joke was great, and would have set that variable to True

# This part I don't yet get - why is the .format used instead of f? He mentions something about loops, and says we'll cover them later 
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# This part makes sense - just adding two variables together, and since they're strings, they just get mashed into one
print(w + e)
