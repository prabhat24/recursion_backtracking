def decode_string(string):
	if string[0] == 0:
		return (False, "")
	if int(string) in range(1, 26 + 1):
		return (True, chr(ord('a') -1 + int(string)))
	else:
		return (False, "")

def print_encodings(string, dssf):
	if len(string) == 0:
		print(dssf)
	else:
		decoded, ch = decode_string(string[0])
		if decoded:
			print_encodings(string[1:], dssf + ch)
		
		if len(string) >= 2:
			decoded ,ch = decode_string(string[:2])
			if decoded:
				print_encodings(string[2:], dssf + ch)



if __name__ == "__main__":
	print_encodings("123", "")