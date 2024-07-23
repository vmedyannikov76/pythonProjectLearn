from source import fast, advice
import itertools
print('Пошли в ', fast.pick())
print('Или может ', advice.give())



for item in itertools.accumulate([1,2,3,5], lambda x,y: y*x):
    print(item)