#!/usr/bin/python
#coding=gbk

import sys
from os import path
from random import choice

class filename:
    def __init__(self):
        self.output = []
        self.oldfilename = sys.argv[1]
        self.percentage = float(sys.argv[2])
        self.newfile = sys.argv[3]
        self.customer = self.createfile()
        self.i = len(self.customer) * self.percentage
        self.bn = 1
        self.a = self.i/100
        self.fi = sys.stdout

    def createfile(self):
        try:
            with open(self.oldfilename,'r') as my_file:
                return list(my_file.readlines())
        except IOError, msg:
            print msg

    def compare(self):
        if len(self.customer) == len(set(self.customer)):
            return True
        else:
            return False

    def rateshow(self, x):
        if x >= (self.a * self.bn):
            rate = (str(self.bn) + '%|' + '>' * self.bn).ljust(100, '-')
            self.fi.write(rate)
            self.fi.flush()
            self.fi.write('\r')
            self.bn += 1
        else:
            pass

    def random_file(self):
        number = 0
        print '\033[1;31m =====> ���������ȡ���ݣ���ȴ� <===== \033[0m'
        while True:
            if number < int(self.i):
                randomcustomer = str(choice(self.customer))
                self.output.append(randomcustomer)
                self.customer.remove(randomcustomer)
                number += 1
                self.rateshow(number)
            else:
                print '\033[1;34m \n-----> ���ݼ���������� <------ \033[0m'
                break

        print '\033[1;32m'
        print "===========�����ṩ�İٷֱ������ɵ��ļ�(%s)������%s������==========" %(self.newfile,len(self.output))
        print "-----------δ��ȡ����:%s-----------" %(len(self.customer))
        print '\033[0m'

    def write_new_file(self):
        self.random_file()
        new_comstor_file = open(self.newfile, 'w+')
        try:
            print '\033[1;31m'
            print "***********���������д������ָ��%s�ļ�***********" %self.newfile
            print '\033[0m'
            new_comstor_file.writelines(self.output)
            new_comstor_file.close()
        except Exception, msg:
            print msg

if __name__ == '__main__':
    if len(sys.argv) == 4:
        if path.exists(sys.argv[1]) and float(sys.argv[2]) and sys.argv[3]:
            a = filename()
            if a.compare():
                a.write_new_file()
            else:
                print '\033[1;33m'
                print '######���ṩ���ļ��������ظ����ݣ�����######'
                print '\033[0m'
                sys.exit(2)
        else:
            print '\033[1;33m'
            print '######��ȷ�����ṩ�Ĳ�����ȷ�𣿣�����######'
            print '\033[0m'
            sys.exit(2)
    else:
        print '\033[1;35m'
        print "usage: %s ��Ҫ��ȡ���ļ��� �ٷֱ�(�ٷ�֮70����0.7��������0.7) �����ɵ��ļ���" % sys.argv[0]
        print '\033[0m'
        sys.exit(2)
