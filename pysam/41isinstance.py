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
