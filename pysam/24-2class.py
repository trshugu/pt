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
