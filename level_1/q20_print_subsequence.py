def print_subsequences(string, ind, asf):
	if ind == len(string):
		print(asf)
	else:
		print_subsequences(string, ind+1, asf+string[ind])
		print_subsequences(string, ind+1, asf)

if __name__ == '__main__':
	print_subsequences("abcd", 0, "")