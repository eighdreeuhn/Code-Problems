# Comment time!

# foods = ['carrots', 'kale', 'beets']

# # for veg in enumerate(foods):
# #     print(f'I like {veg}')

# i = 1
# end = 50


# dict = {'name': 'Adrian', 'age': 43}

# cookie = 'Chocolate Chip'

# tuple = (dict, cookie)

# dict['name'] = 'Frank'

# print(tuple)

# def reverse3(nums):
#
#   return nums.reverse()
#
#
#
#
# nums = [1, 2, 3]
# print(reverse3(nums))


# def calculate_distance(r):
#   return r + (r * (2 / 3) ** 0.5)



#


# def interpret(code):
#     instructions_matrix = code.split('\n')
#     cursor_position = [0, 0]
#     stack = []
#     output = ""
#     direction = 'east'
#     for index, row in enumerate(instructions_matrix):
#         instructions_matrix[index] = list(row)
#     while not instructions_matrix[cursor_position[0]][cursor_position[1]] == '@':
#         curr_inst = instructions_matrix[cursor_position[0]][cursor_position[1]]
#         if curr_inst in range(0, 10):
#             stack.append(curr_inst)
#         elif curr_inst == '>':
#             cursor_position[1] = cursor_position[1] + 1 % len(instructions_matrix[cursor_position[0]])
#         elif curr_inst == '<':
#             direction = 'west'
#             cursor_position[1] = cursor_position[1] - 1 % len(instructions_matrix[cursor_position[0]])
#         elif curr_inst == '^':
#             direction = 'north'
#             cursor_position[0] = cursor_position[0] + 1 % len(instructions_matrix)\
#                 if instructions_matrix[cursor_position[0 + 1]]\
#                 else 0
#         elif curr_inst == 'v':
#             direction = 'south'
#             cursor_position[0] = cursor_position[0] - 1 % len(instructions_matrix)\
#                 if instructions_matrix[cursor_position[0 - 1]]\
#                 else 0
#         elif
#
#     return instructions_matrix
#
#
# instructions = '>987v>.v\nv456<  :\n>321 ^ _@'
#
# print(interpret(instructions))


# def sum_dig_pow(a, b):
#     solution = []
#     for index, num in enumerate(range(a, b + 1)):
#         sum = 0
#         digits = [int(d) for d in str(num)]
#         for place, digit in enumerate(digits):
#             sum += digit ** (place + 1)
#         if sum == num:
#             solution.append(num)
#     return solution


# print(sum_dig_pow(1, 10))


# def next_bigger(n):
#     s = str(n)
#
#     return
#
#
# print(next_bigger(123))





# def makesquare(sticks):
#     side = sum(sticks) / 4
#     sides = 4
#     num_matches = len(sticks)
#     while side in sticks:
#         sticks.pop(sticks.index(side))
#         sides -= 1
#     while sides > 0:
#         if sum(sticks) == side:
#             return True
#     if sides == 0 and sticks == []
#         return True
#     return False
#
#
# matchsticks = [1,1,2,2,2]
#
# print(makesquare(matchsticks))






def count_nines(n):
    counter = 0
    for num in range(1, n + 1):
        print(num)
        counter += str(num).count('9')
    return counter


print(count_nines(17))