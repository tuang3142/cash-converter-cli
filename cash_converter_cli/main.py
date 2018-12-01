import requests
import json
import click
from pkg_resources import resource_filename


@click.group()
@click.version_option(message='v%(version)s')
def cli():
    """Currency converter using latest data from fixer.io"""
    pass


@cli.command()
@click.argument('amount', type=float)
@click.argument('fr')
@click.argument('to')
def convert(amount, fr, to):
    filename = resource_filename(__name__, 'data/exchange_rate.json')
    with open(filename, 'r') as f:
        data = json.load(f)

    try:
        FROM, TO = fr.upper(), to.upper()
        A = data['rates'][FROM]
        B = data['rates'][TO]
        res = amount * B / A
        message = '{:.2f} {} equals {:.2f} {}'.format(amount, FROM, res, TO)
        click.echo(message)
    except KeyError:
        message = 'Error: Currency not found.'
        click.echo(message)


@cli.command()
def update():
    """Update exchange rate."""
    url = "http://data.fixer.io/api/latest"
    key = '4e0450f7efcc0b01e0c908591a539b9d'
    p = { 'access_key': key }
    response = requests.get(url, params=p)

    filename = resource_filename(__name__, 'data/exchange_rate.json')
    with open(filename, 'w') as f:
        f.write(response.text)

    date = response.json()['date']
    message = 'Updated {}.'.format(date)
    click.echo(message)


@cli.command()
@click.argument('query')
def look(query):
    """Look for currency code.""" 
    filename = resource_filename(__name__, 'data/currency_code.json')
    with open(filename, 'r') as file:
        currency_code = json.load(file)
    
    def lookname(word):
        import re
        query = re.compile(word, flags=re.I)
        ret = []
        for it in currency_code:
            if re.search(query, it['name']):
                ret.append(it)
        return ret
        
    results = lookname(query)
    if len(results) == 0:
        click.echo('Error: Currency not found.')
    else:
        for r in results:
            currency, code = r['name'], r['code']
            message = "{1} ({0})".format(currency, code)
            click.echo(message)
            