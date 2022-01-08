def display_bottom_up(arr, ind):
	if ind == len(arr):
		return
	display_bottom_up(arr, ind+1)	
	print(arr[ind])

def display_top_down(arr, ind):
	if ind < 0:
		return
	print(arr[ind])
	display_top_down(arr, ind-1)

if __name__ == "__main__":
	arr = [1,2,3,4]
	display_bottom_up(arr, 0)
	display_top_down(arr, len(arr)-1)
