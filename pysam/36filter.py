def even(n):
	return (n % 2 == 0); # 2で割って0になる数値を返す

a = [1,2,3,4,5,6,7,8,9,0]
print filter(even, a) # [2, 4, 6, 8, 0]
