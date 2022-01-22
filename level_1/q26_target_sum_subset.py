def target_sum_subset(arr, ind, target, lst):
	if ind == len(arr):
		if target == 0:
			print(lst)
		return
	else:
		# include
		lst.append(arr[ind])
		target_sum_subset(arr, ind +1, target-arr[ind], lst)
		# backtracking
		lst.pop(-1)

		# exclude
		target_sum_subset(arr, ind +1, target, lst)


if __name__ == '__main__':
	arr = [10, 20, 30, 40, 50]
	lst = []
	target_sum_subset(arr, 0, 70, lst)
