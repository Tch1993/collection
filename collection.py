import urllib.request, http.cookiejar, os, gzip, io, time, queue, config, function
class collection:
	data = [];	#所有执行的结果
	fail = [];	#失败的结果
	cookie = {};	#手动设置cookie
	QUEUE_Q = queue.Queue();
	_SLEEP_TIME = 0;
	def __init__(self, queue_q, cls_name):
		conf = config.config();
		self.fail = [];
		self.data = [];
		self.QUEUE_Q = queue_q;
		self._SLEEP_TIME = float(conf.get(cls_name, 'time'));
		self.cookie = {};

	def start(self, pat, file_cookie = '', func = '', s_gzip = ''):
		if isinstance(file_cookie, dict):
			self.cookie = file_cookie;
		elif os.path.exists(file_cookie):
			cj = http.cookiejar.LWPCookieJar();
			cj.load(file_cookie, True, True)
			cookie_support = urllib.request.HTTPCookieProcessor(cj);
			opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler);
			urllib.request.install_opener(opener);
		while not self.QUEUE_Q.empty():
			if func != '':
				func();
			url = self.QUEUE_Q.get();
			# print(self, url);
			content = self.getHtml(url, s_gzip);
			m = pat.findall(content);
			# f = open('data5.txt', 'w+', encoding = 'utf-8');
			# f.write(content);
			# f.close();
			# print(m);exit();
			if(m):
				self.data.append([m, url]); 
			else:
				self.fail.append(url);
			time.sleep(self._SLEEP_TIME);
		return self.data, self.fail;

	def getHtml(self, url, s_gzip = ''):
		url = function.is_chinese(url);
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
			"Accept-Encoding": "gzip",
			'Referer' : url};
		if len(self.cookie) > 0:
			headers.update(self.cookie);
		request = urllib.request.Request(url = url, 
			headers = headers
		);
		try:
			resqonse = urllib.request.urlopen(request);
			content = resqonse.read();
			if s_gzip == '':
				bi = io.BytesIO(content);
				gf = gzip.GzipFile(fileobj=bi, mode="rb");
				html = gf.read().decode("utf-8", "ignore"); 
			else:
				html = content.decode("utf-8", "ignore");
		except Exception as e:
			print(e);
			# exit();
		return html;