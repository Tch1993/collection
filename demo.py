# import weiboLogin, collection, queue, http.cookiejar, urllib.request, re, urllib.parse;


# from selenium import webdriver
# driver = webdriver.PhantomJS();
# driver.quit()
import urllib.request  
# proxy_handler = urllib.request.ProxyHandler({'http':'122.114.92.149:808'})  
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()  
# proxy_auth_handler.add_password('realm', '122.114.92.149', 'user', 'password')  
# opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)  
# f = opener.open('http://www.baidu.com')   
# a = f.read() 
url = 'http://www.veryeast.cn/';
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
	'url' : 'http://www.veryeast.cn/'};
proxy_support = urllib.request.ProxyHandler({'http': '112.193.13.207:8888'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
req = urllib.request.Request(url = url, headers = headers);

a = urllib.request.urlopen(req).read()
print(a)
input('\n');
# filename = './weibo_cookie.txt';
# url = 'http://weibo.com/newcenturyhotelgroup?is_all=1';
# weibo = weiboLogin.weiboLogin();
# weibo.login('tch_ceshi2@126.com', 'ceshi123');
# cj = http.cookiejar.LWPCookieJar()
# cookie_support = urllib.request.HTTPCookieProcessor(cj)
# opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)

# all_url = 'http://s.weibo.com/ajax/jsonp/gettopsug?uid=3655689037&ref=PC_topsug&url=http://weibo.com/newcenturyhotelgroup?is_all=1&Mozilla=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.87 Safari/537.36 QQBrowser/9.2.5063.400&_cb=STK_14586119666486';
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'};

# # 'cookie' : 'SINAGLOBAL=3040419854223.728.1448931835172; pf_feednav_bub_all_3898433904=1; SUHB=05i7URdqI2Kigy; un=13077915580; pf_feednav_bub_hot_1810647553=1; myuid=1810647553; SUB=_2AkMhL1eHdcPhrAJZmfgTyGznaY5Jywv0vtH4MUvZHyMdf3d_7DxnqiRqtUF8Obag2UPvCBxpudtHKN_DL5zu4lCj8Bls; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5SOhLQx-_X2dv7-TuqwJWE5JpVho20ehMN1K2fSKn7TJSV; _s_tentry=www.ttlsa.com; UOR=,,www.ttlsa.com; YF-V5-G0=69afb7c26160eb8b724e8855d7b705c6; YF-Page-G0=82a2c733169b8fbd551fc09977b0f608; Apache=7149741293396.801.1450684038115; ULV=1450684038130:5:5:1:7149741293396.801.1450684038115:1450323937241'};
# # data = urllib.parse.urlencode({'is_all' : '1'}).encode('utf8');
# req = urllib.request.Request(
# 	url = url,
# 	# data = data,
# 	headers = headers
# 	);
# result = urllib.request.urlopen(req);
# driver = webdriver.PhantomJS();
# ss = driver.get('https://www.baidu.com');
# print(ss)
# try:
# 	data = driver.find_element_by_id('bottom_container').text
# 	print(data);
# except Exception as e:
# 	print(e);
# finally:
# 	driver.quit()
# data = driver.find_element_by_id('sina').text
# print(result.headers);
# print(result.code);
# req = urllib.request.Request(
# 	url = url,
# 	headers = headers
# 	);
# result = urllib.request.urlopen(req);
# cj.save(filename, ignore_discard=True, ignore_expires=True)
# queue = queue.Queue();
# queue.put('http://weibo.com/newcenturyhotelgroup?is_all=1');
# pat = re.compile(r'<strong class=\\"W_f\d+\\">(\d+)<\\/strong>');
# collection = collection.collection(queue, 'weibo');
# date = collection.start(pat,filename);#,filename
# print(date);