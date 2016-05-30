#!/usr/bin/python

import time
import sys


fmt = '{:3d} [{:<20}]'.format

def progressbar():
    for n in range(21):
        time.sleep(0.1)
        print '\r',fmt(n*5, '='*n),

progressbar()
print

# f = sys.stdout

# for n in range(1, 101):
#     s = ('>' * n).ljust(100, '-')
#     f.write(s)
#     f.flush()
#     time.sleep(0.3)
#     f.write('\r')
# f.write('\n')

# for i in xrange(1,100):
#     print i


# i = 0
# a = 38500/100
#
# b = 1
#
# def xyz(x):
#     global b
#     if x >= (a * b):
#         s = ('>' * b).ljust(100, '-')
#         f.write(s)
#         f.flush()
#         f.write('\r')
#         b += 1
#     else:
#         pass
#
#
#
# while True:
#     if i < 38500:
#         i += 1
#         xyz(i)
#     else:
#         break
#
# f.write('\n')
#



#
# def test():
#     a = {'a':1,'b':2}
#     return a
#
# for i,y in test().items():
#     if y >= 2:
#         print y
#
# x_ora = '/bin/sh ' + 'checkiooracle.sh ' + '213'
# print x_ora
#
#
# a = None
#
# if a:
#     print "111"
# else:
#     print "222"
#

# b = [1,2,3,4]
# c = ["a","b","c","d"]
#
# for i in b,c:
#     if i == b:
#         print "ok"
#     if i == c:
#         print "this is c"
    # for x in i:
    #     print x





# a = {'a':[123,345,789], 'b':456,'cjx':{'i':'12131','o':'sdfafa','p':'yxz'}}
# a['c'] = {}
# i = ["a", "c", "d", "b"]
# y = ['0','0','0','0']
#
# i.append([0,0,0,0])
# a['zy'] = i
#
# print i
# print i[:4]
# print i[4][0]
# print a
#
#

# if int(0.7):
#     print "111"
# else:
#     print "222"

# a =['a','b','a']
#
#
# if len(a) == len(set(a)):
#     print "111"
# else:
#     print "222"



# print 1261311810-1245198746
#
#
# y = (5242880/1024)/8
#
# print y
#
#
#
# a = {'a':2,'b':1,'c':3,'d':11}
#
#
# if max(a.values()) > 5:
#     print "aaa"
#
#
# b = [1,2,3,4,5]
# print b
# b = []
# print b


# def dy(test):
#     for key,value in test.items():
#         if value > 5:
#             return key, value
#
#
#
# def abc(toppid, count, bit):
#     print toppid, count, bit
#
#
#
# toppid ,topvalue = dy(a)
#
# abc(toppid, topvalue, 'aaa')


# def test(a,b):
#     print a, b
#
# a = 100
#
# test(a,'riops')





#
# if a['cjx'].get('i'):
#     print a['cjx']['i']
#
#
#
# if a.get('a'):
#     print a['a']
#
#
# if len(i) == 4:
#     print "aaa"
#
# i.insert(4,'f')
#
#
# print len(i), i[:5]
#
# if 'c' in a['c'].keys():
#     print a['c'].keys()



# d = {}
#
#
# d["a"]= ['xyz']
#
# try:
#     if d['a'][1]:
#         print d[a][1]
# except IndexError:
#     print d['a'][0]


# d["a"].append(1)
#
# d['a'][1] += 1
#
# for k, v in d.items():
#     print v[0]



#
# for x in i:
#     try:
#         if x in a.keys():
#             print a[x]
#     except KeyError, msg:
#         print msg
#         continue
#
#     if 1 > 0:
#         print "1111"
#     else:
#         print "2222"
#
# abc = "000"
#
# a["a"][0] = abc
#
# print a["a"][0]

# b = a.get("a")
#
# del a["c"]
#
# print b







# a = b = c = 0
# e = f = g = {}
# h = i = j = []
# c = 40
# h = [1,2,3]
# print b, h, i, g
#
#
# def pd():
#     if c > a:
#         print c
#
# pd()

