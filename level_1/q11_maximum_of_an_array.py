def max_bottom_up(arr, ind):
	if ind == len(arr) - 1:
		return arr[ind]
	lm = max_bottom_up(arr, ind + 1)
	return max(lm, arr[ind])


def max_top_down(arr, ind, msf):
	if ind == len(arr):
		return msf
	msf = max(msf, arr[ind])
	return max_top_down(arr, ind+1, msf)

if __name__ == '__main__':
	arr = [23,56,9,40,8,20]
	print(max_bottom_up(arr, 0))
	print(max_top_down(arr, 0, -1))
