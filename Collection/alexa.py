import re, collection
class alexa(collection.collection):
	def __init__(self, queue):
		super(alexa, self).__init__(queue, self.__class__.__name__);

	def rule(self):
		filename = './Cookie/alexa_cookie.txt';
		pat = re.compile(r'<li>≈([\d,]+)</li>',re.S);
		self.start(pat, '', '', 1);
		return self.data;
