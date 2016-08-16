# -*- coding: utf-8 -*-
from helper_sms import SMS
from helper_kakou import Kakou

ini = {
    'host': '10.47.222.50',
    'port': 80
}


def add_car_info():
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

def get_temp():
    c = Kakou(**ini)
    print c.get_temp()

def get_temp_by_id():
    c = Kakou(**ini)
    print c.get_temp_by_id(125)

def del_temp_by_id():
    c = Kakou(**ini)
    print c.del_temp_by_id(125)

if __name__ == '__main__':
    get_temp()
    get_temp_by_id()
    del_temp_by_id()


