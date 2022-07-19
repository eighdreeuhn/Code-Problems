# Ego boosting 8kyu Codewars porblems for staying sharp

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


# from collections import Counter
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