# d = {"a":1, "b":2}
# c = {"a":1, "c":2}
# e = [30,40,50]
#
#
# y = 40
#
# if e[0] > y:
#     y = e[0]
#     print y
# else:
#     print y
#
#
#
# if len(e) > 0:
#     print c
#
# for k, v in d.items():
#     if k in c.keys():
#         c[k] += v
#     else:
#         c[k] = v
#
# print c
#
# print "-" * 15

# ex_ora = '/bin/sh ' + '/root/11.sh ' + '230'
#
#
#
# def test(a='OK'):
#     return a
#
#
#
# print test(ex_ora)





# import sys
#
# print ("this is echo messges:", sys.stdin.read())
#
#
# a = 1
#
# if a:
#     print "aaaa"
# else:
#     print "bbbb"
#
#
#
#
# def read(self):
#     def extract(line):
#         return int(line.split()[1]) * 1024
#
#     for line in self.vmstat_file:
#         if line.startswith('pgpgin '):
#             pgpgin = extract(line)
#             break
#
#     for line in self.vmstat_file:
#         if line.startswith('pgpgout '):
#             pgpgout = extract(line)
#             break
#
#     self.vmstat_file.seek(0)
#     return pgpgin, pgpgout
#
#
# def delta(self):
#     now = self.read()
#     delta = now[0] - self.vmstat[0], now[1] - self.vmstat[1]
#     self.vmstat = now
#     return delta
#
# import datetime
#
#
# import ctypes
# import socket
# import os
#
# libc = ctypes.CDLL(None)
#
# class SOCKADDR_NL(ctypes.Structure):
#     _fields_ = [("nl_family", ctypes.c_ushort),
#                 ("nl_pad",    ctypes.c_ushort),
#                 ("nl_pid",    ctypes.c_int),
#                 ("nl_groups", ctypes.c_int)]
#
# def _nl_bind(descriptor, addr):
#     addr = SOCKADDR_NL(socket.AF_NETLINK, 0, os.getpid(), 0)
#     return libc.bind(descriptor.fileno(),
#                      ctypes.pointer(addr),
#                      ctypes.sizeof(addr))
#
# def _nl_getsockname(descriptor):
#     addr = SOCKADDR_NL(0, 0, 0, 0)
#     len = ctypes.c_int(ctypes.sizeof(addr));
#     libc.getsockname(descriptor.fileno(),
#                      ctypes.pointer(addr),
#                      ctypes.pointer(len))
#     return addr.nl_pid, addr.nl_groups;
#
# def _nl_send(descriptor, msg):
#     return libc.send(descriptor.fileno(), msg, len(msg), 0);
#
# def _nl_recv(descriptor, bufs=16384):
#     addr = SOCKADDR_NL(0, 0, 0, 0)
#     len = ctypes.c_int(ctypes.sizeof(addr))
#     buf = ctypes.create_string_buffer(bufs)
#
#     r = libc.recvfrom(descriptor.fileno(),
#                       buf, bufs, 0,
#                       ctypes.pointer(addr), ctypes.pointer(len))
#
#     ret = ctypes.string_at(ctypes.pointer(buf), r)
#     return ret, (addr.nl_pid, addr.nl_groups)



# for x in range(1,9):
#     print x
#     yesterday = (datetime.datetime.today() - datetime.timedelta(days=x)).strftime("%Y-%m-%d")
#     print yesterday


# year = datetime.datetime.today().strftime("%Y")
# month =  datetime.datetime.today().strftime("%m")
# day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%d")
#
# import glob
# filenames = glob.glob(s, year + "*" + month + "*" + day + "*" )


# encoding=utf-8
# Filename: thread-function.py

