def toh(n, src, dest, helper):
	if n == 0:
		return
	toh(n-1, src, helper, dest)
	print(f"move {n}th disc from {src} to {dest}")
	toh(n-1, helper, dest, src)

if __name__ == '__main__':
	toh(3, "A", "C", "B")