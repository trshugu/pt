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
