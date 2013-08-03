def f(x):
	return (x + '?')

def f2(x, y):
	return (str(x) + str(y))

a = ['a', 'b', 'c']
print map(f, a) # ['a?', 'b?', 'c?']
b = ['A', 'B', 'C', 'D']
print map(None, b) #  ['A', 'B', 'C', 'D']
print map(f2, b, a) #  ['Aa', 'Bb', 'Cc', 'DNone']
