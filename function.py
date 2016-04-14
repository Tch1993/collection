import re, urllib.request, time, os
def file_wrtie(filename, arr, time_status = 0):
	data_time = time.localtime(time.time());
	modifytime = time.strftime('%Y-%m-%d %H:%M:%S', data_time);
	filename = './' + filename + '.txt';
	if os.path.exists(filename):
		f = open(filename, 'a');
		content = '\n' + '\n'.join(arr);
	else:
		f = open(filename, 'w+');
		content = '\n'.join(arr);
	if time_status == 0:
		content += '\ntime:' + modifytime;
	f.write(content);
	f.close();

def data_repeat(data):	#重复的数据分离
	arr = [];
	arr_data = [];
	arr_repeat = [];
	for v in data:
		arr.append(v);
	for v in arr:
		if v not in arr_data:
			arr_data.append(v);
		elif v not in arr_repeat:
			arr_repeat.append(v);
	return arr_data, arr_repeat;

def is_chinese(str):
	zhPattern = re.compile(r'[\u4e00-\u9fa5]+');
	s = '';
	for x in str:
		if zhPattern.search(x):
			s += urllib.request.quote(x);
		else:
			s += x;
	return s;