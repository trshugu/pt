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
