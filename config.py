import configparser, time
class config:
	config = configparser.ConfigParser();
	def __init__(self, url = 'Config\\config.ini'):
		self.url = open(url);
		self.config.readfp(self.url);

	def get(self, k, v):
		return self.config.get(k, v);

	def isset(self, cls, name):
		if hasattr(cls, name):
			return True;
		else:
			return False;
