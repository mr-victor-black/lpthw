from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
new_input = input("Enter one last thing here ")
print(f"Here's your last thing: {new_input}")



#Imports allow you to add features from python and docuument what they are for anyone reading your code
#argv is an arguement variable - this holds whatever arguments you pass to your python script when you run it
#Line 3 is unpacking the argv - it gets assigned to 4 variables
#this needs to be run as python3.6, ex13.py first 2nd 3rd
#if you try running it like ex13.py, it'll tell you there arent enough arguments to unpack
#argv lets an input happen before the script runs. input() takes inputs while the script is running
