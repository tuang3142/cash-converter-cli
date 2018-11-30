import requests
import json
import click


def update(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    url = "http://data.fixer.io/api/latest"
    key = '4e0450f7efcc0b01e0c908591a539b9d'
    p = { 'access_key': key }
    response = requests.get(url, params=p)

    with open('scripts/exchange_rate.json', 'w') as f:
        f.write(response.text)
        f.close()
    
    date = response.json()['date']
    message = 'Updated {}.'.format(date)
    click.echo(message)
    ctx.exit()


@click.command()
@click.argument('amount', type=float)
@click.argument('fr')
@click.argument('to')
@click.version_option(message='v%(version)s')
@click.option('--update', help='Update exchange rate and exit.', callback=update, expose_value=False, is_eager=True, is_flag=True)
def cli(amount, fr, to):
    """
    Currency converter using latest data from fixer.io
    """
    with open('scripts/exchange_rate.json', 'r') as f:
        data = json.load(f)

    try:
        A = data['rates'][fr]
        B = data['rates'][to]
        res = amount * B / A
        click.echo('{:.2f} {} equals {:.2f} {}'.format(amount, fr, res, to))
    except KeyError:
        message = 'Error: Currency not found.'
        click.echo(message)