###########################################################################
#	Q＜読み方は
#	∪・人・)＜基本的にプリントの#のあとの文字は出てくる結果ですいじょう。
#	Q＜そんだけですか
#	∪・人・)＜コピペで実行するときは改行とかに気をつけてくださいいじょう
#	Q＜まだなんかあるのでは
#	∪・人・)＜かれんとディレクトリがpysamのほうが実行しやすいジョー
#	Q＜そもそもパイソンってどこにあるのよ
#	∪・人−)＜http://www.python.jp/Zope/download/pythoncore ここと
#	∪−人・)＜http://www.python.jp/Zope/download/JapaneseCodecs これ
###########################################################################
＊基本
01:組(タプル)：( )で囲んで表現。変更不可
a = 'a', 'b', 'c'
print a # ('a', 'b', 'c')
b = a, 'd'
print b # (('a', 'b', 'c'), 'd')
x = [1, 2, 3, b]
print x # [1, 2, 3, (('a', 'b', 'c'), 'd')]

02:リスト:[ ]で囲んで表現。連続した値はrange関数。変更可
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

03:ディクショナリ(マッピング)：中カッコ{ }で値のペアを囲んで表現
x = {"I":"Me","You":"You","He":"Him"}
print x
print x["I"]

x = {"I":"me", "You":"you", "He":"him", "She":"her"}
print x # {'He': 'him', 'She': 'her', 'You': 'you', 'I': 'me'}
print x["He"] # him

04:解釈実行される文字列：` `で囲まれた中身は解釈実行。Perlでは" "の中身は解釈されるが、Pythonでは解釈されない
x = 10
y = 20
s = "Value = " + `x + y`
print s # Value = 30
s = "Value = `x + y`"
print s # Value = `x + y`

05:複素数：Pythonでは標準で複素数をサポート
x = 1 - 1j # 1-jとは書けないことに注意
y = 2 + 2j
print x + y # (3+1j)

06:演算子：C言語のような++や--, +=,-=などは使えない。代わりにC言語にない**（べき乗）が使える
論理演算子：~, |, &, ^
ブール演算子：and,or,not
比較演算子：==,<,>,<=,>=。これらは算術演算子のように連続して書ける。
(例)：a > b == c (a > bかつa ==c)
オブジェクトの比較演算子：isとis not。2つのオブジェクトが同じものか(あるいはそうでないか)を判別
ブール演算：Visual BasicやPascalのようなtrue,falseという値はなく、Cライクに0と0以外の値で論理を判定
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
c = 0xff
print b | c, b & c, b ^ c # 255 29 226

＊単純なステートメント

07:assert文：デバッグ時にある条件が発生したとき変数内容を表示。assert文は次の文と同値。
if __debug__: if not expression: raise AssertionError
try:
	for x in range(0, 10):
		assert x < 5
except:
	print x # x >= 5になったとき例外が発生し、５が表示される

08:代入文：Pythonでは変数はCやPascalのように「型」を持たない。代入は型を考えずに行える
#リストの代入
x = [1,3,5]
print x # [1,3,5]
#複数の変数への代入
x,y = 10,20
print x,y # 10 20

09:pass文：C言語での空文
#スレッドがstateを０以外の値に変更するまで待つような文
#C言語 
while (state == 0)
;
#Python
while state == 0:
	pass

10:del文：リストを再帰的に削除。リソース(ヒープメモリ)を解放するのに使う
# del文
x = range(1, 10)
print x
del x
print x  # xが削除されたのでこの文は例外を発生させる

11:print文：標準出力に値のリストを出力
x = "Hell world!"
print x # Hell world!
x = [4,5,9]
print x # [4,5,9]
y = "JIGOKU\n"
print y
print y, # カンマをつけると"\n"が含まれていても改行が2回されない

12:return文：関数を終了するとき呼び出す。C言語と異なり複数の値も返す
# 関数とreturn文
def func1():
	x = [0,2,5]
	return x, "Hello"
print func1() # ([0, 2, 5], 'Hello')

13:raise文：例外を発生させる。引数は一般的にはオブジェクトを指定
#raise文
raise # 引数のないraiseは直前に発生した例外を再発生させます。
raise "Exception1"
raise "Exception","Type1" # 一般的には3つの引数を取り、複雑な例外を起こせる

14:break文：繰り返し文からの脱出。try ..finallyで囲まれていたときは、finally部分はbreak前に実行
# break文
for i in range(0, 5):
	if i == 2:
		break
print i # 2

