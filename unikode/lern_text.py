import re

source = 'Белый снег лег на пол в квартире за диваном'

m = re.search('.*лег', source)

if m:
    print(m.group())
else:
    print('нет совпадений')