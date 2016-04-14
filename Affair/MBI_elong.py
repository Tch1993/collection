import Collection.elong, config, database, affair_father, time
class MBI_elong(affair_father.affair):
	@classmethod
	def run(cls):
		conf = config.config();
		_WORKER = int(conf.get('Default', 'thread'));
		mysql = database.Mysql();
		# queue = mysql._select(['weibo_url'])._from('single_hotel')._where("`weibo_url` != ''")._order('id')._limit(4).run();
		# print(queue);
		queue = [['http://hotel.elong.com/beijing/10101795/'],['http://hotel.elong.com/beijing/00101006/'],['http://hotel.elong.com/beijing/3213213/'],['http://hotel.elong.com/beijing/32132333/'],['http://hotel.elong.com/beijing/32132333/']];
		data = cls.queue(queue, 'Repeat/mci_elong').thread(_WORKER, 'Fail/mci_elong', Collection.elong.elong);
		# arr = [];
		# data_time = time.localtime(time.time());
		# date = time.strftime('%Y-%m', data_time);
		# modifytime = time.strftime('%Y-%m-%d %H:%M:%S', data_time);
		# for x in data:
		# 	arr.append((x[1], x[0][1], x[0][2], date, modifytime));
		# # ret = mysql._insert(['data1','data2','data3','url'], arr)._from('weibo').run();
		# # ret = mysql._insert(['url', 'data1', 'data2', 'date', 'modifytime'], arr)._from('bi_weibo_data').run();
		# print(arr);
