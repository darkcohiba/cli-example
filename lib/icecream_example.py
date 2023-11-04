from icecream import ic

# variables
# num1 = 2
# ic(num1)
# output ic| num1: 2

def greeting(name):
    return f'Hello {name}'

# ic(greeting("Sam"))
# ic| greeting("Sam"): 'Hello Sam'

# def check_weight(weight, height):
#     if height + weight > 200:
#         return "Good"
#     elif height + weight > 150:
#         return 'Good Too'
#     elif height + weight > 100:
#         return 'Still Good'
#     else:
#         return 'The most good, but everything is good!'
# ic(check_weight(100, 94))
# output ic| check_weight(100, 94): 'Good Too'

def foo():
    name = input("What is your name ")
    ic(name)
    greeting(name)

    if 1 > 2:
        name = input("What is your name ")
        ic(name)
        greeting(name)
        ic()
    else:
        name = input("What is your name else ")
        ic(name)
        ic(greeting(name))
        ic()

foo()

