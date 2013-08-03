#ƒNƒ‰ƒX’è‹`-1
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
