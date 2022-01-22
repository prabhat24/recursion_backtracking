
def valid(board, r, c, R, C):
	# col check
	i = r
	while i>=0:
		if board[i][c]:
			return False
		i -=1
	# left diag check
	i = r
	j = c
	while i>=0 and j>=0:
		if board[i][j]:
			return False
		i -=1
		j-=1 

	# right diagonal
	i = r
	j = c
	while i>=0 and j>=0 and i<R and j<C:
		if board[i][j]:
			return False
		i-=1
		j+=1
	return True

def solve(board, r, R, C):
	if r == R:
		print("_______________")
		for i in range(0, R):
			for j in range(0, C):
				print(board[i][j], end=" ")
			print()
	else:
		for c in range(0, C):
			if valid(board, r, c, R, C):
				board[r][c] = 1
				solve(board, r+1, R, C)
				board[r][c] = 0

def solve_tf(board, r, R, C):
	if r == R:
		return True
	else:
		for c in range(0, C):
			if valid(board, r, c, R, C):
				board[r][c] = 1
				can_solve = solve_tf(board, r+1, R, C)
				if can_solve:
					return True
				else:
					board[r][c] = 0
		return False

if __name__ == '__main__':
	N = 5
	board = [[0] * N for k in range(0, N)]
	a = solve_tf(board, 0, len(board), len(board[0]))
	print(a)