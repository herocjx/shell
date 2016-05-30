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
        print '\033[1;31m =====> 正在随机抽取数据，请等待 <===== \033[0m'
        while True:
            if number < int(self.i):
                randomcustomer = str(choice(self.customer))
                self.output.append(randomcustomer)
                self.customer.remove(randomcustomer)
                number += 1
                self.rateshow(number)
            else:
                print '\033[1;34m \n-----> 数据己经生成完成 <------ \033[0m'
                break

        print '\033[1;32m'
        print "===========按照提供的百分比新生成的文件(%s)将会有%s条数据==========" %(self.newfile,len(self.output))
        print "-----------未抽取条数:%s-----------" %(len(self.customer))
        print '\033[0m'

    def write_new_file(self):
        self.random_file()
        new_comstor_file = open(self.newfile, 'w+')
        try:
            print '\033[1;31m'
            print "***********将随机数据写入您刚指定%s文件***********" %self.newfile
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
                print '######您提供的文件里面有重复数据，请检查######'
                print '\033[0m'
                sys.exit(2)
        else:
            print '\033[1;33m'
            print '######您确定您提供的参数正确吗？，请检查######'
            print '\033[0m'
            sys.exit(2)
    else:
        print '\033[1;35m'
        print "usage: %s 需要抽取的文件名 百分比(百分之70等于0.7，请输入0.7) 新生成的文件名" % sys.argv[0]
        print '\033[0m'
        sys.exit(2)
