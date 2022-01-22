def flood_fill(board, asf, r, c, R, C):
	if r == R -1 and c == C-1:
		board[r][c] = 2
		print(asf)
		print("______")
		for i in range(len(board)):
			for j in range(len(board[0])):
				print(board[i][j], end=" ")
			print()
	else:
		board[r][c] = 2
		moves = [(-1, 0, "T"), (0, -1, "L"), (1, 0, "D"), (0, 1, "R")]
		for mi, mj, m in moves:
			if r + mi >=0 and c+mj >= 0 and r + mi < R and c+mj < C and board[r + mi][c+mj] == 0:
				flood_fill(board, asf + m, r + mi, c+mj, R, C)
				board[r + mi][c+mj] = 0




if __name__ == "__main__":
	board =[[0, 0, 0, 1],[1, 0, 1, 0],[0, 0, 0, 1], [0, 0, 0, 0]]
	flood_fill(board, "", 0, 0, len(board), len(board[0]))