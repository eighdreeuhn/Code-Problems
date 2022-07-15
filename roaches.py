# def cockroaches(room):
#     hole_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     def scatter(row, column, direction):
#         hiding = False
#         while not hiding:
#             print(row, column, direction)
#             if direction == 'U':
#                 while room[row - 1][column] == ' ' and not hiding:
#                     if room[row][column - 1].isnumeric():
#                         hole_counter[int(room[row][column - 1])] += 1
#                         hiding = True
#                     elif room[row][column + 1].isnumeric():
#                         hole_counter[int(room[row][column + 1])] += 1
#                         hiding = True
#                     else:
#                         row -= 1
#                 if room[row - 1][column] == '-':
#                     if room[row - 1][column + 1].isnumeric() and room[row][column + 1] == '|':
#                         hole_counter[int(room[row - 1][column + 1])] += 1
#                         hiding = True
#                     elif room[row - 1][column - 1].isnumeric() and room[row][column - 1] == '|':
#                         hole_counter[int(room[row - 1][column - 1])] += 1
#                         hiding = True
#                     else:
#                         direction = 'L'
#                 elif not hiding:
#                     hole_counter[int(room[row - 1][column])] += 1
#                     hiding = True
#             elif direction == 'L':
#                 while room[row][column - 1] == ' ' and not hiding:
#                     if room[row - 1][column].isnumeric():
#                         hole_counter[int(room[row - 1][column])] += 1
#                         hiding = True
#                     elif room[row + 1][column].isnumeric():
#                         hole_counter[int(room[row + 1][column])] += 1
#                         hiding = True
#                     else:
#                         column -= 1
#                 if room[row][column - 1] == '|':
#                     if room[row - 1][column - 1].isnumeric() and room[row - 1][column] == '-':
#                         hole_counter[int(room[row - 1][column - 1])] += 1
#                         hiding = True
#                     elif room[row + 1][column - 1].isnumeric() and room[row + 1][column] == '-':
#                         hole_counter[int(room[row + 1][column - 1])] += 1
#                         hiding = True
#                     else:
#                         direction = 'D'
#                 elif not hiding:
#                     hole_counter[int(room[row][column - 1])] += 1
#                     hiding = True
#             elif direction == 'D':
#                 while room[row + 1][column] == ' ' and not hiding:
#                     if room[row][column - 1].isnumeric():
#                         print('Found a hole!', row, column, room[row][column - 1])
#                         hole_counter[int(room[row][column - 1])] += 1
#                         hiding = True
#                     elif room[row][column + 1].isnumeric():
#                         hole_counter[int(room[row][column + 1])] += 1
#                         hiding = True
#                     else:
#                         row += 1
#                 if room[row + 1][column] == '-':
#                     if room[row + 1][column + 1].isnumeric() and room[row][column + 1] == '|':
#                         hole_counter[int(room[row + 1][column + 1])] += 1
#                         hiding = True
#                     elif room[row + 1][column - 1].isnumeric() and room[row][column - 1] == '|':
#                         hole_counter[int(room[row - 1][column - 1])] += 1
#                         hiding = True
#                     else:
#                         direction = 'R'
#                 elif not hiding:
#                     hole_counter[int(room[row + 1][column])] += 1
#                     hiding = True
#             elif direction == 'R':
#                 while room[row][column + 1] == ' ' and not hiding:
#                     if room[row - 1][column].isnumeric():
#                         hole_counter[int(room[row - 1][column])] += 1
#                         hiding = True
#                     elif room[row + 1][column].isnumeric():
#                         hole_counter[int(room[row + 1][column])] += 1
#                         hiding = True
#                     else:
#                         column += 1
#                 if room[row][column + 1] == '|':
#                     if room[row - 1][column + 1].isnumeric() and room[row - 1][column] == '-':
#                         hole_counter[int(room[row - 1][column + 1])] += 1
#                         hiding = True
#                     elif room[row + 1][column + 1].isnumeric() and room[row + 1][column] == '-':
#                         hole_counter[int(room[row - 1][column - 1])] += 1
#                         hiding = True
#                     else:
#                         direction = 'U'
#                 elif not hiding:
#                     hole_counter[int(room[row][column + 1])] += 1
#                     hiding = True
#
#     for i, row in enumerate(room):
#         for j, column in enumerate(row):
#             if room[i][j].isalpha():
#                 scatter(i, j, room[i][j])
#     return hole_counter
#
#
# def cockroaches(room):
#     hole_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     right = len(room[0]) - 1
#     bottom = len(room) - 1
#
#     def find_hidey_hole_top(column):
#         print('Top', column)
#         while column > 1:
#             if room[0][column].isnumeric():
#                 hole_counter[int(room[0][column])] += 1
#                 return
#             column -= 1
#         if room[0][0].isnumeric():
#             hole_counter[int(room[0][0])] += 1
#             return
#         elif room[1][0].isnumeric():
#             hole_counter[int(room[1][0])] += 1
#             return
#         else:
#             find_hidey_hole_left(1)
#
#     def find_hidey_hole_bottom(column):
#         print('Bottom', column)
#         while column < right - 1:
#             if room[bottom][column].isnumeric():
#                 hole_counter[int(room[bottom][column])] += 1
#                 return
#             column += 1
#         if room[bottom][right].isnumeric():
#             hole_counter[int(room[bottom][right])] += 1
#             return
#         elif room[bottom - 1][right].isnumeric():
#             hole_counter[int(room[bottom - 1][right])] += 1
#             return
#         else:
#             find_hidey_hole_right(bottom - 1)
#
#     def find_hidey_hole_right(row):
#         print('Right', row)
#         while row > 1:
#             if room[row][right].isnumeric():
#                 hole_counter[int(room[row][right])] += 1
#                 return
#             row -= 1
#         if room[0][right].isnumeric():
#             hole_counter[int(room[0][right])] += 1
#             return
#         elif room[0][right - 1].isnumeric():
#             hole_counter[int(room[0][right - 1])] += 1
#             return
#         else:
#             find_hidey_hole_top(right - 1)
#
#     def find_hidey_hole_left(row):
#         print('Left', row)
#         while row < bottom - 1:
#             if room[row][0].isnumeric():
#                 hole_counter[int(room[row][0])] += 1
#                 return
#             row += 1
#         if room[bottom][0].isnumeric():
#             hole_counter[int(room[bottom][0])] += 1
#             return
#         elif room[bottom][1].isnumeric():
#             hole_counter[int(room[bottom][1])] += 1
#             return
#         else:
#             find_hidey_hole_bottom(1)
#
#     def scatter_up(row, column):
#         while row > 1:
#             row -= 1
#         find_hidey_hole_top(column)
#
#     def scatter_down(row, column):
#         while row < bottom:
#             row += 1
#         find_hidey_hole_bottom(column)
#
#     def scatter_left(row, column):
#         while column > 1:
#             column -= 1
#         if room[row][column - 1].isnumeric():
#             hole_counter[int(room[row][column - 1])] += 1
#             return
#         else:
#             find_hidey_hole_left(row)
#
#     def scatter_right(row, column):
#         while column < right - 1:
#             column += 1
#         if room[row][column + 1].isnumeric():
#             hole_counter[int(room[row][column + 1])] += 1
#             return
#         else:
#             find_hidey_hole_right(row)
#
#     def reverse_top(column):
#         while column < right - 1:
#             if room[0][column].isnumeric():
#                 hole_counter[int(room[0][column])] += 1
#                 return
#             column += 1
#         if room[0][right].isnumeric():
#             hole_counter[int(room[0][right])] += 1
#             return
#         elif room[1][right].isnumeric():
#             hole_counter[int(room[1][right])] += 1
#             return
#         else:
#             find_hidey_hole_top(right - 1)
#
#     def reverse_bottom(column):
#         while column > 1:
#             if room[bottom][column].isnumeric():
#                 hole_counter[int(room[bottom][column])] += 1
#                 return
#             column -= 1
#         if room[bottom][0].isnumeric():
#             hole_counter[int(room[bottom][0])] += 1
#             return
#         elif room[bottom - 1][0].isnumeric():
#             hole_counter[int(room[bottom - 1][0])] += 1
#             return
#         else:
#             find_hidey_hole_bottom(1)
#
#     def reverse_left(row):
#         while row > 1:
#             if room[row][0].isnumeric():
#                 hole_counter[int(room[row][0])] += 1
#                 return
#             row -= 1
#         if room[0][0].isnumeric():
#             hole_counter[int(room[0][0])] += 1
#             return
#         elif room[0][1].isnumeric():
#             hole_counter[int(room[0][1])] += 1
#             return
#         else:
#             find_hidey_hole_left(1)
#
#     def reverse_right(row):
#         while row < bottom - 1:
#             if room[row][right].isnumeric():
#                 hole_counter[int(room[row][right])] += 1
#                 return
#             row += 1
#         if room[bottom][right].isnumeric():
#             hole_counter[int(room[bottom][right])] += 1
#             return
#         elif room[bottom][right - 1].isnumeric():
#             hole_counter[int(room[bottom][right - 1])] += 1
#             return
#         else:
#             find_hidey_hole_right(right - 1)
#
#     for r in range(1, bottom):
#         for c in range(1, right):
#             print(r, c, hole_counter)
#             roach = room[r][c]
#             if roach.isalpha():
#                 if roach == 'U':
#                     if c == 1:
#                         reverse_left(r)
#                     else:
#                         scatter_up(r, c)
#                 elif roach == 'D':
#                     if c == right - 1:
#                         reverse_right(r)
#                     else:
#                         scatter_down(r, c)
#                 elif roach == 'L':
#                     if r == bottom - 1:
#                         reverse_bottom(c)
#                     else:
#                         scatter_left(r, c)
#                 elif roach == 'R':
#                     if r == 1:
#                         reverse_top(c)
#                     else:
#                         scatter_right(r, c)
#     return hole_counter
#
#
# room_test=[
#     "+----------------0---------------+",
#     "|                                |",
#     "|                                |",
#     "|          U        D            |",
#     "|     L                          |",
#     "|              R                 |",
#     "|           L                    |",
#     "|  U                             1",
#     "3        U    D                  |",
#     "|         L              R       |",
#     "|                                |",
#     "+----------------2---------------+"
# ]
#
#
# print(cockroaches(room_test))
