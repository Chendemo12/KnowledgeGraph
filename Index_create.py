# -*- coding: utf-8 -*-
# @Author: Li Chenguang
# @Email:  chendemo12@gmail.com
# @Date:   2019-09-24
# @Last Modified by:   chendemo12
# @Last Modified time: 2019-09-24

import html2text
import os
import get_FileInfo as F


def index_create():
    """
    生成  Index.md 文件
    # get_FileInfo返回文档信息字典
    info_dict['create_time']：创建时间
    info_dict['last_modified_time']：最后修改时间
    info_dict['file_size']：文件大小
    """

    base_url = "https://github.com/Chendemo12/KnowledgeGraph/wiki/"
    path = os.getcwd() + "\\KnowledgeGraph.wiki\\"
    filename = path + "_Index.md"
    md_files = []
    local = "LOCAL"

    files = os.listdir(path)  # 获取当前目录下的所有文件
    for file in files:
        if ".md" in file and "_" not in file:
            md_files.append(file)    # 获取markdown文件

    f = open(filename, "w", encoding="utf")

    f.write("# Index 目录导航\n\n")
    f.write("| 网络地址 | 本地地址 | 修改时间 | 文件大小 |\n")
    f.write("| :-- | :-: | :-: | :-: |\n")
    for file in md_files:
        filepath = path + file
        fi = F.fileInfo(filepath)
        info = fi.get_FileInfo()
        file = file.replace(" ", "-")
        full_url = base_url + file.replace(".md", "")
        # f.write("[{}]({})".format(file,full_url))
        # f.write("\n\n")

        f.write("| [{}]({}) | [{}]({}) | {} | {} |\n".format(
            file, full_url, local, filepath, info['last_modified_time'], info['file_size']))
    f.close()


if __name__ == "__main__":

    index_create()
