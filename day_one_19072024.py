spells = [
    "Riddikulus!",
    "Wingardium Leviosa",
    "Avada Kedavra",
    "Expecto Patronum",
    "Nox!",
    "Lumos!",
]
strok = 'qwertyuiop'
# print('\t#\n'.join(spells))
# def print_kwargs(**kwargs):
#     'название функции'
#     print( "Некоторые аргументы:", kwargs)

def answer():
    print(42)

def run_sommeting(fun):
    fun()

def add_args(arg1,arg2):
    print(arg1+arg2)

def run_someting_with_args(fun, arg1,arg2):
    fun(arg1, arg2)

# run_someting_with_args(add_args, 5,9)

def sum_args(*args):
    return sum(args)

def run_with_positional_args(fun, *args):
    return fun(*args)

print(run_with_positional_args(sum_args, 1,2,3,4,5))
