# import time for its ability to slow down the program and make it pause
import time
# import os to access system, here I need to clear the terminal
import os

# Ansi Escape Codes directly into the code
# print("\033[48;5;236m\033[38;5;123m1. \033[38;5;208mRegister\033[0;0m")

# basic hello
# name = input('what is your name: ')
# print(f"Hello {name}")

# we can add color to basic print statements with ANSI escape codes
# RED = '\033[91m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# RESET = '\033[0m'

# # multiline in a loop
# data = []
# print("Tell me about yourself")
# while True:
#     if line := input():
#         data.append(line)
#     else:
#         break
# finalText = '\n'.join(data)
# print("\n")
# # to use a color we interpolate it at the beginning of our f string, this color will run forever unless we RESET
# print(f'{RED}Are you ready to see your story!')
# time.sleep(1)
# # os.system('clear')
# print(f'{GREEN}I cant feel the excitement!')
# time.sleep(2)
# print('Ok here you go!!')
# time.sleep(3)
# print("Final text input")
# print(finalText)



