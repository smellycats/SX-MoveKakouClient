# -*- coding: utf-8 -*-
import time
import json

import arrow
import requests
#import gevent
#from gevent import monkey
#monkey.patch_all()
import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
import gevent
import gevent.socket
import gevent.monkey
gevent.monkey.patch_all()

import helper
from helper_kakou import Kakou
from helper_recg import Recg
from ini_conf import MyIni
from my_logger import *


debug_logging(u'logs/error.log')
logger = logging.getLogger('root')


class MoveKakou(object):
    def __init__(self):
        self.my_ini = MyIni()
	self.kakou_ini = self.my_ini.get_kakou()
	self.recg_ini = self.my_ini.get_recg()

        self.kakou = Kakou(**self.kakou_ini)
	self.recg = Recg(**self.recg_ini)
	print 'movekakou123'

    def __del__(self):
        pass

    def get_recgs(self):
	t = self.kakou.get_temp(10)

	urls = []
	if t['total_count'] > 0:
	    for i in t['items']:
		#ids.append(i['id'])
		urls.append(i['url_img'])

	jobs = [gevent.spawn(self.recg.post_recg, url) for url in urls]
	gevent.joinall(jobs, timeout=10)

	for i in range(t['total_count']):
	    data = {}
	    data['uuid'] = helper.get_uuid()
	    data['date_upload'] = t['items'][i]['timeflag']
	    data['jgsj'] = helper.gmt2time(t['items'][i]['time'])
	    if jobs[i].value[0] == 400:
		self.kakou.del_img_by_id(t['items'][i]['id'])
		continue
	    elif jobs[i].value[0] == 201:
		if jobs[i].value[1]['recginfo'] == []:
		    self.kakou.del_img_by_id(t['items'][i]['id'])
		    continue
		else:
		    data['hphm'] = jobs[i].value[1]['recginfo'][0]['hphm']
		    data['hpys'] = helper.hpzl2hpys(jobs[i].value[1]['recginfo'][0]['hpzl'])
	    else:
		logger.error(jobs[i].value)
		logger.error(t['items'][i])
		continue
	    data['wc'] = '[]'
	    data['place_name'] = ''
	    data['img_path'] = t['items'][i]['path']
	    data['disk'] = t['items'][i]['disk']
	    data['user_id'] = t['items'][i]['user_id']
	    # 上传车辆信息
	    self.kakou.post_car_info(data)
	    self.kakou.del_temp_by_id(t['items'][i]['id'])

        
    def run(self):
        while 1:
            try:
                self.main()
            except Exception as e:
                logger.error(e)
                time.sleep(10)
            finally:
                time.sleep(1)

if __name__ == "__main__":
    mv = MoveKakou()
    #print mv.get_temp()
    mv.get_recgs()

