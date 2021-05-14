import os
import random as rand
import configparser as cp
from copy import copy
from data_source import DataSource

config = cp.ConfigParser()
config.read(os.path.dirname(__file__) + '/config.ini')
config_file = config['JSONONSENSE']


class JSONonsense:
    MIN_KEY_PER_OBJECT = int(config_file['MIN_KEY_PER_OBJECT'])
    MAX_KEY_PER_OBJECT = int(config_file['MAX_KEY_PER_OBJECT'])
    MAX_DEPTH = int(config_file['MAX_DEPTH'])
    NEST_OBJ_CHANCE = float(config_file['NEST_OBJ_CHANCE'])

    def __init__(self, data_source: DataSource = DataSource(), refresh=False, config=None):
        if config:
            for key, value in config:
                if hasattr(JSONonsense, key):
                    setattr(JSONonsense, key, value)

        if JSONonsense.MAX_DEPTH > 20:
            JSONonsense.MAX_DEPTH = 20

        self.data_source = data_source
        self.refresh = refresh
        self.all_keys = data_source.get_keys()
        self.all_vals = data_source.get_vals()

        self.key_iter = copy(self.all_keys)
        self.val_iter = copy(self.all_vals)
        self.key_amount = 0
        self.val_amount = 0

    def _refresh_keys(self):
        if self.refresh:
            return self.data_source.get_keys()
        return copy(self.all_keys)

    def _refresh_vals(self):
        if self.refresh:
            return self.data_source.get_vals()
        return copy(self.all_vals)

    def _get_key(self):
        try:
            key = next(self.key_iter)
        except StopIteration:
            self.key_iter = self._refresh_keys()
            key = next(self.key_iter)
        self.key_amount += 1
        return key

    def _get_val(self):
        try:
            val = next(self.val_iter)
        except StopIteration:
            self.val_iter = self._refresh_vals()
            val = next(self.val_iter)
        self.val_amount += 1
        return val

    def populate(self, obj=None, depth=-1):
        depth += 1

        if not obj:
            obj = {}

        if depth == JSONonsense.MAX_DEPTH:
            return

        for _ in range(rand.randint(JSONonsense.MIN_KEY_PER_OBJECT, JSONonsense.MAX_KEY_PER_OBJECT)):
            key = self._get_key()

            while key in obj:
                key = self._get_key()

            # Roll the dice, could be a value, could be another object!
            if rand.random() < JSONonsense.NEST_OBJ_CHANCE:
                obj[key] = self.populate(depth=depth)
            else:
                val = self._get_val()
                obj[key] = val
        return obj

    def create_jsonsense(self):
        return self.populate({})
