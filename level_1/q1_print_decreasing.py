# given a number n.... print numbers from n to 1 in decreasing order

def recursion_desc(n):
	if n == 0:
		return
	print(n)
	recursion_desc(n-1)

if __name__ == '__main__':
	recursion_desc(5)