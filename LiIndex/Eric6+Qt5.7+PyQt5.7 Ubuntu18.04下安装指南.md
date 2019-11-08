# Eric6+Qt5.7+PyQt5.7 Ubuntu18.04下安装指南

Eric 是一个python Gui开发平台，使用方便结构合理，利用Qt部署界面，修改界面不用重新修改代码，非常人性化。对于希望进行python图形化快速开发的同行来说，可以说是很好的选择。eric在windows上部署还是很便捷的，基本上不会出现什么问题，而在linux上部署显得困难重重，天坑不断，我花了几天时间总结了ubuntu下的部署方法，基本排除了大部分常见问题。希望能帮到各位。



## 1. 确认Python版本

首先确认下Python的版本，我安装的是最新版（2018.11）的Ubuntu 18.04。可以看到python3的版本已经是3.6.5了。所以我不需要安装python3了。低版本的还需要安装python3+。需要注意的是 Ubuntu 18.04的一个好处是，默认使用Python3版本，不再默认支持Python2，这在老版本中Python2和Python3并行，造成了安装过程中很多版本切换方面的意外。

![img](https://img-blog.csdnimg.cn/2018121115113269.jpg)

我们安装一个额外Python包 python3-dev 这个包包含了一系列的头文件和静态库。

```bash
sudo apt-get install python3-dev
```



## 2. 安装Qt

因为 ubuntu 没有默认安装C++包因此我们需要再装上 C++包,还有一些gui相关库。

```bash
sudo apt-get -y install cmake g++
sudo apt-get -y install mesa-common-dev
sudo apt-get -y install libglu1-mesa-dev
```

我们下载Qt 5.7.0 这个版本适应性较好，我曾经试过5.10和5.11，并没有感觉有特别好的体验，在和最新版PyQt对应方面会产生莫名的问题。下载完成后我们将其改为可执行文件，并执行安装。

```bash
sudo  chmod a+x qt-opensource-linux-x64-5.7.0.run
./qt-opensource-linux-x64-5.7.0.run     
```

 

 安装需要一个Qt账号。没有也可以跳过，我因为以前有账号就输入了。不影响任何安装结果。

 ![img](https://img-blog.csdnimg.cn/20181211152138825.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

后面安装界面√记得都打上。要不就装了个工具可就尴尬了。安装完毕后可以打开 Qt Creator 就算安装成功了。

 ![img](https://img-blog.csdnimg.cn/20181211152252841.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 安装完成后需要将Qt5的环境变量加进去。修改 bash配置文件 在最后添加图中字段(大小写敏感）。

```bash
vi  ~/.bashrc 
```

这些目录可以ls找到后黏贴进来。为了防止无脑黏贴造成系统问题，我仅放了图片。

 ![img](https://img-blog.csdnimg.cn/20181211152947640.jpg)

重新打开终端，打qm 按tab键补全能出现Qt命令即可。比如qmake



## 3. 安装SIP

SIP主要为Python生成C++接口代码提供了支持，毕竟QT是基于C的软件。我选择了 sip-4.18.1，参考了网上的成功案例，因为SIP这个工具非常敏感，不同的版本一旦出现不兼容，会引起大量的未知问题。所以尽量以成功案例为基础下载相应版本，我曾经下载了4.19，还有使用pip3安装 pyqt.sip 都废了，浪费了大量的时间。

https://sourceforge.net/projects/pyqt/files/sip/sip-4.18.1/

 ![img](https://img-blog.csdnimg.cn/2018121115315255.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 下载 sip-4.18.1.tar.gz ，源码下载下来以后解压缩，之后就是源代码编译素质三连：配置，make，make install 。

```bash
tar -zxvf sip-4.18.1.tar.gz     
cd sip-4.18.1     
python3 configure.py     
sudo make     
sudo make install     
```

安装完毕后验证，进入python3导入 sip 没有报错即可。如果其他版本的系统会遇到sip已经安装过的情况，需要确定SIP版本。这里不需要。见下图

 ![img](https://img-blog.csdnimg.cn/20181211153350757.jpg)



## 4. 安装PIP3

因为ubuntu默认没有安装 pip3 所以我们还要安装一下，之后要用。

```bash
sudo  apt-get  install  python3-pip
```

 

## 5. 安装 qscintilla/Qt4Qt5

Scintilla是支持语法高亮的控件，包括语法高亮、错误指示、代码补全等等。QScintilla是Scintilla在QT上的移植，换句话说就是一个提高编程效率的帮助控件。

[下载链接](https://www.riverbankcomputing.com/software/qscintilla/download)

我们下载QScintilla-2.9.3.tar.gz

![img](https://img-blog.csdnimg.cn/20181211153845139.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

QScintilla安装分3步，Qt4Qt5 要在 PyQt安装之前安装，另外两个需要再PyQt安装完毕后安装。解压压缩包，并且进入 Qt4Qt5目录，素质三连。

```bash
tar -xzvf QScintilla_gpl-2.9.3.tar.gz     
cd QScintilla-gpl-2.9.3/Qt4Qt5    
qmake qscintilla.pro     
sudo make     
sudo make install      
```



## 6. 安装PyQt5

PyQt是Python和Qt交流的必备工具，是连接Python和Qt的桥梁。我们选择了PyQt5.7，版本很重要，版本的差异会直接导致安装的成功与否。安装编译过程会持续相当长时间，毕竟几百个类，几千个函数方法。

![img](https://img-blog.csdnimg.cn/20181211154500288.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 解压压缩包，并且进入 目录，素质三连。

```bash
tar -zxvf PyQt-gpl-5.7.tar.gz     
cd PyQt-gpl-5.7     
python3 configure.py     
sudo make     
sudo make install     
```

在PyQt安装完毕后可以验证一下，在python环境下导入PyQt5库没有报错即可。尽量使用源码安装，这样出现问题可以比较直观的看到并解决。pip也可以一站式安装，直接安装 PyQt5 ，会把sip pyqt5 qscintill全都安装上，但是基本上无法排错，一个进度条走完全部听天由命。

 ![img](https://img-blog.csdnimg.cn/20181211154842632.jpg)



## 7. 安装 qscintilla/Designer

```bash
cd QScintilla-gpl-2.9.3/designer-Qt4Qt5     
qmake designer.pro     
sudo make     
sudo make install     
```



## 8. 安装 qscintilla/Python

因为默认是在PyQt4环境进行配置，所以在配置命令上要加参数 --pyqt=PyQt5

```bash
cd QScintilla-gpl-2.9.3/Python     python3 configure.py --pyqt=PyQt5     sudo make     sudo make install    
```



## 9. 安装eric

这个非常重要！！！安装 SSL包。德班系列默认安装SSL1.1的包。但是QT使用的是SSL1.0的库，因此我们需要安装 1.0的SSL库。如果没有找到请升级下 apt-get 没有安装的后果是在运行eric6的时候会报错：

```
QSslSocket: cannot call unresolved function SSLv23_client_method
QSslSocket: cannot call unresolved function SSL_CTX_new
QSslSocket: cannot call unresolved function SSL_library_init
QSslSocket: cannot call unresolved function ERR_get_error
```



## 10. 安装SSL1.0库

```bash
sudo apt-get install libssl1.0-dev     
```

[下载eric6](https://sourceforge.net/projects/eric-ide/files/eric6/stable/)

 ![img](https://img-blog.csdnimg.cn/20181211155616323.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 下载最新的版本。解压下载包，之后键入 sudo eric6 就可以运行了。

```bash
tar -xzvf eric6-18.12.tar.gz     
cd  eric-18.12     
python3  install.py 
sudo eric6   
```

第一次运行要进行初始配置,自动补全和提示。

Editor -> Autocompletion -> QSintilla  勾选show single 和 Use fill-up characters

![img](https://img-blog.csdnimg.cn/20181211155847611.jpg)

 Editor -> Autocompletion     勾选 Automatic Completion Enabled

 ![img](https://img-blog.csdnimg.cn/20181211155926142.jpg)

Editor -> APIs

 ![img](https://img-blog.csdnimg.cn/20181211160151943.jpg)

 语言选择python3 类型选择 Eric6 Plugin

![img](https://img-blog.csdnimg.cn/20181211160232998.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 使用下列按键编译API进工具

![img](https://img-blog.csdnimg.cn/20181211160312938.jpg)

 选择 eric6 的 api

![img](https://img-blog.csdnimg.cn/20181211160345709.jpg)

 点击compile APIs 开始编译

![img](https://img-blog.csdnimg.cn/20181211160416498.jpg)

 同样配置PyQt5 GUI

![img](https://img-blog.csdnimg.cn/20181211160459360.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

 ![img](https://img-blog.csdnimg.cn/2018121116053328.jpg)

 最后配置多项目工作目录，默认是根目录，一般需要修改进自定义目录。

![img](https://img-blog.csdnimg.cn/20181211160622236.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

配置完成后就可以使用了。