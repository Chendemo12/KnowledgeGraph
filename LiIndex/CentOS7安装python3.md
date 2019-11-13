## 新装的CentOS 7安装python3

centos7 自带有 python，但是却是 python2 版本的 python，如果你想安装个python3怎么办呢？难道要从github上把源码clone下来进行编译安装么？没错！因为 yum 源中并没有现成的 python3 程序，所以必须要自己手动编译安装。

但是你也不用害怕，跟着我的步骤往下走，相信我，你也会在 centos7 上轻松的装上 python3 的。

### 1.首先，你要知道系统现在的python的位置在哪儿：

```bash 
[root@root ~]# whereis python
python: /usr/bin/python2.7 /usr/bin/python /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /usr/share/man/man1/python.1.gz12
```

可以知道我们的python在 /usr/bin目录中

```bash
[root@root ~]# cd /usr/bin/
[root@root bin]# ll python*
lrwxrwxrwx. 1 root root    7 2月   7 09:30 python -> python2
lrwxrwxrwx. 1 root root    9 2月   7 09:30 python2 -> python2.7
-rwxr-xr-x. 1 root root 7136 8月   4 2017 python2.712345
```

可以看到，python指向的是python2，python2指向的是python2.7，因此我们可以装个python3，然后将python指向python3，然后python2指向python2.7，那么两个版本的python就能共存了。

### 2.因为我们要安装python3，所以要先安装相关包，用于下载编译python3：

```bash
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
```


运行了以上命令以后，就安装了编译python3所用到的相关依赖

### 3.默认的，centos7也没有安装pip，不知道是不是因为我安装软件的时候选择的是最小安装的模式。

```bash
#运行这个命令添加epel扩展源
yum -y install epel-release

#安装pip
yum install python-pip12345
```

### 4.用pip装wget

```bash
pip install wget1
```

### 5.用wget下载python3的源码包

```bash
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz1
```

### 6.编译python3源码包

```bash
#解压
xz -d Python-3.6.4.tar.xz
tar -xf Python-3.6.4.tar

#进入解压后的目录，依次执行下面命令进行手动编译
./configure prefix=/usr/local/python3
make && make install1234567
```

如果最后没提示出错，就代表正确安装了，在/usr/local/目录下就会有python3目录

### 7.添加软链接

```bash
#将原来的链接备份
mv /usr/bin/python /usr/bin/python.bak

#添加python3的软链接
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python

#测试是否安装成功了
python -V12345678
```

### 8.更改yum配置，因为其要用到python2才能执行，否则会导致yum不能正常使用

```bash
vi /usr/bin/yum
把#! /usr/bin/python修改为#! /usr/bin/python2

vi /usr/libexec/urlgrabber-ext-down
把#! /usr/bin/python 修改为#! /usr/bin/python2
```