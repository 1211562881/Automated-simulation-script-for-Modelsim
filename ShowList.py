######################################################################
#
# 文件名称 : ShowList.py
# 文件作者 : XXX
# 电子邮箱 : XXX
# 修改日期 : 2021/9/26
#
# @ 本 Python 脚本用于自动生成 Verilog 源文件的列表
#
######################################################################

import os
import re

##########################  -Parameter-  ##########################
RelativePath     = True        # 相对路径格式：True为写入相对路径；False为写入绝对路径
PathSlantMode    = True        # 路径斜杠或反斜杠模式设置：True为斜杠(/)；False为反斜杠(\)
VerilogFileLevel = 1           # 当前文件夹相对于仿真工程文件夹相差的层级
###################################################################

PresentPath = os.getcwd()                   # 获取当前路径
os.system("DIR /D . /s /B > FileList.lst")  # 递归查看当前目录下所有文件的绝对路径


ListFp = open('./FileList.lst', 'r')        # 打开 FileList 文件
ListFileAllLines = ListFp.readlines()       # 读取 FileList 的所有内容
ListFp.close()  # 关闭 FileList

LineNum = 0     # Verilog 文件路径所在行数
ListFp = open('./FileList.lst', 'w')        # 打开 FileList 文件
for EachLine in ListFileAllLines:
    LineNum = LineNum + 1
    MatchChar = str(re.findall(r'\.v', EachLine))
    MatchChar = MatchChar.replace('[\'.v\']', str(LineNum))
    if MatchChar != '[]':
        ListFp.writelines(EachLine)
        print(EachLine)

ListFp.close()


if RelativePath == True:
    # 打开修改过的只有 Verilog 文件的 lst
    ListFp = open('./FileList.lst', 'r')        # 打开 FileList 文件
    ListFileAllLines = ListFp.readlines()       # 读取 FileList 的所有内容
    ListFp.close()  # 关闭 FileList

    ListFp = open('./FileList.lst', 'w')        # 打开 FileList 文件
    for EachLine in ListFileAllLines:
        MatchChar = EachLine.replace(PresentPath, '')
        if PathSlantMode == True:
            MatchChar = MatchChar.replace('\\', '/')  # 反斜杠替换成斜杠
        MatchChar = MatchChar.replace(MatchChar, '.' + MatchChar)   # 加上当前路径标识符
        MatchChar = MatchChar.replace(MatchChar, VerilogFileLevel * '../' + MatchChar)
        ListFp.writelines(MatchChar)
        print(MatchChar)

    ListFp.close()




