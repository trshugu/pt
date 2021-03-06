# -*- coding:utf-8 -*-
"""
"""






"""
fact = lambda n: 1 if n == 0 else n * fact(n - 1) 

print( fact(8) )


print( (fact, 8) )


t = (fact, 8)
print( t[0](t[1]) )
"""



"""
print((1,2))
print((1,))
print((1))
print([1,2])



print( (1,2) )
print( tuple )
print( (1,2,3,4,5,6) )
print( len( (1,2,3,4,5,6) ) )
print( (1,2,3,4,5,6).count(3) )
print( (1,2,3,4,5,6)[0] )
print( (1,2,3,4,5,6)[1:] )

def cons(a, t):
  return (a,)+ tuple(map(lambda x: x, t) )

print( cons(1, (4,5)) )
print( (1,) + (4,5) )


def zero(): return ()
def inc(x): return ("♪",) + x
def dec(x): return x[1:]

print( zero() )
print( inc(zero()) )
print( dec(inc(inc(zero()))) )
print( dec(inc(inc(inc(zero())))) )

def add(x, y):
  if not y:
    return x
  else:
    return add(inc(x), dec(y))

print("====")
print( add( dec(inc(inc(inc(zero())))), inc(inc(inc(zero()))) ) )

def sub(x, y):
  if not x:
    return x
  elif not y:
    return x
  else:
    return sub( dec(x), dec(y) )

print( sub( inc(inc(inc(zero()))), inc(inc(zero())) ) )


def mul(x, y): return muli(x, y, zero())
def muli(x, y, n):
  if not y:
    return n
  else:
    return muli(x, dec(y), add(n,x))


print( mul( inc(inc(inc(zero()))), inc(inc(zero())) ) )

def div(x, y): return divi(x, y, zero())
def divi(x, y, n):
  if not x:
    return n
  else:
    return divi(sub(x, y), y, inc(n))


print( div( inc(inc(inc(inc(inc(inc(inc(inc(zero())))))))), inc(inc(zero())) ) )
"""



"""
# フェルマー法
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n//x) // 2
    return x

# print(isqrt(36))
# print(isqrt(133))
# print(isqrt(14884))

def is_square(n):
    if not n % 48 in (0, 1, 4, 9, 16, 25, 33, 36):
        return False

    x = isqrt(n)
    return x*x == n

# print(is_square(36))
# print(is_square(133))
# print(is_square(14884))



def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    while not is_square(b2):
        a += 1
        b2 = a*a - n
    return a - isqrt(b2)
"""




"""
if __name__ == '__main__':
    n = long(17772938775798494671)
    p = fermat(n)
    if p:
        print "%d = %d * %d" % (n, p, n/p)
    else:
        print "%d is prime" % n
"""


"""
# rsa
import random

# 高速指数演算
def modular_exp(a, b, n):
  res = 1
  while b != 0:
    if b & 1 != 0:
      res = (res * a) % n
    
    a = (a * a) % n
    b = b >> 1
  
  return res

# print(modular_exp(13,11,141))

# ランダムな素数
def gen_rand(bit_length):
  bits = [random.randint(0,1) for _ in range(bit_length - 2)]
  ret = 1
  for b in bits:
    ret = ret * 2 + int(b)
  return ret * 2 + 1

# 素数確認
def mr_primary_test(n, k=100):
  if n == 1:
    return False
  
  if n == 2:
    return True
  
  if n % 2 == 0:
    return False
  
  d = n - 1
  s = 0
  while d % 2 != 0:
    d /= 2
    print(d)
    s += 1
  
  r = [random.randint(1, n - 1) for _ in range(k)]
  for a in r:
    # print(a)
    # print(modular_exp(a, d, n))
    if modular_exp(a, d, n) != 1:
      # print("====")
      # print(s)
      pl = [(2 ** rr) * d for rr in range(s)]
      # print(pl)
      
      flg = True
      for p in pl:
        # そもそもここに入らない
        # print(modular_exp(a, p, n))
        if modular_exp(a, p, n) == 1:
          # 指数が1のものがplにあったら継続して処理
          flg = False
          # このfor文を抜ける
          break
      
      if flg:
        # なかった(flgがTrueのままだった)らFalseを返却
        return False
  
  return True

# print(mr_primary_test(2999)) # 

# print(mr_primary_test(1)) # f
# print(mr_primary_test(2)) # t
# print(mr_primary_test(3)) # t
# print(mr_primary_test(4)) # f

# print(mr_primary_test(9007199254740991)) # f

# print(mr_primary_test(9007199254740993)) # f

# print(mr_primary_test(12)) # f
# print(mr_primary_test(13)) # t
# print(mr_primary_test(141)) # f
# print(mr_primary_test(142)) # f
"""



