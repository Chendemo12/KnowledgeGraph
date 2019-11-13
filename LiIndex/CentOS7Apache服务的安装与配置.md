# CentOS 7 Apache服务的安装与配置

[原文链接](https://blog.51cto.com/13525470/2070375)

## 一、Apache简介

Apache 是一个知名的开源Web服务器。
早期的Apache服务器由Apache Group来维护，直到1999年6月Apache Group在美国德拉瓦市成立了非盈利性组织的公司，即Apache软件基金会（Apache Software Foundation，ASF）。
网站需要web服务器来架构，网页设计美工人员(flash,dreamweaver,firework,photoshop等)，网页开发人员（php,.net,jsp等),网站建立好后，需要我们维护，优化，排错，架构延伸扩容等。
简单点说就是我们如果要浏览一个网页的话，基本上所有的网站都使用的是http协议来进行数据传输的！至于怎么样传输，我们做为运维来说就没有必要去深究了，那是做html前端开发人员要去考虑的事情！
Apache由内核、标准模块和第三方提供的模块三个层次组成。
![CentOS 7 Apache服务的安装与配置](https://s1.51cto.com/images/blog/201802/05/c4ef48abd31f4770e13041894e735c6d.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
通常Apache在默认安装时，只安装图中的1、2两部分。根据用户需要，用户可以通过修改配置去掉一些默认安装的标准模块；也可以通过修改配置安装一些默认不安装的模块。
同时，如果用户需要，也可以安装一些第三方提供的模块。

```
[survey.netcraft.net此网站会有每月份的世界上网站使用的WEB服务器的使用率统计](https://news.netcraft.com/archives/category/web-server-survey/)
Apache是世界上应用最广泛的web服务器之一
[www.apache.org Apache官网](http://www.apache.org/)   
```

## 二、CentOS下的Apache

### 1. 网站分为两种

- 静态网站：Apache,Nginx,html
- 动态网站：php/perl/python,jsp(java), .net

### 2. Apache服务概览

> 软件包： httpd, httpd-devel, httpd-manual
> 服务类型：由systemd启动的守护进程
> 配置单元： /usr/lib/systemd/system/httpd.service
> 守护进程： /usr/sbin/httpd
> 端口： 80(http), 443(https)
> 配置： /etc/httpd/
> Web文档： /var/www/html/

Apache日志记录目录：/var/log/httpd/
该目录下有两种文件：

```
access_log      # 记录客户端访问Apache的信息，比如客户端的ip
error_log       # 记录访问页面错误信息
```

Apache服务启动的记录日志：

```
/var/log/messages   # 这个日志是系统的大集合
```

### 3. 配置Apache服务器的准备工作

**系统平台：** CentOS 7.3
**DHCP Server：** 192.168.1.20
第1步：服务器设置静态IP
第2步：更改主机名，写/etc/hosts记录

```
[root@Apache ~]# echo "192.168.1.20  Apache" >> /etc/hosts         --往/etc/hosts添加ip和主机名
[root@Apache ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.1.20  Apache
```

第3步：关闭防火墙

```
[root@Apache ~]# systemctl stop firewalld         --临时关闭防火墙 
[root@Apache ~]# systemctl disable firewalld    --永久关闭防火墙
```

第4步：关闭selinux

```
临时关闭：
[root@Apache ~]# setenforce 0
setenforce: SELinux is disabled

永久关闭：
[root@Apache ~]# vim /etc/selinux/config
SELINUX=disabled                 # 将enforcing改为disabled

[root@Apache ~]# reboot   --重启系统永久生效
```

## 三、Apache服务的搭建与配置

### 1. 使用yum包安装Apache软件

```
[root@Apache ~]# yum -y install httpd*
[root@Apache ~]# rpm -qa | grep httpd     --查看安装的http包
httpd-manual-2.4.6-67.el7.centos.6.noarch
httpd-tools-2.4.6-67.el7.centos.6.x86_64
httpd-2.4.6-67.el7.centos.6.x86_64
httpd-devel-2.4.6-67.el7.centos.6.x86_64
```

安装成功后，会产生下面两个文件

```
/etc/httpd/conf/httpd.conf  # 主配置文件
/var/www/html                   # 默认网站家目录
```

### 2. 认识配置文件里的主要参数

```
[root@Apache ~]# vim /etc/httpd/conf/httpd.conf
 31 serverRoot "/etc/httpd"           # 存放配置文件的目录
 42 Listen 80           # Apache服务监听端口
 66 User apache     # 子进程的用户
 67 Group apache   # 子进程的组
 86 ServerAdmin root@localhost  # 设置管理员邮件地址
119 DocumentRoot "/var/www/html" --网站家目录
# 设置DocumentRoot指定目录的属性
131 <Directory "/var/www/html">   # 网站容器开始标识
144 Options Indexes FollowSymLinks   # 找不到主页时，以目录的方式呈现，并允许链接到网站根目录以外
151 AllowOverride None                # none不使用.htaccess控制,all允许
156 Require all granted                 # granted表示运行所有访问，denied表示拒绝所有访问
157 </Directory>    # 容器结束
164 DirectoryIndex index.html       # 定义主页文件，当访问到网站目录时如果有定义的主页文件，网站会自动访问
316 AddDefaultCharset UTF-8      # 字符编码，如果中文的话，有可能需要改为gb2312或者gbk,因你的网站文件的默认编码而异
```

### 3. 启动Apache网站

```
[root@Apache ~]# systemctl start httpd.service
[root@Apache ~]# lsof -i:80         --查看httpd服务是否启动
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
httpd   20585   root    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
httpd   20586 apache    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
httpd   20587 apache    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
httpd   20588 apache    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
httpd   20589 apache    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
httpd   20590 apache    4u  IPv6 402909      0t0  TCP *:http (LISTEN)
```

启动成功后使用浏览器：输入自己的IP地址会看到一个红帽的欢迎页面：

```
[root@Apache ~]# firefox 192.168.1.20
```

每次打开浏览器不是很方便，因此我们可以使用文本浏览器，方便测试。

```
[root@Apache ~]# yum -y install elinks         --安装elinks文本浏览器
[root@Apache ~]# elinks 192.168.5.20         --按ctrl + c退出
[root@Apache ~]# curl 192.168.1.20            --或者使用curl
```

**例1：**建立网站主页,在网站根目录下建立一个主页文件
格式1：

```
[root@Apache ~]# echo 'main page' > /var/www/html/index.html   --往index.html添加内容
[root@Apache ~]#systemctl restart httpd.service      --重启服务
[root@Apache ~]# firefox http://192.168.1.20             --在浏览器进行测试，显示的信息为刚才我们输入的内容main page
```

格式2：

```
[root@Apache ~]# vim /var/www/html/index.html        --把主页文件写成html标签的格式，添加一下内容
<html>
<head>
<title>测试站点</title>
</head>
<body>
<center><h1>欢迎来到测试站点!@_@</h1></center>
</body>
</html>
[root@Apache ~]# systemctl restart httpd.service      --重启服务
[root@Apache ~]# firefox http://192.168.1.20             --在浏览器进行测试，显示的信息为刚才我们输入的内容main page
```

**例2：**将网站家目录修改成：/www目录

```
[root@Apache ~]# mkdir /www      --创建/www目录

[root@Apache ~]# vim /etc/httpd/conf/httpd.conf
119  DocumentRoot "/www"            --修改网站根目录为/www
131  <Directory "/www">               --把这个也对应的修改为/www

[root@Apache ~]# systemctl restart httpd.service      --重新启动apache服务

[root@Apache ~]# echo "这是新修改的网站家目录/www" > /www/index.html        --往index.html添加内容

[root@Apache ~]# firefox http://192.168.1.20            --访问网站，看到新网站根目录下的刚添加的信息
```

**例3：**修改主页类型或者主页名

```
[root@Apache ~]# vim /etc/httpd/conf/httpd.conf
164 DirectoryIndex index.php              --将index.html改成index.php

[root@Apache ~]# systemctl reload httpd.service     --重新加载服务或重启

[root@Apache ~]# echo 'php main page' > /www/index.php      --这时我们创建一个index.php页面，再使用浏览器访问就能看到了

[root@Apache ~]# elinks 192.168.1.20
```

## 四、编译安装Apache服务

### 1. 安装编译所需要的信赖软件包

```
[root@Apache ~]# yum -y install gcc* make* apr apr-util pcre apr-devel apr-util-devel  pcre-devel
```

### 2. 安装OpenSSL和Apache

安装Open SSL

```
[root@Apache ~]# wget https://www.openssl.org/source/openssl-1.0.2m.tar.gz      --下载openssl软件包
[root@Apache ~]# tar xf ./openssl-1.0.2m.tar.gz -C /usr/src       --解压到/usr/src目录
[root@Apache ~]# cd /usr/src/openssl-1.0.2m/        --切换路径到/usr/src目录
[root@Apache ~]# ./config --prefix=/usr/local/ssl --shared          --检查配置，指定路径
[root@Apache ~]# make && make install                --编译，安装
[root@Apache ~]# echo  /usr/local/ssl/lib >> /etc/ld.so.conf
[root@Apache ~]# ldconfig            --使库文件生效
```

安装Apache

```
[root@Apache ~]# wget http://archive.apache.org/dist/httpd/httpd-2.4.28.tar.gz    --下载apache软件包
[root@Apache ~]# tar xf httpd-2.4.28.tar.gz -C /usr/src      --解压到/usr/src目录
[root@Apache ~]# cd /usr/src/httpd-2.4.28/          --cd到解压路径

[root@Apache ~]# ./configure -help        --查看参数帮助

[root@Apache ~]# ./configure --prefix=/usr/local/apache2 --enable-so --enable-rewrite --enable-ssl --with-ssl=/usr/local/ssl --with-mpm=prefork
[root@Apache ~]# make
[root@Apache ~]# make install
```

> --prefix 指定安装路径
> --enable-so 让apache核心装载DSO（动态共享目标）
> --enable-rewrite 启用重写功能
> --enable-modules 将模块编译到apache中
> --enable-ssl 打开ssl协议
> --with-mpm 指定运行模型

运行模式：/etc/httpd/conf.modules.d/00-mpm.conf
多进程模型：prefork（预派生）
多进程多线程混合模型：worker（工作者）、event（事件）

编译安装成功后，安装在：/usr/local/apache2/ 目录下
配置文件：/usr/local/apache2/conf/httpd.conf
启动命令：/usr/local/apache2/bin/apachectl
默认网站家目录：/usr/local/apache2/htdcos

### 3. 修改家目录

```
[root@Apache ~]# vim /usr/local/apache2/conf/httpd.conf  --修改配置文件
220 DocumentRoot "/www"     --修改网站家目录，由/usr/local/apache2/htdocs改成/www
221 <Directory "/www">          --家目录这里建议一同修改

[root@Apache ~]# mkdir /www     --创建网站家目录
[root@Apache ~]# echo "main page" > /www/index.html

先停掉rpm包安转的http
[root@Apache ~]# systemctl stop httpd.service

启动源码包安装的http
[root@Apache ~]# /usr/local/apache2/bin/apachectl start
```

### 4. 配置支持中文

```
[root@Apache ~]# vim /usr/local/apache2/conf/httpd.conf
# 在文件的最后新增以下参数
AddDefaultCharset UTF-8       # 默认以utf-8编码显示中文
```

### 5. 启动源码包版Apache

```
[root@Apache ~]# /usr/local/apache2/bin/apachectl restart       --重新启动apache
```

### 6. 测试

```
[root@Apache ~]# echo "<h1>Apache源码包版，测试</h1>" > /www/index.html
[root@Apache ~]# firefox http://192.168.1.20
```

## 五、Apache配置虚拟主机

在一台Web服务器上，通过多个独立的IP地址、域名或端口号提供不同的Web站点。
**基于IP地址的虚拟主机：**
每个网站拥有不同的 IP 地址
通过访问服务器上不同的IP地址访问不同的网站
**基于域名的虚拟主机：**
所有的虚拟主机可以共享同一个IP地址
使用不同的域名来访问不同的网站
**基于端口的虚拟主机：**
所有的虚拟主机可以共享同一个IP地址
各虚拟主机之间通过不同的端口号进行区分

准备工作：

```
[root@Apache ~]# vim /usr/local/apache2/conf/htttpd.conf
  52 #Listen 80         # 将这行注释掉
220 #DocumentRoot "/usr/local/apache2/htdocs"        # 将这行注释掉
```

## 1. Apache基于IP的虚拟主机配置

**第一步：**使用ifconfig设置3个虚拟ip

```
[root@Apache ~]# ifconfig ens33:1 192.168.1.11/24
[root@Apache ~]# ifconfig ens33:2 192.168.1.12/24
[root@Apache ~]# ifconfig ens33:3 192.168.1.13/24

[root@Apache ~]# ifconfig 
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.20  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::20c:29ff:fe14:1fb9  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:14:1f:b9  txqueuelen 1000  (Ethernet)
        RX packets 216515  bytes 207352525 (197.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 109646  bytes 23077100 (22.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens33:1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.11  netmask 255.255.255.0  broadcast 192.168.1.255
        ether 00:0c:29:14:1f:b9  txqueuelen 1000  (Ethernet)

ens33:2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.12  netmask 255.255.255.0  broadcast 192.168.1.255
        ether 00:0c:29:14:1f:b9  txqueuelen 1000  (Ethernet)

ens33:3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.13  netmask 255.255.255.0  broadcast 192.168.1.255
        ether 00:0c:29:14:1f:b9  txqueuelen 1000  (Ethernet)
```

**第二步：**配置主机的hosts文件，便于测试

```
[root@Apache ~]# echo "192.168.1.11  test1.com" >> /etc/hosts
[root@Apache ~]# echo "192.168.1.12  test2.com" >> /etc/hosts
[root@Apache ~]# echo "192.168.1.13  test3.com" >> /etc/hosts

[root@Apache ~]# tail -3 /etc/hosts
192.168.1.11  test1.com
192.168.1.12  test2.com
192.168.1.13  test3.com
```

**第三步：**建立虚拟主机存放网页的根目录，并创建首页文件index.html

```
[root@Apache ~]# cd /www
[root@Apache ~]# mkdir 11
[root@Apache ~]# mkdir 12
[root@Apache ~]# mkdir 13
[root@Apache ~]# echo "192.168.1.11" > 11/index.html
[root@Apache ~]# echo "192.168.1.12" > 12/index.html
[root@Apache ~]# echo "192.168.1.13" > 13/index.html
```

**第四步：**修改httpd.conf在文件末尾加入以下配置

```
[root@Apache ~]# vim /usr/local/apache2/conf/httpd.conf    --文件末尾加入以下配置
Listen 192.168.1.11:80
Listen 192.168.1.12:80
Listen 192.168.1.13:80
Include conf/vhost/*.conf            # 文件包含vhost目录下所有以.conf结尾的文件
```

**第五步：**编辑每个ip的配置文件

```
[root@Apache ~]# mkdir  /usr/local/apache2/conf/vhost
[root@Apache ~]# cd /usr/local/apache2/conf/vhost
[root@Apache ~]# vim test11.conf        --一定要以.conf为后缀，这是第一台机器
<VirtualHost 192.168.1.11:80>
      ServerName test11.com
    DocumentRoot /www/11
      <Directory "/www/11/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

参数介绍：

> 虚拟主机配置格式：
> <VirtualHost 主机ip:端口>
> 配置内容
> </VirtualHost>
>
> 指定虚拟主机使用的域名
> ServerName 域名
>
> 指定虚拟主机的主目录
> DocumentRoot 目录
>
> 虚拟目录的格式：
> <Directory 目录的路径>
> 目录相关的配置参数和指令
> </Directory>
>
> Options Indexes FollowSymLinks --找不到主页时，以目录的方式呈现，并允许链接到网站根目录以外
>
> 是否允许.htaccess文件覆盖httpd.conf文件中关于虚拟主机目录的配置。
> AllowOverride None # 不使用
> AllowOverride all # 使用
>
> 允许、拒绝所有访问指令
> Require all granted # 允许
> Require all denied # 拒绝

```
[root@Apache ~]# vim test12.conf          --这是第二台机器
<VirtualHost 192.168.1.12:80>
      ServerName test12.com
    DocumentRoot "/www/12"
      <Directory "/www/12/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

[root@Apache ~]# vim test13.conf          --这是第三台机器
<VirtualHost 192.168.1.13:80>
      ServerName test13.com
    DocumentRoot "/www/13"
      <Directory "/www/13/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

**第六步：**启动服务并测试

```
[root@Apache ~]# /usr/local/apache2/bin/apachectl -t        --检查配置文件是否正确
Syntax OK
[root@Apache ~]# /usr/local/apache2/bin/apachectl restart    --重新启动Apache
检查虚拟主机是否运行
[root@Apache ~]# curl 192.168.1.11
192.168.1.11
[root@Apache ~]# curl 192.168.1.12
192.168.1.12
[root@Apache ~]# curl 192.168.1.13
192.168.1.13
```

## 2. Apache基于端口的虚拟主机配置

**第一步：**使用ifconfig设置1个虚拟ip

```
[root@Apache ~]# ifconfig ens33:4 192.168.1.14/24
```

**第二步：**配置主机的hosts文件，便于测试

```
[root@Apache ~]# echo "192.168.1.14  test4.com" >> /etc/hosts
```

**第三步：**建立虚拟主机存放网页的根目录，并创建首页文件index.html

```
[root@Apache ~]# cd /www
[root@Apache ~]# mkdir port
[root@Apache ~]# cd port
[root@Apache ~]# mkdir 6081
[root@Apache ~]# mkdir 7081
[root@Apache ~]# mkdir 9081
[root@Apache ~]# echo "port 6081" > 6081/index.html
[root@Apache ~]# echo "port 7081" > 7081/index.html
[root@Apache ~]# echo "port 9081" > 9081/index.html
```

**第四步：**修改httpd.conf在文件末尾加入以下配置

```
[root@Apache ~]# vim /usr/local/apache2/conf/httpd.conf      --文件末尾加入以下配置
Listen 192.168.1.14:6081
Listen 192.168.1.14:7081
Listen 192.168.1.14:9081
Include conf/vhost/*.conf
```

**第五步：**编辑每个端口的配置文件

```
[root@Apache ~]# cd /usr/local/apache2/conf/vhost
[root@Apache ~]# vim test14.6081.conf       --一定要以.conf为后缀，这是第一台机器
<VirtualHost 192.168.1.14:6081>
      ServerName test14.com
    DocumentRoot "/www/port/6081"
      <Directory "/www/port/6081/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

[root@Apache ~]# vim test14.7081.conf          --这是第二台机器
<VirtualHost 192.168.1.14:7081>
      ServerName test14.com
    DocumentRoot "/www/port/7081"
      <Directory "/www/port/7081/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

[root@Apache ~]# vim test14.9081.conf          --这是第三台机器
<VirtualHost 192.168.1.14:9081>
      ServerName test14.com
     DocumentRoot "/www/port/9081"
      <Directory "/data/port/9081/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

**第六步：**启动服务并测试

```
[root@Apache ~]# /usr/local/apache2/bin/apachectl -t              --检查配置文件是否正确
Syntax OK
[root@Apache ~]# /usr/local/apache2/bin/apachectl restart    --重新启动apache
检查虚拟主机是否运行
[root@Apache ~]# curl 192.168.1.14:6081
port 6081
[root@Apache ~]# curl 192.168.1.14:7081
port 7081
[root@Apache ~]# curl 192.168.1.14:9081
port 9081
```

## 3. Apache基于域名的虚拟主机配置

**第一步：**使用ifconfig设置1个虚拟ip

```
[root@Apache ~]# ifconfig ens33:5 192.168.1.15/24
```

**第二步：**配置主机的hosts文件，便于测试

```
[root@Apache ~]# echo "192.168.1.15  www.aa.com" >> /etc/hosts
[root@Apache ~]# echo "192.168.1.15  www.bb.com" >> /etc/hosts
[root@Apache ~]# echo "192.168.1.15  www.cc.com" >> /etc/hosts
```

**第三步：**建立虚拟主机存放网页的根目录，并创建首页文件index.html

```
[root@Apache ~]# cd /www
[root@Apache ~]# mkdir www.aa.com
[root@Apache ~]# mkdir www.bb.com
[root@Apache ~]# mkdir www.cc.com
[root@Apache ~]# echo "www.aa.com" > www.aa.com/index.html
[root@Apache ~]# echo "www.bb.com" > www.bb.com/index.html
[root@Apache ~]# echo "www.cc.com" > www.cc.com/index.html
```

**第四步：**修改httpd.conf在文件末尾加入以下配置

```
[root@Apache ~]# vim /usr/local/apache2/conf/httpd.conf      --文件末尾加入以下配置
Listen 192.168.1.15:80
Include conf/vhost/*.conf
```

**第五步：**编辑每个域名的配置文件

```
[root@Apache ~]# cd /usr/local/apache2/conf/vhost
[root@Apache ~]# vim www.aa.com.conf        --一定要以.conf为后缀，这是第一台机器
<VirtualHost 192.168.1.15:80>
      ServerName www.aa.com
    DocumentRoot "/www/www.aa.com"
      <Directory "/www/www.aa.com/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

[root@Apache ~]# vim www.bb.com.conf          --这是第二台机器
<VirtualHost 192.168.1.15:80>
      ServerName www.bb.com
    DocumentRoot "/www/www.bb.com"
      <Directory "/www/www.bb.com/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

[root@Apache ~]# vim www.cc.com.conf          --这是第三台机器
<VirtualHost 192.168.1.15:80>
      ServerName www.cc.com
    DocumentRoot "/www/www.cc.com"
      <Directory "/www/www.cc.com/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

**第六步：**启动服务并测试

```
[root@Apache ~]# /usr/local/apache2/bin/apachectl -t              --检查配置文件是否正确
Syntax OK
[root@Apache ~]# /usr/local/apache2/bin/apachectl restart    --重新启动apache
检查虚拟主机是否运行
[root@Apache ~]# curl www.aa.com
www.aa.com
[root@Apache ~]# curl www.bb.com
www.bb.com
[root@Apache ~]# curl www.cc.com
www.cc.com
```