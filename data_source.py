from iterators import get_iterators


class DataSource:
    """
        Returns separate iterators for both keys and values.
    """

    @staticmethod
    def get_keys():
        return get_iterators(types=[str])

    @staticmethod
    def get_vals():
        return get_iterators()


class APISource(DataSource):
    def __init__(self, key_source, val_source=None):
        if not val_source:
            val_source = key_source

    def get_keys(self):
        pass

    def get_vals(self):
        pass
