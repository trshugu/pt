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
