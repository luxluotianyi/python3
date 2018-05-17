#!/usr/bin/env python3

import sys

wages = sys.argv[1]
try:
    wages = int(wages)
except:
    print('Parameter Error')
    sys.exit()
taxable = wages - 3500
if taxable  <= 0:
    print(format(0,'.2f'))
elif taxable <= 1500:
    print(format(taxable * 0.03,'.2f'))
elif taxable < 4500:
    print(format(taxable * 0.1 - 105,'.2f'))
elif taxable < 9000:
    print(format(taxable * 0.2 - 555, '.2f'))
elif taxable < 35000:
    print(format(taxable * 0.25 - 1005, '.2f'))
elif taxable < 55000:
    print(format(taxable * 0.3 - 2755, '.2f'))
elif taxable < 80000:
    print(format(taxable * 0.35 - 5505, '.2f'))
elif taxable > 80000:
    print(format(taxable * 0.45 - 13505, '.2f'))
