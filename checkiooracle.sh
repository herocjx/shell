#!/bin/bash

export ORACLE_HOME="/app/oracle/product/1120/dbhome_1"
export ORACLE_BASE="/app/oracle/product/1120"
export NLS_LANG="AMERICAN_AMERICA.ZHS16GBK"
export PATH="/app/oracle/product/1120/dbhome_1/bin:/usr/lib64/qt-3.3/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/oracle/bin:/home/oracle/bin"
export ORACLE_SID="bisys"

sqlplus -S "sys/123456 as SYSDBA" <<EOF
set echo off;
set linesize 30;
select * from (
select e1
  from (select s.SQL_ADDRESS, s.sql_hash_value
          from v\$session s
         where s.PADDR in
               (select p.ADDR from v\$process p where p.SPID = $1)
           and s.STATUS = 'ACTIVE') a,
       (select cast(buffer_gets / decode(EXECUTions, 0, 10000, EXECUTions) as int) a1,
               t.EXECUTions b1,
               t.buffer_gets c1,
               t.disk_reads d1,
               t.sql_text e1,
               t.ADDRESS,
               t.HASH_VALUE,
               t.SQL_ID
          from v\$sqlarea t) b
 where a.SQL_ADDRESS = b.ADDRESS
   and a.sql_hash_value = b.HASH_VALUE
 order by d1 desc)
 where ROWNUM <= 1;
EOF
