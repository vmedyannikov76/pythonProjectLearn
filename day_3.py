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
    # print('Старт')
    def new_function(*args):
        print('Енд')
        return func(*args)        
    return new_function

@test
def add_ints(a,b):
    return a+b

# print(add_ints(3,5))


# Объекты и классы

class Cat():
    def __init__(self,name):
        self.name = name
    

a_cat = Cat('Grindolf')
another_cat = Cat('Uebook')

a_cat.age = 3


# print(a_cat.name, a_cat.age)

class Car():# Родительский класс
    def exclaim(self):
        print(' I m a Car')
        
        

class Yogo(Car): # наследование родительского класса
    def exclaim(self):
        print('А вот херушки я другой')
    
    def need_a_push(self):
        print('Я вообщето я малолитражка')




give_me_a_car =  Car() 
give_me_a_yogo =  Yogo()

# print(give_me_a_car.exclaim())
# print(give_me_a_yogo.need_a_push())

class Person():
    def __init__(self, name):
        self.name = name.capitalize()
        
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email



bob = EmailPerson('bob slitsky', 'test@mail.ru')
# print(bob.name) 
# print(bob.email) 

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self,name):
        self.name = name + " Адвокат"


person = Person('Fudd')
doctor = MDPerson('Aybolit')
lawuer = JDPerson('Rick')

# print(person.name)
# print(doctor.name)
# print(lawuer.name)

# print(a_cat, '\n', another_cat)

# Геттеры и сеттеры
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
        
    def get_name(self):
        print('Это геттер')
        return self.hidden_name
    
    def set_name(self, input_name):
        print('Это сеттер')
        self.hidden_name = input_name
        
    name = property(get_name, set_name)
        
don = Duck('Donald')
don.set_name('BOB')
# print(don.get_name())
# print(don.hidden_name)
# print(don.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    @property    
    def diametr(self):
        return 2*  self.radius
    
a = Circle(5)
# print(a.radius)
# print(a.diametr)

# Методы класса - влияют на все объекты

class As():
    count = 0
    def __init__(self):
        As.count += 1
    def exclamp(self):
        print('Я класс А')
        
    @classmethod
    def kids(cls):
        print(f'Это количество дочерних классов: {cls.count}')
            
easy_a = As()
easy_b = As()
easy_c = As()
As.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('Какойто статический метод')


CoyoteWeapon.commercial()

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
        
    def who(self):
        return self.person
    
    def says(self):
        return self.words + ' ###'
    
class Question(Quote):
    def says(self):
        return self.words + '???'
    
class ExclamationQote(Quote):
    def says(self):
        return self.words + ' @@@@'
    
hanter = Quote('Kanalya', 'я наследник класса')
print(hanter.who(), hanter.says())

hanter1 = Question('Kanalya', 'я наследник класса')
print(hanter1.who(), hanter1.says())

hanter2 = ExclamationQote('Kanalya', 'я наследник класса')
print(hanter2.who(), hanter2.says())

class BabblinBrook():
    def who(self):
        return 'Brok'
    
    def says(self):
        return 'Babble'
    
brook = BabblinBrook()

def who_says(obj):
    print(obj.who(), obj.says())
    
who_says(hanter)
who_says(hanter1)
who_says(hanter2)
who_says(brook)

class Words():
    def __init__(self,text):
        self.text = text
        
    def __eq__(self, text2): #магический метод сравнения
        return self.text.lower() == text2.text.lower()
    
    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str:
        return self.text
    
first = Words('ha')


print(first)
# first

class Bill():
    def __init__(self, description):
        self.description = description
        
class Tail():
    def __init__(self, length):
        self.length = length
        
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
        
    def about(self):
        print('Это утка, ее описание: ', self.bill.description, self.tail.length)

a_tail = Tail('long')
a_bill = Bill('orange')
duck = Duck(a_bill, a_tail)
duck.about()