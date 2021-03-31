def game_rule(row_select, column_select):
    return_value = 0
    strikerow1 = row_select[1]
    strikerow2 = row_select[2]
    strikerow3 = row_select[3]
    strikecolumn1 = column_select[1]
    strikecolumn2 = column_select[2]
    strikecolumn3 = column_select[3]
    strikediagonal1 = [row_select[1][0], row_select[2][1], row_select[3][2]]
    strikediagonal2 = [row_select[1][2], row_select[2][1], row_select[3][2]]
    all_combinations = [strikerow1, strikerow2, strikerow3, strikecolumn1, strikecolumn2, strikecolumn3,
                        strikediagonal1, strikediagonal2]
    for i in all_combinations:
        if i == ["O", "O", "O"] or i == ["X", "X", "X"]:
            return_value = 1
    return return_value


def user_input():
    valid_value = ["1", "2", "3"]
    r_string = "wrong"
    c_string = "wrong"
    while (r_string.isdigit() is False) or (r_string in valid_value is False):
        r_string = input("Enter row")
        if r_string.isdigit() is False or (r_string in valid_value is False):
            print("Enter a valid value")
    while (c_string.isdigit() is False) or (c_string in valid_value is False):
        c_string = input("Enter column")
        if c_string.isdigit() is False or (c_string in valid_value is False):
            print("Enter a valid value")
    r = int(r_string)
    c = int(c_string)
    my_tup = (r, c - 1)
    return my_tup


def display(row1=[" ", " ", " "], row2=[" ", " ", " "], row3=[" ", " ", " "], count=0):
    dot_or_x = "0"
    if count % 2 == 0:
        dot_or_x = "O"
    else:
        dot_or_x = "X"
    print(f"\n{dot_or_x} is playing")
    print("   1  2   3")
    print(f"1{row1}")
    print(f"2{row2}")
    print(f"3{row3}")
    row_select = {1: row1, 2: row2, 3: row3}
    column_select = {1: [row1[0], row2[0], row3[0]], 2: [row1[1], row2[1], row3[1]], 3: [row1[2], row2[2], row3[2]]}
    if count == 9 and not game_rule(row_select, column_select) == 1:
        print("tie")
        quit()
    if game_rule(row_select, column_select) == 0:
        my_tup = (0, 0)
        while my_tup[0] not in (1, 2, 3) and my_tup[1] not in (1, 2, 3):
            my_tup = user_input()
            if my_tup[0] not in (1, 2, 3) and my_tup[1] not in (1, 2, 3):
                print("enter a valid value")
        row_select[my_tup[0]][my_tup[1]] = dot_or_x
        count += 1
        display(row1, row2, row3, count)
    if game_rule(row_select, column_select) == 1:
        if dot_or_x == "O":
            dot_or_x = "X"
        else:
            dot_or_x = "O"
        print("yay " + dot_or_x + " won")
        quit()


display()
# counter for who wins how many
