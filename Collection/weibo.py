#coding=utf-8
# import urllib.request
# import re,urllib.request, http.cookiejar, os, chardet, sys, gzip, io, time, pymysql, queue, threading
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8');
# share_q = queue.Queue();
# _WORKER_THREAD_NUM = 3;
# _SLEEP_time = 5;
# class Mythraed(threading.Thread):
# 	def __init__(self, func):
# 		super(Mythraed, self).__init__();
# 		self.func = func

# 	def run(self):
# 		self.func();

import re, collection, weiboLogin, time, function
user_weibo_length = 0;	#执行个数
MAX_WEIBO_LENGTH = 100;	#每次从登入次数
user_queue = weiboLogin.weiboLogin.user_queue();
class weibo(collection.collection):
	def __init__(self, queue):
		super(weibo, self).__init__(queue, self.__class__.__name__);

	# def getValue(self):		#微博采集
	# 	global share_q, _WORKER_THREAD_NUM;

	# 	filename = 'F:\\python\\cookie.txt';
	# 	cj = http.cookiejar.LWPCookieJar();
	# 	if os.path.exists(filename):
	# 		cj.load(filename, True, True)
	# 		cookie_support = urllib.request.HTTPCookieProcessor(cj);
	# 		opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler);
	# 		urllib.request.install_opener(opener);

	# 	f = open("./url3.txt" , "r")             # 返回一个文件对象  
	# 	line = f.readline()             # 调用文件的 readline()方法  
	# 	while line:  
	# 		share_q.put(line.strip());
	# 		line = f.readline();
	# 	f.close();

		# get.read_db();
		# threads = [];
		# for i in range(_WORKER_THREAD_NUM):
		# 	thread = Mythraed(get.read_db);
		# 	thread.start();
		# 	threads.append(thread);

		# for thread in threads:
		# 	thread.join();

	def rule(self):
		# filename = './Cookie/weibo_cookie.txt';
		filename = {'cookie' : 'SINAGLOBAL=6618145541287.959.1458696813874; wb_feed_unfolded_3655689037=1; SUB=_2AkMhrw6-f8NhqwJRmP0Vz2Pjbo51zAzEiebDAHzsJxJjHkhG7T9lqCQ-knBL0ZGTBaBun_JXuzvc21t87w..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55z29P9D9WFEp5zsk3MUl_7hAgacriB-; YF-Page-G0=f994131fbcce91e683b080a4ad83c421; _s_tentry=-; Apache=6923986480105.668.1458897026846; ULV=1458897026861:3:3:3:6923986480105.668.1458897026846:1458730403187'};
		# elif user_weibo_length > MAX_WEIBO_LENGTH:
		# 	time.sleep(1);
		# print(user_queue);
		# cj = http.cookiejar.LWPCookieJar();
		# if os.path.exists(filename):
		# 	cj.load(filename, True, True)
		# 	cookie_support = urllib.request.HTTPCookieProcessor(cj);
		# 	opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler);
		# 	urllib.request.install_opener(opener);
		pat = re.compile(r'<strong class=\\"W_f\d+\\">(\d+)<\\/strong>');
		self.start(pat, filename);#self.login
		# conn = pymysql.connect(host = 'localhost', user = 'root', passwd = '', db = 'collection', port = 3306, charset = 'utf8');
		# cur = conn.cursor();
		# while not self.QUEUE_Q.empty():
		# 	url = self.QUEUE_Q.get();
		# 	content = self.getHtml(url);
		# 	m = pat.findall(content);
		# 	self.data.append([m, url]); 
		# 	# log = open('./data3.txt', 'w+', encoding = 'utf-8');
		# 	# log.write(content);
		# 	# log.close();
		# 	# return 0;
		# 	# m = pat.search(content);
		# 	# print(m.groups()) # 在 Python 3中使用  
		# 	# if m:
		# 	# 	cur.execute("insert into weibo(`data1`, `data2`, `data3`, `url`) values(" + m[0] + "," + m[1] + "," + m[2] + ",'" + url + "')");
		# 	# 	conn.commit();
		# 	# else:
		# 	# 	cur.execute("insert into weibo(`data1`, `data2`, `data3`, `url`) values('','', '','" + url + "')");
		# 	# 	conn.commit();
		# 	time.sleep(self._SLEEP_TIME);

		# cur.close();
		# conn.close();
		return self.data;

	@staticmethod
	def login(status = 0):
		global user_weibo_length, user_queue, MAX_WEIBO_LENGTH;
		user_weibo_length += 1;
		if user_weibo_length % MAX_WEIBO_LENGTH == 0 or status == 1:
			keys = list(user_queue.keys());
			if keys:
				user = keys[0];
				pwd = user_queue.pop(user);
				weibologin = weiboLogin.weiboLogin();
				weibologin.login(user, pwd);
				# print(user , pwd);
				function.file_wrtie('Invalid/' + time.strftime('%Y%m%d', time.localtime(time.time())) + '_weibo', [user], 1);
				# user_weibo_length = 1;
			else:
				print('账号已用完！');
# weibo.login(1);

	# def getHtml(self,url):
	# 	# page = urllib.request.urlopen(url);
	# 	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
	# 		"Accept-Encoding": "gzip",
	# 		'Referer' : url};
	# 		# 'cookie' : 'SINAGLOBAL=3040419854223.728.1448931835172; pf_feednav_bub_all_3898433904=1; SUHB=05i7URdqI2Kigy; un=13077915580; pf_feednav_bub_hot_1810647553=1; myuid=1810647553; SUB=_2AkMhL1eHdcPhrAJZmfgTyGznaY5Jywv0vtH4MUvZHyMdf3d_7DxnqiRqtUF8Obag2UPvCBxpudtHKN_DL5zu4lCj8Bls; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5SOhLQx-_X2dv7-TuqwJWE5JpVho20ehMN1K2fSKn7TJSV; _s_tentry=www.ttlsa.com; UOR=,,www.ttlsa.com; YF-V5-G0=69afb7c26160eb8b724e8855d7b705c6; YF-Page-G0=82a2c733169b8fbd551fc09977b0f608; Apache=7149741293396.801.1450684038115; ULV=1450684038130:5:5:1:7149741293396.801.1450684038115:1450323937241'};
	# 	# postData = {
	# 	# 	'query_push' : 1,
	# 	# 	# 'is_pc' : 1
	# 	# 	'source' : 209678993,
	# 	# 	'callback' : 'IM_14500855001030',
	# 	# 	'is_hot' : 1
	# 	# }
	# 	# postData = urllib.parse.urlencode(postData).encode('utf8');

	# 	request = urllib.request.Request(url = url, 
	# 		# postData, 
	# 		headers = headers
	# 	);
	# 	try:
	# 		resqonse = urllib.request.urlopen(request);
	# 		content = resqonse.read();
	# 		bi = io.BytesIO(content);
	# 		gf = gzip.GzipFile(fileobj=bi, mode="rb");
	# 		html = gf.read().decode("utf-8", "ignore"); #str(content)
	# 	except Exception as e:
	# 		print(e);
	# 		exit();
		
	# 	# print(html)
	# 	# local_type = sys.getfilesystemencoding();
	# 	# html_type = chardet.detect(content).get('encoding','utf-8');
	# 	# html = content.decode(html_type,'ignore').encode(local_type)
	# 	return html;
