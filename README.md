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
$ cashconverter look vietnam
VND (Vietnamese dong)
$ cashconverter look yen
JPY (Japanese yen)
$ cashconverter convert 3142 jpy vnd
3142.00 JPY equals 645667.10 VND
```

## installation

```bash
pip install cash-converter-cli
```

## credits

special thanks to [Vijay Mahrra](https://github.com/vijinho)'s [data](https://github.com/vijinho/ISO-Country-Data) of country code.

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
