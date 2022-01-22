
def get_maze_paths(R, C, msf, cur_r, cur_c, lsf):
	if cur_c == C - 1 and cur_r == R - 1:
		lsf.append(msf)
	elif cur_c >= C or cur_r >= R:
		return
	else:
		# Horizontal
		get_maze_paths(R, C, "h" + msf, cur_r, cur_c+1, lsf)

		# Vertical
		get_maze_paths(R, C, "v" + msf, cur_r+1, cur_c, lsf)

def get_maze_paths_m2(R, C, cur_r, cur_c):
	if cur_c == C - 1 and cur_r == R - 1:
		return [""]
	elif cur_c >= C or cur_r >= R:
		return []
	else:
		# Horizontal
		h_paths = get_maze_paths_m2(R, C, cur_r, cur_c+1)
		for i in range(len(h_paths)):
			h_paths[i] = "h" + h_paths[i]
		# Vertical
		v_paths = get_maze_paths_m2(R, C, cur_r+1, cur_c)
		for i in range(len(v_paths)):
			v_paths[i] = "v" + v_paths[i]
		return h_paths + v_paths

if __name__ == '__main__':
	lsf = []
	get_maze_paths(3,3, "", 0, 0, lsf)
	print(lsf)
	print(get_maze_paths_m2(3,3, 0, 0))