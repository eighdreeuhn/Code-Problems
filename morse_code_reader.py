# This is still incomplete


def decode_morse(morse_code):
    words = list(map(lambda m: m.split(' '), morse_code.split('   ')))
    return words


print(decode_morse('.... . -.--   .--- ..- -.. .'))
