import fire


def hello(name):
    return f'Hello {name}'

def welcome_weather(name, temp):
    return f'{name}, It is going to be {temp} degrees today!'

if __name__ == '__main__':
    fire.Fire()
