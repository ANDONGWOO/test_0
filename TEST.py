
matrix = [[0] * 6 for _ in range(6)]


top_row = [1] * 6
bottom_row = [1] * 6
matrix.insert(0, top_row)
matrix.append(bottom_row)

for row in matrix:
    row.insert(0, 1)
    row.append(1)
for row in matrix:
    print(row)