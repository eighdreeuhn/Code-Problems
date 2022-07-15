# The classic! The only thing of note here is the use of modulus 15 to handle the case of
# a number being divisible by 5 and 3


def fizzbuzz(i, end):
    '''Produces a fizzbuzz display'''
    while i < end:
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
        i += 1
        

fizzbuzz(i, end)