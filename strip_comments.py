# Still need to tweak this problem a bit


def strip_comments(strng, markers):
    parsed_string = strng.split('\n')
    answer = ''
    for i, row in enumerate(parsed_string):
        min_index = []
        for marker in markers:
            if not row.find(marker) == -1:
                min_index.append(row.find(marker))
        print(min_index)
        min_index = min(min_index) if not min_index == [] else 0
        parsed_string[i] = row[:min_index - 1].rstrip() if not min_index == 0 else parsed_string[i]
        if not i == len(parsed_string):
            answer += parsed_string[i] + '\n'
        else:
            answer += parsed_string[i]
    return answer


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
