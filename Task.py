import mythread, queue, sys



class Mytask:
	Myqueue = mythread.Myqueue();
	_modules = dict();
	def __init__(self, task):
		self.Myqueue.set(task);

	def run(self):
		# print('%s.%s' % (__name__,'saa'));
		# global SHARE_Q;
		# threads = [];
		# while not SHARE_Q.empty():
		# 	func = SHARE_Q.get();
		# 	thread = mythread.Mythread(self.func, func);
		# 	thread.start();
		# 	threads.append(thread);
		self.Myqueue.start(0, self.func);

	def func(self, func):
		# exec('import Affair.' + func + ';Affair.' + func + '.' + func + '.run()');
		obj = self._modules.get(func);
		if obj == None:
			modulePath = 'Affair.'+ func;
			__import__(modulePath);
			eMod = sys.modules[modulePath];
			obj = getattr(eMod, func);
			self._modules[func] = obj;
		obj.run();

	# def MCI_weibo_url(self):
	# 	import weibo;
	# 	MCI_QUEUE_Q = queue.Queue();

	# 	f = open("./url3.txt" , "r");             # 返回一个文件对象  
	# 	line = f.readline();             # 调用文件的 readline()方法  
	# 	while line:  
	# 		MCI_QUEUE_Q.put(line.strip());
	# 		line = f.readline();
	# 	f.close();
	# 	mci_weibo = weibo.weibo(MCI_QUEUE_Q);
	# 	data = mci_weibo.read_db();
	# 	print(data);

	# def MBI_weibo_url(self):
	# 	global MBI_QUEUE_Q;
	# 	import weibo;
	# 	MBI_QUEUE_Q = queue.Queue();
	# 	f = open("./url1.txt" , "r");             # 返回一个文件对象  
	# 	line = f.readline();             # 调用文件的 readline()方法  
	# 	while line:  
	# 		MBI_QUEUE_Q.put(line.strip());
	# 		line = f.readline();
	# 	f.close();
	# 	mbi_weibo = weibo.weibo(MBI_QUEUE_Q);
	# 	data = mbi_weibo.read_db();
	# 	print(data);
