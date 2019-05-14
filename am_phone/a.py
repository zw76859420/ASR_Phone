# -*- coding:utf-8 -*-
# author:zhangwei

filepath = '/home/zhangwei/stcmds_words.txt'

with open(filepath, 'r') as fr:
    with open('/home/zhangwei/stcmds_space.txt', 'w') as fw:
        lines = fr.readlines()
        for line in lines:
            res = line.strip('\n').split(' ')
            label = " ".join(res[1])
            fw.write(res[0] + " " + label + '\n')

