import Collection.alexa, config, database, affair_father, time, urllib.parse, alexaLogin, phpserialize
class Alexa(affair_father.affair):
	@classmethod
	def run(cls):
		conf = config.config();
		_WORKER = int(conf.get('Default', 'thread'));
		mysql = database.Mysql();
		data_time = time.localtime(time.time());
		date = time.strftime('%Y-%m', data_time);
		filename = './Cookie/alexa_cookie.txt';
		status_update = 1;
		alexaLogin.alexaLogin.login(filename);
		data = mysql._select(['brand_id', 'url'])._from('bi_brand_yunying_data')._where("`rank_data_id` = 39 AND `date` = '" + date + "' AND data = -1").run();
		count = mysql._from('bi_brand_yunying_data')._where("`rank_data_id` = 39 AND `date` = '" + date + "'").count('1');
		if not data and count > 0:
			print('本月alexa已采集完成！');
			exit();
		elif not data:
			model = mysql._select(['id', 'arr_rank_class', 'arr_data_item'])._from('bi_rank_model')._where("status = 1").run();#._order('id')._limit(8)
			brand_id = '';
			for i in model:
				if i[1] != '' and b'39' in phpserialize.loads(i[2].encode('utf-8')).values():
					brand_id += ','.join(map(str, list(phpserialize.loads(i[1].encode('utf-8')).values())));
				else:
					continue;
			data = mysql._select(['id', 'brand_url'])._from('bi_brand')._where("brand_url != '--' and brand_url != '' and status=1 and id in(" + brand_id + ")").run();#._order('id')._limit(8)
			status_update = 0;
		url_list = [];
		urlparse = '';
		for i in data:
			if status_update == 0:
				urlparse = urllib.parse.urlsplit(i[1]);
				domain = '';
				if urlparse.netloc != '':
					domain = urlparse.netloc;
				else:
					domain = urlparse.path;
				url_list.append('http://alexa.chinaz.com/alexa_more.aspx?domain=' + domain);
			else:
				url_list.append(i[1]);
		# print(data);input();exit();
		url_data = cls.queue(url_list, 'Repeat/alexa').thread(_WORKER, 'Fail/alexa', Collection.alexa.alexa);
		arr = [];
		modifytime = time.strftime('%Y-%m-%d %H:%M:%S', data_time);
		for x in data:
			if status_update == 0:
				urlparse = urllib.parse.urlsplit(x[1]);
				domain = '';
				if urlparse.netloc != '':
					domain = urlparse.netloc;
				else:
					domain = urlparse.path;
				url = 'http://alexa.chinaz.com/alexa_more.aspx?domain=' + domain;
			else:
				url = x[1];
			temp = (x[0], 39, 0, url, date, modifytime);
			for y in url_data:
				if url == y[1]:
					temp = (x[0], 39, y[0][1].replace(',',''), url, date, modifytime);
					break;
			arr.append(temp);
		if status_update == 0:
			mysql._insert(['brand_id', 'rank_data_id', 'data', 'url', 'date', 'modifytime'], arr)._from('bi_brand_yunying_data').run();
		else:
			for x in arr:
				mysql._update({'data': int(x[2])})._from('bi_brand_yunying_data')._where("`rank_data_id` = 39 AND `date` = '" + date + "' AND brand_id = " + str(x[0])).run();
		# print(arr);
		print('alexa采集完成！');
