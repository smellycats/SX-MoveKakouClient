# -*- coding: utf-8 -*-
import json
import random

import requests


class Recg(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.headers = {'content-type': 'application/json'}

	self.status = False

    def post_recg(self, imgurl):
        """根据时间,地点,方向获取车流量"""
	port = u'806{0}'.format(random.randint(0,4))
        url = 'http://{0}:{1}/v1/recg'.format(self.host, port)
	data = {
	    'imgurl': imgurl,
	    'coord': []
	}
        try:
            r = requests.post(url, headers=self.headers, data=json.dumps(data))
            if r.status_code == 201:
                return (r.status_code, json.loads(r.text))
	    else:
		return (r.status_code, r.text)
                #self.status = False
                #raise Exception('url: %s, status: %s, %s' % (
                    #url, r.status_code, r.text))
        except Exception as e:
            self.status = False
            raise


if __name__ == "__main__":
    ini = {
	'host': '10.47.222.48',
	'port': 8060
    }
    c = Recg(**ini)
    data = {
	'imgurl': u'http://10.47.222.50/SpreadDataE/2016081211/25/dUJ7m7hq.jpg',
	'coord': []
    }
    print c.post_recg(data)

