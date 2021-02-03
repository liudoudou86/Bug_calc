#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import qualitylevel_kfps_dbjc
import qualitylevel_kfps_zscs
import qualitylevel_jccs
import qualitylevel_zscs
import os

# 开发评审的菜单
def menu_kfps():
    while True:
        print('''
        ===================
        1. 集成测试开发评审
        2. 正式测试开发评审
        ===================
        ''')
        choice = int(input('你选择：'))
        if choice == 1:
            grade_kfps_dbjc()
            break
        else:
            grade_kfps_zscs()
            break

# 项目规模的菜单
def grade():
    print('''
    ===================
    1. 项目规模-小
    2. 项目规模-中
    3. 项目规模-较大
    4. 项目规模-大
    5. 项目规模-特大
    6. 项目规模-超大
    ===================
    ''')

# 正式测试的菜单
def grade_zscs():
    while True:
        grade()
        choice = int(input('你选择：'))
        if choice == 1:
            qualitylevel_zscs.zscs_x()
            break
        elif choice == 2:
            qualitylevel_zscs.zscs_z()
            break
        elif choice == 3:
            qualitylevel_zscs.zscs_jd()
            break
        elif choice == 4:
            qualitylevel_zscs.zscs_d()
            break
        elif choice == 5:
            qualitylevel_zscs.zscs_td()
            break
        else:
            qualitylevel_zscs.zscs_cd()
            break

# 集成测试的菜单
def grade_jccs():
    while True:
        grade()
        choice = int(input('你选择：'))
        if choice == 1:
            qualitylevel_jccs.jccs_x()
            break
        elif choice == 2:
            qualitylevel_jccs.jccs_z()
            break
        elif choice == 3:
            qualitylevel_jccs.jccs_jd()
            break
        elif choice == 4:
            qualitylevel_jccs.jccs_d()
            break
        elif choice == 5:
            qualitylevel_jccs.jccs_td()
            break
        else:
            qualitylevel_jccs.jccs_cd()
            break

# 定版集成开发评审的菜单
def grade_kfps_dbjc():
    while True:
        grade()
        choice = int(input('你选择：'))
        if choice == 1:
            qualitylevel_kfps_dbjc.dbjc_kfps_x()
            break
        elif choice == 2:
            qualitylevel_kfps_dbjc.dbjc_kfps_z()
            break
        elif choice == 3:
            qualitylevel_kfps_dbjc.dbjc_kfps_jd()
            break
        elif choice == 4:
            qualitylevel_kfps_dbjc.dbjc_kfps_d()
            break
        elif choice == 5:
            qualitylevel_kfps_dbjc.dbjc_kfps_td()
            break
        else:
            qualitylevel_kfps_dbjc.dbjc_kfps_cd()
            break

#正式测试开发评审的菜单
def grade_kfps_zscs():
    while True:
        grade()
        choice = int(input('你选择：'))
        if choice == 1:
            qualitylevel_kfps_zscs.zscs_kfps_x()
            break
        elif choice == 2:
            qualitylevel_kfps_zscs.zscs_kfps_z()
            break
        elif choice == 3:
            qualitylevel_kfps_zscs.zscs_kfps_jd()
            break
        elif choice == 4:
            qualitylevel_kfps_zscs.zscs_kfps_d()
            break
        elif choice == 5:
            qualitylevel_kfps_zscs.zscs_kfps_td()
            break
        else:
            qualitylevel_kfps_zscs.zscs_kfps_cd()
            break

# 主菜单
def main_menu():
    while True: 
        print('''
        ===================
        1. 开发评审
        2. 集成测试
        3. 正式测试
        ===================
        ''')
        choice = int(input('你选择：'))
        if choice == 1:
            menu_kfps()
            break
        elif choice == 2:
            grade_jccs()
            break
        else:
            grade_zscs()
            break


if __name__ == '__main__':
    main_menu()
    print("===================")
    os.system("pause")
