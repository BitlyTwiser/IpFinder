import click
import main

click.group()
def ipfinder():
    pass


ipfinder.add_command(main.external_IP)
