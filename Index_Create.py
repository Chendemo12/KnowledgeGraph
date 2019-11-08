# -*- coding: utf-8 -*-
# @Author: LiChenguang
# @Date:   2019-09-24
# @Email:  chendemo12@gmail.com
# @sys:    elementary OS
# @Last Modified by:   LiChenguang
# @Last Modified time: 2019-11-08

import os
import get_FileInfo as F


def index_create(folder):
    """
    生成  _**Index.md 文件
    folder：文件保存文件夹
    # get_FileInfo返回文档信息字典
        info_dict['create_time']：创建时间
        info_dict['last_modified_time']：最后修改时间
        info_dict['file_size']：文件大小
    """

    base_url = "https://github.com/Chendemo12/KnowledgeGraph/wiki/"
    path = os.getcwd() + "//" + folder + "//"
    indexfile = path + "_{}.md".format(folder)
    md_files = []
    local = "LOCAL"

    files = os.listdir(path)  # 获取当前目录下的所有文件
    for file in files:
        if ".md" in file and "_" not in file:
            md_files.append(file)    # 获取markdown文件


    with open(indexfile, "w", encoding="utf-8") as f:
        f.write("# {} 目录导航\n\n".format(folder))
        f.write("| 网络地址 | 本地地址 | 修改时间 | 文件大小 |\n")
        f.write("| :-- | :-: | :-: | :-: |\n")
        for file in md_files:
            filepath = path + file
            fi = F.fileInfo(filepath)
            info = fi.get_FileInfo()
            file = file.replace(" ", "-")
            full_url = base_url + file.replace(".md", "")

            f.write("| [{}]({}) | [{}]({}) | {} | {} |\n".format(
                file, full_url, local, filepath, info['last_modified_time'], info['file_size']))


def index_make():
    """
    创建所有文件索引_Index.md
    """

    # 清空_Index.md文件
    with open("_Index.md",'w',encoding = 'utf-8') as ind:
        ind.write("\n")

    folders = ["PyIndex","MyIndex","LiIndex"]
    for fo in folders:
        index_file = os.getcwd() + "//{}//_{}.md".format(fo,fo)
        with open(index_file,'r',encoding = 'utf-8') as f:
            text = f.read()
        with open("_Index.md",'a',encoding = 'utf-8') as ind:
            ind.write(text)



if __name__ == "__main__":

    indexfiles  = ["PyIndex","MyIndex","LiIndex"]
    for indexfile in indexfiles:
        index_create(indexfile)
        print("——{}.md已更新".format(indexfile))

    index_make()
    print("——{}已更新".format("Index.md"))