"""
# 1のものがあった→Trueをかえす
def aa():
  flg = True
  for p in range(3):
    print(p)
    if p == 5:
      print("kiteru")
      print(p)
      flg = False
      #  ここでfor文を抜ける
      break
    
    print("dokokaeru")
    
  if flg:
    print("11")
    return False
    print("222")
  print("3333")
  return True


print(aa())
"""

"""
# 素数生成
def gen_prime(bit):
  while True:
    ret = gen_rand(bit)
    if mr_primary_test(ret):
      break
  return ret

# print(gen_prime(128))


# ユークリッドの互除法
def xgcd(b, n):
  x0, x1, y0, y1 = 1, 0, 0, 1
  while n != 0:
    q, b, n = b // n, n, b % n
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
  return b, x0, y0

# 鍵生成
def gen_d(e, l):
  _, x, _ = xgcd(e, l)
  print x
  print l
  print x % l
  return x % l

print(xgcd(22, 45))


# print(gen_prime(128))
"""


"""
byt = 1024
# p = gen_prime(byt)
# q = gen_prime(byt)
# e = gen_prime(byt)

p = 195531435739008959673282737963575264469
q = 242779475795881938335203689155820874691
e = 188952817630177726230187917619251142649

d = gen_d(e, (p-1)*(q-1))
n = p*q

m=1010101

c = modular_exp(m, e, n)

import zlib
comp = zlib.compress(str(c))

decomp = zlib.decompress(comp)

text = modular_exp(int(decomp), d, n)

print("==c==")
print(c)
print("==d==")
print(d)
# print(n)


# print(n)
# print("===")
# print(p)
# print(q)
# print(e)
# print("===")
# print(d)
# 11540259110620643804050581540467802225296462730371363615562484385880968849053
# print(c)
# print(comp)
# print(decomp)
# print(text)
"""


"""
# 必要なものはe,d,n
print("e")
print(e)
print("d")
print(d)
print("n")
print(n)
print("c")
print(c)
print("text")
print(text)
"""



"""
import math

def cc(c,t):
  return  math.ceil(((c**t - (c-1)**t) / c**t) * 100000000) / 1000000


# print(cc(4,4))

print(cc(16**16, 10000000))
"""

"""
for i in range(16):
  for j in range(10000000):
    if (j+1) % 1000000 == 0:
      print(str(i+1) + "文字" + str(j+1) + "回試行：" + str(cc(16**(i+1), j+1)))
"""



"""
class Calc:
  def ichi(self):
    return "anokutara"
  
  def king(self):
    return 12

class fzbz:
  def shi(self, i):
    return i
  
  def check(i):
    return "さん" + str(i)


# print(Fzbz.check(2))
"""








"""
# 3のつく数字も
def fb(i):
  if i % 3 == 0:
    return "Fizz"
  elif str(i).find("3") != -1:
    return "Fizz"
  else:
    return str(i)
"""




"""
# 3の倍数だけ
def fb(i):
  if i % 3 == 0: return "Fizz"
  else: return str(i)


print( fb(1) )
print( fb(2) )
print( fb(15) )
print( fb(9) )
print( fb(3) )
print( fb(5) )
print( fb(10) )
print( fb(30) )
print( fb(32) )
print( fb(33) )
print( fb(35) )
print( fb(36) )
"""



