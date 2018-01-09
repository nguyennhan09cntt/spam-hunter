import os
import json
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/..')

from underthesea import word_sent
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from lib.classsify.base import Base
from lib.utils import Utils

JSON_FILE = Utils().get_full_path("data/categoty/rent.json")

class ClasssifyRent(Base):
  def __init__(self):
    print("initialized CategoryRent")
    with open(JSON_FILE) as fp:
      self.classifier = NaiveBayesClassifier(fp, format="json")

