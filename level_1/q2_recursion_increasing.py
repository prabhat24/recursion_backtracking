# given a number n.... print numbers from 1 to n in increasing order

def recursion_inc(n):
	if n == 0:
		return
	recursion_inc(n-1)
	print(n)

if __name__ == '__main__':
	recursion_inc(5)