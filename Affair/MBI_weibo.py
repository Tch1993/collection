import Collection.weibo, config, database, affair_father, time
class MBI_weibo(affair_father.affair):
	@classmethod
	def run(cls):
		conf = config.config();
		_WORKER = int(conf.get('weibo', 'thread'));
		arr = [];
		data_time = time.localtime(time.time());
		date = time.strftime('%Y-%m', data_time);
		modifytime = time.strftime('%Y-%m-%d %H:%M:%S', data_time);
		temp = ();
		status_update = 1;
		mysql = database.Mysql();
		data = mysql._select(['brand_id', 'url'])._from('bi_weibo_data')._where("`date` = '" + date + "' AND data1 = -1 AND data2 = -1").run();
		count = mysql._from('bi_weibo_data')._where("`date` = '" + date + "'").count('id');
		if not data and count > 0:
			print('MBI本月微博已采集完成！');
			exit();
		elif not data:
			data = mysql._select(['id', 'weibo_url'])._from('bi_brand')._where("`weibo_url` != ''").run();	#._order('id')._limit(4)
			status_update = 0;
		# status_update = 0;
		# data = mysql._select(['id', 'weibo_url'])._from('bi_brand')._where("`weibo_url` != ''")._order('id')._limit(20).run();
		queue = [];
		for v in data:
			queue.append(v[1]);
		url_data = cls.queue(queue, 'Repeat/mbi_weibo').thread(_WORKER, 'Fail/mbi_weibo', Collection.weibo.weibo);
		# print(url_data);exit();
		for x in data:
			temp = (x[0], x[1], -1, -1, date, modifytime);
			for y in url_data:
				if x[1] == y[1]:
					temp = (x[0], x[1], y[0][1], y[0][2], date, modifytime);
					break;
			arr.append(temp);
		# ret = mysql._insert(['data1','data2','data3','url'], arr)._from('weibo').run();
		if status_update == 0:
			ret = mysql._insert(['brand_id', 'url', 'data1', 'data2', 'date', 'modifytime'], arr)._from('bi_weibo_data').run();
		else:
			for x in arr:
				mysql._update({'data1': int(x[2]) ,'data2': int(x[3])})._from('bi_weibo_data')._where("`date` = '" + date + "' AND brand_id = " + str(x[0])).run();
		# print(arr);
		print('MBI_weibo采集结束');



		# for y in url_data:
		# 	arr.append((y[0][0], y[0][1], y[0][2], y[1]));
		# mysql._insert(['data1', 'data2', 'data3', 'url'], arr)._from('weibo').run();
		# queue = ['http://weibo.com/3407398070','http://weibo.com/3928552585'];
		# url_data = cls.queue(queue, 'Repeat/mbi_weibo').thread(_WORKER, 'Fail/mbi_weibo', Collection.weibo.weibo);
		# print(url_data);