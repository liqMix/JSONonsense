from jsononsense.data_sources import APISource
from jsononsense import JSONonsense
from pprint import pprint

KEY_URL = "https://jsonplaceholder.typicode.com/comments"
api_data = APISource(key_source=KEY_URL)
pprint(JSONonsense(data_source=api_data).create())