"""
# 通常のfizzbuzz
def fb(i):
  if i % 3 == 0 and i % 5 == 0:
    return "FizzBuzz"
  elif i % 3 == 0:
    return "Fizz"
  elif i % 5 == 0:
    return "Buzz"
  else:
    return str(i)



print( fb(1) )
print( fb(2) )
print( fb(15) )
print( fb(9) )
print( fb(3) )
print( fb(5) )
print( fb(10) )
print( fb(30) )
print( fb(32) )
print( fb(33) )
print( fb(35) )
print( fb(36) )
"""





"""
print("░░░░░░░░░░░░██░░░░░░░░░░░░░░")
print("░░░░░░░░░░░█░░█░░░░░░░░░░░░░")
print("░░░░░░░░░░░█░░█░░░░░░░░░░░░░")
print("░░░░░░░░░░█░░░█░░░░░░░░░░░░░")
print("░░░░░░░░░█░░░░█░░░░░░░░░░░░░")
print("██████▄▄█░░░░░██████▄░░░░░░░")
print("▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░")
print("▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░")
print("▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░")
print("▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░")
print("▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░░░░░")
print("▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░")
print("█████▀░░░░▀▀████████░░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
"""



"""
print("あああ")
"""


# ここから3.6

"""
import datetime, freezegun
from time import sleep

date = datetime.datetime.now()

def test_method():
    print('１回目:' + str(datetime.datetime.now()))
    sleep(5)
    print('２回目:' + str(datetime.datetime.now()))

if __name__ == '__main__':
    test_method()
"""


"""
# py2向けクロージャ
def kuro(x):
  def uja():
    uja.x = uja.x + 1
    return uja.x
  
  uja.x = x
  return uja

a = kuro(0)

print(a())
print(a())
print(a())
print(a())
"""











"""
# tupleについての考察
# print (1,2,4)

t = 2,3,1,9
print t
# print len(t)
print t[0]
print t[1:]
print t[:1]



# for i in t:
#   print i
"""

"""
u = 100,
print u
print len(u)

# アンパック
a,b,e,f = t
c = u
"""



"""
s = tuple("asddkl\"'\"j',")
print s
print len(s)
"""


"""
import types

class UnicodeDecodeError(Exception):
    def __str__(self):
        return 'CharacterEncoding of an acquired file isn\'t UTF-8'

class SystemError(Exception):
    def __str__(self):
        return 'SystemErrorOccurred'

def nanika():
  print "nanikastart"
  
  try:
    print "tryasan"
    # raise UnicodeDecodeError("ude")
    # raise "kjasdf"
    return {"body": unicode("aaaa", 'utf-8')}
    
    print "tryend"
  except ValueError as de:
    print "ve"
    print(de)
    return
  except UnicodeError as de:
    print "ue"
    print(de)
  except UnicodeDecodeError as de:
    print(de)
    # raise UnicodeDecodeError()
    # return 'aaaa'
  except SystemError as e:
    print "sysysys"
    print e
  except Exception as e:
    print "ex"
    print e
    print type(e)
  
  print "nanikaendt"


print nanika()
"""



"""
class Calc:
  def ichi(self):
    return "anokutara"
  
  def king(self):
    return Exception("eeee")


class UnicodeError(Exception):
  # print Exception
  # print "dokujidayoo"
  
  def __init__(self, value):
    self.value = value
    return
  
  def __str__(self):
    return repr(self.value + "UNIERA")
  
class UnicodeDecodeError(Exception):
  # print Exception
  # print "dokudekodekodekojidayoo"
  
  # def __init__(self, value):
  #   self.value = value
  #   return
  
  def __str__(self):
    return "waritotekitounanaiyou"
    # return repr(self.value + "DEKODEKO")

try:
  raise UnicodeDecodeError("boiboi")
  # raise UnicodeError("boiboi")
  a = unicode('ああああ','utf-8')
  
  print "owari"

except UnicodeError as e:
  print "reigaiSuniuniuni"
  print e
  # raise NameError("nameee")
  # print x # x >= 5になったとき例外が発生し、５が表示される
  # c = Calc()
  # print c.ichi()
  # raise c.king()

except UnicodeDecodeError as e:
  print "reigaidekoooon"
  print e

except Exception as e:
  print "reigaisita"
  print e
  # print x # x >= 5になったとき例外が発生し、５が表示される


# c = Calc()
# print c.ichi()
"""


