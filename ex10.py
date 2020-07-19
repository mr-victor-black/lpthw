"I am 6'2\" tall." #escaped the double quote that's inside the string
'I am 6\'2" tall.' #escaped the single quote, to avoid closing the string

#escaping lets the quote show up inside of the string, instead of ending the string early

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#everything within the triple quotes is escaped.
#why escape a slash? it's going to show up anyways


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
