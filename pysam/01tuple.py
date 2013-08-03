a = 'a', 'b', 'c'
print a # ('a', 'b', 'c')
b = a, 'd'
print b # (('a', 'b', 'c'), 'd')
x = [1, 2, 3, b]
print x # [1, 2, 3, (('a', 'b', 'c'), 'd')]