"""
# py2とpy3
#print "aaaa"
print("aaaa")
"""


"""
# not global
import time
from multiprocessing import Process

#LOOP = 1000 * 1000 * 100
LOOP = 10

def incre1():
  value = 0
  for i in range(LOOP):
    print value
    time.sleep(0.1)
    value += 1

def incre2():
  value = 0
  for i in range(LOOP):
    print value
    value -= 1

if __name__ == "__main__":
  Pr1 = Process(target=incre1)
  Pr2 = Process(target=incre2)
  
  Pr1.start()
  Pr2.start()
  
  Pr1.join()
  Pr2.join()
"""



"""
# マルチプロセスアウトオブオーダー
from multiprocessing import Process

LOOP = 1000 * 1000 * 10
#LOOP = 1000
value = 0

def check(value):
  if value != 1 and value != -1:
    print "nattta"
    raise

def ichi():
  global value,LOOP
  for i in range(LOOP):
    value = 1
    check(value)

def mai():
  global value,LOOP
  for i in range(LOOP):
    value = -1
    check(value)

if __name__ == "__main__":
  print value
  
  Pr1 = Process(target=ichi)
  Pr2 = Process(target=mai)
  
  Pr1.start()
  Pr2.start()
  
  Pr1.join()
  Pr2.join()
  
  print value
"""





"""
# マルチプロセスインクリメント
from multiprocessing import Process

#LOOP = 1000 * 1000 * 100
LOOP = 10
value = 0

def incre():
  global value,LOOP
  for i in range(LOOP):
    print value
    value += 1

if __name__ == "__main__":
  print value
  
  Pr1 = Process(target=incre)
  Pr2 = Process(target=incre)
  
  Pr1.start()
  Pr2.start()
  
  Pr1.join()
  Pr2.join()
  
  print value
"""




"""
# インクリメント移植
import sys
from threading import Thread
import cProfile

LOOP = 1000 * 1000 * 100
#LOOP = 1000
value = 0

def incre():
  global value,LOOP
  for i in range(LOOP):
    value += 1

if __name__ == "__main__":
  print value
  
  th1 = Thread(target=incre)
  th2 = Thread(target=incre)
  
  th1.start()
  th2.start()
  
  th1.join()
  th2.join()
  
  print value
"""




"""
# java'sアウトオブオーダー移植
import sys
from threading import Thread
import cProfile

#LOOP = 1000 * 1000 * 1000
LOOP = 1000 * 1000 * 10
value = 0

def check(value):
  if value != 1 and value != -1:
    print "nattta"
    raise

def ichi():
  global value,LOOP
  for i in range(LOOP):
    value = 1
    check(value)


def mai():
  global value,LOOP
  for i in range(LOOP):
    value = -1
    check(value)

if __name__ == "__main__":
  print value
  
  th1 = Thread(target=ichi)
  th2 = Thread(target=mai)
  
  th1.start()
  th2.start()
  
  th1.join()
  th2.join()
  
  print value
"""



"""
# マルチプロセス1
from multiprocessing import Pool
p = Pool(5)
def f(x):
  return x*x

p.map(f,[1,2,3])
"""


"""
# Juno
from juno import *

@route('/')
def index(web):
    return 'Juno hell is come here'

@route('/hell/:name/')
def hello(web, name):
    return 'Hello, %s' %name

run()
"""


"""
# テスト用
class Calc:
  def ichi(self):
    return "anokutara"
  
  def king(self):
    return 12

#c = Calc()
#print c.ichi()
"""



"""
# flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()
"""




"""
# jinja2
from jinja2 import Template

template = Template(u'''\
<html>
<head><title>{{ variable }}</title></head>
<body>
<ul>
{% for item in item_list %}
   <li>{{ item }}</li>
{% endfor %}
</ul>
</body>
</html>''')

print template.render(
  variable='Value with <unsafe> data',
  item_list=[1, 2, 3, 4, 5, 6]
)
"""



