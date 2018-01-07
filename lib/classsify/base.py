from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from underthesea import word_sent
from lib.singleton import Singleton

class Base(metaclass=Singleton):
	def singleton_init(self):
		print("initialized base")

	def classify(self, advertisement):
		print("classify")
		return self.classifier.classify(advertisement)

	def accuracy(self, advertisement):
		print("accuracy")
		return "{0}".format(self.classifier.accuracy(advertisement))