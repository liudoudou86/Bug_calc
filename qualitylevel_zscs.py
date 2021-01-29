#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import data


# 正式测试的质量等级计算
def zscs_x():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 20 < bug_zscs <= 100:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 10 < bug_zscs <= 20:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 1 < bug_zscs <= 10:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 1:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break

def zscs_z():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 30 < bug_zscs <= 100:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 20 < bug_zscs <= 30:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 5 < bug_zscs <= 20:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 5:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break

def zscs_jd():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 40 < bug_zscs <= 100:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 30 < bug_zscs <= 40:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 10 < bug_zscs <= 30:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 10:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break

def zscs_d():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 70 < bug_zscs <= 120:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 50 < bug_zscs <= 70:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 30 < bug_zscs <= 50:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 30:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break

def zscs_td():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 90 < bug_zscs <= 150:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 60 < bug_zscs <= 90:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 40 < bug_zscs <= 60:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 40:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break

def zscs_cd():
    while True:
        bug_zscs = (data.cs.fatal_zscs()*50)+(data.cs.serious_zscs()*5)+(data.cs.general_zscs()*1)+(data.cs.slight_zscs()*0)
        if 100 < bug_zscs <= 150:
            print("Bug值:",bug_zscs)
            print("质量等级:D")
            break
        elif 70 < bug_zscs <= 100:
            print("Bug值:",bug_zscs)
            print("质量等级:C")
            break
        elif 50 < bug_zscs <= 70:
            print("Bug值:",bug_zscs)
            print("质量等级:B")
            break
        elif 0 < bug_zscs <= 50:
            print("Bug值:",bug_zscs)
            print("质量等级:A")
            break
        else:
            print("Bug值:",bug_zscs)
            print("质量等级超出范围")
            break