"""
# ユニットテスト
import unittest

class testFunc(unittest.TestCase):
  def setup(self):
    self.seq = range(10)
  
  def test_aaaa(self):
    self.assertTrue(True)

  def test_aaab(self):
    self.assertTrue(True)


if __name__ == '__main__':
  unittest.main()
"""




"""
# ロギング
import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler("test.log", maxBytes=20, backupCount=5)
my_logger.addHandler(handler)

my_logger.warn("wawaw")
my_logger.debug("mymy")

my_logger.setLevel(logging.WARN)
my_logger.warn("wawa2")
my_logger.debug("mymy2")
"""


"""
# ログファイル出力
logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.debug("dddd3")

"""


"""
# 最初に実行される前にログレベルが設定されていないといけない
logging.basicConfig(level=logging.DEBUG)
logging.error("eeee")
logging.debug("dd")


if __name__ == '__main__':
  logging.error("eeee2")
  logging.debug("dd2")
"""




"""
# 56:xrange：指定した範囲を返す。tolist()メソッドによってリストに変換可能
print xrange(1, 10) # xrange(1, 10)
print range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


"""
# 55:type：引数の型を返す。型を判別するとき、サンプルのようにtypesモジュールをインポートして、typesのメンバと比較を行う
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
"""


"""
# 54:tuple：引数をタプルに変換
print tuple('ABC') # ('A', 'B', 'C')
print tuple([1,2,3,4]) # (1, 2, 3, 4)
"""


"""
# 53:str：引数を文字列に変換
print str(100) # '100'
print str(1.4e-5) # '1.4e-005'
print str(2+5j) # '(2+5j)'
print str((1,2,3)) # '(1, 2, 3)'
"""


"""
# 52:round：四捨五入
print round(5.5) # 6.0
print int(5.5) # 5
"""

"""
# 51:raw_input：コンソールから入力。文字のみ
a=raw_input('文字入力>>') # 文字入力>>
print a
"""


"""
# 50:pow：べき乗。x**yでも可能
print pow(2, 4) # 16
print pow(3.14, 0.5) # 1.772004514666935
print pow(1j, 2) # (-1+0j)
print 2**4 # 16
"""


# 49:open：ファイルオブジェクトを作成
#open(filename [,mode [,buffsize]])
#filename：ファイル名
#mode：'r', 'w','a','b' # read, write, append, binary +もつけられる
# buffsize：ファイルオブジェクトのバッファサイズ。
# 0：バッファリングなし
# 1：ラインバッファ
# その他の正数：実際のバッファサイズ
# 負数：システムデフォルト値


"""
# 48:oct：8進数に変換
print oct(16) # '020'
print oct(10000L) # '023420L'
"""

"""
# 47:min：最小値
print min(['X','XX','XXX','0']) # '0'
print min('C','B','A','T') # 'A'
"""

"""
# 46:max：最大値
print max((3,10,5,12,0)) # 12
print max(1,2,3,4,5,6) # 6
"""


"""
# 45:map：function(関数)をリストに適用。引数functionは'None'も指定可能(何もしない)
def f(x):
  return (x + '?')

def f2(x, y):
  return (str(x) + str(y))

a = ['a', 'b', 'c']
print map(f, a) # ['a?', 'b?', 'c?']
b = ['A', 'B', 'C', 'D']
print map(None, b) #  ['A', 'B', 'C', 'D']
print map(f2, b, a) #  ['Aa', 'Bb', 'Cc', 'DNone']
"""

"""
# 44:long：Long整数に変換
n=long(1e8)
print n # 100000000L
n=long(67)
print n # 67L
"""


"""
# 43:list：リストに変換
a=list("ABCD")
print a # ['A', 'B', 'C', 'D']
a=list(('AA','AB','AC','AD'))
print a # ['AA', 'AB', 'AC', 'AD']
"""


"""
# 42:len：シーケンスの長さを返す
n=len('AAA')
print n # 3

n=len("0123456")
print n # 7

n=len((1,2,3,4,5,6))
print n # 6

