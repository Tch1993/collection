import urllib.request, http.cookiejar, re

class alexaLogin:
	@staticmethod
	def login(filename):
		cj = http.cookiejar.LWPCookieJar()
		cookie_support = urllib.request.HTTPCookieProcessor(cj)
		opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
		urllib.request.install_opener(opener)
		init_url = "http://alexa.chinaz.com/?domain=ascottchina.com";

		init_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
			'Referer' : init_url,
			'Host' : "alexa.chinaz.com"};
		init_request = urllib.request.Request(url = init_url, 
			headers = init_headers
		);
		urllib.request.urlopen(init_request);
		cj.save(filename, ignore_discard=True, ignore_expires=True)
		# url = "http://alexa.chinaz.com/alexa_more.aspx?domain=ascottchina.com"
		# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
		# 	'Referer' : 'http://alexa.chinaz.com',
		# 	'Host' : "alexa.chinaz.com"};
		# request = urllib.request.Request(url = url, 
		# 	headers = headers
		# );
		# content = urllib.request.urlopen(request);

		# f = open('data6.txt', 'w+', encoding = 'utf-8');
		# f.write(content.read().decode('utf-8'));
		# f.close();
