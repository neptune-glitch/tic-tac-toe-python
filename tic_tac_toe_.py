# Tic Tac Toe - Final Fixed Version

def display(row1, row2, row3):
    print(" | ".join(row1))
    print("--------")
    print(" | ".join(row2))
    print("--------")
    print(" | ".join(row3))

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def position_user(UserRow, position):
    if UserRow == 'row1':
        if row1[position] == " ":
            row1[position] = "X"
        else:
            print("That spot is already taken!")
    elif UserRow == 'row2':
        if row2[position] == " ":
            row2[position] = "X"
        else:
            print("That spot is already taken!")
    elif UserRow == 'row3':
        if row3[position] == " ":
            row3[position] = "X"
        else:
            print("That spot is already taken!")
    else:
        print("Not valid row")
    display(row1, row2, row3)

def check_wins(row1, row2, row3):
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] != " ":
            print("Player wins!" if row[0] == "X" else "Computer wins!")
            return True

    for i in range(3):
        if row1[i] == row2[i] == row3[i] != " ":
            print("Player wins!" if row1[i] == "X" else "Computer wins!")
            return True

    if row1[0] == row2[1] == row3[2] != " ":
        print("Player wins!" if row1[0] == "X" else "Computer wins!")
        return True

    if row1[2] == row2[1] == row3[0] != " ":
        print("Player wins!" if row1[2] == "X" else "Computer wins!")
        return True

    return False

def computer_move():
    rows = [row1, row2, row3]

    for row in rows:
        if row[0] == row[1] != ' ' and row[2] == ' ':
            row[2] = '0'; return
        if row[1] == row[2] != ' ' and row[0] == ' ':
            row[0] = '0'; return
        if row[0] == row[2] != ' ' and row[1] == ' ':
            row[1] = '0'; return

    for i in range(3):
        if row1[i] == row2[i] != ' ' and row3[i] == ' ':
            row3[i] = '0'; return
        if row2[i] == row3[i] != ' ' and row1[i] == ' ':
            row1[i] = '0'; return
        if row1[i] == row3[i] != ' ' and row2[i] == ' ':
            row2[i] = '0'; return

    if row1[0] == row2[1] != ' ' and row3[2] == ' ':
        row3[2] = '0'; return
    if row2[1] == row3[2] != ' ' and row1[0] == ' ':
        row1[0] = '0'; return
    if row1[2] == row2[1] != ' ' and row3[0] == ' ':
        row3[0] = '0'; return
    if row2[1] == row3[0] != ' ' and row1[2] == ' ':
        row1[2] = '0'; return

    for row in rows:
        for i in range(3):
            if row[i] == ' ':
                row[i] = '0'
                return

display(row1, row2, row3)

while True:
    UserRow = input("Enter row (row1, row2, row3): ")
    position = int(input("Enter position (0, 1, or 2): "))
    position_user(UserRow, position)

    if check_wins(row1, row2, row3):
        break

    computer_move()
    display(row1, row2, row3)

    if check_wins(row1, row2, row3):
        break

    if ' ' not in row1 and ' ' not in row2 and ' ' not in row3:
        print("It's a draw!")
        break
