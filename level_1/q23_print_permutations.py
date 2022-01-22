def print_permutations(string, ssf):
	if len(string) == 0:
		print(ssf)
	else:
		N = len(string)
		for i in range(0, N):
			new_string = string[0:i] + string[i+1: N]
			print_permutations(new_string, ssf + string[i])



if __name__ == "__main__":
	string = "abc"
	print_permutations(string, "")