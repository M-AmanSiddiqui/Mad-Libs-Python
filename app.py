print('Welcome to the Mad Libs Generator!')

# User input for the story 

adjective1= input('Enter an adjective: ')  

noun1 = input('Enter a noun: ')

verb1 = input('Enter a verb: ')

place = input('Enter a place: ')

noun2 = input('Enter another noun: ')

adjective2= input('Enter another adjective: ')

# Story

story = f"Once upon a time in {place}, there was a {adjective1} {noun1} that loved to {verb1}. " \
        f"One day, it met a {adjective2} {noun2} and they became best friends! "

print("\nHere is your Mad Libs Story:")

print(story)


