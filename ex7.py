# More Printing

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # Looks like this * 10 notation actually adds 10 .'s, instead of having to type all them out

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# it looks like end = ' ' prevents a new line from happening, and instead appends line 23 to the end of line 22
