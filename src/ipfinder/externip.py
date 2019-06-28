import requests
import click

@click.command()
def external_IP():
    """
    Super simple function to obtain the Public IP.
    """
    try:
        response = requests.get('https://ident.me')
    except Exception as e:
        print('There was an error: \nError: {}'.format(e))
    else:
        if int(response.status_code) == 200:
            print("Your External IP: {}".format(response.text))
        else:
            raise Exception("Invalid Status Code.\n "
                            "Status Code: {}".format(response.status_code))
