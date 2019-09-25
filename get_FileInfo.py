# -*- coding: utf-8 -*-
# @Author: Li Chenguang
# @Email:  chendemo12@gmail.com
# @Date:   2019-09-24
# @Last Modified by:   chendemo12
# @Last Modified time: 2019-09-24
# -*- coding: UTF8 -*-

import time
import os


class fileInfo():
    """
    获取文件的属性信息
    filepath：文件路径
    """

    def __init__(self,filepath):
        # 初始化

        self.filepath = filepath
        self.info = os.stat(filepath)
        self.info_dict = {}


    def TimeStampToTime(self,timestamp):
        # 把时间戳转化为时间: 1479264792 to 2016-11-16

        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d',timeStruct)


    def get_FileInfo(self):
        # 获取文件属性信息

        create_time = str(self.TimeStampToTime(self.info.st_ctime))
        last_modified_time = str(self.TimeStampToTime(self.info.st_mtime))
        file_size = str(round(self.info.st_size/1024,2) )    #单位kb,2位小数

        self.info_dict['create_time'] = create_time
        self.info_dict['last_modified_time'] = last_modified_time
        self.info_dict['file_size'] = file_size

        return self.info_dict


if __name__ == '__main__':

    filepath = os.getcwd() + "\\KnowledgeGraph.wiki\\Git.md"
    fi = fileInfo(filepath)
    info = fi.get_FileInfo()
    print(info)
