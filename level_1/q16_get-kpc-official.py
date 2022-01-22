def func(str1, ind, AR, lsf, ssf):
	if ind == len(str1):
		lsf.append(ssf)
	else:
		inte = int(str1[ind])
		b_list = AR[inte]
		for ch in b_list:
			func(str1, ind+1, AR, lsf, ssf + ch)

def func2(string, AR):
	if not string:
		return [""]
	inte = int(string[0])
	ros = string[1:]
	lst = func2(ros, AR)

	mylist = []
	for ch in AR[inte]:
		for item in lst:
			mylist.append(ch + item)
	return mylist

if __name__ == '__main__':
	AR = [".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"]
	str1 = "578"	
	lsf = []
	func(str1, 0, AR, lsf, "")
	print(lsf)

	print(func2(str1, AR))
