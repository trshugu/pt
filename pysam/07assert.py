# assert文の例
try:
	for x in range(0, 10):
		assert x < 5
except:
	print x # x >= 5になったとき例外が発生し、５が表示される
