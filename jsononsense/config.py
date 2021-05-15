import configparser as cp
import os

config = cp.ConfigParser()
path = os.path.abspath(os.path.dirname(__file__)) + '/config.ini'
config.read(path)