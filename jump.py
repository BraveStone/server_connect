#!/usr/bin/env python
# coding:utf-8

import os
import sys

'''
host 格式
第一行描述
后面每一行代表一台机器，格式为 描述,host,user,

如：
 xxxx节点
computer1,host1,user1,
computer2,host2,user2,
computer3,host3,user3,
'''
host_dic = {}
user_dic = {}
display_dic = {}

desc = ''


def readData():
    global display_dic, host_dic, user_dic, desc
    ip_file = sys.argv[1]
    f = file(ip_file)
    num = 0
    bFir = True
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if bFir:
            desc = line
            bFir = False
            continue

        vec = line.split(',')
        num += 1
        display_dic[num] = vec[0]
        host_dic[num] = vec[1]
        user_dic[num] = vec[2]
    f.close()


def main1():
    global display_dic, host_dic, user_dic, desc
    while True:
        try:
            os.system('clear')
            print '\033[1;35m \
    ==============================================================================\n \
                            %s \
    ============================================================================== \033[0m' % desc
            for a, b in display_dic.items():
                print '%02d: %s     %s\n' % (a, b, host_dic[a]),

            option = int(
                raw_input('\nplease choose one server to connect:'))
            if option in host_dic.keys():
                cmd = 'ssh %s@%s' % (user_dic[option], host_dic[option])
                print cmd
                os.system(cmd)
            else:
                print 'Input error!'
        except ValueError:
            print 'Wrong value!'


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print 'please input host files'
    else:
        readData()
        main1()
