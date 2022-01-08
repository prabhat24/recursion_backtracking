def pow(x, n):
	print(x, n)
	if n == 0:
		return 1
	p = pow(x, n//2)
	if n & 1 == 0:
		return p * p 
	else:
		return x * p * p

if __name__ == '__main__':
	print(pow(5, 3))