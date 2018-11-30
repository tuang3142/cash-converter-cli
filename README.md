# cash converter 0.1.1

currency converter using latest data from [fixer.io](https://fixer.io/)

![demo](https://rawcdn.githack.com/daenylio/cash-converter-cli/master/demo.svg "demo")

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

## installation

in the extracted folder run

```bash
$ pip install cash-converter-cli
$ cashconverter --update
```

## to do

next version should have

- [x] come with package
- [x] svg image
- [x] use api
- [x] not use api?
- [x] custom help
- [x] update
- [ ] look up for currency code
- [ ] database
