
def last_occurence_bottom_up(arr, ind, key):
	if ind == len(arr):
		return None
	lst_occur = last_occurence_bottom_up(arr, ind+1, key)
	if lst_occur:
		return lst_occur
	if arr[ind] == key:
		return ind
	else:
		return None

if __name__ == "__main__" :
	arr = [2,4,5,2,8,6,3,5,6,2]
	ind = 0
	print(last_occurence_bottom_up(arr, ind, 4))