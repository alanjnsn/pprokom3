from operator import *
b=5.0
a=1
print('a={}'.format(a))
print('b={}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a,b): {}'.format(func.__name__,func(a,b)))
