#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import data


# 定版集成开发评审的质量等级计算
def dbjc_kfps_x():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 30:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 10 < bug_kfps < 30:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 5 < bug_kfps <= 10:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 1 < bug_kfps <= 5:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 1 < bug_kfps <= 1:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break

def dbjc_kfps_z():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 50:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 20 < bug_kfps < 50:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 10 < bug_kfps <= 20:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 3 < bug_kfps <= 10:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 3:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break

def dbjc_kfps_jd():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 100:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 30 < bug_kfps < 100:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 20 < bug_kfps <= 30:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 5 < bug_kfps <= 20:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 5:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break

def dbjc_kfps_d():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 120:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 50 < bug_kfps < 120:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 30 < bug_kfps <= 50:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 10 < bug_kfps <= 30:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 10:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break

def dbjc_kfps_td():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 150:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 80 < bug_kfps < 150:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 50 < bug_kfps <= 80:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 20 < bug_kfps <= 50:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 20:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break

def dbjc_kfps_cd():
    while True:
        bug_kfps = (data.kfps.fatal_kfps()*100)+(data.kfps.serious_kfps()*10)+(data.kfps.general_kfps()*1)+(data.kfps.slight_kfps()*0.1)
        if bug_kfps >= 150:
            print("Bug值:",bug_kfps)
            print("质量等级:不通过")
            break
        elif 80 < bug_kfps < 150:
            print("Bug值:",bug_kfps)
            print("质量等级:D")
            break
        elif 50 < bug_kfps <= 80:
            print("Bug值:",bug_kfps)
            print("质量等级:C")
            break
        elif 20 < bug_kfps <= 50:
            print("Bug值:",bug_kfps)
            print("质量等级:B")
            break
        elif 0 < bug_kfps <= 20:
            print("Bug值:",bug_kfps)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_kfps)
            print("质量等级超出范围")
            break