n=len(['AAA', 'BCD','AHX', 'AQW'])
print n # 4
"""

"""
# 41:isinstance：クラスからオブジェクトが生成されていればtrue
class Class1:
  def __init__(self):
    x = 0
  def inc():
    x = x + 1

class Class2:
  def __init__(self):
    y = 0
  def dec():
    y = y - 1

o = Class1() # oがClass1のインスタンスに(つまりClass1からoが生成)
print isinstance(o, Class1)  # 1=true=Class1から生成されている
print isinstance(o, Class2)  # 0=false=Class2から生成されていない
"""

"""
# 40:int：引数を整数型に。複素数は引数として使えない
n=int("64")
print n # 64
n=int(-2.4)
print n # -2
"""

"""
# 39:input：コンソールから入力。数値のみ
a = input('入力>>') # 入力>> 150
print a # 150
"""


"""
# 38:hex：16進数に変換
print hex(255) # '0xff'
print hex(65536) # '0x10000'
#print hex(48.5) # <==エラー。実数は不可
print hex(100000L) # '0x186A0L'
"""


"""
# 37:hash：ハッシュ値を返す。ディクショナリのキーをすばやく検索するのに使う
print hash("abc") # -1600925533
print hash("ABC") # 826005955
print hash("oiiiajajk") # -359209788
"""


"""
# 36:filter：関数が真になるものだけリスト
def even(n):
  return (n % 2 == 0); # 2で割って0になる数値を返す

a = [1,2,3,4,5,6,7,8,9,0]
print filter(even, a) # [2, 4, 6, 8, 0]
"""

"""
# 35:float：引数を実数に。複素数は不可
a = float("1.45")
print a # 1.45
"""


"""
# 34:execfile：ファイル実行。戻り値はNone
execfile("34Tst.py")
"""


"""
# 33:eval：文字列を解釈実行
x=10
y=eval('x+1')
print y # 11
"""


"""
# 32:divmod：商と剰余をタプルで
a = divmod(100, 3)
print a # (33, 1)
print a[0] # 33 表のいっこ目
"""


"""
# 31:complex：2つの引数を実部、虚部とする複素数を値として返す。
#2つ目の引数を省略すると虚部が0である複素数(実数型でないことに注意)を返す。
#引数が文字列の場合、虚部は無視され0とみなされる。→エラーになる
z = complex(0, 1)
print z # 1j
w = complex('-1', '1')
print w # (-1+0j)→エラー
w = complex(2, 0)
print w # (2+0j)
"""


"""
# 30:cmp：比較 < -1、== 0、> 1
a = 0
print cmp(a, 0) # 0
print cmp(a, 1) # -1
print cmp(a, -1) # 1

z = 1+1j
print cmp(z, 2+2j) # -1?
print cmp(z, -1-1j) # 1?
"""


"""
# 29:ord：文字を整数値(ASCIIコード)に
b = ord('a')
print hex(b) #  0x61
"""

"""
# 28:chr：整数値を文字に
a = chr(0x41)
print a # A
"""

"""
# 27:buffer：引数の一部分を取り出す
a = buffer('123456789', 3, 4)
print a # 4567
"""

"""
# 26:apply：関数を実行
def func(x):
  return x+1

a = [2]
print a # [2]
print apply(func, a) # 3
"""

"""
# 25:abs：絶対値を取得
print abs(-1) # 1
print abs(5) # 5
print abs(1+1j) # 1.41421356237
"""


"""
# 24:classキーワード：クラスを定義。()で基底クラスを指定することによって継承を行うことも可能です。
# 継承は多重継承が可能で（）内をカンマで区切って基底クラスを書きます。
#クラス定義-1
class Point:
  x = 0
  y = 0
  def SetPoint(newX, newY):
    x = newX
    y = newY

p = Point()
p.x = 1
p.y = 2
print "p.x = ", p.x # p.x = 1
print "p.y = ", p.y # p.y = 2

p.SetPoint(3)
print "p.x = ", p.x # p.x = 1
print "p.y = ", p.y # p.y = 2

#クラス定義-2
class Base:
  x = 0

class InhClass(Base):
  y = 1

