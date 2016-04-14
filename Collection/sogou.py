import re, collection
class sogou(collection.collection):
	def __init__(self, queue):
		super(sogou, self).__init__(queue, self.__class__.__name__);
		