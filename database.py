import pymysql, config
class Mysql:
	conf = config.config('Config\\database.ini');
	sql = '';
	def __init__(self, k = 'Default'):
		host = self.conf.get(k, 'host');
		user = self.conf.get(k, 'user');
		passwd = self.conf.get(k, 'passwd');
		db = self.conf.get(k, 'db');
		port = int(self.conf.get(k, 'port'));
		charset = self.conf.get(k, 'charset');
		try:
			self.conn = pymysql.connect(host = host, user = user, passwd = passwd, db = db, port = port, charset = charset);
			self.cur = self.conn.cursor();
		except pymysql.Error as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]));
			exit();

	def _select(self, _select):
		if isinstance(_select, list):
			s = [];
			for i in _select:
				s.append('`' + i + '`');
			_select = ','.join(s);
		self._select = _select;
		self._select_status = 1;
		return self;

	def _insert(self, _insert, _insert_values = ''):
		if isinstance(_insert, dict):
			s = [];
			v = [];
			for i in _insert:
				s.append('`' + i + '`');
				v.append(_insert[i]);
			self._insert = ','.join(s);
			self._insert_values = ','.join(v);
			self._insert_status = 1;
		else:
			# if isinstance(_insert, str):
			# 	_insert = _insert.sqlit(',');
			if isinstance(_insert, list):
				_insert = '`' + '`,`'.join(_insert) + '`';

			self._insert = _insert;
			self._insert_values = _insert_values;
			self._insert_status = 2;
		return self;

	def _delete(self, _delete):
		self._delete = _delete;
		self._delete_status = 1;
		return self;

	def _update(self, _update):
		if isinstance(_update, dict):
			s = [];
			for i in _update:
				s.append(i + '=' + str(_update[i]));
			_update = ','.join(s);
		self._update = _update;
		self._update_status = 1;
		return self;

	def _from(self, _from):
		self._sql_from = _from;
		return self;

	def _join(self, _join, _on):
		self._sql_join = _join;
		self._sql_on = _on;
		return self;

	def _where(self, _where):
		self._sql_where = _where;
		return self;

	def _order(self, _order):
		self._sql_order = _order;
		return self;

	def _group(self, _group):
		self._sql_group = _group;
		return self;

	def _limit(self, _limit, _offset = 0):
		self._sql_offset = _offset;
		self._sql_limit = _limit;
		return self;

	def _having(self, _having):
		self._sql_having = _having;
		return self;

	def _get_from(self):
		if self.isset('_sql_from'):
			sql_from = self._sql_from;
			del self._sql_from;
			return ' from %s' % sql_from;
		else:
			print('error:请设置from');exit();
			return '';

	def _get_where(self):
		if self.isset('_sql_where'):
			sql_where = self._sql_where;
			del self._sql_where;
			return ' where %s' % sql_where;
		else:
			return '';

	def _get_join(self):
		if self.isset('_sql_join'):
			sql_join = self._sql_join;
			sql_on = self._sql_on;
			del self._sql_join;
			del self._sql_on;
			return ' join %s on %s' % (sql_join, sql_on);
		else:
			return '';

	def _get_order(self):
		if self.isset('_sql_order'):
			return ' order by %s' % self._sql_order;
		else:
			return '';

	def _get_group(self):
		if self.isset('_sql_group'):
			sql_group = self._sql_group;
			del self._sql_group;
			return ' group by %s' % sql_group;
		else:
			return '';

	def _get_having(self):
		if self.isset('_sql_having'):
			sql_having = self._sql_having;
			del self._sql_having;
			return ' having %s' % sql_having;
		else:
			return '';

	def _get_limit(self):
		if self.isset('_sql_limit'):
			if self.isset('_sql_order'):
				sql_offset = self._sql_offset;
				sql_limit = self._sql_limit;
				del self._sql_offset;
				del self._sql_limit;
				del self._sql_order;
				return ' limit %s,%s' % (sql_offset, sql_limit);
			else:
				print("error: 请设置order by");
				exit();
				return '';
		else:
			if self.isset('_sql_order'):
				del self._sql_order;
			return '';
	def count(self, field = '*'):
		Must = {'_sql_from':'from'};
		if not self.isset(Must):
			return False;
		sql = 'select %s%s%s%s' % (field, self._get_from(), self._get_join(), self._get_where());
		try:
			ret = self.cur.execute(sql);
			return ret;
		except pymysql.Error as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]));
			exit();

	def run(self):
		sql = '';
		Must = {};
		status = 0;
		many_status = 0;
		if self.isset('_select') and self.isset('_select_status'):
			# if self._select_status == 1:
			Must = {'_sql_from':'from'};
			if not self.isset(Must):
				return False;
			sql = 'select %s%s%s%s%s%s%s%s' % (self._select, self._get_from(), self._get_join(), self._get_where(), self._get_order(), self._get_group(), self._get_having(), self._get_limit());
			del self._select_status;
			del self._select;
			status = 1;
		elif self.isset('_update') and self.isset('_update_status'):
			# if self._update_status == 1:
			Must = {'_sql_from':'from'};
			if not self.isset(Must):
				return False;
			sql = 'update %s set %s%s' % (self._sql_from, self._update, self._get_where());
			del self._update_status;
			del self._sql_from;
			del self._update;
		elif self.isset('_delete') and self.isset('_delete_status'):
			# if self._delete_status == 1:
			Must = {'_sql_from':'from'};
			if not self.isset(Must):
				return False;
			sql = 'delete from %s%s' % (self._delete, self._get_where());
			# self._delete_status = 0;
			del self._delete_status;
			del self._delete;
		elif self.isset('_insert') and self.isset('_insert_status'):
			Must = {'_sql_from':'from'};
			if not self.isset(Must):
				return False;
			if self._insert_status == 1:
				sql = 'insert into %s(%s) values(%s)' % (self._sql_from, self._insert, self._insert_values);
				status = 2;
			elif self._insert_status == 2:
				_insert_values = '';
				for i in range(len(self._insert.split(','))):
					_insert_values += '%s,';
				_insert_values = _insert_values[:-1];
				sql = 'insert into ' + self._sql_from +'(' + self._insert + ') values(' + _insert_values + ')';
				_insert_values_data = self._insert_values;
				many_status = 1;	#批量添加
			del self._insert_status;
			del self._sql_from;
			del self._insert;
			del self._insert_values;
		else:
			return 0;
		# print(self.isset('_select_status'));exit();
		# print(sql);exit();
		try:
			if many_status == 0:
				ret = self.cur.execute(sql);
			elif many_status == 1:
				ret = self.cur.executemany(sql, _insert_values_data);
			if status != 1:
				self.conn.commit();
			if status == 1:
				data = self.cur.fetchall();
				return data;
			elif status == 2:
				self.cur.execute('SELECT LAST_INSERT_ID()');
				data = self.cur.fetchone();
				return data[0];
			else:
				return ret;
		except pymysql.Error as e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]));
			# return None;
			exit();
	def isset(self, var):
		if isinstance(var, dict):
			for i in var:
				if not hasattr(self, i):
					print('error: %s' % var[i]);
					return False;
			return True;	
		else:
			return hasattr(self, var);
	def __del__(self):
		self.cur.close();
		self.conn.close();


# mysql = Mysql('collection');
# mysql = Mysql();
# print(mysql._select(['id'])._from('single_hotel a')._order('id')._limit(2).run());
# print(mysql._select(['id'])._from('weibo')._order('id')._limit(2).run());
# print(mysql._insert({'data1' : '1', 'data2' : '1', 'data3' : '1', 'url' : '1'})._from('weibo').run());
# print(mysql._insert(['data1', 'data2', 'data3', 'url'], [('11','11','11','11'),('22','22','22','22')])._from('weibo').run());
# mysql._update({'data1' : '3', 'data2' : '3', 'data3' : '2', 'url' : '2'})._from('weibo')._where('id = 866').run();