a = Base # aにBaseクラスが入る
print a.x # 0 Base.xがプリント
b = InhClass # bにInhClass(Base)が入る
print b.y # 1 InhClass.yがプリント
print b.x # 0 InhClass.x ココがポイント
"""


"""
# 23:defキーワード：関数を定義。パラメータのデフォルト値を指定することもできる
# 関数定義-1
def sum(a):
  y = 0
  for x in a:
    y = y + x
  return y
print sum([1,2,3,4]) # 10

# 関数定義-2
def f(x = 1, y = 1):
  return 2 * x + y
print f() # 3 = (2*1)+1
print f(0,2) # 2 = (2*0)+2
"""


"""
# 22:try文：try…except…とtry…finally…の2つの形式がある。これはC言語の構造化例外構文と似ている
# except節：例外が発生したとき実行される
# finally節は例外の有無に関わらず必ず1回実行される
# これら2つのtry文はネストさせることはできるが try…except…finally… と書くことはできない。

# try文
for x in [1,3,0]:
  print x # 1 3 0
  try:
    try:
      y = 10 / x # 計算できるかの判定
    except:
      print "Exception"
  finally:
    print "End"
"""



"""
# 21:for文：C言語のfor文とは異なり、Visual BasicのFor Each文に似ている。while文同様、else節を付けられる。
#"for" target_list "in" expression_list ":" suite ["else" ":" suite]
# for文
for x in [1,2,3,4,5]:
  print x # 1 2 3 4 5
else:
  print "End" # End

for x in range(1,5):
  print x # 1 2 3 4
else:
  print "End" # End
"""


"""
# 20:while文：C言語と違ってelse:を付けられる。else節はwhileから抜けたとき1回だけ実行される。
#"while" expression ":" suite ["else" ":" suite]
# while文
i = 0
a = 10
while i < 10:
  i = i + 1
  print i, a # 1～10 10
else:
  a = 5
print i, a # 10 5
"""


"""
# C言語のswitch文に相当する文はないが、if文の構文が単純なので
#if-2
x=input("0か1か2")
if x == 0:
  print "xは0"
if x == 1:
  print "xは1"
if x == 2:
  print "xは2"
"""


"""
# if文のみ。if,elif,elseの後には：(コロン)が必要。インデントで{}を表現。
#"if" expression ":" suite ("elif" expression ":" suite)* ["else" ":" suite]
#if-1
x=input("数字入れて")
if x > 0:
  print "xは0以上"
elif x == 0:
  print "xは0"
else:
  print "xは0以下"
"""



"""
# 18:exec文：動的なPythonコードを実行
# "exec" expression ["in" expression ["," expression]]
# expression：Pythonプログラム文字列、またはPythonプログラムファイル、コードオブジェクト

#exec文
import os
e = "x=2\nprint `x+1`"
exec e # 3

f = open("18Tst.py") # 18Tst.pyの内容(print 'exec文から実行')
exec f # exec文から実行
"""


"""
# 17:global文：プロジェクト全体に有効な名前を宣言。通常の変数はモジュール内の名前空間だけで有効。
#global文
global Wahuwahu
"""


"""
# 16:import文：外部モジュールをインポートし、その中のオブジェクトを使えるようにする。
# ビルトインモジュール以外のPythonモジュールを使う場合もimport文が必要になる。
# import文には3つの形式がある。
# (形式1) import モジュール,モジュール・・・
# (形式2）from モジュール import *
# (形式3）from モジュール import ( 識別子.)識別子

#import
import os
from sys import *

# import文は２つのステップで実行される
# (ステップ1)モジュールを見つけ初期化
# (ステップ2)ローカルな名前空間でモジュールに含まれるオブジェクトの名前を定義
# これによって、module.nameと表現しないでnameだけで表現できることを意味する
"""

"""
# 15:continue文：ループ内の先頭の文へジャンプ。ループ内の残りの文の実行をキャンセルし、次の繰り返しを行う
#continue文
#ある場合(continueを6から繰り返し9まで到達する)
for i in range(0, 10):
  if i > 5:
    continue
  print i # 0 1 2 3 4 5

#ない場合
for i in range(0, 10):
  if i > 5:
    pass
  print i # 0 1 2 3 4 5 6 7 8 9
