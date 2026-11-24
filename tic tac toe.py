board = [
    ["X", "X", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"],
]

def print_board(b):
    for row in b:
        print(" | ".join(row))
    print("-" * 9)

print_board(board)

for i in range(len(board)):
  row = board[i]
  if row[0] == row[1] == row[2] and row[0] != "":
    print(f"Row {i} is a winning row for {row[0]}!")
    break
else:
    print("No winning row found")