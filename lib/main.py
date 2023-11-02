# basic hello
# name = input('what is your name: ')
# print(f"Hello {name}")

# multiline in a loop
# data = []
# print("Tell me about yourself")
# while True:
#     line = input()
#     if line:
#         data.append(line)
#     else:
#         break
# finalText = '\n'.join(data)
# print("\n")
# print("Final text input")
# print(finalText)


# import inquirer 
import inquirer

# inquirer has one theme other then default
from inquirer.themes import GreenPassion


questions = [
    # base text question
    inquirer.Text(name='name', message="What's your name?"),
    # confirm question
    inquirer.Confirm('continue', message="Ready to Shop!"),
    # list question
    inquirer.List(
        "size",
        message="What size do you shop for?",
        choices=["Jumbo", "Large", "Medium", "Small", "Micro"],
    ),
    # checkbox, multiple choice
    inquirer.Checkbox(
        "Language",
        message="What is your favorite coding language?",
        choices=["Javascript", "C++", "C#", "Python", "Go"],
    ),
]

# call our questions through the prompt and add the green passion theme!
answers = inquirer.prompt(questions, theme=GreenPassion())
# to access the answers we can use block notation.
print(f"Name: {answers['name']}\n")
print(f"Excited: {answers['continue']}\n")
print(f"Size: {answers['size']}\n")
print(f"Favorite Languages: {list(answers['Language'])}\n")

print(answers)

