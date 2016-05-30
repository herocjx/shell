#!/usr/bin/python
#coding=utf8

import os
import stat
import pwd
import logging
import time
from daemon import Daemon

def c_logfile():
    if os.path.exists('iologs'):
        pass
    else:
        os.mkdir('iologs')

def initlog():
    c_logfile()
    logger = logging.getLogger()
    LOG_FILE = "iologs/debug.log"
    ckio = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    ckio.setFormatter(formatter)
    logger.addHandler(ckio)
    logger.setLevel(logging.NOTSET)
    return logger

def parse_proc_pid_status(pid):
    result_dict = {}
    try:
        for line in open('/proc/%s/status' % pid):
            key, value = line.split(':\t', 1)
            result_dict[key] = value.strip()
    except IOError, msg:
        logging.error("%s" %(msg))
    return result_dict

def list_tgids():
    tgids = os.listdir('/proc')
    if tgids:
        return [str(tgid) for tgid in tgids if '0' <= tgid[0] <= '9']

def zd_compare():
    for piddata_pid in piddata.keys():
        if piddata_pid == 'riopstop' or piddata_pid == 'wiopstop' or piddata_pid == 'rttop' or piddata_pid == 'wttop':
            pass
        elif piddata_pid in list_tgids():
            pass
        else:
            logging.info("删除系统里不存在的PID数据,PID:%s" %piddata_pid)
            try:
                del piddata[piddata_pid]
            except KeyError,msg:
                logging.info("key error %s" %msg)

def compare_riops(pid,data):
    riops.append(pid)

    if piddata.get(pid) and piddata[pid][4][0] != 0:
        if piddata[pid][4][0] < data:
            piddata[pid][4][0] = data
    else:
        piddata[pid][4][0] = data

    logging.info("程序进程PID:%s" "当前每秒读次数:%s" "\t" "程序的生命周期读IOPS最高值是：%s" %(pid, str(data), piddata[pid][4][0]))

def compare_wiops(pid, data):
    wiops.append(pid)

    if piddata.get(pid) and piddata[pid][4][1] != 0:
        if piddata[pid][4][1] < data:
            piddata[pid][4][1] = data
    else:
        piddata[pid][4][1] = data

    logging.info("程序进程PID:%s" "当前每秒写次数:%s" "\t" "程序的生命周期写IOPS最高值是：%s" %(pid, str(data), piddata[pid][4][1]))

def compare_r(pid,data):
    rb.append(pid)

    if piddata.get(pid) and piddata[pid][4][2] != 0:
        if piddata[pid][4][2] < data:
            piddata[pid][4][2] = data
    else:
        piddata[pid][4][2] = data

    logging.info("程序进程PID:%s" "当前每秒读字节数:%s" "\t" "程序的生命周期每秒读最高值是：%s 字节" %(pid, str(data), piddata[pid][4][2]))

def compare_w(pid,data):
    wb.append(pid)
    print "======================wb============================="
    if piddata.get(pid) and piddata[pid][4][3] != 0:
        if piddata[pid][4][3] < data:
            piddata[pid][4][3] = data
    else:
        piddata[pid][4][3] = data

    logging.info("程序进程PID:%s" "当前每秒写字节数:%s" "\t" "程序的生命周期每秒写最高值是：%s 字节" %(pid, str(data), piddata[pid][4][3]))

def pid_ora_check(pid):
    ex_ora = '/bin/sh ' + '/root/iocheck/checkiooracle.sh ' + pid
    print ex_ora
    ora_result = os.popen(ex_ora)
    return ora_result.read()

def zabbix_reslut(pid):
    try:
        oral_reslut = pid_ora_check(pid)
    except Exception, msg:
        logging.error("%s" %msg)
    else:
        if oral_reslut == 'no rows selected':
            logging.info("查到PID:%s, 但是数据库没有查到对应的SQL语句，执行SQL脚本没有返回结果" %pid)
            oral_reslut = "查到PID:%s, 但是数据库没有查到对应的SQL语句，执行SQL脚本没有返回结果" %pid
        else:
            logging.info("这是进程pid：%s，这是数据库检查出来的SQL语句：%s" %(pid,oral_reslut))
    finally:
	logging.info("send message")
        send_zabbix(oral_reslut)

