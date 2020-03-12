# Ubuntu 18.04 配置PyQt5开发环境

## 1. 准备软件

### 1.1. 确认Python版本

+ 首先确认下Python的版本，需要安装python3+。

![1573294425542](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221538.png)



+ 我们安装一个额外Python包 python3-dev 这个包包含了一系列的头文件和静态库。

```bash
sudo apt-get install python3-dev
```



### 1.2. 安装Qt

可以去[官网下载](https://www.qt.io/download#section-3)(记住下载页面右边的开源版本,这是免费的)下载你对应平台的包。

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

 

 安装需要一个Qt账号。没有也可以跳过，不影响任何安装结果。

 ![img](https://img-blog.csdnimg.cn/20181211152138825.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)



后面安装界面√记得都打上。要不就装了个工具可就尴尬了。安装完毕后可以打开 Qt Creator 就算安装成功了。

 ![img](https://img-blog.csdnimg.cn/20181211152252841.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N5c2h6YnR0,size_16,color_FFFFFF,t_70)

(可选) 安装完成后需要将Qt5的环境变量加进去。修改 bash配置文件 在最后添加图中字段(大小写敏感）。

```bash
vi  ~/.bashrc 
```

这些目录可以ls找到后黏贴进来。为了防止无脑黏贴造成系统问题，我仅放了图片。

 ![img](https://img-blog.csdnimg.cn/20181211152947640.jpg)

重新打开终端，打qm 按tab键补全能出现Qt命令即可。比如qmake



### 1.3. 安装SIP

SIP主要为Python生成C++接口代码提供了支持，毕竟QT是基于C的软件。我选择了 sip-4.18.1，参考了网上的成功案例，因为SIP这个工具非常敏感，不同的版本一旦出现不兼容，会引起大量的未知问题。所以尽量以成功案例为基础下载相应版本，我曾经下载了4.19，还有使用pip3安装 pyqt.sip 都废了，浪费了大量的时间。

sip属于python依赖库,我们直接使用命令安装即可.

```bash
pip3 install sip
```

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



### 1.4. 安装PIP3

因为ubuntu默认没有安装 pip3 所以我们还要安装一下，之后要用。

```bash
sudo  apt-get  install  python3-pip
```

 

### 1.5. 安装PyQt5

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



## 2. 配置开发环境

### 2.1 VS Code + PyQt5

去VS Code扩展商店安装PYQT扩展包

![1573295603612](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221539.png)

按照要求做下配置，这里需要在设置里配置`pyqt-integration.qtdesigner.path`、`pyqt-integration.pyuic.cmd`两个地方，

+ `pyqt-integration.qtdesigner.path`：designer的路径,
+ `pyqt-integration.pyuic.cmd`：uic程序的路径,

![1573295688412](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221540.png)

+ 我这里用的是anaconda3，

```json
{
    "python.pythonPath": "/home/user/anaconda3/bin/python",
    "pyqt-integration.qtdesigner.path": "/home/user/anaconda3/bin/designer",
    // 实际使用中，调用程序生成了C代码，在settings文件里留空，
    // VS Code设置里填pyuic5即可。
   // "pyqt-integration.pyuic.cmd": "/home/user/anaconda3/bin/uic"
}
```

+ qt5默认路径

```json
{
    "pyqt-integration.qtdesigner.path": "/home/user/Qt5.11.3/5.11.3/gcc_64/bin/designer",
    //"或者/usr/lib/qt5/bin/designer"
    "pyqt-integration.pyuic.cmd": "/home/user/Qt5.11.3/5.11.3/gcc_64/bin/uic"
    //"或者/usr/lib/qt5/bin/uic"
}
```

之后在`.ui`文件上右击即可调出`PYQT`命令。

+ 设置`-x`参数，默认生成Python测试函数

![1574670884339](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221541.png)

这样会在生成的`py`文件里添加调用函数：

```python
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = AdminPage()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

```



### 2.2 Pycharm + PyQt5

打开`File`——`Setting`——`Tools`——`External Tools`，添加如下配置：

![1573296505734](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221542.png)

**添加designer：**

![1573296593983](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221543.png)

+ `Name`、`Group`、`Description`可以自由写；
+ `Program`：填写`designer`的路径，同`VS Code填写的路径`
+ `Arguments`：填写`$FileName$`，固定值；
+ `Working directory`：工作路径，`$ProjectFileDir$`表示生成文件在工作区里，

**添加PyUIC**:

![1573296923844](https://gitee.com//chendemo12/FigureBed/raw/master//PicGo//20200312221544.png)

+ `Name`、`Group`、`Description`可以自由写；
+ `Program`：填写`Python`的路径，比如anaconda——`/home/userg/anaconda3/bin/python3.7`；
+ `Arguments`：填写`-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`，固定值；
+ `Working directory`：工作路径，`$FileDir$`；

之后在`.ui`文件上右击即可调出`PYQT`命令。

