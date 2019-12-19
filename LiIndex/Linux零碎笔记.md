# Linux 零碎笔记



[TOC]

## 1. ubuntu更改镜像源（软件源）

### 更新Ubuntu软件下载地址
#### 1. 寻找国内镜像源

所谓的镜像源：可以理解为提供下载软件的地方，比如Android手机上可以下载软件的91手机助手；iOS手机上可以下载软件的AppStore

[清华大学镜像源](https://mirrors.tuna.tsinghua.edu.cn/)

![img](https://img-blog.csdn.net/20180308102919796?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308102942887?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308102959993?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308103020856?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



#### 2. 备份Ubuntu默认的源地址

```shell
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
```

![img](https://img-blog.csdn.net/20180308103133506?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#### 3. 更新源服务器列表

![img](https://img-blog.csdn.net/20180308103251912?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308103305551?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308103347616?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#### 4. Ubuntu 镜像使用帮助

Ubuntu 的软件源配置文件是 /etc/apt/sources.list。将系统自带的该文件做个备份，将该文件替换为下面内容，即可使用 TUNA 的软件源镜像。

选择你的ubuntu版本: `18.04 LTS`

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```

#### 5. 更新源

做完此步骤之后，就可以进行`apt-get install` 下载了

![img](https://img-blog.csdn.net/2018030810342152?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180308103439916?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2VpeGluXzQxNzYyMTcz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



## 2. Ubuntu软件操作的相关命令

```
sudo apt-get update  更新源 
sudo apt-get install package 安装包 
sudo apt-get remove package 删除包
sudo apt-cache search package 搜索软件包 
sudo apt-cache show package  获取包的相关信息，如说明、大小、版本等 
sudo apt-get install package --reinstall   重新安装包 
sudo apt-get -f install   修复安装 
sudo apt-get remove package --purge 删除包，包括配置文件等 
sudo apt-get build-dep package 安装相关的编译环境 
sudo apt-get upgrade 更新已安装的包 
sudo apt-get dist-upgrade 升级系统 
sudo apt-cache depends package 了解使用该包依赖那些包 
sudo apt-cache rdepends package 查看该包被哪些包依赖 
sudo apt-get source package  下载该包的源代码 
sudo apt-get clean && sudo apt-get autoclean 清理无用的包 
sudo apt-get check 检查是否有损坏的依赖
```



## 3. Linux软件安装（rpm和yum）

### 1. rpm和yum的区别：

**rpm：**

- 用来安装已经下载在本地机器上的rpm包，类似Windows里面的“添加/删除程序”
- 可以发现并提示某个依赖包尚未安装，但需要手动先安装依赖包

**yum：**

- 能够自动下载并安装rpm包
- 能够处理包的依赖关系
- 能够更新系统
- 使用存储库（repository），即包的集合

**rpm用法：**

- 安装一个软件包：rpm -i <包名>.rpm
- 软件包升级：rpm -Uvh *.rpm [http:///abc.rpm](https://blog.csdn.net/abc.rpm)
  - 根据当前目录下已经下载的所有rpm包升级软件包；另外通过网络中升级abc.rpm包
  - -U：软件升级
  - -v：详细信息(verbose)
  - -h：软件包安装的时候列出哈希标记 (和 -v 一起使用效果更好)
- 删除一个软件包：`rpm -e <包名>.rpm`

**yum用法：**

- 查找：`yum list | grep net-tools`
- 安装：`yum install net-tools`
- 更新以gr开头的软件包：`yum update 'gr*'`
- 删除：`yum erase net-tools`
- 找出某个命令（比如ifconfig这个命令）的安装包：`yum provides ifconfig`

**yum库文件（.repo）**

- 用于指定安装包所在的下载位置
- 所在的目录：`/etc/yum.repos.d/`

**yum配置文件：**`/etc/yum.conf`



**附：**

**搜索rpm包的网站：**

- [https://www.rpmfind.net](https://www.rpmfind.net/)
- http://www.rpm-find.net/

**缩略语：**

RPM：`Redhat Package Manager`

YUM：`Yellowdog Updater Modified`



### 2. RPM命令详解：

#### 2.1 rpm 执行安装包

二进制包（Binary）以及源代码包（Source）两种。二进制包可以直接安装在计算机中，而源代码包将会由RPM自动编译、安装。源代码包经常以src.rpm作为后缀名。

常用命令组合：

`－ivh：`安装显示安装进度`--install--verbose--hash`

`－Uvh：`升级软件包`	--Update`；

`－qpl：`列出RPM软件包内的文件信息`[Query Package list]`；

`－qpi：`列出RPM软件包的描述信息`[Query Package install package(s)]`；

`－qf：`查找指定文件属于哪个RPM软件包`[Query File]`；

`－Va：`校验所有的RPM软件包，查找丢失的文件`[View Lost]`；

`－e：`删除包

`rpm -q samba：` 查询程序是否安装

`rpm -ivh /media/cdrom/RedHat/RPMS/samba-3.0.10-1.4E.i386.rpm：` 按路径安装并显示进度

`rpm -ivh --relocate /=/opt/gaim gaim-1.3.0-1.fc4.i386.rpm：`  指定安装目录

`rpm -ivh --test gaim-1.3.0-1.fc4.i386.rpm：` 用来检查依赖关系；并不是真正的安装；

`rpm -Uvh --oldpackage gaim-1.3.0-1.fc4.i386.rpm：`   新版本降级为旧版本

`rpm -qa | grep httpd：` [搜索指定rpm包是否安装]--all搜索*httpd*

`rpm -ql httpd：` [搜索rpm包]--list所有文件安装目录

`rpm -qpi Linux-1.4-6.i368.rpm：` [查看rpm包]--query--package--install package信息

`rpm -qpf Linux-1.4-6.i368.rpm：` [查看rpm包]--file

`rpm -qpR file.rpm：` [查看包]依赖关系

`rpm2cpio file.rpm |cpio -div：`  [抽出文件]

`rpm -ivh file.rpm：`  [安装新的rpm]--install--verbose--hash

`rpm -ivh [URL]`[URL](http://mirrors.kernel.org/fedora/core/4/i386/os/Fedora/RPMS/gaim-1.3.0-1.fc4.i386.rpm)

`rpm -Uvh file.rpm `  [升级一个rpm]--upgrade

`rpm -e file.rpm `   [删除一个rpm包]--erase



常用参数：`Install/Upgrade/Erase options:`

```
-i, --install                   	   install package(s)
-v, --verbose                     provide more detailed output
-h, --hash                       	 print hash marks as package installs (good with -v)
-e, --erase                       	 erase (uninstall) package
-U, --upgrade=<packagefile>+      upgrade package(s)
－-replacepkge                    无论软件包是否已被安装，都强行安装软件包
--test                            		  安装测试，并不实际安装
--nodeps                          	忽略软件包的依赖关系强行安装
--force                          		忽略软件包及文件的冲突

Query options (with -q or --query):
-a, --all                         		  query/verify all packages
-p, --package                     query/verify a package file
-l, --list                        			list files in package
-d, --docfiles                   	list all documentation files
-f, --file                        			query/verify package(s) owning file
```


#### 2.2 RPM源代码包装安装

`.src.rpm`结尾的文件，这些文件是由软件的源代码包装而成的，用户要安装这类RPM软件包，必须使用命令：`rpm`　`--recompile  vim-4.6-4.src.rpm `  ＃这个命令会把源代码解包并编译、安装它，如果用户使用命令：`rpm`　`--rebuild  vim-4.6-4.src.rpm`　　＃在安装完成后，还会把编译生成的可执行文件重新包装成i386.rpm的RPM软件包。



## 4. Linux 的软件安装目录

Linux 的软件安装目录是也是有讲究的，理解这一点，在对系统管理是有益的

`/usr：`系统级的目录，可以理解为`C:/Windows/`，
`/usr/lib：`理解为`C:/Windows/System32`。
`/usr/local：`用户级的程序目录，可以理解为`C:/Progrem Files/`。用户自己编译的软件默认会安装到这个目录下。
`/opt：`用户级的程序目录，可以理解为`D:/Software`，`opt`有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接`rm -rf`掉即可。在硬盘容量不够时，也可将`/opt`单独挂载到其他磁盘上使用。

源码放哪里？
`/usr/src：`系统级的源码目录。
`/usr/local/src：`用户级的源码目录。



-----------------翻译-------------------

/opt

> Here’s where optional stuff is put. Trying out the latest Firefox beta? Install it to /opt where you can delete it without affecting other settings. Programs in here usually live inside a single folder whick contains all of their data, libraries, etc.
> 这里主要存放那些可选的程序。你想尝试最新的firefox测试版吗?那就装到/opt目录下吧，这样，当你尝试完，想删掉firefox的时候，你就可 以直接删除它，而不影响系统其他任何设置。安装到/opt目录下的程序，它所有的数据、库文件等等都是放在同个目录下面。
> 举个例子：刚才装的测试版firefox，就可以装到/opt/firefox_beta目录下，/opt/firefox_beta目录下面就包含了运 行firefox所需要的所有文件、库、数据等等。要删除firefox的时候，你只需删除/opt/firefox_beta目录即可，非常简单。



> This is where most manually installed(ie. outside of your package manager) software goes. It has the same structure as /usr. It is a good idea to leave /usr to your package manager and put any custom scripts and things into /usr/local, since nothing important normally lives in /usr/local.
>
> 这里主要存放那些手动安装的软件，
>
> 即不是通过“新立得”或apt-get安装的软件。它和/usr目录具有相类似的目录结构。
>
> 让软件包管理器来管理/usr目录，而把自定义的脚本(scripts)放到/usr/local目录下面，我想这应该是个不错的主意。
> 



## 5. linux 软件卸载

+ 使用`apt-get`命令，这是用于管理已安装程序的通用命令。
+ 浏览已安装的程序: `dpkg --list`
+ 卸载程序和所有配置文件: `sudo apt-get --purge remove <programname>` 
+ 移除程序但保留配置文件，请输入以下命令: `sudo apt-get remove <programname>`

### ubuntu 命令行卸载并清理软件
#### 删除软件

+ 方法一、如果你知道要删除软件的具体名称，可以使用
  +` sudo apt-get remove --purge 软件名称`  
  + `sudo apt-get autoremove --purge 软件名称` 

+ 方法二、如果不知道要删除软件的具体名称，可以使用
  + `dpkg --get-selections | grep '软件相关名称'`
  + `sudo apt-get purge` 一个带core的package，如果没有带core的package，则是情况而定。


#### 清理残留数据
+ `dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P`

### 卸载遗留

+ 配置文件：`\~/.软件名`、`~/.config/软件名`、`/etc/软件名`
+ 数据文件：`\~/.软件名`、`~/.local/share/软件名`
+ 日志：`/var/log/软件名`
+ 缓存：`\~/.cache/软件名`

这些基本都能安全删除，自己每个地方都找找。


## 6. Boomaga虚拟打印机

### Ubuntu
`Boomaga`可从Ubuntu存储库中获得，并可通过软件中心或在终端中使用以下命令进行安装：

```shell
sudo apt-get install boomaga
```

但是，新版本的软件包通常需要几个月的时间才能到达官方存储库，因此它们可能很快就会过时。这就是为什么最好从我们的[PPA](https://launchpad.net/~boomaga/+archive/ppa)存储库中安装`Boomaga` ，该存储库可用于所有现代Ubuntu版本。打开终端并输入以下命令：

```shell
sudo add-apt-repository ppa:boomaga
sudo apt-get update
sudo apt-get install boomaga
```

## 7. 修复wine下软件界面过小


### 1、修复微信，QQ，Tim等软件

- 终端执行：

```shell
WINEPREFIX=~/.deepinwine/Deepin-WeChat deepin-wine winecfg
```

### 2、修改网易云界面过小：

- 终端执行：

```shell
sudo gedit /usr/share/applications/netease-cloud-music.desktop
```

- 修改Exec=行 为：

```shell
Exec=netease-cloud-music --force-device-scale-factor=1.25 %U
# 1.25可自行修改，表示缩放比
```



## 8. 更改Ubuntu默认Python版本方法

一般Ubuntu默认的Python版本都为2.x, 如何改变Python的默认版本呢？假设我们需要把Python3.5设置为默认版本：
首先查看Python默认版本:

```ruby
ubuntu@user~$:python --version
Python 2.7
```

搜索系统是否已经安装Python3.5:

```ruby
ubuntu@user~$:whereis python3.5
```

如果结果里有`/usr/bin/python3.5`说明已经安装，如果没有则需要手动安装。

安装完成后，需要删除原有的Python连接文件:

```ruby
ubuntu@user~:rm /user/bin/python
```

然后建立指向Python3.5的软连接：

```ruby
ubuntu@user~:ln -s /usr/bin/python3.5 /usr/bin/python
```

之后把路径`/usr/bin/`加入环境变量PATH中：

```ruby
ubuntu@user~:PATH=/usr/bin:$PATH
```

现在输入`python --version`你就会发现python默认版本变为Python3.5了:)

## 9. 修改anaconda为默认Python

1.修改`~/.bashrc`

```bash
sudo gedit ~/.bashrc
```

2.添加`export PATH=/home/lishanliao/anaconda3/bin:$PATH`

3.更新`bashrc`

```bash
source ~/.bashrc
```

然后输入python得到显示

![1573471625935](Linux%E9%9B%B6%E7%A2%8E%E7%AC%94%E8%AE%B0.assets/1573471625935.png)

说明启动的是anaconda的python。



## 10. 修改环境变量_1

[原文链接](https://blog.csdn.net/White_Idiot/article/details/78253004)

###  1 查看环境变量
查看环境变量有三个命令：
```bash
env：env命令是environment的缩写，用于列出所有的环境变量；
export：单独使用export命令也可以像env列出所有的环境变量，不过export命令还有其他额外的功能；
echo $PATH： echo $PATH用于列出变量PATH的值，里面包含了已添加的目录。
```

### 2 设置方式
设置环境变量通常有两种方式。

#### 2.1 把你的路径加入PATH
可以直接添加到环境变量PATH中。`$PATH`表示变量PATH的值，包含已有的目录。

这种方法需要注意路径的顺序，如果遇到有同名的命令，那么PATH里面哪个目录先被查询，则那个目录下的命令就会被先执行，如下所示：

+  加到PATH末尾
```bash
export PATH=$PATH:/path/to/your/dir
```

+ 加到PATH开头
```bash
export PATH=/path/to/your/dir:$PATH
```

#### 2.2 命名一个新的环境变量
也可以直接命名一个新的环境变量，用于其它程序引用：
```bash
export VAR_NAME=value
```

### 3 作用域
环境变量的作用域通常有三个。

#### 3.1 用于当前终端
打开一个终端，输入添加环境变量的语句：
```bash
export CLASS_PATH=./JAVA_HOME/lib:$JAVA_HOME/jre/lib
```

终端所添加的环境变量是临时的，只适用于当前终端，关闭当前终端或在另一个终端中，添加的环境变量无效。

#### 3.2 用于当前用户
如果只需要添加的环境变量对当前用户有效，可以写入用户主目录下的.bashrc文件：
```bash
vim ~/.bashrc
```

添加语句：
```basg
export CLASS_PATH=./JAVA_HOME/lib:$JAVA_HOME/jre/lib
```
注销或者重启可以使修改生效，如果要使添加的环境变量马上生效：
```bash
source ~/.bashrc
```

#### 3.3 用于所有用户
要使环境变量对所有用户有效，可以修改profile文件：
```bash
sudo vim /etc/profile 
```

添加语句：
```bash
export CLASS_PATH=./JAVA_HOME/lib:$JAVA_HOME/jre/lib
```
注销或者重启可以使修改生效，如果要使添加的环境变量马上生效：
```bash
source /etc/profile
```



## 11.  修改环境变量_2

[原文链接](https://blog.csdn.net/weixin_36296538/article/details/83044639)

### 1. 什么是环境变量
环境变量（environment variables）一般是指在操作系统中用来指定操作系统运行环境的一些参数，这些参数会对系统行为产生影响。

比如常用的PATH环境变量，当要求系统运行一个程序而没有告诉它程序所在的完整路径时，系统除了在当前目录下面寻找此程序外，还会到PATH中指定的路径去找。你可以在终端使用`printenv PATH`查看当前PATH变量的值。

### 2. 用户环境变量和系统环境变量
Ubuntu系统包含两类环境变量：系统环境变量和用户环境变量。系统环境变量对所有系统用户都有效，用户环境变量仅仅对当前的用户有效。

+ 用户环境变量可存储在以下文件中：
```bash
~/.profile
~/.bashrc
~/.bash_profile
~/.bash_login
```

+ 推荐将环境变量保存在`~/.profile`中，因为无论是通过控制台还是图形界面启动程序时，都会自动执行该文件。而`~/.bashrc`, `~/.bash_profile`, `~/.bash_login`这些文件，当通过shell启动程序时，它们也会被加载；但当通过图形界面环境启动程序时，这些文件中的环境变量设置便不可用了。

    

+ 系统环境变量可存储在以下文件中：
```bash
/etc/profile
/etc/profile.d（它是文件夹）
/etc/bash.bashrc
```
+   `/etc/profile`和`/etc/profile.d`都是常用的设置环境的地方。其中`/etc/profile.d`文件夹来源于`/etc/profile`，在该目录下的`*.sh`，即以sh为后缀的文件都会被加载。
    类似地，不推荐使用`/etc/bash.bashr`c，因为在图形界面环境下启动程序时，不会加载它里边的环境变量设置。

### 3. 设置永久环境变量实例（以/etc/profile为例）

```bash
gedit /etc/profile
```

在文件末尾处添加如下，保存并退出：
```bash
export JAVA_HOME=/usr/lib/jvm/jdk1.7.0
export PATH=$PATH:$JAVA_HOME/bin
```
其中，
`export`命令：使得变量真正输出成为环境变量。

等号=左边为变量名，右边为变量实际值。export后，可以通过$variable_name的形式访问变量，如$`JAVA_HOME`，即可替换为`JAVA_HOME=/usr/lib/jvm/jdk1.7.0`。

PATH变量中通常有多个指定路径，中间用冒号隔开。拼接上$PATH变量，则不影响原先的路径设置。

环境变量更改后，在用户下次登陆时生效。如果想立刻生效，则执行下面的语句
```bash
source /etc/profile
```

注意：请在使用时将路径替换为你电脑下的实际路径。
如果只是测试，直接复制上面的命令也行，只不过最后会提示“No such file or directory”。

### 4. 查看环境变量是否已经生效
在控制台下输入
```bash
$JAVA_HOME
$PATH
```
可以看到，环境变量已经生效了！



## 12. 设置终端走代理

修改文件`~/.bashrc`，原理：开机自启

 在末尾添加如下语句，删除则取消终端走代理

```bash
# 设置终端走代理
unset all_proxy && unset ALL_PROXY
export all_proxy="socks5://127.0.0.1:1080"
```



## 13. 设置开机自启

### 1 使用gnome-session

打开启动应用程序的图标，打开对应的对话框如下：

[![选区_125.png](Linux%E9%9B%B6%E7%A2%8E%E7%AC%94%E8%AE%B0.assets/thum-59a41501403358.png)](http://www.mryu.top/content/uploadfile/201707/59a41501403358.png)

根据界面提示进行相关操作，例如添加启动项、删除启动项以及编辑启动项

### 2. 编辑rc.local脚本

Ubuntu开机之后会自动执行`/etc/rc.local`文件中的脚本，所以我们可以直接在`/etc/rc.local`中添加启动脚本，但必须添加到语句`exit 0`前面才行。

### 3. 通过命令添加一个Ubuntu的开机启动服务

如果要添加为开机自动执行的脚本文件，可先将脚本复制或者软连接到`/etc/init.d/`目录下，然后用`update-rc.d　xxx defaults NN `命令（NN为启动顺序），将脚本添加到初始化执行的队列中区。注意如果脚本需要用到网络，则NN需要设置一个比较大的数字，如99。步骤如下：

1)将你的启动脚本复制到/etc/init.d目录下（以下假设你的脚本为test）

2)设置脚本文件的权限

```bash
sudo chmod 775 /etc/init.d/test
```

3)执行如下命令脚本放到启动脚本中去

```bash
cd /etc/init.d
sudo update-rc.d test defaults 95 
```

需要注意的是数字95是脚本的启动顺序号，按照自己的需要相应的修改即可。在你有多个启动脚本，而它们之间又有先后启动的依赖关系时你就知道这个数字的具体作用了。

4)卸载启动脚本

```bash
cd /etc/init.d
sudo update-rc.d -f test remove 
```



