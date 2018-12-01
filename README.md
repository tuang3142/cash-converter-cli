# cash converter 0.2

currency converter using latest data from [fixer.io](https://fixer.io/)

![demo](https://rawcdn.githack.com/daenylio/cash-converter-cli/master/demo.svg "demo")

## help

```bash
Usage: cashconverter [OPTIONS] COMMAND [ARGS]...

  Currency converter using latest data from fixer.io

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  convert
  look     Look for currency code.
  update   Update exchange rate.
```

## examples

```bash
$ cashconverter look japan
> CURRENCY: Yen
> CODE: JPY

$ cashconverter convert 3142 jpy usd
> 3142.00 JPY equals 27.68 USD
```

## installation

in the extracted folder run

```bash
pip install cash-converter-cli
```

## to do

next version should have

- [x] come with package
- [x] svg image
- [x] use api
- [x] not use api?
- [x] custom help
- [x] update
- [x] look up for currency code
- [x] database
