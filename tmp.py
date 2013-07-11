# -*- coding:utf-8 -*-
"""
"""

"""
"""
# ライブラリ読み込み(json)

"""
"""

"""
# クロージャ
def closure(n):
  x = n
  print x
  return lambda y: x + y + 2

x = -100

f = closure(3)
print f.__closure__[0].cell_contents
print f(1)

f = closure(4)
print f(f(3))
"""



"""
# リストに入れるとできる
def a():
  b = [2]
  def c():
    b[0] = b[0] + 2
    print b
  return c

f = a()
f()
f()
f()
f()
f()
f()
f()
"""


"""
def callFunc(item):
  def func(*args):
    print(item)
  return func

items = ['a', 'b', 'c', 'd', 'e']
for item in items:
  fnc = callFunc(item)
  fnc()
"""




"""
# ラムダ式
f = lambda x,y: x + y
print f(y=2, x=4)
"""


"""
# 関数
def func(a,b):
  return a + b

def tion():
  return "modori"

print func(3,1)
print tion()
"""



"""
# foreach
arr = range(1,7)
m  = {
  "onne" : "sdf",
  "ttwo" : "erere",
  "tthe" : "mmmmm",
}

for x in arr:
  print x

for y, z in m.iteritems():
  print y, z
"""


"""
# hash
m = {
  "onne" : "sdf",
  "ttwo" : "erere",
  "tthe" : "mmmmm",
}
print m
print len(m)
print m["ttwo"]
del m["ttwo"]
print len(m)

for k,v in m.iteritems():
  print k, v

print m.keys()
print m.values()
print m.has_key("onne")
print "onne" in m
print "onne" not in m
print "oaaa" in m

#print [m for m in  m.iterkeys()]
#print [m for m in  m.itervalues()]
print m.get("mmmmm")
"""




"""
# array
a = []
a.insert(0,"aaa")
a.insert(0,"bbb")
a.append("xcc")
a.insert(-1,"lsa")
#print type(a)
print a
print a.count("aaa")
print a.index("lsa")
print a.pop()
print a
print a[2]
print len(a)
for i in a:
  print i

for i in xrange(len(a)):
  print a[i]
"""


"""
# for
#for i in range(3):
#for i in range(2,5):
#  print i

# forステップ
for i in range(2,10,3):
  print i
"""


# pipのupgrade方法 freezeでテキストにし ==[\d.]+ でバージョン抜き

"""
# pythonに複数行コメントはなかった・・・
print "aaaa"
"""