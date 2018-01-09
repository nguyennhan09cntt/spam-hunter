import os
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/..')

from lib.process_data import ProcessData
from lib.utils import Utils

JSON_FILE = Utils().get_full_path("data/plaintext/rent.json")
OUT_FILE = Utils().get_full_path("data/categoty/rent.json")
Utils().process_data_json(JSON_FILE, OUT_FILE)