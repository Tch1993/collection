import urllib.request, urllib.parse, http.cookiejar, re, json, hashlib, base64, rsa, binascii, time, os


class weiboLogin:
	filename = './Cookie/weibo_cookie.txt'
	login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'

	cj = http.cookiejar.LWPCookieJar()
	cookie_support = urllib.request.HTTPCookieProcessor(cj)
	opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)

	postdata = {
		'entry':'weibo',
		'gateway':'1',
		'from':'',
		'savestate':'7',
		'useticket':'1',
		# 'pagerefer':'http://weibo.com/redwallgardenhotel',
		'pagerefer':'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
		# 'pcid':'gz-a037c91c238040cae0f209411ebd1b95bc93',
		# 'door':'kfxng',
		'vsnf':'1',
		'su':'MTU4Njg3NTg3MTg=',
		'service':'miniblog',
		'servertime':'1450336987',
		'nonce':'9ADYB0',
		'pwencode':'rsa2',
		# 'pwencode':'wsse',
		'rsakv':'rsakv',
		'sp':'df2d5a70a3d52f5f64221aceda9a0ff820b50fa5e141d22111418b0982a0a7de2364756df80808d3837ca49c33028b1cfb23d85f7024ef0123ecd16a7edb969c3413e7cb588a625c7742b9a1028559715239aee28132ee213d5d66e729250ed6df849d9af3f76c7e24ef610ce36fb501c3216d786d96bffb0c38676c2a08e0be',
		'sr':'1920*1080',
		'encoding':'UTF-8',
		# 'cdult':'2',
		# 'domain':'weibo.com',
		# 'prelt':'69',
		'prelt':'64',
		# 'returntype':'TEXT',
		'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
		'returntype':'META'
	}

	def get_pwencode(self, username, plt):
		codeurl = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=%s' % (username, plt)
		data = urllib.request.urlopen(codeurl).read().decode('gbk');
		pat = re.compile(r'\((.*)\)');
		try:
			data = json.loads(pat.search(data).group(1));
			servertime = str(data['servertime'])
			nonce = data['nonce']
			pubkey = str(data['pubkey'])
			rsakv = str(data['rsakv'])
			exectime = int(data['exectime'])
			return servertime, nonce, pubkey, rsakv, exectime
		except:
			print('获取验证码出错！');
			return None
	def get_username(self, username):
		username_ = urllib.request.quote(username);
		username = base64.b64encode(username_.encode())
		return username.decode()

	def get_password(self, pwd, servertime, nonce, pubkey):
		# pwd1 = hashlib.sha1(pwd).hexdigest().encode();
		# pwd2 = hashlib.sha1(pwd1).hexdigest();
		# pwd3_ = pwd2 + servertime + nonce;
		# pwd3 = hashlib.sha1(pwd3_.encode()).hexdigest();
		# return pwd3
		n = int(pubkey, 16)
		e = int('10001', 16) #Convert the 16 string e to number 
		message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd.decode())
		key = rsa.PublicKey(n, e) 
		sp = rsa.encrypt(message.encode(), key) 
		return binascii.b2a_hex(sp).decode()
	def __mtime(self):
		return int(time.time() * 1000)
	def login(self, user, pwd):
		username = self.get_username(user);
		try:
			plt = self.__mtime();
			servertime, nonce, pubkey, rsakv, exectime = self.get_pwencode(username, plt);
			self.postdata['servertime'] = servertime;
			self.postdata['nonce'] = nonce;
			self.postdata['rsakv'] = rsakv;
		except:
			print('获取不到code');
			return 0;

		password = self.get_password(pwd.encode(), servertime, nonce, pubkey);
		# print(password);return 0;
		self.postdata['su'] = username;
		self.postdata['sp'] = password;
		endPre = self.__mtime();
		self.postdata['prelt'] = endPre - plt - exectime;
		self.postdata = urllib.parse.urlencode(self.postdata).encode('utf8');
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'};
		
		# 'cookie' : 'SINAGLOBAL=3040419854223.728.1448931835172; pf_feednav_bub_all_3898433904=1; SUHB=05i7URdqI2Kigy; un=13077915580; pf_feednav_bub_hot_1810647553=1; myuid=1810647553; SUB=_2AkMhL1eHdcPhrAJZmfgTyGznaY5Jywv0vtH4MUvZHyMdf3d_7DxnqiRqtUF8Obag2UPvCBxpudtHKN_DL5zu4lCj8Bls; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5SOhLQx-_X2dv7-TuqwJWE5JpVho20ehMN1K2fSKn7TJSV; _s_tentry=www.ttlsa.com; UOR=,,www.ttlsa.com; YF-V5-G0=69afb7c26160eb8b724e8855d7b705c6; YF-Page-G0=82a2c733169b8fbd551fc09977b0f608; Apache=7149741293396.801.1450684038115; ULV=1450684038130:5:5:1:7149741293396.801.1450684038115:1450323937241'};
		req = urllib.request.Request(
			url = self.login_url,
			data = self.postdata,
			headers = headers
			);
		result = urllib.request.urlopen(req);
		test = result.read().decode('gb2312');
		p = re.compile('location\.replace\(\'(.*?)\'\)')
		# code = re.compile('retcode=(\d+)\&')
		try:
		    login_url = p.search(test).group(1);
		    # code = code.search(login_url).group(1);
		    # if code != 0:
		    # 	print(urllib.parse.unquote(msg));
		    # 	return 0;
		    code = urllib.request.urlopen(login_url)
		    # print(login_url);return 0;
		    print("登录成功!")
		    self.cj.save(self.filename, ignore_discard=True, ignore_expires=True)
		    return 1;
		except:
		    print('Login error!')
		    return 0;
	# print(test.decode('gbk'));
	# print(json.loads(test.decode('utf8')));

	# file = urllib.request.urlopen('http://www.baidu.com');
	# for v in cj:
	# 	print(v.name, v.value);

	@staticmethod
	def user_queue():
		user = {
			'tch_ceshi@126.com' : 'ceshi123',
			'tch_ceshi1@126.com' : 'ceshi123',
			'tch_ceshi2@126.com' : 'ceshi123',
			'tch_ceshi3@126.com' : 'ceshi123',
			'tch_ceshi4@126.com' : 'ceshi123',
			'tch_ceshi5@126.com' : 'ceshi123',
			'tch_ceshi6@126.com' : 'ceshi123',
			'tch_ceshi7@126.com' : 'ceshi123',
			'tch_ceshi8@126.com' : 'ceshi123'
		};
		filename = './Invalid/' + time.strftime('%Y%m%d', time.localtime(time.time())) + '_weibo.txt';
		if os.path.exists(filename):
			f = open(filename);
			content = f.readline();
			while content:
				key = content.strip();
				if user.get(key):
					del user[key];
				content = f.readline();
			f.close();
		return user;


# def encryptPassword(self, pw, preObj):
# 	import rsa, binascii 
# 	if not isinstance(pw, types.StringType): 
# 		return None n = int(preObj['pubkey'], 16) #Convert the 16 string n to number 
# 		e = int('10001', 16) #Convert the 16 string e to number 
# 		message = str(preObj['servertime']) + '\t' + str(preObj['nonce']) + '\n' + str(pw) 
# 		key = rsa.PublicKey(n, e) 
# 		sp = rsa.encrypt(message, key) 
# 		return binascii.b2a_hex(sp)