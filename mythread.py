import threading
class Mythread(threading.Thread):
	def __init__(self, lock, func, args = None):
		super(Mythread, self).__init__();
		self.lock = lock;
		self.func = func;
		if args != None:
			self.args = args;

	def run(self):
		if hasattr(self, 'args'):
			self.func(self.args);
		else:
			self.func();
		if self.lock.acquire():
			self.lock.release();



class Myqueue:
	queue = [];
	threads = [];
	def __init__(self):
		self.queue = [];
		self.threads = [];

	def set(self, array):
		self.queue = array;

	def start(self, num = 0, func = None):
		status = 1;
		lock = threading.Lock();
		if not num:
			queue = self.queue;
			status = 2;
		else:
			queue = range(num);
		for args in queue:
			if status == 2:
				thread = Mythread(lock, func, args);
			else:
				thread = Mythread(lock, func);
			thread.start();
			self.threads.append(thread);

		for thread in self.threads:
			thread.join();