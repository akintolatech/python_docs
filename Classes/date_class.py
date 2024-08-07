"""
Programming Python
Desc: Class notation
All rights reserved Lotus Code Studios Sept 2021
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __format__(self, code):
        if code == "":
            code = 'ymd'
            fmt = _format[code]
            return fmt.format(d=self)

_format = {
    'ymd':'{d.year}--{d.month}--{d.day}',
    'mdy':'{d.year}/{d.month}/{d.day}',
    'dmy':'{d.year}/{d.month}/{d.day}',
}

d = Date(2012, 12, 21)
print(format(d, 'mdy'))