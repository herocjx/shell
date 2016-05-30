#!/usr/bin/python
#coding=utf8

import os
import stat
import pwd
import logging

def initlog():
    logger = logging.getLogger()
    LOG_FILE = "/root/checkio/logs/debug.log"
    hdlr = logging.FileHandler(LOG_FILE)
    # hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE,when='D',interval='1',backupCount='7')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger

def safe_utf8_decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.encode('string_escape')
    except AttributeError:
        return s

def parse_proc_pid_status(pid):   #获取pid下的状态信息，主要是获取name 的值。
    result_dict = {}              #生成一个空的字典
    try:
        for line in open('/proc/%d/status' % pid):
            key, value = line.split(':\t', 1)
            result_dict[key] = value.strip()   #去掉值后面的空格和回车符
    except IOError:
        pass  # No such process
    return result_dict  #返回生成的字典

def list_tgids():
    tgids = os.listdir('/proc')
    if tgids:
        return [str(tgid) for tgid in tgids if '0' <= tgid[0] <= '9']  #生成/proc下面的以数字开头的list

def compare_date(pid,list):
    if list[0] >= 50:
        logging.info("程序进程PID:"  '%s' "每秒读次数:" '%s') %str(pid, list[0])
    if list[1] >= 50:
        logging.info("程序进程PID:"  '%s' "每秒写次数:" '%s') %str(pid, list[1])
    if list[2] >= 40960:
        rb.append(pid)
        logging.debug("程序进程PID:" '%s' "每秒读字节数:" '%s') %str(pid, list[2])
    if list[3] >= 40960:
        wb.append(pid)
        logging.error("程序进程PID:" '%s' "每秒写字节数:" '%s') %str(pid, list[3])

def total_count(tlist):
    for pidc in tc.keys():    #从字典中去掉列中没有的pid进程号
        if pidc in tlist:
            pass
        else:
            del tc[pidc]

    for pic in tlist:        #生成连续的pid进程号
        if pic in tc.keys():
            tc[pic] += 1
        else:
            tc[pic] = 1

    return tc

def uid_oracle():
    if Process.get_uid() == "501":
        print Process.get_uid()
    if Process.get_user() == "oracle":
        print Process.get_user()

class ProcessInfo(object):
    def __init__(self, i):
        self.pid = i
        self.uid = None
        self.user = None

    def get_uid(self):
        try:
            uid = os.stat('/proc/%s' % self.pid)[stat.ST_UID]   #查看进程pid对应的用户uid
            return uid
        except OSError:
            pass

    def get_user(self):
        uid = self.get_uid()
        if uid is not None:
            try:
                self.user = safe_utf8_decode(pwd.getpwuid(uid).pw_name)  #根据uid查找用户
            except (KeyError, AttributeError):
                self.user = str(uid)
        return self.user or '{none}'

    def process(self):
        try:
            with open("/proc/" + self.pid + "/cmdline") as proc_cmdline:
                cmdline = proc_cmdline.read(4096)
                if cmdline:
                    return cmdline
                else:
                    proc_status_name = parse_proc_pid_status(pid).get("name",'')
                    return proc_status_name
        except IOError:
            pass

if __name__ == '__main__':
    logging = initlog()
    tc = {}
    piddata = {}
    while True:
        rb = []
        wb = []
        for pid in list_tgids():
            try:
                with open("/proc/" + pid + "/io") as f:
                    for line in f:
                        if line.startswith('syscr: '):
                            syscr = int(line.split()[1])

                        if line.startswith('syscw: '):
                            syscw = int(line.split()[1])

                        if line.startswith('read_bytes: '):
                            read_bytes = int(line.split()[1])

                        if line.startswith('write_bytes: '):
                            write_bytes = int(line.split()[1])

                    iodata = [syscr, syscw, read_bytes, write_bytes]
            except IOError:
                pass
            if piddata.get(pid):
                v = list(map(lambda x: x[0] - x[1], zip(iodata, piddata[pid])))
                compare_date(pid,v)
                piddata[pid] = iodata
            else:
                piddata[pid] = iodata

        wb_conut = total_count(rb)
        for i in wb_conut.keys():
            Process = ProcessInfo(i)
            # print Process.get_uid(), Process.get_user(), Process.process()
            logging.info("用户: " "%s"  "程序：" "%s"  "己经连续读了：" "%s"  "秒" %(Process.get_user().decode('utf-8'),Process.process(),wb_conut[i]))
            # print "程序进程pid：", i, "己经连续读了：", wb_conut[i], "秒"
        import time
        print "compare end"
        time.sleep(1)