# This was an interesting problem... A little trickier than it seemed at first


def get_accuracy(perfect, hundreds, fifties, misses):
    accuracy = '{percentage: .2f}%'
    perfect_score = (perfect + hundreds + fifties + misses)*300
    hits = perfect*300 + hundreds*100 + fifties*50 + misses*0
    return None if perfect_score == 0 else accuracy.format(percentage=(hits/perfect_score*100))


test = (1819, 11, 0, 0)
test2 = (178, 114, 43, 48)
print(get_accuracy(178, 114, 43, 48))
