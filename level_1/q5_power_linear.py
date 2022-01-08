def power_recursion_tp_down(x, n, ansf):
	if n == 0:
		return ansf
	ansf = ansf * x
	return power_recursion_tp_down(x, n-1, ansf)

def power_recursion_tp_bottom_up(x, n):
	if n == 0:
		return 1
	return x * power_recursion_tp_bottom_up(x, n-1)

if __name__ == '__main__':
	print(power_recursion_tp_down(5, 5, 1))
	print(power_recursion_tp_bottom_up(5, 5))
 	