15:continue文：ループ内の先頭の文へジャンプ。ループ内の残りの文の実行をキャンセルし、次の繰り返しを行う
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

16:import文：外部モジュールをインポートし、その中のオブジェクトを使えるようにする。
ビルトインモジュール以外のPythonモジュールを使う場合もimport文が必要になる。
import文には3つの形式がある。
(形式1) import モジュール,モジュール・・・
(形式2）from モジュール import *
(形式3）from モジュール import ( 識別子.)識別子

#import
import os
from sys import *

import文は２つのステップで実行される
(ステップ1)モジュールを見つけ初期化
(ステップ2)ローカルな名前空間でモジュールに含まれるオブジェクトの名前を定義
これによって、module.nameと表現しないでnameだけで表現できることを意味する

17:global文：プロジェクト全体に有効な名前を宣言。通常の変数はモジュール内の名前空間だけで有効。
#global文
global Wahuwahu

18:exec文：動的なPythonコードを実行
"exec" expression ["in" expression ["," expression]]
expression：Pythonプログラム文字列、またはPythonプログラムファイル、コードオブジェクト

#exec文
import os
e = "x=2\nprint `x+1`"
exec e # 3
f = open("18Tst.py") # 18Tst.pyの内容(print 'exec文から実行')
exec f # exec文から実行

＊判断文

if文のみ。if,elif,elseの後には：(コロン)が必要。インデントで{}を表現。
"if" expression ":" suite ("elif" expression ":" suite)* ["else" ":" suite]
#if-1
x=input("数字入れて")
if x > 0:
	print "xは0以上"
elif x == 0:
	print "xは0"
else:
	print "xは0以下"

C言語のswitch文に相当する文はないが、if文の構文が単純なので
#if-2
x=input("0か1か2")
if x == 0:
	print "xは0"
if x == 1:
	print "xは1"
if x == 2:
	print "xは2"

などと記述する

＊繰り返し文

20:while文：C言語と違ってelse:を付けられる。else節はwhileから抜けたとき1回だけ実行される。
"while" expression ":" suite ["else" ":" suite]
# while文
i = 0
a = 10
while i < 10:
	i = i + 1
	print i, a # 1〜10 10
else:
	a = 5
print i, a # 10 5

21:for文：C言語のfor文とは異なり、Visual BasicのFor Each文に似ている。while文同様、else節を付けられる。
"for" target_list "in" expression_list ":" suite ["else" ":" suite]
# for文
for x in [1,2,3,4,5]:
	print x # 1 2 3 4 5
else:
	print "End" # End

for x in range(1,5):
	print x # 1 2 3 4
else:
	print "End" # End

22:try文：try…except…とtry…finally…の2つの形式がある。これはC言語の構造化例外構文と似ている
except節：例外が発生したとき実行される
finally節は例外の有無に関わらず必ず1回実行される
これら2つのtry文はネストさせることはできるが try…except…finally… と書くことはできない。
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

＊関数定義

23:defキーワード：関数を定義。パラメータのデフォルト値を指定することもできる
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

＊クラス定義

24:classキーワード：クラスを定義。()で基底クラスを指定することによって継承を行うことも可能です。継承は多重継承が可能で（）内をカンマで区切って基底クラスを書きます。
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
b = InhClass bにInhClass(Base)が入る
print b.y # 1 InhClass.yがプリント
print b.x # 0 InhClass.x ココがポイント

＊関数

25:abs：絶対値を取得
print abs(-1) # 1
print abs(5) # 5
print abs(1+1j) # 1.41421356237

26:apply：関数を実行
def func(x):
	return x+1

a = [2]
print a # [2]
print apply(func, a) # 3

27:buffer：引数の一部分を取り出す
a = buffer('123456789', 3, 4)
print a # 4567

28:chr：整数値を文字に
a = chr(0x41)
print a # A

29:ord：文字を整数値(ASCIIコード)に
b = ord('a')
print hex(b) #  0x61

30:cmp：比較 < -1、== 0、> 1
a = 0
print cmp(a, 0) # 0
print cmp(a, 1) # -1
print cmp(a, -1) # 1
z = 1+1j
print cmp(z, 2+2j) # -1 
print cmp(z, -1-1j) # 1

31:complex：2つの引数を実部、虚部とする複素数を値として返す。
2つ目の引数を省略すると虚部が0である複素数(実数型でないことに注意)を返す。
引数が文字列の場合、虚部は無視され0とみなされる。
z = complex(0, 1)
print z # 1j
w = complex('-1', '1')
print w # (-1+0j)
w = complex(2, 0)
print w # (2+0j)

32:divmod：商と剰余をタプルで
a = divmod(100, 3)
print a # (33, 1)
print a[0] # 33 表のいっこ目

33:eval：文字列を解釈実行
x=10
y=eval('x+1')
print y # 11

34:execfile：ファイル実行。戻り値はNone
execfile("34Tst.py") # ∪・人・)＜出演

35:float：引数を実数に。複素数は不可
a = float("1.45")
print a # 1.45

36:filter：関数が真になるものだけリスト
def even(n):
	return (n % 2 == 0); # 2で割って0になる数値を返す

a = [1,2,3,4,5,6,7,8,9,0]
print filter(even, a) # [2, 4, 6, 8, 0]

37:hash：ハッシュ値を返す。ディクショナリのキーをすばやく検索するのに使う
hash("abc") # -1600925533
hash("ABC") # 826005955
hash("oiiiajajk") # -359209788

38:hex：16進数に変換
hex(255) # '0xff'
hex(65536) # '0x10000'
hex(48.5) # <==エラー。実数は不可
hex(100000L) # '0x186A0L'

39:input：コンソールから入力。数値のみ
a = input('入力>>') # 入力>> 150
a # 150

40:int：引数を整数型に。複素数は引数として使えない
n=int("64")
n # 64
n=int(-2.4)
n # -2

41:isinstance：クラスからオブジェクトが生成されていればtrue
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

42:len：シーケンスの長さを返す
n=len('AAA')
n # 3
n=len("0123456")
n # 7
n=len((1,2,3,4,5,6))
n # 6
n=len(['AAA', 'BCD','AHX', 'AQW'])
n # 4

43:list：リストに変換
a=list("ABCD")
a # ['A', 'B', 'C', 'D']
a=list(('AA','AB','AC','AD'))
a # ['AA', 'AB', 'AC', 'AD']

44:long：Long整数に変換
n=long(1e8)
n # 100000000L
n=long(67)
n # 67L

45:map：function(関数)をリストに適用。引数functionは'None'も指定可能(何もしない)
def f(x):
	return (x + '?')

def f2(x, y):
	return (str(x) + str(y))

a = ['a', 'b', 'c']
print map(f, a) # ['a?', 'b?', 'c?']
b = ['A', 'B', 'C', 'D']
print map(None, b) #  ['A', 'B', 'C', 'D']
print map(f2, b, a) #  ['Aa', 'Bb', 'Cc', 'DNone']

46:max：最大値
max((3,10,5,12,0)) # 12
max(1,2,3,4,5,6) # 6

47:min：最小値
min(['X','XX','XXX','0']) # '0'
min('C','B','A','T') # 'A'

48:oct：8進数に変換
oct(16) # '020'
oct(10000L) # '023420L'

49:open：ファイルオブジェクトを作成
open(filename [,mode [,buffsize]])
filename：ファイル名
mode：'r', 'w','a','b' # read, write, append, binary +もつけられる
buffsize：ファイルオブジェクトのバッファサイズ。
0：バッファリングなし
1：ラインバッファ
その他の正数：実際のバッファサイズ
負数：システムデフォルト値

50:pow：べき乗。x**yでも可能
pow(2, 4) # 16
pow(3.14, 0.5) # 1.772004514666935
pow(1j, 2) # (-1+0j)
2**4 # 16

51:raw_input：コンソールから入力。文字のみ
a=raw_input('文字入力>>') # 文字入力>> wahuwahu
print a # wahuwahu

52:round：四捨五入
round(5.5) # 6.0
int(5.5) # 5

53:str：引数を文字列に変換
str(100) # '100'
str(1.4e-5) # '1.4e-005'
str(2+5j) # '(2+5j)'
str((1,2,3)) # '(1, 2, 3)'

54:tuple：引数をタプルに変換
tuple('ABC') # ('A', 'B', 'C')
tuple([1,2,3,4]) # (1, 2, 3, 4)

55:type：引数の型を返す。型を判別するとき、サンプルのようにtypesモジュールをインポートして、typesのメンバと比較を行う
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

56:xrange：指定した範囲を返す。tolist()メソッドによってリストに変換可能
print xrange(1, 10) # xrange(1, 10)
print range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

57:

58:


＊文字列

x = 'abcde'
x[1] # 'b' インデクシング
x[1:3] # 'bc' スライス
x[1:-1] # 'bcd' スライス
"a %s pen" % 'red' # 文字列フォーマット
"One %d Three" % 2 # 文字列フォーマット
'a' in x # 1 シーケンスメンバーテスト
'abc' is x # 0 比較演算









