def fact_tp_bottom_up(n):
	if n == 0:
		return 1
	return fact_tp_bottom_up(n-1) * n

def fact_top_down(n, fact):
	if n == 0:
		return fact
	fact = fact * n
	return fact_top_down(n-1, fact) 


if __name__ == '__main__':
	print(fact_tp_bottom_up(5))
	print(fact_top_down(5, 1))