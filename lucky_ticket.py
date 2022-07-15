# July Codewars problem - 2022


def luck_check(string):
    if string.isdigit():
        n = len(string) // 2
        sums = [0, 0]
        for i in range(0, n):
            sums[0] += int(string[i])
            sums[1] += int(string[- i - 1])
        if sums[0] == sums[1]:
            return True
        else: return False
    else:
        raise Exception('String is invalid')


print(luck_check('683179'))
