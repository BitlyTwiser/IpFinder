import click

try:
    from . import main
except ImportError:
    import main

@click.group()
def ipfinder():
    pass


ipfinder.add_command(main.external_IP)
