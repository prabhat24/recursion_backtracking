def knight_tour(board, r, c, R, C, msf):

	if msf == (R*C):
		board[r][c] = msf
		print(board)
	else:
		board[r][c] = msf
		moves = [
			(-2, +1),
			(-1, +2),
			(+1, +2),
			(+2, +1),
			(+2, -1),
			(+1, -2),
			(-1, -2),
			(-2 ,-1),
		]
		for i, j in moves:
			if r + i >= 0 and c+j >=0  and  r + i < R and c + j < C and board[r + i][c + j]==0:
				knight_tour(board, r+i, c+j, R, C, msf + 1)
				board[r+i][c+j] = 0

if __name__ == '__main__':
	N = 5
	board = [[0] * N for i in range(0, N)]
	board[2][0] = 1
	knight_tour(board, 2, 0, N, N, 1)

