import random as rand
import requests
import string


class IteratorCollection:
    """
        Wraps separate iterators into a single iterator
        Allows randomly picking values between iterators
    """

    def __init__(self, iterators: list):
        super(IteratorCollection, self).__init__()
        self.iterators = [iterator for iterator in iterators]

    def __iter__(self):
        return self

    def __next__(self):
        iterator = self.iterators[rand.randint(0, len(self.iterators) - 1)]
        return next(iterator)


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


class NoneIterator:
    def __iter__(self):
        return self

    def __next__(self):
        return None


class APIIterator:
    def __init__(self, url: str, get_keys: bool, get_vals: bool):
        self.get_keys = get_keys
        self.get_vals = get_vals

        data = requests.get(url).json()
        self.item_list = []
        self._get_items(data)
        rand.shuffle(self.item_list)
        self.item_iterator = iter(self.item_list)

    def _get_items(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if self.get_keys:
                    self.item_list.append(key)
                self._get_items(value)

        elif isinstance(obj, list):
            for item in obj:
                self._get_items(item)

        elif self.get_vals:
            self.item_list.append(obj)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.item_iterator)


class APIIteratorCollection(IteratorCollection):
    def __init__(self, urls: list, get_keys: bool = True, get_vals: bool = True):
        api_iterators = []
        for url in urls:
            api_iterators.append(APIIterator(url, get_keys, get_vals))

        super(APIIteratorCollection, self).__init__(iterators=api_iterators)


# class WeightedIteratorCollection:
#     """
#         Allows weighting of particular iterators,
#         defining how likely they are to appear.
#     """
#     def __init__(self, iterators: dict):
#         """
#
#         :param iterators:
#         """
#


def get_iterators(types):
    iterator_map = {
        'str': RandStringIterator(),
        'int': RandIntIterator(),
        'float': RandFloatIterator(),
        'None': NoneIterator()
    }

    if not isinstance(types, list):
        types = [types]

    iterators = []
    for type_ in types:
        if type_ in iterator_map:
            iterators.append(iterator_map[type_])
        else:
            raise Exception(f'Iteration not defined for type: {str(type_)}')
    return IteratorCollection(iterators)