"""

"""
# 14:break文：繰り返し文からの脱出。try ..finallyで囲まれていたときは、finally部分はbreak前に実行
# break文
for i in range(0, 5):
  if i == 2:
    break

print i # 2
"""

"""
# 13:raise文：例外を発生させる。引数は一般的にはオブジェクトを指定
#raise文
raise # 引数のないraiseは直前に発生した例外を再発生させます。
raise "Exception1"
raise "Exception","Type1" # 一般的には3つの引数を取り、複雑な例外を起こせる
"""

"""
# 12:return文：関数を終了するとき呼び出す。C言語と異なり複数の値も返す
# 関数とreturn文
def func1():
  x = [0,2,5]
  return x, "Hello"

print func1() # ([0, 2, 5], 'Hello')
"""



"""
# 11:print文：標準出力に値のリストを出力
x = "Hell world!"
print x # Hell world!

x = [4,5,9]
print x # [4,5,9]
y = "JIGOKU\n"
print y
print y, # カンマをつけると"\n"が含まれていても改行が2回されない
"""


"""
# 10:del文：リストを再帰的に削除。リソース(ヒープメモリ)を解放するのに使う
# del文
x = range(1, 10)
print x
del x
print x  # xが削除されたのでこの文は例外を発生させる
"""


"""
# 09:pass文：C言語での空文
#スレッドがstateを０以外の値に変更するまで待つような文
#C言語
#while (state == 0)
;
#Python
while state == 0:
  pass
"""


"""
# 08:代入文：Pythonでは変数はCやPascalのように「型」を持たない。代入は型を考えずに行える
# リストの代入
x = [1,3,5]
print x # [1,3,5]

# 複数の変数への代入
x,y = 10,20
print x,y # 10 20
"""


"""
# 07:assert文：デバッグ時にある条件が発生したとき変数内容を表示。assert文は次の文と同値。
# if __debug__: if not expression: raise AssertionError
try:
  for x in range(0, 10):
    assert x < 5
except:
  print x # x >= 5になったとき例外が発生し、５が表示される
"""


"""
# 06:演算子：C言語のような++や--, +=,-=などは使えない。代わりにC言語にない**（べき乗）が使える
# ブール演算子：and,or,not
# 比較演算子：==,<,>,<=,>=。これらは算術演算子のように連続して書ける。
# (例)：a > b == c (a > bかつa ==c)
# オブジェクトの比較演算子：isとis not。2つのオブジェクトが同じものか(あるいはそうでないか)を判別
# ブール演算：Visual BasicやPascalのようなtrue,falseという値はなく、Cライクに0と0以外の値で論理を判定
x = 4
print x**2 # 16

y = 1+2j # 複素数
print x*y # (4+8j)

i = 0
# print i++ # これは不正
# i += 10 # これは不正

x = [1,2,3]
print 2 * x # [1, 2, 3, 1, 2, 3]
# print x - 1 # これは不正

x = {0:5,1:10,3:17}
# print 2 * x # これは不正

b = 0x1d
print ~b # -30

# 論理演算子：~, |, &, ^
c = 0xff
print b | c, b & c, b ^ c # 255 29 226
"""



"""
# 05:複素数：Pythonでは標準で複素数をサポート
x = 1 - 1j # 1-jとは書けないことに注意
y = 2 + 2j
print x + y # (3+1j)
"""

"""
# 04:解釈実行される文字列：` `で囲まれた中身は解釈実行。
# Perlでは" "の中身は解釈されるが、Pythonでは解釈されない
x = 10
y = 20
s = "Value = " + `x + y`
print s # Value = 30
s = "Value = `x + y`"
print s # Value = `x + y`
"""

"""
# 03:ディクショナリ(マッピング)：中カッコ{ }で値のペアを囲んで表現
x = {"I":"Me","You":"You","He":"Him"}
print x
print x["I"]

x = {"I":"me", "You":"you", "He":"him", "She":"her"}
print x # {'He': 'him', 'She': 'her', 'You': 'you', 'I': 'me'}
print x["He"] # him
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