def send_zabbix(ioreslut = 'Ok'):
    logging.info(ioreslut)
    # zabbix_sender="/usr/local/zabbix/bin/zabbix_sender -z 10.100.30.50 -s oracledatabase -k oracleiocheck -o %s" %ioreslut.decode('gbk').encode('utf8')
    # os.popen(zabbix_sender)

def J_zabbix(toppid,count,bit):
    if toppid == 'Ok' and count == 'Ok' and bit:
        send_zabbix()
    else:
        Process = ProcessInfo(toppid)
        print "PID:%s 用户:%s UID:%s 程序:%s 己经连续%s: %s秒" %(toppid,Process.get_user(),Process.get_uid(),Process.process(),bit,count)
        if Process.get_user() == 'oracle' and Process.get_uid() == 501:
            print "*******************"
            zabbix_reslut(toppid)
            logging.info("PID: " "%s" "用户: " "%s"  "程序: " "%s"  "己经连续%s: " "%s"  "秒" %(toppid,Process.get_user(),Process.process(),bit,count))
        elif Process.get_user() != 'oracle' and Process.get_uid() != 501:
            Process = ProcessInfo(toppid)
            send_zabbix(ioreslut='PID:%s,user:%s,process:%s,time:%s' %(toppid, Process.get_user(),Process.process(),count))
            logging.info("PID: " "%s" "用户: " "%s"  "程序: " "%s"  "己经连续%s: " "%s"  "秒" %(toppid,Process.get_user(),Process.process(),bit,count))

class ProcessInfo():
    def __init__(self, i):
        self.pid = i
        self.uid = None
        self.user = None

    def get_uid(self):
        try:
            uid = os.stat('/proc/%s' % self.pid)[stat.ST_UID]
            return uid
        except OSError, msg:
            logging.error("%s" %msg)

    def get_user(self):
        uid = self.get_uid()
        if uid is not None:
            try:
                self.user = pwd.getpwuid(uid).pw_name
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
        except IOError, msg:
            logging.error("%s" %msg)

