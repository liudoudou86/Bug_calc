#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import data


# 集成测试的质量等级计算
def jccs_x():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 30 < bug_jccs <= 100:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 20 < bug_jccs <= 30:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 10 < bug_jccs <= 20:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 10:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break

def jccs_z():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 40 < bug_jccs <= 100:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 30 < bug_jccs <= 40:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 20 < bug_jccs <= 30:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 20:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break

def jccs_jd():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 50 < bug_jccs <= 100:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 40 < bug_jccs <= 50:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 30 < bug_jccs <= 40:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 30:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break

def jccs_d():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 120 < bug_jccs <= 150:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 100 < bug_jccs <= 120:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 80 < bug_jccs <= 100:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 80:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break

def jccs_td():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 180 < bug_jccs <= 240:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 150 < bug_jccs <= 180:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 100 < bug_jccs <= 150:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 100:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break

def jccs_cd():
    while True:
        bug_jccs = (data.cs.fatal_jccs()*15)+(data.cs.serious_jccs()*1.5)+(data.cs.general_jccs()*0.3)+(data.cs.slight_jccs()*0)
        if 200 < bug_jccs <= 300:
            print("bug值:",bug_jccs)
            print("质量等级:D")
            break
        elif 180 < bug_jccs <= 200:
            print("bug值:",bug_jccs)
            print("质量等级:C")
            break
        elif 120 < bug_jccs <= 180:
            print("bug值:",bug_jccs)
            print("质量等级:B")
            break
        elif 0 < bug_jccs <= 120:
            print("bug值:",bug_jccs)
            print("质量等级:A")
            break
        else:
            print("bug值:",bug_jccs)
            print("质量等级超出范围")
            break
