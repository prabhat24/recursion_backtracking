def print_stairs_path(step, ans):
	if step<0:
		return
	elif step == 0:
		print(ans)
	else:
		print_stairs_path(step-1, ans + "1")
		print_stairs_path(step-2, ans + "2")
		print_stairs_path(step-3, ans + "3")



if __name__ == '__main__':
	print_stairs_path(5, "")
