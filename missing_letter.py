# Thinking maybe character codes?


def find_missing_letter(chars):
    for i in range(0, len(chars) - 1):
        if not ord(chars[i + 1]) == ord(chars[i]) + 1:
            return chr(ord(chars[i]) + 1)


sequence1 = ['O','Q','R','S']

print(find_missing_letter(sequence1))