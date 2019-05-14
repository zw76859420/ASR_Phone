#-*- coding:utf-8 -*-
#author:zhangwei

# with open('/home/zhangwei/PycharmProjects/ASR_Thchs30/data_list_phone/train.syllable.txt', 'r') as fr:
#     dict = []
#     lines = fr.readlines()
#     for line in lines:
#         res = line.split()[1:]
#         for i in res:
#             if i not in dict:
#                 dict.append(i)
#
#     with open('/home/zhangwei/PycharmProjects/ASR_Thchs30/am_phone/dict.txt', 'w') as fw:
#         for j in dict:
#             fw.write(j + '\n')


with open('/home/zhangwei/PycharmProjects/ASR_Thchs30/data_list_phone/test.syllable.txt', 'r') as fr:
    lines = fr.readlines()
    for line in lines:
        res = line.split()[1:]
        if len(res) > 96:
            print(res)
