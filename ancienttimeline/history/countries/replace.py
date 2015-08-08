

import os
import sys


limit = (
    'primary_culture = irish',
    'primary_culture = briton',
    'primary_culture = picts',
)
find = 'celtiberians'
replace = 'british'


for doc in os.listdir():
    if doc[-3:] == '.py':
        continue
    f = open(doc, 'r')
    c = f.read()
    f.close()
    for l in limit:
        if l in c:
            c = c.replace(find, replace)
    f = open(doc, 'w')
    f.write(c)
