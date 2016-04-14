import http.cookiejar, urllib.request, time, random, os, gzip, io, re
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
login_url = 'http://weixin.sogou.com/';
listcookie = [];
for i in range(10):
	urllib.request.urlopen(login_url)
	listcookie.append(cj)
	time.sleep(2);

# cj1 = http.cookiejar.LWPCookieJar()
for i in range(1000):
	k = random.randint(0, 9)
	# cj1.load(listcookie[k], True, True)
	cookie_support = urllib.request.HTTPCookieProcessor(listcookie[k]);
	opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler);
	urllib.request.install_opener(opener);
	url = 'http://weixin.sogou.com/weixin?query=%E6%B4%B2%E9%99%85%E9%85%92%E5%BA%97&fr=sgsearch&sut=5034&type=2&ie=utf8&sst0=1446185232711&sourceid=inttime_month&interation=&interV=kKIOkrELjboJmLkElbYTkKIKmbELjbkRmLkElbk%3D_1893302304&tsn=3';
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
		"Accept-Encoding": "gzip",
		'Referer' : url};
	request = urllib.request.Request(url = url, 
		headers = headers
	);
	resqonse = urllib.request.urlopen(request);
	content = resqonse.read();
	bi = io.BytesIO(content);
	gf = gzip.GzipFile(fileobj=bi, mode="rb");
	html = gf.read().decode("utf-8", "ignore"); 
	r = re.compile(r'您的访问过于频繁，为确认本次访问为正常用户行为');
	if r.search(html):
		print(i);
		print('出现验证码了！');
		break;
		time.sleep(3);
