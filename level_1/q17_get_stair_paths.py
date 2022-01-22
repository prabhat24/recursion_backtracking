def stair_paths(n):
	if n < 0:
		return []
	elif n == 0:
		return [""]

	else:
		one_step_res = stair_paths(n-1)
		for i in range(len(one_step_res)):
			one_step_res[i] = "1" + one_step_res[i]
		two_step_res = stair_paths(n-2)
		for i in range(len(two_step_res)):
			two_step_res[i] = "2" + two_step_res[i]
		three_step_res = stair_paths(n-3)
		for i in range(len(three_step_res)):
			three_step_res[i] = "3" + three_step_res[i]
		return one_step_res + two_step_res + three_step_res

if __name__ == '__main__':
	print(stair_paths(3))