import click

# @click.command()
# def hello():
#     click.echo(click.style('Hello World!', fg='yellow', bg='blue', bold=True))
#     click.secho('HELLO!', bold=True)

# hello()


# groups
# two ways to create groups, one with the click decorator and one with the group as the decorator
# @click.group()
# def cli():
#     pass

# @click.command()
# def initdb():
#     click.echo('Initialized the database')

# @click.command()
# def dropdb():
#     click.echo('Dropped the database')

# cli.add_command(initdb)
# cli.add_command(dropdb)

# @click.group(chain=True)
# def cli():
#     pass

# @cli.command()
# def initdb():
#     click.echo('Initialized the database')

# @cli.command()
# def dropdb():
#     click.echo('Dropped the database')


# if __name__ == '__main__':
#     cli()


# getting a user input of a single character
# click.echo('Continue? [yn] ', nl=False)
# c = click.getchar()
# click.echo()
# if c == 'y':
#     click.echo('We will go on')
# elif c == 'n':
#     click.echo('Abort!')
# else:
#     click.echo('Invalid input :(')

# progress bar
# import time

# with click.progressbar([1, 2, 3]) as bar:
#     for x in bar:
#         print(f"sleep({x})...")
#         time.sleep(x)


# args and options
# @click.command()
# @click.option('--name', prompt=True, help='Your name')
# @click.option('--size', type=click.Choice(['Small', 'Medium', 'Large', 'Extra Large'], case_sensitive=False),
#               prompt=True, help='Your clothing size')
# def get_user_info(name, size):
#     # Output the collected information
#     click.echo(f"Name: {name}, Selected size: {size}")

# get_user_info()


# multiple choice options
# @click.command()
# @click.option("--size", prompt=True, multiple=True, type=click.Choice(['Small', 'Medium', 'Large', 'Extra Large'], case_sensitive=False))
# def select_size(size):
#     options = list(size)
#     # size = click.prompt("Select your size", type=click.Choice(['Small', 'Medium', 'Large', 'Extra Large'], case_sensitive=False))
#     click.echo(f"You selected: {options}")

# select_size()
