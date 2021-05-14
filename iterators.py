import random as rand
import string


class RandStringIterator:
    MAX_LENGTH = 10
    CHARACTER_SET = string.ascii_letters

    def __iter__(self):
        return self

    def __next__(self):
        return ''.join([rand.choice(RandStringIterator.CHARACTER_SET) for _ in range(RandStringIterator.MAX_LENGTH)])


class RandIntIterator:
    MIN_INT = 0
    MAX_INT = 9999

    def __iter__(self):
        return self

    def __next__(self):
        return rand.randint(RandIntIterator.MIN_INT, RandIntIterator.MAX_INT)


class RandFloatIterator:
    MIN_FRACTIONAL_LEN = 1
    MAX_FRACTIONAL_LEN = 4
    MIN_INTEGRAL = 0
    MAX_INTEGRAL = 100

    def __iter__(self):
        return self

    def __next__(self):
        float_ = rand.uniform(RandFloatIterator.MIN_INTEGRAL, RandFloatIterator.MAX_INTEGRAL)
        frac_len = rand.randint(RandFloatIterator.MIN_FRACTIONAL_LEN, RandFloatIterator.MAX_FRACTIONAL_LEN)
        return round(float_, frac_len)


class IteratorCollection:
    """
        Wraps separate iterators into a single iterator
        Allows randomly picking values between iterators
    """
    def __init__(self, iterators):
        super(IteratorCollection, self).__init__()
        self.iterators = [iterator for iterator in iterators]

    def __iter__(self):
        return self

    def __next__(self):
        iterator = self.iterators[rand.randint(0, len(self.iterators) - 1)]
        return next(iterator)


ITERATOR_MAP = {
    str: RandStringIterator(),
    int: RandIntIterator(),
    float: RandFloatIterator()
}


def get_iterators(types=None):
    if not types:
        types = [str, int, float]

    if not isinstance(types, list):
        types = [types]

    iterators = []
    for type_ in types:
        if type_ in ITERATOR_MAP:
            iterators.append(ITERATOR_MAP[type_])
        else:
            raise Exception(f'Iteration not defined for type: {str(type_)}')
    return IteratorCollection(iterators)
