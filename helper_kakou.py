# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class Kakou(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
	#self.username = kwargs['username']
	#self.password = kwargs['password']
        self.headers = {'content-type': 'application/json'}

	self.status = False

    def get_temp(self, per_page=8):
        """根据时间,地点,方向获取车流量"""
        url = 'http://{0}:{1}/move_kakou4/index.php/temp/getTemp?page=1&per_page={2}'.format(
	    self.host, self.port, per_page)
        #print url
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
	    else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
	    self.status = False
            raise

    def get_temp_by_id(self, _id):
        """根据id获取临时表"""
        url = 'http://{0}:{1}/move_kakou4/index.php/temp/getTempById?id={2}'.format(
	    self.host, self.port, _id)
        #print url
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
	    else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
	    self.status = False
            raise

    def del_temp_by_id(self, _id):
        """根据id删除临时表信息"""
        url = 'http://{0}:{1}/move_kakou4/index.php/temp/delTempById?id={2}'.format(
	    self.host, self.port, _id)
        #print url
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
	    else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
	    self.status = False
            raise

    def del_img_by_id(self, _id):
        """根据id删除图片和临时表信息"""
        url = 'http://{0}:{1}/move_kakou4/index.php/temp/delImgById?id={2}'.format(
	    self.host, self.port, _id)
        #print url
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return json.loads(r.text)
	    else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
	    self.status = False
            raise

    def post_car_info(self, data):
        """添加过车信息"""
        url = 'http://{0}:{1}/move_kakou4/index.php/carinfo/post_car_info'.format(
	    self.host, self.port)
        #print url
        try:
            r = requests.post(url, data=data)
            if r.status_code == 200:
                return r.text
	    else:
                self.status = False
                raise Exception('url: %s, status: %s, %s' % (
                    url, r.status_code, r.text))
        except Exception as e:
	    self.status = False
            raise


if __name__ == "__main__":
    ini = {
	'host': '10.47.222.50',
	'port': 80
    }
    c = Kakou(**ini)
    data = {
	'uuid': u'123',
	'date_upload': '2016-08-12 00:00:00',
	'jgsj': '2016-08-12 00:00:00',
	'hphm': u'粤L12345',
	'hpys': u'QT',
	'wc': '[]',
	'place_name': '',
	'img_path': '123.jpg',
	'disk': 'E'
    }
    print (c.post_car_info(data),)
