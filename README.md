# cash converter 0.1

currency converter using latest data from [fixer.io](https://fixer.io/)

## usage

```bash
Syntax:
$ cashconverter [OPTIONS] AMOUNT FR TO

Options:
  --version  Show the version and exit.
  --update   Update exchange rate and exit.
  --help     Show this message and exit.

Example:
$ cashconverter 10 USD VND
10.00 USD equals 233359.96 VND
```

## demo

![demo](https://rawcdn.githack.com/daenylio/cash-converter-cli/master/demo.svg "demo")

## installation

in the extracted folder run

```bash
$ pip install --editable .
$ cashconverter --update
Updated.
```

## to do

next version should have

- [ ] come with package
- [ ] look up for currency code
- [x] svg image
- [x] use api
- [x] not use api?
- [x] custom help
- [x] update
