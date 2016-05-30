#!/usr/bin/python
#coding=gbk

import os,shutil, tarfile, datetime, glob

applogs = [['/app/yxpt1.0/msgsave/main/logs/server/','/logsbackup/msgsave/server/'],
           ['/app/yxpt1.0/msgsave/main/logs/ttyout/','/logsbackup/msgsave/ttyout/'],
           ['/app/yxpt1.0/hd/lxreport/main/logs/server/','/logsbackup/lxreport/server/'],
           ['/app/yxpt1.0/hd/lxreport/main/logs/ttyout/','/logsbackup/lxreport/ttyout/']]

yesterday = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime("%Y%m%d")
year = datetime.datetime.today().strftime("%Y")
month = datetime.datetime.today().strftime("%m")
day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime("%d")

def movefile(s,d):
    # filename = glob.glob(s + yesterday + "*")
    filename = glob.glob(s + year + "*" + month + "*" + day + "." + "*")
    if filename:
        print s + "有需要的日志需要备份， 建立备份目录"
        os.makedirs(d)
    else:
        print s + "没有需要备份的日志"
    for f in filename:
        shutil.move(f, d)
    return True

def tarfiel(s,f):
    if os.path.exists(s + f):
        print s + f + "正在备份目录"
        os.chdir(s)
        tar = tarfile.open(f + '.tar.gz', "w:gz")
        tar.add(f)
        tar.close()
        shutil.rmtree(f)
    else:
        print s + "没有需要备份的日志"

if __name__ == '__main__':
    for logs in applogs:
        x, y = logs[0], logs[1]
        y = y + yesterday
        if movefile(x, y):
            tarfiel(logs[1], yesterday)