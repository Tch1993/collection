import queue, mythread, function;
class affair:
	@classmethod
	def queue(cls, url, filename):
		QUEUE_Q = queue.Queue();
		queue_q, arr_repeat = function.data_repeat(url);	#用于过滤重复数据
		if arr_repeat:
			function.file_wrtie(filename, arr_repeat);	#将重复数据记录下来

		for i in queue_q:
			QUEUE_Q.put(i);
		cls.QUEUE_Q = QUEUE_Q;
		return cls;

	@classmethod
	def thread(self_cls, worker, filename, cls, func = ''):
		cls = cls(self_cls.QUEUE_Q);
		if func == '':
			func = cls.rule;
		thread = mythread.Myqueue();
		thread.start(worker, func);
		if cls.fail:									#采集不到的链接
			function.file_wrtie(filename, cls.fail);	#将采集不到的链接记录下来
		return cls.data;
