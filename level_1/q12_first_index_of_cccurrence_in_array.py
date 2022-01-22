
def first_occurence_tpdown(arr, ind, key):
	if ind == len(arr):
		return None
	if arr[ind] == key:
		return ind
	return first_occurence_tpdown(arr, ind+1, key)

if __name__ == "__main__" :
	arr = [2,4,5,2,8,6,3,5,6,2]
	ind = 0
	print(first_occurence_tpdown(arr, ind, 5))