#!/bin/bash

######author:chenjunxiong#######
######�����޸Ľű���֪ͨ����##########

export JAVA_HOME="/app/jsdk1.8"
export JAVA_BIN="$JAVA_HOME/bin"
export PATH="$JAVA_BIN:$PATH"
export LANG="zh_CN.GBK"


trap 'if [[ `ps aux |grep -i $1 |wc -l` -ge 2 ]]; then echo -e "\033[34;1m ����ִ�����......\033[0m"; else echo -e "\033[1;31;5m $1 ��������ִ��ʧ�ܣ�����Ӧ��.......\033[0m \a"; fi' 2

all_stop()
    {
        $JAVA_BIN/java -jar /app/resin/lib/resin.jar -conf /app/resin/conf/o2oboss.conf -server o2oboss stop
        Returned_Value
        $JAVA_BIN/java -jar /app/resin/lib/resin.jar -conf /app/resin/conf/webrwjk.conf -server webrwjk stop
        Returned_Value
        cd /app/yxpt1.0/monited/sbin/;./xstop.sh
        Returned_Value
        cd /app/yxpt1.0/qdserver/sbin/;./xstop.sh
        Returned_Value
    }

all_start()
    {
        $JAVA_BIN/java -jar /app/resin/lib/resin.jar -conf /app/resin/conf/o2oboss.conf -server o2oboss start
        Returned_Value
        $JAVA_BIN/java -jar /app/resin/lib/resin.jar -conf /app/resin/conf/webrwjk.conf -server webrwjk start
        Returned_Value
        cd /app/yxpt1.0/monited/sbin/;./start.sh -xp
        Returned_Value
        cd /app/yxpt1.0/qdserver/sbin/;./start.sh -xp
        Returned_Value
    }

Returned_Value()
    {
	   sleep 10
        if [ "$?" -eq 0 ];
            then
                echo -e "\033[34;1m $1 ��������ִ�гɹ�........\033[0m"
        else
                echo -e "\033[1;31;5m $1 ��������ִ��ʧ�ܣ�����Ӧ��.......\033[0m \a"
        fi
    }

resin_Returned_Value()
    {
	   sleep 3
	   if [[ `grep "Can't start new task because of old task" /tmp/AppStartAndStop.log` =~ "Can't start new task because of old task" ]];
	   then
	       echo -e "\033[1;31;5m $1 �������������У�����Ӧ��.......\033[0m \a"
	   elif [[ `grep "ConnectException" /tmp/AppStartAndStop.log` =~ "ConnectException" ]];
	   then
	       echo -e "\033[1;31;5m $1 ����ֹͣ������Ӧ��.......\033[0m \a"
	   else
	       echo -e "\033[34;1m $1 ��������ִ�гɹ�........\033[0m"
        fi
    }

help_info()
    {
        echo -e "\033[1;35m ����˵����
        |o2oboss ����|ֹͣ��o2oboss start|stop|status|restart
        |webrwjk ����|ֹͣ��webrwjk start|stop|status|restart
        |monited ����|ֹͣ��monited start|stop
        |qdserver����|ֹͣ��qdserver start|stop
        |lxserver����|ֹͣ��lxserver start|stop
        |����all start �� ��������Ӧ�ã��������־�������в鿴ÿ��Ӧ�õ���־��
        |����all stop  �� ֹͣ����Ӧ�ã��������־�������в鿴ÿ��Ӧ�õ���־��\033[0m"  
    }

Resin_App_Start_Stop()
    {
        if [ "$2" = "start" ]; then
    	   echo -e "\033[34;1m �������� $1�������ĵȴ�......\033[0m"
        elif [ "$2" = "stop" ]; then
    	   echo -e "\033[34;1m ����ֹͣ $1�������ĵȴ�......\033[0m"
        elif [ "$2" = "restart" ]; then
    	   echo -e "\033[34;1m �������� $1�������ĵȴ�......\033[0m"
        fi
        nohup $JAVA_BIN/java -jar /app/resin/lib/resin.jar -conf /app/resin/conf/$1.conf -server $1 $2 >/tmp/AppStartAndStop.log 2>&1 &
    }

App_logs_path()
    {
        sleep 3
        if [ "$1" = "o2oboss" -o "$1" = "webrwjk" ]; then
            tail -f /app/resin/log/jvm-$1.log
        elif [ "$1" = "qdserver" ]; then
            tail -f /app/yxpt1.0/monited/main/logs/ttyout/`date +%Y-%m-%d`.H`date +%H`
        elif [ "$1" = "monited" ]; then
            tail -f /app/yxpt1.0/monited/main/logs/ttyout/`date +%Y-%m-%d`.log
        elif [[ "$1" = "lxserver" ]]; then
            tail -f /app/yxpt1.0/HD/lxserver/main/logs/ttyout/`date +%Y-%m-%d`.log
        fi
    }

if [ "$1" = "all" -a "$2" = "stop" ];
then
        all_stop

elif [ "$1" = "all" -a "$2" = "start" ];
then
        all_start

elif [ -e "/app/resin/conf/$1.conf" -o -e "/app/yxpt1.0/$1/sbin/$2.sh" -o -e "/app/yxpt1.0/$1/sbin/x$2.sh" ];
then
        case "$2" in
            Start|start)
                if [[ -e "/app/yxpt1.0/$1/sbin/$2.sh" ]]; then
                    echo -e "\033[34;1m �������� $1�������ĵȴ�......\033[0m"
                    cd /app/yxpt1.0/$1/sbin; ./$2.sh -xp
                    Returned_Value $1
                    App_logs_path $1
                elif [[ -e "/app/yxpt1.0/HD/$1/sbin/$2.sh" ]]; then
                    cd /app/yxpt1.0/HD/$1/sbin; ./$2.sh -xp
                    Returned_Value $1
                    App_logs_path $1
                else
                    Resin_App_Start_Stop $1 $2
                    resin_Returned_Value $1
                    App_logs_path $1
                fi
                 ;;
            Stop|stop)
                if [[ -e "/app/yxpt1.0/$1/sbin/x$2.sh" ]]; then
                    echo -e "\033[34;1m ����ֹͣ $1�������ĵȴ�......\033[0m"
                    cd /app/yxpt1.0/$1/sbin; ./x$2.sh
                    Returned_Value $1
                    App_logs_path $1
                elif [[ -e "/app/yxpt1.0/HD/$1/sbin/x$2.sh" ]]; then
                    cd /app/yxpt1.0/HD/lxserver/sbin; ./x$2.sh
                    Returned_Value $1
                    App_logs_path $1
                else
                    Resin_App_Start_Stop $1 $2
                    resin_Returned_Value $1
                    App_logs_path $1
                fi
                ;;
            Status|status):
                Resin_App_Start_Stop $1 $2
                Returned_Value $1
                ;;
            Restart|restart):
                Resin_App_Start_Stop $1 $2
                resin_Returned_Value $1
                App_logs_path $1
                ;;
            *):
                help_info
                ;;
        esac
else
        help_info
fi
