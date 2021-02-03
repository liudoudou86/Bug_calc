#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import re
import os
import pymysql


def gateway():
    # 粗略找IP地址的正则表达式，包括掩码在内一起找
    pr = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    # 通过默认路由得到网关地址，可能存在多条，但只取第一条[0]，通过正则找IP得到的列表第三个元素就是网关[2]
    gw = re.findall(pr,os.popen('route print | find " 0.0.0.0 "').read().strip().split('\n')[0])[2]
    # 向网关发udp请求包，避免无脑的随意udp包游荡在内网中，通过udp的ip头部获取到发包的源地址，也就是本机生产地址
    wg = (gw[:-5])
    if wg == '192.168':
        ip_cs = str('192.168.25.247')
        return ip_cs
    else:
        ip_gz = str('10.30.12.247')
        return ip_gz

info = gateway()
# print(info)

project = str(input("请输入项目名称："))
start = str(input("请输入开发评审开始时间：")) + ' 00:00:00'
end = str(input("请输入开发评审结束时间：")) + ' 23:59:59'

class kfps():

    def fatal_kfps():
        # 连接到mysql数据库
        # TODO：项目：XM20200317_监察委执纪监督V2.0T
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        # 创建游标对象
        cursor = conn.cursor()
        # sql语句
        sql_fatal = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE bug_status in ('新提交','问题未解决','待反测的') and name LIKE '%"+project+"%' and lastdiffed between '"+start+"' and '"+end+"' and bug_severity = '致命';"
        # print(sql_fatal)
        # 执行sql语句
        try:
            cursor.execute(sql_fatal)
            result_fatal = cursor.fetchone()
            for fatal in result_fatal:
                print("致命:",fatal,"个")
            return fatal
        except:
            print("数据库异常_致命")
        # 关闭游标
        cursor.close()
        # 关闭数据库
        conn.close()

    def serious_kfps():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_serious = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE bug_status in ('新提交','问题未解决','待反测的') and name LIKE '%"+project+"%' and lastdiffed Between '"+start+"' AND '"+end+"' and bug_severity = '严重';"
        try:
            cursor.execute(sql_serious)
            result_serious = cursor.fetchone()
            for serious in result_serious:
                print("严重:",serious,"个")
            return serious
        except:
            print("数据库异常_严重")
        cursor.close()
        conn.close()

    def general_kfps():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_general = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE bug_status in ('新提交','问题未解决','待反测的') and name LIKE '%"+project+"%' and lastdiffed Between '"+start+"' AND '"+end+"' and bug_severity = '一般';"
        try:
            cursor.execute(sql_general)
            result_general = cursor.fetchone()
            for general in result_general:
                print("一般:",general,"个")
            return general
        except:
            print("数据库异常_一般")
        cursor.close()
        conn.close()

    def slight_kfps():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_slight = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE bug_status in ('新提交','问题未解决','待反测的') and name LIKE '%"+project+"%' and lastdiffed Between '"+start+"' AND '"+end+"' and bug_severity = '轻微';"
        try:
            cursor.execute(sql_slight)
            result_slight = cursor.fetchone()
            for slight in result_slight:
                print("轻微:",slight,"个")
            return slight
        except:
            print("数据库异常_轻微")
        cursor.close()
        conn.close()

class cs():

    def fatal_jccs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_fatal = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('定版集成','定版集成（二）') and name LIKE '%"+project+"%' and bug_severity = '致命';"
        try:
            cursor.execute(sql_fatal)
            result_fatal = cursor.fetchone()
            for fatal in result_fatal:
                print("致命:",fatal,"个")
            return fatal
        except:
            print("数据库异常_致命")
        cursor.close()
        conn.close()

    def serious_jccs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_serious = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('定版集成','定版集成（二）') and name LIKE '%"+project+"%' and bug_severity = '严重';"
        try:
            cursor.execute(sql_serious)
            result_serious = cursor.fetchone()
            for serious in result_serious:
                print("严重:",serious,"个")
            return serious
        except:
            print("数据库异常_严重")
        cursor.close()
        conn.close()

    def general_jccs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_general = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('定版集成','定版集成（二）') and name LIKE '%"+project+"%' and bug_severity = '一般';"
        try:
            cursor.execute(sql_general)
            result_general = cursor.fetchone()
            for general in result_general:
                print("一般:",general,"个")
            return general
        except:
            print("数据库异常_一般")
        cursor.close()
        conn.close()

    def slight_jccs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_slight = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('定版集成','定版集成（二）') and name LIKE '%"+project+"%' and bug_severity = '轻微';"
        try:
            cursor.execute(sql_slight)
            result_slight = cursor.fetchone()
            for slight in result_slight:
                print("轻微:",slight,"个")
            return slight
        except:
            print("数据库异常_轻微")
        cursor.close()
        conn.close()

    def fatal_zscs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_fatal = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('正式测试（一）','正式测试（二）','正式测试（三及以后）') and name LIKE '%"+project+"%' and bug_severity = '致命';"
        try:
            cursor.execute(sql_fatal)
            result_fatal = cursor.fetchone()
            for fatal in result_fatal:
                print("致命:",fatal,"个")
            return fatal
        except:
            print("数据库异常_致命")
        cursor.close()
        conn.close()

    def serious_zscs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_serious = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('正式测试（一）','正式测试（二）','正式测试（三及以后）') and name LIKE '%"+project+"%' and bug_severity = '严重';"
        try:
            cursor.execute(sql_serious)
            result_serious = cursor.fetchone()
            for serious in result_serious:
                print("严重:",serious,"个")
            return serious
        except:
            print("数据库异常_严重")
        cursor.close()
        conn.close()

    def general_zscs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_general = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('正式测试（一）','正式测试（二）','正式测试（三及以后）') and name LIKE '%"+project+"%' and bug_severity = '一般';"
        try:
            cursor.execute(sql_general)
            result_general = cursor.fetchone()
            for general in result_general:
                print("一般:",general,"个")
            return general
        except:
            print("数据库异常_一般")
        cursor.close()
        conn.close()

    def slight_zscs():
        conn = pymysql.connect(host=info, user='report', password='report', port=3306, db='bugs', charset='UTF8')
        cursor = conn.cursor()
        sql_slight = "SELECT count(*) FROM bugs INNER JOIN products ON bugs.product_id = products.id WHERE cf_tijiaojieduan in ('正式测试（一）','正式测试（二）','正式测试（三及以后）') and name LIKE '%"+project+"%' and bug_severity = '轻微';"
        try:
            cursor.execute(sql_slight)
            result_slight = cursor.fetchone()
            for slight in result_slight:
                print("轻微:",slight,"个")
            return slight
        except:
            print("数据库异常_轻微")
        cursor.close()
        conn.close()
