# GNOME Shell 扩展

本质上讲，GNOME Shell 拓展是增强 GNOME 桌面的一小段代码，以插件的形式呈现给用户，就像你使用的浏览器，可以安装一些去广告的插件一样。所以这些拓展本身是没有自带的，需要用户根据自己的喜欢安装。

GNOME Shell 通常是安装在 GNOME 桌面系统之上的第三方组件和插件，主要是为了完成某个特定的功能，比如显示网速，显示天气，显示系统信息等。



## 1. 安装gnome-tweaks

安装：

 ```bash
sudo apt-get install gnome-tweaks
 ```



打开它，点到 extensions 菜单上，如下图：

![img](https://pic1.zhimg.com/80/v2-0e718655ed1944c61e8986a00fc1ca44_hd.jpg)

这里默认就有两个 Ubuntu 系统自带的拓展了，一个是在顶部状态栏显示运行的程序图标，一个是 Ubuntu 默认的 dock。



## 2. 使用 Ubuntu 自带的拓展集安装

我们先打开终端，安装如下软件包：gnome-shell-extensions。

```bash
sudo apt-get install gnome-shell-extensions
```

![image-20191218223024654](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218223024654.png)

安装完后需要重启电脑才能生效，重启电脑后，我们打开 gnome-tweaks 软件，再点到 extensions 菜单，你会发现这个时候多出了很多拓展插件。



## 3. 安装常用扩展

### 1)、Dash To Dock

+   Dock栏

+   只需要安装 Dash To Dock，您的全部 Dash 偏好设置都将以 dock 形式呈现以供访问。Dash To Dock 可以显示在屏幕左侧、右侧或者底部，甚至能够自动隐藏。要对其进行设置，右键点击九方形网格图标（即显示应用按钮）即可。

![image-20191218223405683](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218223405683.png)



### 2)、Clipboard Indicator

+   剪贴板历史

在安装之后，Clipboard Indicator 会出现在顶部面板当中，用以提供曾经复制至剪贴板的全部历史记录。只需要点击该标识而后选择要使用的文本内容（如图二），再配合 `Ctrl+V` 即可完成历史文本复制。

![image-20191218223725767](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218223725767.png)



### 3)、Drop Down Terminal

如果大家仍然需要使用终端，那么在 GNOME Shell 中完全可以使用对应的扩展实现此类功能。Drop Down Terminal 提供一套可快速切换的终端，且可自屏幕上方（见图三）或者下方直接弹出。这种便捷的终端使用体验绝对能够让生产力上升一个层级。

![图三：Drop Down Terminal使用图](https://img.linux.net.cn/data/attachment/album/201609/22/171020ud8cs2234ws3iy8o.png)



### 4)、Coverflow Alt-Tab

尽管这项扩展并没有太多实效性可言，但却能够以更为高效的方式完成当前窗口滚动。如果大家按下 `Alt+Tab`，该扩展将以 coverflow 风格打开容器。



![图四：Coverflow风格能够让已打开的应用更易于往来滚动](https://img.linux.net.cn/data/attachment/album/201609/22/171023rxlwchpqt5758xtl.png)



### 5)、Recent Items

如果大家需要经常访问最近打开过的文件，则 Recent Items 正是各位乐见的扩展。此项扩展会在 GNOME 面板中添加一个快捷按钮，大家可以点击以查看最近使用过的文件（见图五）。直接点击对应条目即可将其重新打开。

![图五：快速访问最近打开的条目](https://img.linux.net.cn/data/attachment/album/201609/22/171025htt7bt98ztjtgyie.png)



### 6)、Places Status Indicator

如果大家希望利用下拉菜单快速返回驱动器上的常用位置（见图六），Places Status Indicator 绝对不容错过。这项扩展能够帮助大家快速访问 Home、图片、视频、文档、下载、音乐、计算机以及其他任何云盘及网络位置。

![图六：点击一个位置，大家的文件管理器会自动打开与之对应的启动点或者文件夹](https://img.linux.net.cn/data/attachment/album/201609/22/171029j7zr9qk3yq475k44.png)



### 7)、Easy Screen Cast

如果大家需要轻松在 GNOME 桌面中进行视频/音频截取，这项扩展必须一试。只需要安装 Easy Screen Cast，问题将迎刃而解。

大家甚至能够将视频文件格式变更为 MP4、WebM、Mkv 或者 Ogg。利用 Easy Screen Cast，大家只需要点击相机图标并点击 Start Recording（见图七）即可。在完成后，再次点击该图标并选择 Stop Recording。

![图七：Easy Screen Cast 堪称最为便捷的桌面视频截取工具](https://img.linux.net.cn/data/attachment/album/201609/22/171033pa443ka223gg2i3k.png)



### 8)、Dynamic Top Bar

+   顶栏透明效果

+   利用 Dynamic Top Bar，顶栏会在不存在最大化窗口时以透明方式显示（见图八）。而在对窗口进行最大化后，顶栏会重新出现供我们使用。

![图八：Dynamic Top Bar 让 GNOME 桌面的外观更为清爽](https://img.linux.net.cn/data/attachment/album/201609/22/171037iqzzypgeprvbmopl.png)



### 9)、Top Panel Workspace Scroll

自从开始使用 Linux 以来，我发现这套桌面的最佳特性就是能够提供高效的工作区。过去我们能够快速在不同工作区间往来切换，但如今的新版本却放弃了这一重要特性。好在 Top Panel Workspace Scroll 能够帮助我们重拾这一功能，通过鼠标滚轮或者触摸板双指操作完成工作区切换。



### 10). Applications menu

+   应用程序菜单

+   该插件将Ubuntu左上角的活动变成了应用程序菜单，效果颇像elementary OS。

![image-20191218224119152](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218224119152.png)



### 11). Auto move windows

该插件通过设置可以自动将打开的应用按照设置移动到指定的工作区。

![image-20191218224641407](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218224641407.png)



### 12). Bluetooth quick connect

+    快速连接蓝牙设备，插件会在蓝牙开关下显示最近连接的设备。

![image-20191218225032983](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218225032983.png)



### 13). Blyr

+   添加状态栏(顶栏)背景模糊效果，和`Dynamic Top Bar`效果相反，

![image-20191218225207730](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218225207730.png)



### 14). Dash to panel

+   会将顶栏变成类似于为windows的状态栏，

![image-20191218225413120](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218225413120.png)



### 15) Files menu

+   顶栏文件浏览器

![image-20191218225715597](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218225715597.png)



### 16).  Netspeed

+   在顶栏显示网速



### 17). Simple net speed

+   网速扩展



### 18). Openweather

+   天气插件

![image-20191218225949489](GNOME-Shell%E6%89%A9%E5%B1%95.assets/image-20191218225949489.png)

