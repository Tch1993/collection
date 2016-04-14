import re, collection
class elong(collection.collection):
	def __init__(self, queue):
		super(elong, self).__init__(queue, self.__class__.__name__);

	def rule(self):
		filename = '';
		pat = re.compile(r'<div id="txt2" class="pertxt_num" data-rate="([0-9\.,]*)"></div>.*<p class="t12 tc">共([0-9\.,]*)人评价</p>',re.S);
		self.start(pat);
		return self.data;