# -*- encoding: utf-8 -*-
# @Author  :  LiChenguang
# @Data  :  2019-09-24
# @Email  :  chendemo12@gmail.com
# @sys  :  elementary OS
# @WebSite  :  www.searcher.ltd
# @Last Modified time  :  2019/11/10


import os
import get_FileInfo as F


def web_indexCreate(folder):
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

    files = os.listdir(path)  # 获取当前目录下的所有文件
    for file in files:
        if ".md" in file and "_" not in file:
            md_files.append(file)    # 获取markdown文件

    with open(indexfile, "w", encoding="utf-8") as f:
        f.write("# {} 目录导航\n\n".format(folder))
        f.write("| 网络地址  | 修改时间 | 文件大小KB |\n")
        f.write("| :-- | :-: | :-: |\n")

        for file in md_files:
            filepath = path + file
            fi = F.fileInfo(filepath)
            info = fi.get_FileInfo()
            file = file.replace(" ", "-")
            full_url = base_url + file.replace(".md", "")

            f.write("| [{}]({}) | {} | {} |\n".format(
                file, full_url, info['last_modified_time'], info['file_size']))


def web_homeIndex():
    """
    创建所有文件索引_Index.md
    """

    # 清空_Index.md文件
    with open("_Index.md", 'w', encoding='utf-8') as ind:
        ind.write("\n")

    folders = ["PyIndex", "MyIndex", "LiIndex"]
    for fo in folders:
        index_file = os.getcwd() + "//{}//_{}.md".format(fo, fo)
        with open(index_file, 'r', encoding='utf-8') as f:
            text = f.read()
        with open("_Index.md", 'a', encoding='utf-8') as ind:
            ind.write(text)


def local_indexCreate(folder):

    base_url = "https://github.com/Chendemo12/KnowledgeGraph/wiki/"
    path = os.getcwd() + "//" + folder + "//"
    indexfile = path + "{}.md".format(folder)
    md_files = []
    local = "LOCAL"

    # 获取当前目录下的所有md文件
    for file in os.listdir(path):
        if ".md" in file and "_" not in file:
            md_files.append(file)    # 获取markdown文件

    with open(indexfile, "w", encoding="utf-8") as f:
        f.write("# {} 目录导航\n\n".format(folder))
        f.write("| 网络地址 | 本地地址 | 修改时间 | 文件大小KB |\n")
        f.write("| :-- | :-: | :-: | :-: |\n")

    for file in md_files:
        filepath = path + file
        fi = F.fileInfo(filepath)
        info = fi.get_FileInfo()
        file = file.replace(" ", "-")
        full_url = base_url + file.replace(".md", "")

        f.write("| [{}]({}) | [{}]({}) | {} | {} |\n".format
            (file,full_url, local, filepath, info['last_modified_time'],
                info['file_size']))


def local_homeIndex():
    # 清空Index.md文件

    with open("Index.md", 'w', encoding='utf-8') as ind:
        ind.write("\n")

    folders = ["PyIndex", "MyIndex", "LiIndex"]
    for fo in folders:
        index_file = os.getcwd() + "//{}//{}.md".format(fo, fo)
        with open(index_file, 'r', encoding='utf-8') as f:
            text = f.read()
        with open("Index.md", 'a', encoding='utf-8') as ind:
            ind.write(text)



if __name__ == "__main__":

    indexfiles = ["PyIndex", "MyIndex", "LiIndex"]
    print("*****1、更新网络索引文件\n*****2、更新本地索引文件\n")

    num = int(input("——请输入序号选择操作:"))

    if num == 1:
        print("\n****************更新网络索引文件****************")
        for indexfile in indexfiles:
            web_indexCreate(indexfile)
            print("——{}.md已更新".format(indexfile))

        web_homeIndex()
        print("——{}已更新".format("Index.md"))

    else:
        print("\n****************更新本地索引文件****************")
        for indexfile in indexfiles:
            local_indexCreate(indexfile)
            print("——{}.md已更新".format(indexfile))

        local_homeIndex()
        print("——{}已更新".format("Index.md"))

