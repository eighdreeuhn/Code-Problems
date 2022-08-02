# Ego boosting 8kyu Codewars problems for staying sharp
import math
# from collections import Counter
#
# def is_opposite(s1,s2):
#     if s1.lower() == s2.lower():
#         for i in range(0, len(s1)):
#             if not ((s1[i].islower() and s2[i].isupper()) or (s1[i].isupper() and s2[i].islower())):
#                 return False
#         return True
#     return False
#
#
# print(is_opposite("aBcd","AbCD"))
#
#
# def alpha_pos(a):
#     return ord(a)
#
#
# print(alpha_pos('a'))


# def reverse_words(s):
#     return ' '.join([*reversed(s.split(' '))])
#
#
# print(reverse_words("hello world!"))
#
#
# def well(x):
#     count = Counter(x)
#     return 'I smell a series!' if count['good'] > 2 else 'Publish!' if count['good'] > 0 else 'Fail!'
#
#
# well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])


# def array(string):
#     return ' '.join(string.split(',')[1:-1])
#
#
# print(array('1,2,3,4,5'))


# def remove_exclamation_marks(s):
#     return ''.join([l for l in s if not l == '!'])
#
#
# print(remove_exclamation_marks("Hi! Hello!"))


# def find_function(func, arr):
#     print(type(func[2]).__name__)
#     funky = [*filter(lambda f: type(f).__name__ =='function', func)][0]
#     print(funky)
#     return list(map(funky, arr))
#
#
# print(find_function([5,'a',lambda a: a*4!=0,1,0],[0,1,2,3,4]))


# def two_highest(arg1):
#     l = list(sorted(list(set(arg1)), reverse=True))
#     return l[:2]
# #
# # print(two_highest([15, 20, 20, 17]))
#
#
# def multi_table(number):
#     return '/n'.join(([f"{str(n)} * {number} = {n*number}" for n in range(1, number + 1)]))
#
#
# print(multi_table(5))


# def two_sort(array):
#     array.sort()
#     return '***'.join([l for l in array[0]])
#
#
# print(two_sort(['Lets', 'all', 'go', 'on', 'holiday', 'somewhere', 'very', 'cold']))


# def maxlen(L1, L2):
#     smaller = min(L1, L2)
#     larger = max(L1, L2)
#     return smaller if larger >= 2* smaller else maxlen(smaller, larger - smaller)
#
#
# print(maxlen(5, 12))


# heavenly = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
# earthly = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# def how_old(birth_year, present_year):
#     year =
#     return year
#
#
# print(how_old("甲子", "乙丑"))


# elements = [1, 3, 2, 3, 0, 1, 3]
# curr = 0
#
# for ele in elements:
#     pass
#     if (ele == 0):
#         curr = ele
#         break
#     elif (ele % 2 == 0):
#         continue
#     print(ele)
# print(curr)


# def solution(n, b):
#     b_index_1 = -int(math.log(b, 2)) - 1
#     print(b_index_1, bin(b))
#     return [num for num in range(1, 2**n) if bin(num)[b_index_1] == '1']
#
#
# print(solution(4, 2))


# def gcd_lcm(x, y):
#     for n in range(x + 1, y):
#         print(n, x*y//n)
#         if (x*y)/n == (x*y)//n:
#             return n, (x * y) / n
#     return None
#
#
# gcd_lcm(6, 36)


# def knight_path(start, end):
#     path = [start]
#     distance = ((path[-1][0] - end[0]) ** 2 + (path[-1][1] - end[1]) ** 2) ** 0.5
#
#     def seek(pos, target):
#         pi = math.pi
#         angle_of_attack = math.atan2(target[1] - pos[1], target[0] - pos[0])
#         if 0 <= angle_of_attack < pi/4:
#             return pos[0] + 2, pos[1] + 1
#         elif pi/4 <= angle_of_attack < pi/2:
#             return pos[0] + 1, pos[0] + 2
#         elif pi/2 <= angle_of_attack < 3*pi/4:
#             return pos[0] - 1, pos[0] + 2
#         elif 3*pi/4 <= angle_of_attack < pi:
#             return pos[0] - 2, pos[0] + 1
#         elif pi <= angle_of_attack < 5*pi/4:
#             return pos[0] - 2, pos[0] - 1
#         else:
#             return pos[0] - 1, pos[0] - 2
#
#     while distance > 3:
#         path.append(seek(path[-1], end))
#         distance = ((path[-1][0] - end[0]) ** 2 + (path[-1][1] - end[1]) ** 2) ** 0.5
#
#
#     return path
#
#
# print(knight_path((0, 0), (111, 111)))


# def count_vegetables(string):
#
#     veggies = [
#         "cabbage",
#         "carrot",
#         "celery",
#         "cucumber",
#         "mushroom",
#         "onion",
#         "pepper",
#         "potato",
#         "tofu",
#         "turnip"
#     ]
#
#     solution = [
#         [0, 'cabbage'],
#         [0, 'carrot'],
#         [0, 'celery'],
#         [0, 'cucumber'],
#         [0, 'mushroom'],
#         [0, 'onion'],
#         [0, 'pepper'],
#         [0, 'potato'],
#         [0, 'tofu'],
#         [0, 'turnip']
#     ]
#
#     veg_list = string.split(' ')
#
#     for item in veg_list:
#         if item in veggies:
#             solution[veggies.index(item)][0] += 1
#
#     return list(map(lambda i: (i[0], i[1]), filter(lambda v: v[0] != 0, solution)))
#
#
#
#
# print(count_vegetables('potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'))
#
#
# def is_anagram(s, t):
#     return [*reversed([*s])] == [*t]
#
#
# print(is_anagram('rac', 'car'))


# s = 'Python RockS!'
#
# print(s.swapcase().rpartition('S')[2])


# def split_and_merge(string_, separator):
#     words = string_.split(' ')
#     for i, word in enumerate(words):
#         words[i] = separator.join([letters for letters in word])
#     return ' '.join(words)
#

# print(split_and_merge("My name is John"," "))


def double(l):
    l *= 2
    return l


l = [1, 2, 3, 4, 5]
l = double(l)
print(l)
