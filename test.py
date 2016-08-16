# -*- coding: utf-8 -*-
import time
import json
import random

import requests
import gevent
from gevent import monkey
monkey.patch_socket()

urls = [u'http://10.47.222.50/SpreadDataE/2016081211/25/dUJ7m7hq.jpg']*20

def post_recg(imgpath):
    """根据时间,地点,方向获取车流量"""
    url = u'http://10.47.222.48:806{0}/v1/recg'.format(random.randint(0,4))
    data = {
	'imgurl': imgpath,
	'coord': []
    }
    print url

    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(data))
	if r.status_code == 201:
	    return json.loads(r.text)
	else:
	    raise Exception('url: %s, status: %s, %s' % (
		url, r.status_code, r.text))
    except Exception as e:
        raise

t1 = time.time()
jobs = [gevent.spawn(post_recg, url)for url in urls]
gevent.joinall(jobs)

for i in jobs:
    print i.value
t2 = time.time()
print t2 - t1

#if __name__ == '__main__':
    #get_kkdd_test()
    #get_kakou_count_test()
    #check_kakou_count_test()
    #sms_test()
