# 03:�f�B�N�V���i��(�}�b�s���O)�F���J�b�R{ }�Œl�̃y�A���͂�ŕ\��
x = {"I":"Me","You":"You","He":"Him"}
print x
print x["I"]

x = {"I":"me", "You":"you", "He":"him", "She":"her"}
print x # {'He': 'him', 'She': 'her', 'You': 'you', 'I': 'me'}
print x["He"] # him

# 04:���ߎ��s����镶����F` `�ň͂܂ꂽ���g�͉��ߎ��s�BPerl�ł�" "�̒��g�͉��߂���邪�APython�ł͉��߂���Ȃ�
x = 10
y = 20
s = "Value = " + `x + y`
print s # Value = 30
s = "Value = `x + y`"
print s # Value = `x + y`

# 05:���f���FPython�ł͕W���ŕ��f�����T�|�[�g
x = 1 - 1j # 1-j�Ƃ͏����Ȃ����Ƃɒ���
y = 2 + 2j
print x + y # (3+1j)

# 06:���Z�q�FC����̂悤��++��--, +=,-=�Ȃǂ͎g���Ȃ��B�����C����ɂȂ�**�i�ׂ���j���g����
�_�����Z�q�F~, |, &, ^
�u�[�����Z�q�Fand,or,not
��r���Z�q�F==,<,>,<=,>=�B�����͎Z�p���Z�q�̂悤�ɘA�����ď�����B
(��)�Fa > b == c (a > b����a ==c)
�I�u�W�F�N�g�̔�r���Z�q�Fis��is not�B2�̃I�u�W�F�N�g���������̂�(���邢�͂����łȂ���)�𔻕�
�u�[�����Z�FVisual Basic��Pascal�̂悤��true,false�Ƃ����l�͂Ȃ��AC���C�N��0��0�ȊO�̒l�Ř_���𔻒�
x = 4
print x**2 # 16
y = 1+2j # ���f��
print x*y # (4+8j)
i = 0
# print i++ # ����͕s��
# i += 10 # ����͕s��
x = [1,2,3]
print 2 * x # [1, 2, 3, 1, 2, 3]
# print x - 1 # ����͕s��
x = {0:5,1:10,3:17}
# print 2 * x # ����͕s��
b = 0x1d
print ~b # -30
c = 0xff
print b | c, b & c, b ^ c # 255 29 226


# 07:assert���F�f�o�b�O���ɂ�����������������Ƃ��ϐ����e��\���Bassert���͎��̕��Ɠ��l�B
if __debug__: if not expression: raise AssertionError
try:
	for x in range(0, 10):
		assert x < 5
except:
	print x # x >= 5�ɂȂ����Ƃ���O���������A�T���\�������

# 08:������FPython�ł͕ϐ���C��Pascal�̂悤�Ɂu�^�v�������Ȃ��B����͌^���l�����ɍs����
#���X�g�̑��
x = [1,3,5]
print x # [1,3,5]
#�����̕ϐ��ւ̑��
x,y = 10,20
print x,y # 10 20

# 09:pass���FC����ł̋�
#�X���b�h��state���O�ȊO�̒l�ɕύX����܂ő҂悤�ȕ�
#C���� 
while (state == 0)
;
#Python
while state == 0:
	pass

# 10:del���F���X�g���ċA�I�ɍ폜�B���\�[�X(�q�[�v������)���������̂Ɏg��
# del��
x = range(1, 10)
print x
del x
print x  # x���폜���ꂽ�̂ł��̕��͗�O�𔭐�������

# 11:print���F�W���o�͂ɒl�̃��X�g���o��
x = "Hell world!"
print x # Hell world!
x = [4,5,9]
print x # [4,5,9]
y = "JIGOKU\n"
print y
print y, # �J���}�������"\n"���܂܂�Ă��Ă����s��2�񂳂�Ȃ�

# 12:return���F�֐����I������Ƃ��Ăяo���BC����ƈقȂ蕡���̒l���Ԃ�
# �֐���return��
def func1():
	x = [0,2,5]
	return x, "Hello"
print func1() # ([0, 2, 5], 'Hello')

# 13:raise���F��O�𔭐�������B�����͈�ʓI�ɂ̓I�u�W�F�N�g���w��
#raise��
raise # �����̂Ȃ�raise�͒��O�ɔ���������O���Ĕ��������܂��B
raise "Exception1"
raise "Exception","Type1" # ��ʓI�ɂ�3�̈��������A���G�ȗ�O���N������

# 14:break���F�J��Ԃ�������̒E�o�Btry ..finally�ň͂܂�Ă����Ƃ��́Afinally������break�O�Ɏ��s
# break��
for i in range(0, 5):
	if i == 2:
		break
print i # 2

# 15:continue���F���[�v���̐擪�̕��փW�����v�B���[�v���̎c��̕��̎��s���L�����Z�����A���̌J��Ԃ����s��
#continue��
#����ꍇ(continue��6����J��Ԃ�9�܂œ��B����)
for i in range(0, 10):
	if i > 5:
		continue
	print i # 0 1 2 3 4 5
#�Ȃ��ꍇ
for i in range(0, 10):
	if i > 5:
		pass
	print i # 0 1 2 3 4 5 6 7 8 9

# 16:import���F�O�����W���[�����C���|�[�g���A���̒��̃I�u�W�F�N�g���g����悤�ɂ���B
�r���g�C�����W���[���ȊO��Python���W���[�����g���ꍇ��import�����K�v�ɂȂ�B
import���ɂ�3�̌`��������B
(�`��1) import ���W���[��,���W���[���E�E�E
(�`��2�jfrom ���W���[�� import *
(�`��3�jfrom ���W���[�� import ( ���ʎq.)���ʎq

#import
import os
from sys import *

import���͂Q�̃X�e�b�v�Ŏ��s�����
(�X�e�b�v1)���W���[��������������
(�X�e�b�v2)���[�J���Ȗ��O��ԂŃ��W���[���Ɋ܂܂��I�u�W�F�N�g�̖��O���`
����ɂ���āAmodule.name�ƕ\�����Ȃ���name�����ŕ\���ł��邱�Ƃ��Ӗ�����

# 17:global���F�v���W�F�N�g�S�̂ɗL���Ȗ��O��錾�B�ʏ�̕ϐ��̓��W���[�����̖��O��Ԃ����ŗL���B
#global��
global Wahuwahu

# 18:exec���F���I��Python�R�[�h�����s
"exec" expression ["in" expression ["," expression]]
expression�FPython�v���O����������A�܂���Python�v���O�����t�@�C���A�R�[�h�I�u�W�F�N�g

#exec��
import os
e = "x=2\nprint `x+1`"
exec e # 3
f = open("18Tst.py") # 18Tst.py�̓��e(print 'exec��������s')
exec f # exec��������s



# if���̂݁Bif,elif,else�̌�ɂ́F(�R����)���K�v�B�C���f���g��{}��\���B
"if" expression ":" suite ("elif" expression ":" suite)* ["else" ":" suite]
#if-1
x=input("���������")
if x > 0:
	print "x��0�ȏ�"
elif x == 0:
	print "x��0"
else:
	print "x��0�ȉ�"

# C�����switch���ɑ������镶�͂Ȃ����Aif���̍\�����P���Ȃ̂�
#if-2
x=input("0��1��2")
if x == 0:
	print "x��0"
if x == 1:
	print "x��1"
if x == 2:
	print "x��2"



# 20:while���FC����ƈ����else:��t������Belse�߂�while���甲�����Ƃ�1�񂾂����s�����B
"while" expression ":" suite ["else" ":" suite]
# while��
i = 0
a = 10
while i < 10:
	i = i + 1
	print i, a # 1�`10 10
else:
	a = 5
print i, a # 10 5

# 21:for���FC�����for���Ƃ͈قȂ�AVisual Basic��For Each���Ɏ��Ă���Bwhile�����l�Aelse�߂�t������B
"for" target_list "in" expression_list ":" suite ["else" ":" suite]
# for��
for x in [1,2,3,4,5]:
	print x # 1 2 3 4 5
else:
	print "End" # End

for x in range(1,5):
	print x # 1 2 3 4
else:
	print "End" # End

# 22:try���Ftry�cexcept�c��try�cfinally�c��2�̌`��������B�����C����̍\������O�\���Ǝ��Ă���
# except�߁F��O�����������Ƃ����s�����
# finally�߂͗�O�̗L���Ɋւ�炸�K��1����s�����
# �����2��try���̓l�X�g�����邱�Ƃ͂ł��邪 try�cexcept�cfinally�c �Ə������Ƃ͂ł��Ȃ��B

# try��
for x in [1,3,0]:
	print x # 1 3 0
	try:
		try:
			y = 10 / x # �v�Z�ł��邩�̔���
		except:
			print "Exception"
	finally:
		print "End"



# 23:def�L�[���[�h�F�֐����`�B�p�����[�^�̃f�t�H���g�l���w�肷�邱�Ƃ��ł���
# �֐���`-1
def sum(a):
	y = 0
	for x in a:
		y = y + x
	return y
print sum([1,2,3,4]) # 10

# �֐���`-2
def f(x = 1, y = 1):
	return 2 * x + y
print f() # 3 = (2*1)+1
print f(0,2) # 2 = (2*0)+2


# 24:class�L�[���[�h�F�N���X���`�B()�Ŋ��N���X���w�肷�邱�Ƃɂ���Čp�����s�����Ƃ��\�ł��B�p���͑��d�p�����\�Łi�j�����J���}�ŋ�؂��Ċ��N���X�������܂��B
#�N���X��`-1
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

#�N���X��`-2
class Base:
	x = 0

class InhClass(Base):
	y = 1

a = Base # a��Base�N���X������
print a.x # 0 Base.x���v�����g
b = InhClass b��InhClass(Base)������
print b.y # 1 InhClass.y���v�����g
print b.x # 0 InhClass.x �R�R���|�C���g


# 25:abs�F��Βl���擾
print abs(-1) # 1
print abs(5) # 5
print abs(1+1j) # 1.41421356237

# 26:apply�F�֐������s
def func(x):
	return x+1

a = [2]
print a # [2]
print apply(func, a) # 3

# 27:buffer�F�����̈ꕔ�������o��
a = buffer('123456789', 3, 4)
print a # 4567

# 28:chr�F�����l�𕶎���
a = chr(0x41)
print a # A

# 29:ord�F�����𐮐��l(ASCII�R�[�h)��
b = ord('a')
print hex(b) #  0x61

# 30:cmp�F��r < -1�A== 0�A> 1
a = 0
print cmp(a, 0) # 0
print cmp(a, 1) # -1
print cmp(a, -1) # 1
z = 1+1j
print cmp(z, 2+2j) # -1 
print cmp(z, -1-1j) # 1

# 31:complex�F2�̈����������A�����Ƃ��镡�f����l�Ƃ��ĕԂ��B
2�ڂ̈������ȗ�����Ƌ�����0�ł��镡�f��(�����^�łȂ����Ƃɒ���)��Ԃ��B
������������̏ꍇ�A�����͖�������0�Ƃ݂Ȃ����B
z = complex(0, 1)
print z # 1j
w = complex('-1', '1')
print w # (-1+0j)
w = complex(2, 0)
print w # (2+0j)

# 32:divmod�F���Ə�]���^�v����
a = divmod(100, 3)
print a # (33, 1)
print a[0] # 33 �\�̂�������

# 33:eval�F����������ߎ��s
x=10
y=eval('x+1')
print y # 11

# 34:execfile�F�t�@�C�����s�B�߂�l��None
execfile("34Tst.py")

# 35:float�F�����������ɁB���f���͕s��
a = float("1.45")
print a # 1.45

# 36:filter�F�֐����^�ɂȂ���̂������X�g
def even(n):
	return (n % 2 == 0); # 2�Ŋ�����0�ɂȂ鐔�l��Ԃ�

a = [1,2,3,4,5,6,7,8,9,0]
print filter(even, a) # [2, 4, 6, 8, 0]

# 37:hash�F�n�b�V���l��Ԃ��B�f�B�N�V���i���̃L�[�����΂₭��������̂Ɏg��
hash("abc") # -1600925533
hash("ABC") # 826005955
hash("oiiiajajk") # -359209788

# 38:hex�F16�i���ɕϊ�
hex(255) # '0xff'
hex(65536) # '0x10000'
hex(48.5) # <==�G���[�B�����͕s��
hex(100000L) # '0x186A0L'

# 39:input�F�R���\�[��������́B���l�̂�
a = input('����>>') # ����>> 150
a # 150

# 40:int�F�����𐮐��^�ɁB���f���͈����Ƃ��Ďg���Ȃ�
n=int("64")
n # 64
n=int(-2.4)
n # -2

# 41:isinstance�F�N���X����I�u�W�F�N�g����������Ă����true
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
   
o = Class1() # o��Class1�̃C���X�^���X��(�܂�Class1����o������)
print isinstance(o, Class1)  # 1=true=Class1���琶������Ă���
print isinstance(o, Class2)  # 0=false=Class2���琶������Ă��Ȃ�

# 42:len�F�V�[�P���X�̒�����Ԃ�
n=len('AAA')
n # 3
n=len("0123456")
n # 7
n=len((1,2,3,4,5,6))
n # 6
n=len(['AAA', 'BCD','AHX', 'AQW'])
n # 4

# 43:list�F���X�g�ɕϊ�
a=list("ABCD")
a # ['A', 'B', 'C', 'D']
a=list(('AA','AB','AC','AD'))
a # ['AA', 'AB', 'AC', 'AD']

# 44:long�FLong�����ɕϊ�
n=long(1e8)
n # 100000000L
n=long(67)
n # 67L

# 45:map�Ffunction(�֐�)�����X�g�ɓK�p�B����function��'None'���w��\(�������Ȃ�)
def f(x):
	return (x + '?')

def f2(x, y):
	return (str(x) + str(y))

a = ['a', 'b', 'c']
print map(f, a) # ['a?', 'b?', 'c?']
b = ['A', 'B', 'C', 'D']
print map(None, b) #  ['A', 'B', 'C', 'D']
print map(f2, b, a) #  ['Aa', 'Bb', 'Cc', 'DNone']

# 46:max�F�ő�l
max((3,10,5,12,0)) # 12
max(1,2,3,4,5,6) # 6

# 47:min�F�ŏ��l
min(['X','XX','XXX','0']) # '0'
min('C','B','A','T') # 'A'

# 48:oct�F8�i���ɕϊ�
oct(16) # '020'
oct(10000L) # '023420L'

# 49:open�F�t�@�C���I�u�W�F�N�g���쐬
open(filename [,mode [,buffsize]])
filename�F�t�@�C����
mode�F'r', 'w','a','b' # read, write, append, binary +��������
# buffsize�F�t�@�C���I�u�W�F�N�g�̃o�b�t�@�T�C�Y�B
# 0�F�o�b�t�@�����O�Ȃ�
# 1�F���C���o�b�t�@
# ���̑��̐����F���ۂ̃o�b�t�@�T�C�Y
# �����F�V�X�e���f�t�H���g�l

# 50:pow�F�ׂ���Bx**y�ł��\
pow(2, 4) # 16
pow(3.14, 0.5) # 1.772004514666935
pow(1j, 2) # (-1+0j)
2**4 # 16

# 51:raw_input�F�R���\�[��������́B�����̂�
a=raw_input('��������>>') # ��������>> wahuwahu
print a # wahuwahu

# 52:round�F�l�̌ܓ�
round(5.5) # 6.0
int(5.5) # 5

# 53:str�F�����𕶎���ɕϊ�
str(100) # '100'
str(1.4e-5) # '1.4e-005'
str(2+5j) # '(2+5j)'
str((1,2,3)) # '(1, 2, 3)'

# 54:tuple�F�������^�v���ɕϊ�
tuple('ABC') # ('A', 'B', 'C')
tuple([1,2,3,4]) # (1, 2, 3, 4)

# 55:type�F�����̌^��Ԃ��B�^�𔻕ʂ���Ƃ��A�T���v���̂悤��types���W���[�����C���|�[�g���āAtypes�̃����o�Ɣ�r���s��
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

# 56:xrange�F�w�肵���͈͂�Ԃ��Btolist()���\�b�h�ɂ���ă��X�g�ɕϊ��\
print xrange(1, 10) # xrange(1, 10)
print range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]










