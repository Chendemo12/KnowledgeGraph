# -*- coding: utf-8 -*-
# @Author: Li Chenguang
# @Email:  chendemo12@gmail.com
# @Date:   2019-09-24
# @Last Modified by:   chendemo12
# @Last Modified time: 2019-09-24

import os

def clone():
    """克隆远程仓库"""

    with os.popen(r'adb devices', 'r') as f:
        text = f.read()
    return text

def push(message):
    """推送提交更改"""

    os.system('cd D:\\27251\\Documents\\GitHub\\KnowledgeGraph\\KnowledgeGraph.wiki')

    with os.popen(r'git add .', 'r') as f:
        print(f.read())

    with os.popen(r'git commit -m "{}"'.format(str(message)), 'r') as f:
        print(f.read())

    with os.popen(r'git push', 'r') as f:
        print(f.read())

if __name__ == '__main__':

    print("支持的git操作列表：")
    print("\n\t\t1、克隆远程仓库\n\t\t2、提交本地更改\n")
    num  = int(input("请输入操作序号："))

    if num == 1:
        clone()
    elif num == 2:
        push()

    else:
        print("输入错误！")
