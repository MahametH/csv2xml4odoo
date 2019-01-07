# csv2xml4odoo

## Odoo csv / xml converter

```
Usage: c2x [OPTIONS] [FILE]

  Convert Odoo csv files in xml files Csv is easy to maintain but xml data
  have 'noupdate' and search features

  Limitations:

  - relation field One2many is NOT SUPPORTED

  - ambiguous columns: char type but contains float string, should have
  special suffix on column name '|char'

  - relationnal fields notation in csv should be: myfield_id/id for m2o or
  myfield_ids/id for m2m

Options:
  -u, --update TEXT  Set 'noupdate' attribute to 0 instead of 1
  --help             Show this message and exit.

```

## Installation

`sudo pip3 install -e .`
