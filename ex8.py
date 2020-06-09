# Printing, Printing


formatter = "{} {} {} {}" #Looks like this defines the formatter variable

print(formatter.format(1, 2, 3, 4)) #Is this injecting the 4 things here into the formatter variable?
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) #This is just outputting the unfilled formatter string itself
print(formatter.format(
    "Try your",
    "own Text here",
    "Maybe a poem",
    "or a song about fear"
))

#Interestingly, when the last line only had two lines of the poem, I got a "tuple error"

#So, if I had to hazard a guess, formatter is defined as a variable with four places in it to inject things. Adding three things, or five things, results in an error

#Things to clear up, hopefully down the line - why did he call the variable formatter when the function is called format - just to confuse us? 
