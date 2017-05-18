#!/usr/bin python
# -*- coding:utf-8 -*-
'''
m94密码盘解密脚本
根据具体题目修改密码表、秘钥、密文
'''
#加密表
en_table = ['ZWAXJGDLUBVIQHKYPNTCRMOSFE',
'KPBELNACZDTRXMJQOYHGVSFUWI',
'BDMAIZVRNSJUWFHTEQGYXPLOCK',
'RPLNDVHGFCUKTEBSXQYIZMJWAO',
'IHFRLABEUOTSGJVDKCPMNZQWXY',
'AMKGHIWPNYCJBFZDRUSLOQXVET',
'GWTHSPYBXIZULVKMRAFDCEONJQ',
'NOZUTWDCVRJLXKISEFAPMYGHBQ',
'QWATDSRFHENYVUBMCOIKZGJXPL',
'WABMCXPLTDSRJQZGOIKFHENYVU',
'XPLTDAOIKFZGHENYSRUBMCQWVJ',
'TDSWAYXPLVUBOIKZGJRFHENMCQ',
'BMCSRFHLTDENQWAOXPYVUIKZGJ',
'XPHKZGJTDSENYVUBMLAOIRFCQW']
#秘钥
key_content= '2,5,1,3,6,4,9,7,8,14,10,13,11,12'
#密文
cipher = 'HCBTSXWCRQGLES'

key = key_content.split(',')
offset = []
col_count = len(en_table[0])
line_count = len(en_table)
#设置偏移量
for i in range(len(cipher)):
    ind = en_table[int(key[i])-1].index(cipher[i])
    offset.append(ind)
#根据偏移量竖着输出
for i in range(0,col_count):
    content = ""
    for j in range(0,line_count):
        col_index = (int(offset[j]) + i) % col_count
        line_index = int(key[j])-1
        content = content + en_table[line_index][col_index]
    print content
    print