#
# import threading
# import time
#
# def threadFunc(num):
#     global total, mutex
#
#     print threading.currentThread().getName()
#
#     for x in xrange(0, int(num)):
#         mutex.acquire()
#         total = total + 1
#         mutex.release()
#
# def main(num):
#     global total, mutex
#     total = 0
#     mutex = threading.Lock()
#
#     threads = []
#     for x in xrange(0, num):
#         threads.append(threading.Thread(target=threadFunc, args=(100,)))
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
#     print total
#
#
# if __name__ == '__main__':
#     main(40)
# import optparse,locale
#
# def main():
#     try:
#         locale.setlocale(locale.LC_ALL, '')
#     except locale.Error:
#         print('unable to set locale, falling back to the default locale')
#     parser = optparse.OptionParser(usage='usage', version='iotop ')
#     parser.add_option('-o', '--only', action='store_true',
#                       dest='only', default=False,
#                       help='only show processes or threads actually doing I/O')
#     parser.add_option('-b', '--batch', action='store_true', dest='batch',
#                       help='non-interactive mode')
#     parser.add_option('-n', '--iter', type='int', dest='iterations',
#                       metavar='NUM',
#                       help='number of iterations before ending [infinite]')
#     parser.add_option('-d', '--delay', type='float', dest='delay_seconds',
#                       help='delay between iterations [1 second]',
#                       metavar='SEC', default=1)
#     parser.add_option('-p', '--pid', type='int', dest='pids', action='append',
#                       help='processes/threads to monitor [all]', metavar='PID')
#     parser.add_option('-u', '--user', type='str', dest='users', action='append',
#                       help='users to monitor [all]', metavar='USER')
#     parser.add_option('-P', '--processes', action='store_true',
#                       dest='processes', default=False,
#                       help='only show processes, not all threads')
#     parser.add_option('-a', '--accumulated', action='store_true',
#                       dest='accumulated', default=False,
#                       help='show accumulated I/O instead of bandwidth')
#     parser.add_option('-k', '--kilobytes', action='store_true',
#                       dest='kilobytes', default=False,
#                       help='use kilobytes instead of a human friendly unit')
#     parser.add_option('-t', '--time', action='store_true', dest='time',
#                       help='add a timestamp on each line (implies --batch)')
#     parser.add_option('-q', '--quiet', action='count', dest='quiet', default=0,
#                       help='suppress some lines of header (implies --batch)')
#     parser.add_option('--profile', action='store_true', dest='profile',
#                       default=False, help=optparse.SUPPRESS_HELP)
#
#     options, args = parser.parse_args()
#
#     return options
#
# import pprint
#
# class DumpableObject(object):
#     """Base class for all objects that allows easy introspection when printed"""
#     def __repr__(self):
#         return '%s: %s>' % (str(type(self))[:-1], pprint.pformat(self.__dict__))
#
# if __name__ == '__main__':
#     options = main()
#     print options
#     print '%s: %s>' % (str(type(options))[:-1], pprint.pformat(options))
#
#
#
#
#
#
#
# class Connection:
#     def __init__(self, nltype, groups=0, unexpected_msg_handler=None):
#         self.descriptor = socket.socket(socket.AF_NETLINK,
#                                         socket.SOCK_RAW, nltype)
#         self.descriptor.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
#         self.descriptor.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
#         _nl_bind(self.descriptor, (0, groups))
#         self.pid, self.groups = _nl_getsockname(self.descriptor)
#         self._seq = 0
#         self.unexpected = unexpected_msg_handler
#     def send(self, msg):
#         _nl_send(self.descriptor, msg)
#     def recv(self):
#         contents, (nlpid, nlgrps) = _nl_recv(self.descriptor)
#         # XXX: python doesn't give us message flags, check
#         #      len(contents) vs. msglen for TRUNC
#         msglen, msg_type, flags, seq, pid = struct.unpack("IHHII",
#                                                           contents[:16])
#         print msglen,msg_type, flags, seq, pid
#
#
# if __name__ == '__main__':
#     import struct
#     a = Connection()
#     a.recv()
#
#
# pids = ['938','942']
#
# for x in pids:
#     iodata = []
#     with open('/proc/' + x + '/io') as f:
#         for line in f:
#             if line.startswith('syscr: '):
#                 syscr = int(line.split()[1])
#
#             if line.startswith('syscw: '):
#                 syscw = int(line.split()[1])
#
#             if line.startswith('read_bytes: '):
#                 read_bytes = int(line.split()[1])
#
#             if line.startswith('write_bytes: '):
#                 write_bytes = int(line.split()[1])
#
#         iodata = [syscr, syscw, read_bytes, write_bytes]
#         print iodata



