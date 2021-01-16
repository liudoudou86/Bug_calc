#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import data


# 正式测试开发评审的质量等级计算
def zscs_kfps_x():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 10:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 10 < bug_kfps < 30:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 5 < bug_kfps <= 10:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 1 < bug_kfps <= 5:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 1 < bug_kfps <= 1:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break

def zscs_kfps_z():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 20:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 20 < bug_kfps < 50:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 10 < bug_kfps <= 20:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 3 < bug_kfps <= 10:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 3:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break

def zscs_kfps_jd():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 30:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 30 < bug_kfps < 100:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 20 < bug_kfps <= 30:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 5 < bug_kfps <= 20:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 5:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break

def zscs_kfps_d():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 40:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 50 < bug_kfps < 120:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 30 < bug_kfps <= 50:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 10 < bug_kfps <= 30:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 10:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break

def zscs_kfps_td():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 50:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 80 < bug_kfps < 150:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 50 < bug_kfps <= 80:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 20 < bug_kfps <= 50:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 20:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break

def zscs_kfps_cd():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 50:
            print("bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 80 < bug_kfps < 150:
            print("bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 50 < bug_kfps <= 80:
            print("bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 20 < bug_kfps <= 50:
            print("bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 20:
            print("bug值:",bug_kfps)
            print("质量等级:A")
            break
