import click

# @click.command()
# def hello():
#     click.echo(click.style('Hello World!', fg='yellow', bg='blue', bold=True))
#     click.secho('HELLO!', bold=True)


# groups


# getting a user input of a single character
click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
click.echo()
if c == 'y':
    click.echo('We will go on')
elif c == 'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')

# progress bar
# import time

# with click.progressbar([1, 2, 3]) as bar:
#     for x in bar:
#         print(f"sleep({x})...")
#         time.sleep(x)