# This was a pretty good solution to this problem

def anagrams(word, words):

    def letter_count(str):
        letters = list(str)
        return reduce(lambda counter, letter:
                      {**counter, letter: counter[letter] + 1}
                      if letter in counter
                      else {**counter, letter: 1}, letters, {})

    return list(filter(lambda w: letter_count(w) == letter_count(word), words))


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))