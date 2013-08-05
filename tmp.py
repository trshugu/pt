# -*- coding:utf-8 -*-
"""
"""






"""
# 02:リスト:[ ]で囲んで表現。連続した値はrange関数。変更可
x = [1,2,3,4,5]
print x # [1, 2, 3, 4, 5]
x = range(1, 5)
print x # [1, 2, 3, 4]

a = ["OOP", "INHERITANCE", "CLASS"]
print a # ['OOP', 'INHERITANCE', 'CLASS']
b = [1000, 1010]
print a + b # ['OOP', 'INHERITANCE', 'CLASS', 1000, 1010]
c = range(0, 4)
print c # [0, 1, 2, 3]
d = range(5)
print d # [0, 1, 2, 3, 4]
"""


"""
# 文字列
x = 'abcde'
print x[1] # 'b' インデクシング
print x[1:3] # 'bc' スライス
print x[1:-1] # 'bcd' スライス
print "a %s pen" % 'red' # 文字列フォーマット
print "One %d Three" % 2 # 文字列フォーマット
print 'a' in x # 1 シーケンスメンバーテスト
print 'abc' is x # 0 比較演算
"""



"""
import os
root, ext = os.path.splitext(__file__)
# 絶対パス + ファイル名
print(root)

# 拡張子
print(ext)

# 変換後ファイル名
print(os.path.basename(__file__).replace("py", "txt"))
"""

"""
for line in open(os.path.basename(__file__).replace("py", "txt"), 'r'):
  print(line)
  print(line.replace("http://", "").replace("\n","").split("/",1))
  domain, url = line.replace("http://", "").split("/",1)
  print(domain)
  print(url)
  h = http.client.HTTPConnection(str(domain))
  h.request('GET', "/" + str(url))
  r = h.getresponse()
  print(r.status)
"""



"""
# httpコネクション
import httplib
h = httplib.HTTPConnection('www.aoky.net')
h.request('GET', '/articles/paul_graham/startupmistakes.htm')
res = h.getresponse()
print(res.status)
print(res.reason)
print(httplib.OK)
"""


"""
# ステータスコード取得
import urllib2
print( urllib2.urlopen("http://cruel.org/jindex.html").code )
"""


"""
# sample.json
import json
 
f = open("sample.json")
data = json.load(f)
f.close()
 
# 普通に表示
print(data)
 
# キレイに表示
print(json.dumps(data, sort_keys=True, indent=4))
 
# 中身に直接アクセス
print(data[0]["name"])
print(data[0]["appearedIn"])
print( "Name : {obj[name]}, appearedIn : {obj[appearedIn]}".format(obj = data[0]) )
print( "influencedBy", ", ".join(data[0]["influencedBy"]) )
"""



"""
# jsonデコード
import json
def as_complex(dct):
  if '__complex__' in dct:
    return complex(dct['real'], dct['imag'])
  return dct

print json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
#(1+2j)


import decimal

print json.loads('1.1', parse_float=decimal.Decimal)
#Decimal('1.1')
"""


"""
# ライブラリ読み込み(json)エンコード
import json
print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'

print json.dumps("\"foo\bar")
#"\"foo\bar"

print json.dumps(u'\u1234')
#"\u1234"

print json.dumps('\\')
#"\\"

print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
#{"a": 0, "b": 0, "c": 0}

from StringIO import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print io.getvalue()
#'["streaming API"]'
"""


"""
# 01:組(タプル)：( )で囲んで表現。変更不可
a = 'a', 'b', 'c'
print a # ('a', 'b', 'c')

b = a, 'd'
print b # (('a', 'b', 'c'), 'd')

x = [1, 2, 3, b]
print x # [1, 2, 3, (('a', 'b', 'c'), 'd')]
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