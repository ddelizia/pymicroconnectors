import click
import twine.cli

@click.group()
def cli():
    pass

@click.command()
def upload():
    click.echo('Initialized the database')

@click.command()
def doc():
    click.echo('Dropped the database')

cli.add_command(upload)
cli.add_command(doc)