import os
import json 
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/..')

from underthesea import word_sent
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from lib.classsify.base import Base
from lib.utils import Utils

class CategoryRent(Base):
	JSON_FILE = Utils().get_full_path("data/categoty/rent.json")

	def __init__(self):
		print("initialized CategoryRent")
		with open(JSON_FILE) as data_file:
      data_train = json.load(data_file)
		 
		self.classifier = NaiveBayesClassifier(data_train)