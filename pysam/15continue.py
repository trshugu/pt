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
