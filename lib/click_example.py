import click

# @click.command()
# def hello():
#     click.echo(click.style('Hello World!', fg='yellow', bg='blue', bold=True))
#     click.secho('HELLO!', bold=True)


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