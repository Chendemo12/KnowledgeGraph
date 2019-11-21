## python及库在linux下的目录

[原文链接](https://blog.csdn.net/sodawaterer/article/details/72795468)



在ubuntu下pip需要自行安装

+ 可执行命令`sudo apt-get install python3-pip`安装python3.x的pip，或者`sudo apt-get install python-pip`安装python2.x的pip。

+ 注：安装前最好`sudo apt-get update`一下

+ 可通过pip3 和 pip分别为python3.5和python2.7安装各自的库



pip 包位置

+ python的可执行文件的目录一般在`/usr/bin`下，通过apt-get安装的应用一般会在这个目录；

+ 自行安装的一般在`/usr/local/bin`下；

+ python3.5的自带库目录在`/usr/lib/python3/dist-packages`、`/usr/lib/python3.5/`；
+ python2.7的自带库目录在`/usr/lib/python2.6/dist-packages`、`/usr/lib/python2.7/`；



通过pip安装的模块目录在

+ `~/.local/lib/python3.5/site-packages`

+ `~/.local/lib/python2.7/site-packages`

或者

+ `/usr/local/lib/python2.7/dist-packages`