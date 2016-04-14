import Collection.weibo, config, database, affair_father, time
class MCI_weibo(affair_father.affair):
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
		data = mysql._select(['hotel_id', 'url'])._from('single_hotel_weibo_data')._where("`date` = '" + date + "' AND data1 = -1 AND data2 = -1").run();
		count = mysql._from('single_hotel_weibo_data')._where("`date` = '" + date + "'").count('id');
		if not data and count > 0:
			print('MCI本月微博已采集完成！');
			exit();
		elif not data:
			data = mysql._select(['id', 'weibo_url'])._from('single_hotel')._where("`weibo_url` != ''").run();	#._order('id')._limit(6)
			status_update = 0;
		# exit();
		# for i in data:
		# 	MCI_QUEUE_Q.put(i[0]);
		# print(MCI_QUEUE_Q.qsize());
		# exit();
		# queue = [['http://weibo.com/3407398070/about'],['http://weibo.com/3928552585/about'],['http://weibo.com/u/1884854327?from=usercardnew']];
		# queue = [];
		# f = open('.\\Fail\\mci_weibo.txt');             # 返回一个文件对象  
		# line = f.readline();             # 调用文件的 readline()方法  
		# while line:  
		# 	# MCI_QUEUE_Q.put(line.strip());
		# 	queue.append([line.strip()]);
		# 	line = f.readline();
		# f.close();
		# mci_weibo = Collection.weibo.weibo(MCI_QUEUE_Q);
		# threads = [];
		# for i in range(_WORKER):
		# 	thread = mythread.Mythread(mci_weibo.read_db);
		# 	thread.start();
		# 	threads.append(thread);
		# thread = mythread.Myqueue();
		# thread.start(_WORKER, mci_weibo.read_db);

		# data = mysql._select(['id', 'weibo_url'])._from('single_hotel')._where("`weibo_url` != ''")._order('id')._limit(20).run();
		# status_update = 0;
		queue = [];
		for v in data:
			queue.append(v[1]);
		# queue = ['http://weibo.com/3407398070','http://weibo.com/3928552585','http://weibo.com/u/2101807562','http://weibo.com/bjsbc'];
		url_data = cls.queue(queue, 'Repeat/mci_weibo').thread(_WORKER, 'Fail/mci_weibo', Collection.weibo.weibo);
		# print(url_data);
		for x in data:
			temp = (x[0], x[1], -1, -1, date, modifytime);
			for y in url_data:
				if x[1] == y[1]:
					temp = (x[0], x[1], y[0][1], y[0][2], date, modifytime);
					break;
			arr.append(temp);
		
		if status_update == 0:
			ret = mysql._insert(['hotel_id', 'url', 'data1', 'data2', 'date', 'modifytime'], arr)._from('single_hotel_weibo_data').run();
		else:
			for x in arr:
				mysql._update({'data1': int(x[2]) ,'data2': int(x[3])})._from('single_hotel_weibo_data')._where("`date` = '" + date + "' AND hotel_id = " + str(x[0])).run();
		print('MCI_weibo采集结束');



		# for y in url_data:
		# 	arr.append((y[0][0], y[0][1], y[0][2], y[1]));
		# mysql._insert(['data1', 'data2', 'data3', 'url'], arr)._from('weibo').run();