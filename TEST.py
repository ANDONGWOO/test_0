
matrix = [[0] * 6 for _ in range(6)]


top_row = [0] * 4
bottom_row = [0] * 4
matrix.insert(0, top_row)
matrix.append(bottom_row)

#테두리 가로6 세로6으로 만들다
for row in matrix:
    row.insert(0, 0)# top_row+1
    row.append(0)# bottom_row+1
for row in matrix:
    #상단
    matrix[0][0]=2
    matrix[0][1]=3
    matrix[0][3]=3
    #하단
    matrix[7][0]=2
    matrix[7][1]=1
    matrix[7][2]=3
    matrix[7][4]=2
    matrix[7][5]=3
    #왼쪽
    matrix[1][0]=2
    matrix[2][0]=3
    matrix[3][0]=1
    matrix[4][0]=3
    matrix[5][0]=4
    matrix[6][0]=2
    #오른쪽
    matrix[1][7]=1
    matrix[2][7]=2
    matrix[3][7]=6
    matrix[4][7]=2
    matrix[5][7]=2
    matrix[6][7]=3

numbers = [1, 2, 3, 4, 5, 6]
def is_valid(row, col, number):
    # 가로 방향 중복 체크
    if number in matrix[row][1:6]:
        return False

    # 세로 방향 중복 체크
    for i in range(1, 7):
        if matrix[i][col] == number:
            return False

    return True

def solve(row, col):
    if row == 7:#1시작 
        return True

    next_row = row
    next_col = col + 1
    if next_col == 7:
        next_row += 1
        next_col = 1

    if matrix[row][col] != 0:
        return solve(next_row, next_col)

    for number in numbers:
        if is_valid(row, col, number):
            matrix[row][col] = number
            if solve(next_row, next_col):
                return True
            matrix[row][col] = 0

    return False

solve(1, 1)#시작위치(테두리제외)

# 결과 출력
for row in matrix:
    print(row)




