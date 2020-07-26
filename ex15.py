from sys import argv

script, filename = argv #using argv to get a filename, and as always, run the script

txt = open(filename) #now we're opening that filename

print(f"Here's your file {filename}:")
print(txt.read()) #Looks like it's printing out the contents of the file. Also looks like there are other commands that could follow txt
(txt.close()) #added this to close the file, and then it returns "none"

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) #changed the variable, but it still points to the same file

print(txt_again.read()) #once again prints it out
