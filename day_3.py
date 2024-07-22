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

def document_it(func):
    def new_function(*args, **kwargs):
        print('Название функции', func.__name__)
        print('Позиционные аргументы', args)
        print('Именованные аргументы', kwargs)
        result = func(*args, **kwargs)
        print('Результат', result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        resuit = func(*args, **kwargs)
        return resuit * resuit
    return new_function


@square_it
@document_it
def add_ints(a,b):
    return a+b

# print(add_ints(3,5))

# Создание декоратора в ручную
# coller_add_ints = document_it(add_ints)
# coller_add_ints(3,5)


# Область видимости переменных

animal = 'fruitbat'
def print_global():
    animal = 'qqqq'
    # print('внутренняя переменная за пределами функций', animal)
    # print(locals())
    
# print_global()
# print(globals())
# print(animal)
# def dive():
#     return dive()
# dive()


def test(func):
    print('Старт')
    def new_function(*args):
        print('Енд')
        return func(*args)        
    return new_function

@test
def add_ints(a,b):
    return a+b

print(add_ints(3,5))


# Объекты и классы

