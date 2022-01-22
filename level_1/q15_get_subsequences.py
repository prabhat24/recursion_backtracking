def print_subsequences(string, ssf, ind, lst):
	if ind == len(string):
		lst.append(ssf)
	else:
		print_subsequences(string, ssf + string[ind], ind+1, lst)
		print_subsequences(string, ssf, ind+1, lst)

def print_subsequences_m2(string):
	if string=="":
		return ["",]
	ch = string[0]
	ros = string[1:]
	lst = print_subsequences_m2(ros)
	new_lst = []
	for item in lst:
		new_lst.append(ch + item)
		new_lst.append(item)
	return new_lst


if __name__ == '__main__':
	string = "abcd"
	lst = []
	print_subsequences(string, "", 0, lst)
	abc = print_subsequences_m2(string)
	print(abc)