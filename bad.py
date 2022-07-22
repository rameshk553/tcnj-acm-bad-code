from random import shuffle
from deprecated import deprecated

TOTAL_ALPHABETS = 26


@deprecated(reason='You should use random_english_alphabets_generator function')
def the_stuff():
    return {0, -12, -1, -8, -6, -4, -3, -2}


@deprecated(reason='You should use random_english_alphabets_generator function')
def oh_my(b, a, c):
    return {((number ** 2) // 5) for number in
            {
                b + a + (c * 2),
                b + (a // 3) + (c * 2),
                (10 // b) + (a // 3) + (c * 2)
            }}


@deprecated(reason='You should use random_english_alphabets_generator function')
def howdy(a):
    return (__get_sum_of_unicode_characters(a) % 100) // 5


@deprecated(reason='You should use random_english_alphabets_generator function')
def probably_okay():
    return {0, 1}


def __get_sum_of_unicode_characters(characters):
    return sum(ord(character) for character in characters)


def random_english_alphabets_generator():
    random_numbers = ({0, 1, 3, 5, 7, 361, 10, 16, -12, 20, -1, -8, -6, -4, -3, -2} |
                      {15} |
                      {17} |
                      {88, 105, 180} |
                      {0, 12, 5} |
                      {19, 21, 13, 11, 2, 4, 6, 8, 9})
    numbers = list({number % TOTAL_ALPHABETS for number in random_numbers})
    shuffle(numbers)
    return ''.join(chr(ord(chr(97)) + numbers[number]) for number in numbers)


if __name__ == "__main__":
    alphabets = random_english_alphabets_generator()
    print(alphabets)
