#!/usr/bin/python

import os, shutil

applogs = ['/app/yxpt1.0/msgsave/main/logs/',
	'/app/yxpt1.0/synco2o/main/logs/']

def movefile(s,d):
    filename = os.listdir(s)
    for f in filename:
        shutil.move(s + f, d)

def tarfiel(s,f):
    os.chdir(s)
    shutil.make_archive(f, 'gztar', f)
    os.rmdir(f)


if __name__ == '__main__':
    import datetime
    yesterday = datetime.datetime.today()
    for x in applogs:
        movefile(x, '/logsbackup/msgsave/' + yest)
        tarfiel('/logsbackup/msgsave/', yest)

