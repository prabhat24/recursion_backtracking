
def generate(ind, osf, csf, N, ssf):
	if csf > osf:
		return
	elif osf > N//2:
		return
	elif ind == N and osf == csf:
		print(ssf)
	else:
		generate(ind + 1, osf + 1, csf, N, ssf+"(")
		generate(ind + 1, osf, csf+1, N, ssf+")")


if __name__ == '__main__':
	generate(0, 0, 0, 4, "")
