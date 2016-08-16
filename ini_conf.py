#-*- encoding: utf-8 -*-
import ConfigParser

class MyIni(object):
    def __init__(self, confpath = 'my_ini.conf'):
	self.conf_path = confpath
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(confpath)

    def __del__(self):
        del self.cf

    def get_kakou(self):
        conf = {}
        section = 'KAKOU'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        return conf

    def get_recg(self):
        conf = {}
        section = 'RECG'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        return conf


if __name__ == '__main__':
    mi = MyIni()
    print mi.get_kakou()
    print mi.get_recg()