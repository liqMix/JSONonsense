from data_sources import DataSource
from config import config
import random as rand


class JSONonsense:
    CONFIG = config["JSONONSENSE"]
    MIN_KEY_PER_OBJECT = int(CONFIG['MIN_KEY_PER_OBJECT'])
    MAX_KEY_PER_OBJECT = int(CONFIG['MAX_KEY_PER_OBJECT'])
    MAX_DEPTH = int(CONFIG['MAX_DEPTH'])
    OBJ_CHANCE = float(CONFIG['OBJ_CHANCE'])

    def __init__(self, data_source: DataSource = DataSource(), config=None):
        if config:
            for key, value in config:
                if hasattr(JSONonsense, key):
                    setattr(JSONonsense, key, value)

        if JSONonsense.MAX_DEPTH > 20:
            JSONonsense.MAX_DEPTH = 20

        self.data_source = data_source
        self.keys = data_source.get_keys()
        self.vals = data_source.get_vals()

        self.key_amount = 0
        self.val_amount = 0

    def _get_key(self):
        try:
            key = next(self.keys)
            if not key:
                raise StopIteration
        except StopIteration:
            self.data_source.refresh_keys()
            key = next(self.keys)
        self.key_amount += 1
        return key

    def _get_val(self):
        try:
            val = next(self.vals)
            if not val:
                raise StopIteration
        except StopIteration:
            self.data_source.refresh_vals()
            val = next(self.vals)
        self.val_amount += 1
        return val

    def populate(self, depth=0):
        depth += 1
        if depth == JSONonsense.MAX_DEPTH + 1:
            return

        obj = {}
        for _ in range(rand.randint(JSONonsense.MIN_KEY_PER_OBJECT, JSONonsense.MAX_KEY_PER_OBJECT)):
            key = self._get_key()

            # Roll the dice, could be a value, could be another object!
            if rand.random() < JSONonsense.OBJ_CHANCE:
                obj[key] = self.populate(depth)
            else:
                val = self._get_val()
                obj[key] = val

        return obj

    def create(self):
        return self.populate()


if __name__ == "__main__":
    from pprint import pprint
    pprint(JSONonsense().create())