class MyDaemon(Daemon):
    def run(self):
        logging = initlog()
        global piddata, pid
        piddata = {}
        while True:
            global riops,wiops,rb,wb
            riops = []
            wiops = []
            rb = []
            wb = []
            zd_compare()
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
                        #logging.info("-----这是PID:%s \t 的源始数据%s-----" %(pid,iodata))

                    if piddata.get(pid):
                        v = list(map(lambda x: x[0] - x[1], zip(iodata, piddata[pid][:4])))
                        #logging.info("－－－－－请注意这是PID:%s \t 两次减掉后得出来的值%s－－－－－" %(pid,v))
                        if v == [0, 0, 0, 0]:
                            continue
                        else:
                            piddata[pid][:4] = iodata
                            if v[0] > 50:
                                logging.info("%s ==> riops:%s" %(pid, v[0]))
                                compare_riops(pid, v[0])
                            if v[1] > 50:
                                logging.info("%s ==> wiops:%s" %(pid, v[1]))
                                compare_wiops(pid, v[1])
                            if v[2] > 40960:
                                logging.info("%s ==> read bytes: %s" %(pid, v[2]))
                                compare_r(pid, v[2])
                            if v[3] > 40960:
                                logging.info("%s ==> write bytes: %s" %(pid, v[3]))
                                compare_w(pid, v[3])
                    else:
                        iodata.append([0,0,0,0])
                        piddata[pid] = iodata
                        logging.info("%s --> %s" %(pid, piddata[pid]))

                except IOError, msg:
                    logging.error("文件不存在，这是错误信息:%s" %(msg))


            if len(riops) > 0:
                try:
                    for pidc in piddata['riopstop'].keys():
                        if pidc in riops:
                            pass
                        else:
                            logging.info("删除不连续的PID数据,PID:%s" %piddata['riopstop'][pidc])
                            del piddata['riopstop'][pidc]
                except KeyError, msg:
                    piddata['riopstop'] = {}
                    logging.error("----- riopstop 还没有建立 ----- %s" %msg)

                for pi in riops:
                    if pi in piddata['riopstop'].keys():
                        piddata['riopstop'][pi] += 1
                    else:
                        piddata['riopstop'][pi] = 1

                if max(piddata['riopstop'].values()) > 5:
                    for toppid, topcount in piddata['riopstop'].items():
                        if topcount > 5:
                            J_zabbix(toppid, topcount,'读IOPS超过')
                else:
                    logging.info("发送读IOPS,ok消息")
                    J_zabbix('Ok', 'Ok','读IOPS超过')
            else:
                logging.info("发送读IOPS,ok消息")
                J_zabbix('Ok', 'Ok','读IOPS超过')

            if len(wiops) > 0:
                try:
                    for pidc in piddata['wiopstop'].keys():
                        if pidc in wiops:
                            pass
                        else:
                            logging.info("删除不连续的PID数据,PID:%s" %piddata['wiopstop'][pidc])
                            del piddata['wiopstop'][pidc]
                except KeyError, msg:
                    piddata['wiopstop'] = {}
                    logging.error("----- wiopstop 还没有建立 ----- %s" %msg)

                for pi in wiops:
                    if pi in piddata['wiopstop'].keys():
                        piddata['wiopstop'][pi] += 1
                    else:
                        piddata['wiopstop'][pi] = 1

                if max(piddata['wiopstop'].values()) > 5:
                    for toppid, topcount in piddata['wiopstop'].items():
                        if topcount > 5:
                            J_zabbix(toppid, topcount,'写IOPS超过')
                else:
                    logging.info("发送写IOPS,ok消息")
                    J_zabbix('Ok', 'Ok','写IOPS超过')
            else:
                logging.info("发送写IOPS,ok消息")
                J_zabbix('Ok', 'Ok','写IOPS超过')

            if len(rb) > 0:
                try:
                    for pidc in piddata['rttop'].keys():
                        if pidc in rb:
                            pass
                        else:
                            logging.info("删除不连续的PID数据,PID:%s" %piddata['rttop'][pidc])
                            del piddata['rttop'][pidc]
                except KeyError,msg:
                    piddata['rttop'] = {}
                    logging.error("----- rttop 还没有建立 ----- %s" %msg)

                for pi in rb:
                    if pi in piddata['rttop'].keys():
                        piddata['rttop'][pi] += 1
                    else:
                        piddata['rttop'][pi] = 1

                if max(piddata['rttop'].values()) > 5:
                    for toppid, topcount in piddata['rttop'].items():
                        if topcount > 5:
                            J_zabbix(toppid, topcount,'读字节')
                else:
                    logging.info("发送读字节ok消息")
                    J_zabbix('Ok', 'Ok','读字节')
            else:
                logging.info("发送读字节ok消息")
                J_zabbix('Ok', 'Ok','读字节')

            if len(wb) > 0:
                try:
                    for pidc in piddata['wttop'].keys():
                        if pidc in wb:
                            pass
                        else:
                            logging.info("删除不连续的PID数据,PID:%s" %piddata['wttop'][pidc])
                            del piddata['wttop'][pidc]
                except KeyError,msg:
                    piddata['wttop'] = {}
                    logging.error("----- wttop 还没有建立 ----- %s" %msg)

                for pi in wb:
                    if pi in piddata['wttop'].keys():
                        piddata['wttop'][pi] += 1
                    else:
                        piddata['wttop'][pi] = 1

                if max(piddata['wttop'].values()) > 5:
                    for toppid, topcount in piddata['wttop'].items():
                        print "写字节pid:%s, 连续性:%s" %(toppid,topcount)
                        if topcount > 5:
                            print "进入到写字节"
                            J_zabbix(toppid, topcount,'写字节')
                else:
                    logging.info("发送写字节ok消息")
                    J_zabbix('Ok', 'Ok','写字节')
            else:
                logging.info("发送写字节ok消息")
                J_zabbix('Ok', 'Ok','写字节')

            logging.info(ending)
            time.sleep(1)

if __name__ == '__main__':
    import sys
    ending = "-" * 25 + "compare end" + "-" * 25 + "\n"
    daemon = MyDaemon('/tmp/checkio.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
