import urllib.request,re
url = 'http://weibo.com/newcenturyhotelgroup?is_all=1';
result = urllib.request.urlopen(url);
pat = re.compile(r'<strong class=\\"W_f\d+\\">(\d+)<\\/strong>');
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
	'Referer' : url,
	'cookie' : 'SINAGLOBAL=6618145541287.959.1458696813874; wb_feed_unfolded_3655689037=1; SUB=_2AkMhrw6-f8NhqwJRmP0Vz2Pjbo51zAzEiebDAHzsJxJjHkhG7T9lqCQ-knBL0ZGTBaBun_JXuzvc21t87w..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55z29P9D9WFEp5zsk3MUl_7hAgacriB-; YF-Page-G0=f994131fbcce91e683b080a4ad83c421; _s_tentry=-; Apache=6923986480105.668.1458897026846; ULV=1458897026861:3:3:3:6923986480105.668.1458897026846:1458730403187'};
request = urllib.request.Request(url = url, 
	headers = headers
);
response = urllib.request.urlopen(request);
content = response.read();
html = content.decode("utf-8", "ignore");
m = pat.findall(html);
print(m);