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
