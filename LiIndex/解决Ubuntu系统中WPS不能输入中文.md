## 写在前面

### 1. Ubuntu18.04 GNOME下fcitx不能输入中文，搜狗拼音当然失效

- [引用](https://forum.ubuntu.org.cn/posting.php?mode=quote&f=8&p=3215852&sid=8b21402c4c059919a7c69f3683694f9f)

如题我是安装的Ubuntu 1804.2版之后有安装了gnome界面，登录界面我可以选择

+ `gnome `
+ `在xrog的gnome `
+ `Ubuntu`
+ `Ubuntu on wayland`

登录时选择了第一项`gnome`选项。进入发下我的emacs和wps竟然不能使用搜狗拼音了！
开始以为是搜狗拼音bug，经过仔细观察发现不是搜狗拼音。而是整个fcitx输入不能在wps 和 emacs中用。

+ 考虑是IBus干扰，彻底删了IBus， purge了 一遍。重装fcitx和sogo 问题依旧。
+ 无奈之下选择了网上大能的神通，设置中文utf8，声明变量`(见下文)`，完全无效。
+ 所有方法都试过了问题依旧！
+ 所有方法都试过了问题依旧！
  无意中切换登录界面到 `Ubuntu` ，进入后发现一切正常。
  切换回`gnome`问题回来了，
  切换`在xrog的gnome` 选项 ，输入法又可以用了。
  切换 `Ubuntu on wayland `输入法又不行。



### 2. 总结

+ 在登录中的 `gnome `和 `Ubuntu on waylang` 中`fcitx`在某些程序不能运行。
+ 在 `Ubuntu` 和 `在xrog的gnome` fcitx 一切正常。



### ３. 区别

这四种登录界面有什么区别，我目测没有发现有什么不同。折腾许久终于明白了：
+ `Ubuntu on wayland `: 是gnome新提出的一个界面，它的改动大，很多软件在他运行下会出问题。最大的改动就是配置文件改动后引起sogo不能用。
+ `在xrog的gnome`: 选项比较成熟兼容性好。推荐新手选用。
+ `Ubuntu`: 就是Ubuntu自己的界面实际我觉得也很好，但是Ubuntu不在支持了从1804开始。
+  `在xrog的gnome`: 经典gnome兼容gnome老版本。

搜狗不能用的原因是fcitx不能用。是因为` ～/.xprofiles `配置在`way land`中不起作用。
只要在`～/.pam_environment` 中加入如下内容，删除`.xprofiles`即可。

```bash
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```


就可以在`way land`使用，同时不影响在`xorg`中使用。







## 解决Ubuntu系统中WPS不能输入中文

打开WPS的文档，**右上角的输入法已经是中文了**，但是实际输入的时候，只能输入英文字母，出不了中文

### 1. WPS 文字

+ 在终端输入：

```bash
sudo gedit /usr/bin/wps
```

+ 出现`sudo gedit 错误：Gtk-WARNING **: cannot open display: :0.0`解决办法见后文

+ 从第二行加上：

```bash
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
gOpt=#gOptExt=-multiplygTemplateExt=("wpt" "dot" "dotx")**
```

![1573124208699](/home/lichenguang/.config/Typora/typora-user-images/1573124208699.png)



### 2. WPS 表格

+ 在终端输入：

```bash
sudo gedit/usr/bin/et
```

+　第二行加上：

```bash
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
gOpt=#gOptExt=-multiply
```

![1573124308928](/home/lichenguang/.config/Typora/typora-user-images/1573124308928.png)



### 3. WPS演示
+ 打开终端输入：

```bash
sudo vim /usr/bin/wpp
```

+ 添加以下文字到打开的文本中（添加到“#!/bin/bash”下面）：

```bash
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE="fcitx"
```



### 4. 重启WPS

+ 然后就可以输入中文了



##  sudo gedit 错误：Gtk-WARNING **: cannot open display: :0.0

**原因：**

当使用su 到另外一个用户运行某个程序，而这个程序又要有图形显示的时候，就有可能有下面提示：

```bash
No protocol specified
(gedit:2144): Gtk-WARNING **: cannot open display: :0
```

**解决方法：**

这是因为`Xserver`默认情况下不允许别的用户的图形程序的图形显示在当前屏幕上. 如果需要别的用户的图形显示在当前屏幕上, 则应以当前登陆的用户, 也就是切换身份前的用户执行如下命令。

```bash
xhost +
```

通过执行这条命令，就授予了其它用户访问当前屏幕的权限，于是就可以以另外的用户运行需要运行的程序了。









