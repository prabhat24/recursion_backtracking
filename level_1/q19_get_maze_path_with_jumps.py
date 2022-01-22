
def get_maze_paths(R, C, msf, lsf, cur_r, cur_c):
	if cur_r == R - 1 and cur_c == C - 1:
		lsf.append(msf)
	else:
		avac = (C - cur_c) - 1
		avar = (R - cur_r) - 1
		avad = min(avar, avac)
		for i in range(1, avac+1):
			get_maze_paths(R, C, msf + "h" + str(i), lsf, cur_r, cur_c + i)
		for i in range(1, avar+1):
			get_maze_paths(R, C, msf + "v" + str(i), lsf, cur_r + i, cur_c)
		for i in range(1, avad+1):
			get_maze_paths(R, C, msf + "d" + str(i), lsf, cur_r + i, cur_c + i)

def get_maze_paths_m2(R, C, cur_r, cur_c):
	if cur_r == R - 1 and cur_c == C - 1:
		return [""]
	else:
		all_paths = []
		for i in range(1, C-cur_c):
			h_paths = get_maze_paths_m2(R, C, cur_r, cur_c + i)
			for k in range(len(h_paths)):
				h_paths[k] = "h" + str(i) + h_paths[k]
				all_paths.append(h_paths[k])

		for i in range(1, R-cur_r):
			v_path = get_maze_paths_m2(R, C, cur_r + i, cur_c)
			for k in range(len(v_path)):
				v_path[k] = "v" + str(i) + v_path[k]
				all_paths.append(v_path[k])

		for i in range(1, min((C - cur_c), (R - cur_r))):
			d_paths = get_maze_paths_m2(R, C, cur_r + i, cur_c + i)
			for k in range(len(d_paths)):
				d_paths[k] = "d" + str(i) + d_paths[k]
				all_paths.append(d_paths[k])
		return all_paths

if __name__ == '__main__':
	lsf = []
	get_maze_paths(2, 2, "", lsf, 0, 0)
	print(lsf)
	print(get_maze_paths_m2(2,2, 0,0))