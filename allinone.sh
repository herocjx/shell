#!/bin/bash

######author:chenjunxiong#######
######如需修改脚本请通知作者##########

export JAVA_HOME="/app/jsdk1.8"
export JAVA_BIN="$JAVA_HOME/bin"
export PATH="$JAVA_BIN:$PATH"
export LANG="zh_CN.GBK"


trap 'if [[ `ps aux |grep -i $1 |wc -l` -ge 2 ]]; then echo -e "\033[34;1m 命令执行完成......\033[0m"; else echo -e "\033[1;31;5m $1 服务命令执行失败，请检查应用.......\033[0m \a"; fi' 2

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
                echo -e "\033[34;1m $1 服务命令执行成功........\033[0m"
        else
                echo -e "\033[1;31;5m $1 服务命令执行失败，请检查应用.......\033[0m \a"
        fi
    }

resin_Returned_Value()
    {
	   sleep 3
	   if [[ `grep "Can't start new task because of old task" /tmp/AppStartAndStop.log` =~ "Can't start new task because of old task" ]];
	   then
	       echo -e "\033[1;31;5m $1 己经正在运行中，请检查应用.......\033[0m \a"
	   elif [[ `grep "ConnectException" /tmp/AppStartAndStop.log` =~ "ConnectException" ]];
	   then
	       echo -e "\033[1;31;5m $1 己经停止，请检查应用.......\033[0m \a"
	   else
	       echo -e "\033[34;1m $1 服务命令执行成功........\033[0m"
        fi
    }

help_info()
    {
        echo -e "\033[1;35m 参数说明：
        |o2oboss 启动|停止：o2oboss start|stop|status|restart
        |webrwjk 启动|停止：webrwjk start|stop|status|restart
        |monited 启动|停止：monited start|stop
        |qdserver启动|停止：qdserver start|stop
        |lxserver启动|停止：lxserver start|stop
        |输入all start ： 启动所有应用，不输出日志，请自行查看每个应用的日志。
        |输入all stop  ： 停止所有应用，不输出日志，请自行查看每个应用的日志。\033[0m"  
    }

Resin_App_Start_Stop()
    {
        if [ "$2" = "start" ]; then
    	   echo -e "\033[34;1m 正在启动 $1，请耐心等待......\033[0m"
        elif [ "$2" = "stop" ]; then
    	   echo -e "\033[34;1m 正在停止 $1，请耐心等待......\033[0m"
        elif [ "$2" = "restart" ]; then
    	   echo -e "\033[34;1m 正在重启 $1，请耐心等待......\033[0m"
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
                    echo -e "\033[34;1m 正在启动 $1，请耐心等待......\033[0m"
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
                    echo -e "\033[34;1m 正在停止 $1，请耐心等待......\033[0m"
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
