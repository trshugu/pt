import types
a = 1000
print type(a) # <type 'int'>

s = "1000"
print type(s) #  <type 'str'>

b = ('0', '000')
print type(b) #  <type 'tuple'>

x = 100
if type(x) == type(a):
	print 'same type.' #  same type.

if type(a) == types.IntType:
	print 'integer' #  integer
