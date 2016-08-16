# -*- coding: utf-8 -*-
import time
import uuid


def gmt2time(str):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(str, "%a %b %d %H:%M:%S GMT+0800 %Y"))

def hpzl2hpys(str):
    if str in set(['01', '07', '13', '14', '15', '16', '17']):
	return 'YL'
    if str in set(['20', '21', '22', '23', '24', '31', '32']):
	return 'WT'
    if str in set(['02', '08']):
	return 'BU'
    if str in set(['03', '04', '05', '06', '09', '10', '11', '12']):
	return 'BK'
    return 'QT'

def get_uuid():
    return uuid.uuid1()

    
if __name__ == '__main__':
    #str = 'Thu Nov 08 17:15:30 +0800 2012'
    #print (gmt2time(str),)
    print hpzl2hpys('01')
