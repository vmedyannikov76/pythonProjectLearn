spells = [
    "Riddikulus!",
    "Wingardium Leviosa",
    "Avada Kedavra",
    "Expecto Patronum",
    "Nox!",
    "Lumos!",
]
# Функции

def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)

# print(outer(5,6))

def knights(saying):
    def inner(quote):
        return f'Это строка чтото делает с : {quote}'
    return inner(saying)
# print(knights('Херобора'))

def knights2(saying):
    def inner2():
        return f'Это строка чтото делает с : {saying}'
    return inner2
a = knights2('Херобора')
b = knights2('каоаоао')
# print(a(),'\n',b())

# Анонимные функции lambda
def enliven(word):
    return word.capitalize() + ' !'


def edit_story(words, fun):
    for word in words:
        print(fun(word))

# edit_story(spells,enliven)

# Меняем на lambda

# edit_story(spells, lambda word: word.capitalize() + ' !')
# print(sum(range(1,101)))

# Функции генераторы

def my_range(first=0, last=10, step=1):
    number = first
    while number<last:
        yield number
        number += step
        
range = my_range(1,5)

# for x in range:
#     print(x)


# Декоратор принимает на вход одну функцию и возвращает другую не затрагивая код первой

