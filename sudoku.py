from example import q1

def print_sudoku(l):
    length = len(l)
    length=length*2 +1
    print('--'*length)
    for row in l:
        for val in row:
            t=val if val!=0 else ' '
            print(f'| {t} ', end='', flush=True)
        print('|')
        print('--'*length)


def possible(i,j,n,arr):
    #if n is already in same row or column
    for p in range (0,9):
        if arr[p][j] == n or arr[i][p] == n:
            return False

    #getting block position

    i0=(i//3)*3
    j0=(j//3)*3

    for p in range(3):
        for q in range(3):
            if arr[i0+p][j0+q] == n:
                return False
    return True

def solve(grid):
    for i in range (9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if possible(i,j,n,grid):
                        grid[i][j] = n
                        solve(grid)
                        grid[i][j]=0
                return
    print_sudoku(grid)          

if __name__=='__main__':
    print_sudoku(q1)
    solve(q1)
