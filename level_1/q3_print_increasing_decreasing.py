def pdi(n):
	if n == 0:
		return 0
	print(n)
	pdi(n-1)
	print(n)


if __name__ == '__main__':
	pdi(5)