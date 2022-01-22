def print_kpc(AR, string, ind, asf):
	if ind == len(string):
		print(asf)
	else:
		inte = int(string[ind])
		for ch in AR[inte]:
			print_kpc(AR, string, ind + 1, asf + ch)

if __name__ == "__main__":
	AR = [".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"]
	str1 = "578"
	print_kpc(AR, str1, 0, "")

