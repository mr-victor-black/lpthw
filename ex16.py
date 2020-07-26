from sys import argv

script, filename = argv #asks for the script name, and the file you want to enact the script on

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") #this is what it displays while awaiting a Return or cancel

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate() #these two happen instantly. Python opened the file then wiped it
#also, if I remove truncate, this script still works

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write(f"{line1}" "\n" f"{line2}" "\n" f"{line3}" "\n") #this does the same thing as all the other target.writes, but in one line instead of several

print("And finally, we close it.") #the script ends
target.close()
