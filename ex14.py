from sys import argv

script, user_name = argv #After typing the name of the script, you'll have to type your name in. I'm unclear on how you would know you have to do this, since the script is not yet running and there's no place to actively prompt you. Maybe this assumes you've read the script.
prompt = '> ' #this gets subbed into the inputs to prompt someone to type something

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) #this pauses for an input, and displays the > since that's the value for the prompt variable. I guess this is nicer than just leaving a space 

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

#turns out that you can format things inside of paragraphs too with print(f )
