# PyQt5开发文档



[TOC]

## PyQt5 简介

本教程的目的是带领你入门 PyQt5。教程内所有代码都在 Linux 上测试通过。[PyQt4 教程](http://zetcode.com/gui/pyqt4/)是 PyQt4 的教程，PyQt4 是一个 Python（同时支持 2 和 3）版的 Qt 库。

### 关于 PyQt5

PyQt5 是 Digia 的一套 Qt5 应用框架与 python 的结合，同时支持 2.x 和 3.x。本教程使用的是 3.x。Qt 库由 Riverbank Computing 开发，是最强大的 GUI 库之一 ，官方网站：www.riverbankcomputing.co.uk/news。

PyQt5 是由一系列 Python 模块组成。超过 620 个类，6000 函数和方法。能在诸如 Unix、Windows 和 Mac OS 等主流操作系统上运行。PyQt5 有两种证书，GPL 和商业证书。

PyQt5 类分为很多模块，主要模块有：

- QtCore 包含了核心的非 GUI 的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime 类文件、进程与线程一起使用。
- QtGui 包含了窗口系统、事件处理、2D 图像、基本绘画、字体和文字类。
- QtWidgets 类包含了一系列创建桌面应用的 UI 元素。 

+ QtMultimedia 包含了处理多媒体的内容和调用摄像头 API 的类。 
+ QtBluetooth 模块包含了查找和连接蓝牙的类。 
+ QtNetwork 包含了网络编程的类，这些工具能让 TCP/IP 和 UDP 开发变得更加方便和可靠。 
+ QtPositioning 包含了定位的类，可以使用卫星、WiFi 甚至文本。 
+ Engine 包含了通过客户端进入和管理 Qt Cloud 的类。 
+ QtWebSockets 包含了 WebSocket 协议的类。 
+ QtWebKit 包含了一个基 WebKit2 的 web 浏览器。 
+ QtWebKitWidgets 包含了基于 QtWidgets 的 WebKit1 的类。 
+ QtXml 包含了处理 xml 的类，提供了 SAX 和 DOM API 的工具。 
+ QtSvg 提供了显示 SVG 内容的类，Scalable Vector Graphics (SVG) 是一种是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式（这句话来自于维基百科）。 
+ QtSql 提供了处理数据库的工具。 
+ QtTest 提供了测试 PyQt5 应用的工具。

### PyQt4 和 PyQt5 的区别

**PyQt5 不兼容 PyQt4**。PyQt5 有一些巨大的改进。但是，迁移并不是很难，两者的区别如下：

- 重新组合模块，一些模块已经被废弃 (QtScript)，有些被分为两个子模块 (QtGui, QtWebKit)。
- 添加了新的模块，比如 QtBluetooth, QtPositioning，和 Enginio。
- 废弃了 SINGAL () 和 SLOT () 的调用方式，使用了新的信号和 xx 处理方式。
- 不再支持被标记为废弃的或不建议使用的 API。



## 第一个实例：Hello World

### 本章学习 Qt 的基本功能

### 例 1，简单的窗口

这个简单的小例子展示的是一个小窗口。但是我们可以在这个小窗口上面做很多事情，改变大小，最大化，最小化等，这需要很多代码才能实现。这在很多应用中很常见，没必要每次都要重写这部分代码，Qt 已经提供了这些功能。PyQt5 是一个高级的工具集合，相比使用低级的工具，能省略上百行代码。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create a simple
window in PyQt5.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
```

运行上面的代码，能展示出一个小窗口。

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
```

这里引入了 PyQt5.QtWidgets 模块，这个模块包含了基本的组件。

```python
app = QApplication(sys.argv)
```

每个 PyQt5 应用都必须创建一个应用对象。sys.argv 是一组命令行参数的列表。Python 可以在 shell 里运行，这个参数提供对脚本控制的功能。

```
w = QWidget()
```

QWidge 控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。

```
w.resize(250, 150)
```

resize () 方法能改变控件的大小，这里的意思是窗口宽 250px，高 150px。

```
w.move(300, 300)
```

move () 是修改控件位置的的方法。它把控件放置到屏幕坐标的 (300, 300) 的位置。注：屏幕坐标系的原点是屏幕的左上角。

```
w.setWindowTitle('Simple')
```

我们给这个窗口添加了一个标题，标题在标题栏展示（虽然这看起来是一句废话，但是后面还有各种栏，还是要注意一下，多了就蒙了）。

```
w.show()
```

show () 能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。

```
sys.exit(app.exec_())
```

最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件传入到派发到应用控件里。当调用 `exit()` 方法或直接销毁主控件时，主循环就会结束。`sys.exit()` 方法能确保主循环安全退出。外部环境能通知主控件怎么结束。

`exec_()` 之所以有个下划线，是因为 `exec` 是一个 Python 的关键字。

程序预览：

![simple](https://maicss.gitbooks.io/pyqt5/content/images/1-simple.png)

### 例 2，带窗口图标

窗口图标通常是显示在窗口的左上角，标题栏的最左边。下面的例子就是怎么用 PyQt5 创建一个这样的窗口。

在某些环境下，图标显示不出来。如果你遇到了这个问题，看我在 Stackoverfolw 的[回答](https://stackoverflow.com/questions/44080247/pyqt5-does-now-show-icons/45439678#45439678)

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows an icon
in the titlebar of the window.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))        

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

前一个例子是使用的[过程式编程](https://www.wikiwand.com/zh/过程式编程)。Python 还支持[面向对象](https://www.wikiwand.com/zh/面向对象程序设计)的编程：

```
class Example(QWidget):

    def __init__(self):
        super().__init__()
        ...
```

面向对象编程最重要的三个部分是类 (class)、数据和方法。我们创建了一个类的调用，这个类继承自 `QWidget`。这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。`super()` 构造器方法返回父级的对象。`__init__()` 方法是构造器的一个方法。

```
self.initUI()
```

使用 `initUI()` 方法创建一个 GUI。

```
# 自己准备一个web.png
self.setGeometry(300, 300, 300, 220)
self.setWindowTitle('Icon')
self.setWindowIcon(QIcon('web.png'))
```

上面的三个方法都继承自 `QWidget` 类。`setGeometry()` 有两个作用：把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的 x、y 和窗口大小的宽、高。也就是说这个方法是 `resize()` 和 `move()` 的合体。最后一个方法是添加了图标。先创建一个 QIcon 对象，然后接受一个路径作为参数显示图标。

```
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

应用和示例的对象创立，主循环开始。

程序预览：

![icon](https://maicss.gitbooks.io/pyqt5/content/images/1-icon.png)

### 例 3，提示框

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows a tooltip on 
a window and a button.

"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont    


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

在这个例子中，我们为应用创建了一个提示框。

```
QToolTip.setFont(QFont('SansSerif', 10))
```

这个静态方法设置了提示框的字体，我们使用了 10px 的 SansSerif 字体。

```
self.setToolTip('This is a <b>QWidget</b> widget')
```

调用 `setTooltip()` 创建提示框可以使用富文本格式的内容。

```
btn = QPushButton('Button', self)
btn.setToolTip('This is a <b>QPushButton</b> widget')
```

创建一个按钮，并且为按钮添加了一个提示框。

```
btn.resize(btn.sizeHint())
btn.move(50, 50)
```

调整按钮大小，并让按钮在屏幕上显示出来，`sizeHint()` 方法提供了一个默认的按钮大小。

程序预览：

![tooltip](https://maicss.gitbooks.io/pyqt5/content/images/1-tooltips.png)

### 例 4，关闭窗口

关闭一个窗口最直观的方式就是点击标题栏的那个叉，这个例子里，我们展示的是如何用程序关闭一个窗口。这里我们将接触到一点 single 和 slots 的知识。

本例使用的是 QPushButton 组件类。

```
QPushButton(string text, QWidget parent = None)
```

`text` 参数是想要显示的按钮名称，`parent` 参数是放在按钮上的组件，在我们的 例子里，这个参数是 `QWidget`。应用中的组件都是一层一层（继承而来的？）的，在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a quit
button. When we press the button,
the application terminates. 

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这里创建了一个点击之后就退出窗口的按钮。

```
from PyQt5.QtCore import QCoreApplication
```

程序需要 `QtCore` 对象。

```
qbtn = QPushButton('Quit', self)
```

创建一个继承自 `QPushButton` 的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自 `Qwidget` 的 `Example` 类。

```
qbtn.clicked.connect(QCoreApplication.instance().quit)
```

事件传递系统在 PyQt5 内建的 single 和 slot 机制里面。点击按钮之后，信号会被捕捉并给出既定的反应。`QCoreApplication` 包含了事件的主循环，它能添加和删除所有的事件，`instance()` 创建了一个它的实例。`QCoreApplication` 是在 `QApplication` 里创建的。 点击事件和能终止进程并退出应用的 quit 函数绑定在了一起。在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。

程序预览：

![quitbutton](https://maicss.gitbooks.io/pyqt5/content/images/1-quitbutton.png)

### 例 5，消息盒子

默认情况下，我们点击标题栏的 × 按钮，QWidget 就会关闭。但是有时候，我们修改默认行为。比如，如果我们打开的是一个文本编辑器，并且做了一些修改，我们就会想在关闭按钮的时候让用户进一步确认操作。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program shows a confirmation 
message box when we click on the close
button of the application window. 

"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

如果关闭 QWidget，就会产生一个 QCloseEvent。改变控件的默认行为，就是替换掉默认的事件处理。

```
reply = QMessageBox.question(self, 'Message',
    "Are you sure to quit?", QMessageBox.Yes | 
    QMessageBox.No, QMessageBox.No)
```

我们创建了一个消息框，上面有俩按钮：Yes 和 No. 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量 `reply` 里。

```
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()
```

这里判断返回值，如果点击的是 Yes 按钮，我们就关闭组件和应用，否者就忽略关闭事件。

程序预览：

![messagebox](https://maicss.gitbooks.io/pyqt5/content/images/1-messagebox.png)

### 例 6，窗口居中

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program centers a window 
on the screen. 
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')    
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

`QtGui.QDesktopWidget` 提供了用户的桌面信息，包括屏幕的大小。

```
self.center()
```

这个方法是调用我们下面写的，实现对话框居中的方法。

```
qr = self.frameGeometry()
```

得到了主窗口的大小。

```
cp = QDesktopWidget().availableGeometry().center()
```

获取显示器的分辨率，然后得到中间点的位置。

```
qr.moveCenter(cp)
```

然后把自己窗口的中心点放置到 qr 的中心点。

```
self.move(qr.topLeft())
```

然后把窗口的坐上角的坐标设置为 qr 的矩形左上角的坐标，这样就把窗口居中了。

程序预览：

![center](https://maicss.gitbooks.io/pyqt5/content/images/1-center.png)





## 菜单和工具栏

这个章节，我们会创建状态栏、菜单和工具栏。菜单是一组位于菜单栏的命令。工具栏是应用的一些常用工具按钮。状态栏显示一些状态信息，通常在应用的底部。

### 主窗口

`QMainWindow` 提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。

主窗口是下面这些窗口的合称，所以教程在最下方。

### 状态栏

状态栏是用来显示应用的状态信息的组件。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a statusbar.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

状态栏是由 QMainWindow 创建的。

```
self.statusBar().showMessage('Ready')
```

调用 `QtGui.QMainWindow` 类的 `statusBar()` 方法，创建状态栏。第一次调用创建一个状态栏，返回一个状态栏对象。`showMessage()` 方法在状态栏上显示一条信息。

程序预览：

 ![status](https://maicss.gitbooks.io/pyqt5/content/images/2-status.png)

### 菜单栏

菜单栏是非常常用的。是一组命令的集合（Mac OS 下状态栏的显示不一样，为了得到最相似的外观，我们增加了一句 `menubar.setNativeMenuBar(False)`)。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a menubar. The
menubar has one menu with an exit action.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了只有一个命令的菜单栏，这个命令就是终止应用。同时也创建了一个状态栏。而且还能使用快捷键 `Ctrl+Q` 退出应用。

```
exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
exitAct.setShortcut('Ctrl+Q')
exitAct.setStatusTip('Exit application')
```

`QAction` 是菜单栏、工具栏或者快捷键的动作的组合。前面两行，我们创建了一个图标、一个 exit 的标签和一个快捷键组合，都执行了一个动作。第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。

```
exitAct.triggered.connect(qApp.quit)
```

当执行这个指定的动作时，就触发了一个事件。这个事件跟 `QApplication的quit()` 行为相关联，所以这个动作就能终止这个应用。

```
menubar = self.menuBar()
fileMenu = menubar.addMenu('&File')
fileMenu.addAction(exitAct)
```

`menuBar()` 创建菜单栏。这里创建了一个菜单栏，并在上面添加了一个 file 菜单，并关联了点击退出应用的事件。

程序预览： ![menu](https://maicss.gitbooks.io/pyqt5/content/images/2-menu.png)



### 子菜单

子菜单是嵌套在菜单里面的二级或者三级等的菜单。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" 
This program creates a submenu.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)

        newAct = QAction('New', self)        

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子里，有两个子菜单，一个在 file 菜单下面，一个在 file 的 import 下面。

```
impMenu = QMenu('Import', self)
```

使用 `QMenu` 创建一个新菜单。

```
impAct = QAction('Import mail', self) 
impMenu.addAction(impAct)
```

使用 `addAction` 添加一个动作。

程序预览： ![submenu](https://maicss.gitbooks.io/pyqt5/content/images/2-submenu.png)

### 勾选菜单

下面是一个能勾选菜单的例子

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a checkable menu.
 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。

```
viewStatAct = QAction('View statusbar', self, checkable=True)
```

用 `checkable` 选项创建一个能选中的菜单。

```
viewStatAct.setChecked(True)
```

默认设置为选中状态。

```
def toggleMenu(self, state):

    if state:
        self.statusbar.show()
    else:
        self.statusbar.hide()
```

依据选中状态切换状态栏的显示与否。 程序预览：

![checkmenu](https://maicss.gitbooks.io/pyqt5/content/images/2-checkmenu.png)

### 右键菜单

右键菜单也叫弹出框（！？），是在某些场合下显示的一组命令。例如，Opera 浏览器里，网页上的右键菜单里会有刷新，返回或者查看页面源代码。如果在工具栏上右键，会得到一个不同的用来管理工具栏的菜单。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a context menu.
 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()


    def contextMenuEvent(self, event):

           cmenu = QMenu(self)

           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))

           if action == quitAct:
               qApp.quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

还是使用 `contextMenuEvent()` 方法实现这个菜单。

```
action = cmenu.exec_(self.mapToGlobal(event.pos()))
```

使用 `exec_()` 方法显示菜单。从鼠标右键事件对象中获得当前坐标。`mapToGlobal()` 方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。

```
if action == quitAct:
    qApp.quit()
```

如果右键菜单里触发了事件，也就触发了退出事件，执行关闭菜单行为。

程序预览：

![contextmenu](https://maicss.gitbooks.io/pyqt5/content/images/2-contextmenu.png)

### 工具栏

菜单栏包含了所有的命令，工具栏就是常用的命令的集合。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.
 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

上面的例子中，我们创建了一个工具栏。这个工具栏只有一个退出应用的动作。

```
exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
exitAct.setShortcut('Ctrl+Q')
exitAct.triggered.connect(qApp.quit)
```

和上面的菜单栏差不多，这里使用了一个行为对象，这个对象绑定了一个标签，一个图标和一个快捷键。这些行为被触发的时候，会调用 `QtGui.QMainWindow` 的 quit 方法退出应用。

```
self.toolbar = self.addToolBar('Exit')
self.toolbar.addAction(exitAct)
```

把工具栏展示出来。

程序预览：

![toolbar](https://maicss.gitbooks.io/pyqt5/content/images/2-toolbar.png)

### 主窗口

主窗口就是上面三种栏目的总称，现在我们把上面的三种栏在一个应用里展示出来。

> 首先要自己弄个小图标，命名为 exit24.png

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar, and a central widget. 
 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

上面的代码创建了一个很经典的菜单框架，有右键菜单，工具栏和状态栏。

```
textEdit = QTextEdit()
self.setCentralWidget(textEdit)
```

这里创建了一个文本编辑区域，并把它放在 `QMainWindow` 的中间区域。这个组件或占满所有剩余的区域。

程序预览：

![mainwindow](https://maicss.gitbooks.io/pyqt5/content/images/2-mainwindow.png)





## 布局管理

在一个 GUI 程序里，布局是一个很重要的方面。布局就是如何管理应用中的元素和窗口。有两种方式可以搞定：绝对定位和 PyQt5 的 layout 类

### 绝对定位

每个程序都是以像素为单位区分元素的位置，衡量元素的大小。所以我们完全可以使用绝对定位搞定每个元素和窗口的位置。但是这也有局限性：

- 元素不会随着我们更改窗口的位置和大小而变化。
- 不能适用于不同的平台和不同分辨率的显示器
- 更改应用字体大小会破坏布局
- 如果我们决定重构这个应用，需要全部计算一下每个元素的位置和大小

下面这个就是绝对定位的应用

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows three labels on a window
using absolute positioning. 
 
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)        

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们使用 move () 方法定位了每一个元素，使用 x、y 坐标。x、y 坐标的原点是程序的左上角。

```
lbl1 = QLabel('Zetcode', self)
lbl1.move(15, 10)
```

这个元素的左上角就在这个程序的左上角开始的 (15, 10) 的位置。

程序展示：

![Absolute positioning](https://maicss.gitbooks.io/pyqt5/content/images/3-absolute.png)

### 盒布局

使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。`QHBoxLayout` 和 `QVBoxLayout` 是基本的布局类，分别是水平布局和垂直布局。

如果我们需要把两个按钮放在程序的右下角，创建这样的布局，我们只需要一个水平布局加一个垂直布局的盒子就可以了。再用弹性布局增加一点间隙。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we position two push
buttons in the bottom-right corner 
of the window. 
 
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)    

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

上面的例子完成了在应用的右下角放了两个按钮的需求。当改变窗口大小的时候，它们能依然保持在相对的位置。我们同时使用了 `QHBoxLayout` 和 `QVBoxLayout`。

```
okButton = QPushButton("OK")
cancelButton = QPushButton("Cancel")
```

这是创建了两个按钮。

```
hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)
```

创建一个水平布局，增加两个按钮和弹性空间。stretch 函数在两个按钮前面增加了一些弹性空间。下一步我们把这些元素放在应用的右下角。

```
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)
```

为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面。弹性元素会把所有的元素一起都放置在应用的右下角。

```
self.setLayout(vbox)
```

最后，我们就得到了我们想要的布局。

程序预览：

![buttons](https://maicss.gitbooks.io/pyqt5/content/images/3-buttons.png)

### 栅格布局

最常用的还是栅格布局了。这种布局是把窗口分为行和列。创建和使用栅格布局，需要使用 QGridLayout 模块。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create a skeleton
of a calculator using a QGridLayout.
 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子里，我们创建了栅格化的按钮。

```
grid = QGridLayout()
self.setLayout(grid)
```

创建一个 QGridLayout 实例，并把它放到程序窗口里。

```
names = ['Cls', 'Bck', '', 'Close',
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+']
```

这是我们将要使用的按钮的名称。

```
positions = [(i,j) for i in range(5) for j in range(4)]
```

创建按钮位置列表。

```
for position, name in zip(positions, names):

    if name == '':
        continue
    button = QPushButton(name)
    grid.addWidget(button, *position)
```

创建按钮，并使用 `addWidget()` 方法把按钮放到布局里面。

程序预览：

![Calculator skeleton](https://maicss.gitbooks.io/pyqt5/content/images/3-calculator.png)

### 制作提交反馈信息的布局

组件能跨列和跨行展示，这个例子里，我们就试试这个功能。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create a more 
complicated window layout using
the QGridLayout manager. 
 
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid) 

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个有三个标签的窗口。两个行编辑和一个文版编辑，这是用 `QGridLayout` 模块搞定的。

```
grid = QGridLayout()
grid.setSpacing(10)
```

创建标签之间的空间。

```
grid.addWidget(reviewEdit, 3, 1, 5, 1)
```

我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨 5 行显示。

程序预览：

![review example](https://maicss.gitbooks.io/pyqt5/content/images/3-review.png)





## 事件和信号

### 事件

> signals and slots 被其他人翻译成信号和槽机制，(⊙o⊙)… 我这里还是不翻译好了。

所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件产生方式，比如网络的连接，窗口管理器或者定时器等。调用应用的 exec_() 方法时，应用会进入主循环，主循环会监听和分发事件。

在事件模型中，有三个角色：

- 事件源
- 事件
- 事件目标

事件源就是发生了状态改变的对象。事件是这个对象状态改变的内容。事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。

PyQt5 处理事件方面有个 signal and slot 机制。Signals and slots 用于对象间的通讯。事件触发的时候，发生一个 signal，slot 是用来被 Python 调用的（相当于一个句柄？这个词也好恶心，就是相当于事件的绑定函数）slot 只有在事件触发的时候才能调用。

### Signals & slots

下面是 signal & slot 的演示

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber. 
 
Last edited: January 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

上面的例子中，显示了 `QtGui.QLCDNumber` 和 `QtGui.QSlider` 模块，我们能拖动滑块让数字跟着发生改变。

```
sld.valueChanged.connect(lcd.display)
```

这里是把滑块的变化和数字的变化绑定在一起。

`sender` 是信号的发送者，`receiver` 是信号的接收者，`slot` 是对这个信号应该做出的反应。

程序展示：

![signal & slot](https://maicss.gitbooks.io/pyqt5/content/images/4-sigslot.png)

### 重构事件处理器

在 PyQt5 中，事件处理器经常被重写（也就是用自己的覆盖库自带的）。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we reimplement an 
event handler. 
 
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子中，我们替换了事件处理器函数 `keyPressEvent()`。

```
def keyPressEvent(self, e):

    if e.key() == Qt.Key_Escape:
        self.close()
```

此时如果按下 ESC 键程序就会退出。

程序展示：

这个就一个框，啥也没，就不展示了。

### 事件对象

事件对象是用 python 来描述一系列的事件自身属性的对象。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we display the x and y 
coordinates of a mouse pointer in a label widget.
 
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个示例中，我们在一个组件里显示鼠标的 X 和 Y 坐标。

```
self.text = "x: {0},  y: {1}".format(x, y)

self.label = QLabel(self.text, self)
```

X Y 坐标显示在 `QLabel` 组件里

```
self.setMouseTracking(True)
```

事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件。

```
def mouseMoveEvent(self, e):

    x = e.x()
    y = e.y()

    text = "x: {0},  y: {1}".format(x, y)
    self.label.setText(text)
```

`e` 代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。`x()` 和 `y()` 方法得到鼠标的 x 和 y 坐标点，然后拼成字符串输出到 `QLabel` 组件里。

程序展示：

![event object](https://maicss.gitbooks.io/pyqt5/content/images/4-eventobject.png)

### 事件发送

有时候我们会想知道是哪个组件发出了一个信号，PyQt5 里的 `sender()` 方法能搞定这件事。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we determine the event sender
object.
 
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子里有俩按钮，`buttonClicked()` 方法决定了是哪个按钮能调用 `sender()` 方法。

```
btn1.clicked.connect(self.buttonClicked)            
btn2.clicked.connect(self.buttonClicked)
```

两个按钮都和同一个 slot 绑定。

```
def buttonClicked(self):

    sender = self.sender()
    self.statusBar().showMessage(sender.text() + ' was pressed')
```

我们用调用 `sender()` 方法的方式决定了事件源。状态栏显示了被点击的按钮。

程序展示：

![event sender](https://maicss.gitbooks.io/pyqt5/content/images/4-eventsender.png)

### 信号发送

`QObject` 实例能发送事件信号。下面的例子是发送自定义的信号。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we show how to 
emit a custom signal. 
 
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):

    closeApp = pyqtSignal() 


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)       

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()


    def mousePressEvent(self, event):

        self.c.closeApp.emit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个叫 closeApp 的信号，这个信号会在鼠标按下的时候触发，事件与 `QMainWindow` 绑定。

```
class Communicate(QObject):

    closeApp = pyqtSignal()
```

`Communicate` 类创建了一个 `pyqtSignal()` 属性的信号。

```
self.c = Communicate()
self.c.closeApp.connect(self.close)
```

`closeApp` 信号 `QMainWindow` 的 `close()` 方法绑定。

```
def mousePressEvent(self, event):

    self.c.closeApp.emit()
```

点击窗口的时候，发送 closeApp 信号，程序终止。

程序展示：

这个也是啥也没。



## 对话框

对话框是一个现代 GUI 应用不可或缺的一部分。对话是两个人之间的交流，对话框就是人与电脑之间的对话。对话框用来输入数据，修改数据，修改应用设置等等。

### 输入文字

`QInputDialog` 提供了一个简单方便的对话框，可以输入字符串，数字或列表。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we receive data from
a QInputDialog dialog. 

Aauthor: Jan Bodnar 
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个示例有一个按钮和一个输入框，点击按钮显示对话框，输入的文本会显示在输入框里。

```
text, ok = QInputDialog.getText(self, 'Input Dialog',
    'Enter your name:')
```

这是显示一个输入框的代码。第一个参数是输入框的标题，第二个参数是输入框的占位符。对话框返回输入内容和一个布尔值，如果点击的是 OK 按钮，布尔值就返回 True。

```
if ok:
    self.le.setText(str(text))
```

把得到的字符串放到输入框里。

程序展示：

![input dialog](https://maicss.gitbooks.io/pyqt5/content/images/5-inputdialog.png)

### 选取颜色

QColorDialog 提供颜色的选择。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget. 
 
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        col = QColor(0, 0, 0) 

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

例子里有一个按钮和一个 `QFrame`，默认的背景颜色为黑色，我们可以使用 `QColorDialog` 改变背景颜色。

```
col = QColor(0, 0, 0)
```

初始化 `QtGui.QFrame` 的背景颜色。

```
col = QColorDialog.getColor()
```

弹出一个 `QColorDialog` 对话框。

```
if col.isValid():
    self.frm.setStyleSheet("QWidget { background-color: %s }"
        % col.name())
```

我们可以预览颜色，如果点击取消按钮，没有颜色值返回，如果颜色是我们想要的，就从取色框里选择这个颜色。

程序展示：

![color dialog](https://maicss.gitbooks.io/pyqt5/content/images/5-colordialog.png)

### 选择字体

`QFontDialog` 能做字体的选择。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we select a font name
and change the font of a label. 
 
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()


    def showDialog(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个有一个按钮和一个标签的 `QFontDialog` 的对话框，我们可以使用这个功能修改字体样式。

```
font, ok = QFontDialog.getFont()
```

弹出一个字体选择对话框。`getFont()` 方法返回一个字体名称和状态信息。状态信息有 OK 和其他两种。

```
if ok:
    self.label.setFont(font)
```

如果点击 OK，标签的字体就会随之更改。

程序展示：

![font dialog](https://maicss.gitbooks.io/pyqt5/content/images/5-fontdialog.png)

### 选择文件

`QFileDialog` 给用户提供文件或者文件夹选择的功能。能打开和保存文件。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.
 
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

本例中有一个菜单栏，一个置中的文本编辑框，一个状态栏。点击菜单栏选项会弹出一个 `QtGui.QFileDialog` 对话框，在这个对话框里，你能选择文件，然后文件的内容就会显示在文本编辑框里。

```
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
```

这里设置了一个文本编辑框，文本编辑框是基于 `QMainWindow` 组件的。

```
fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
```

弹出 `QFileDialog` 窗口。`getOpenFileName()` 方法的第一个参数是说明文字，第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。

```
if fname[0]:
    f = open(fname[0], 'r')

    with f:
        data = f.read()
        self.textEdit.setText(data)
```

读取选中的文件，并显示在文本编辑框内（但是打开 HTML 文件时，是渲染后的结果，汗）。

程序展示：

![file Dialog](https://maicss.gitbooks.io/pyqt5/content/images/5-filedialog.png)





## 控件 

控件就像是应用这座房子的一块块砖。PyQt5 有很多的控件，比如按钮，单选框，滑动条，复选框等等。在本章，我们将介绍一些很有用的控件：`QCheckBox`，`ToggleButton`，`QSlider`，`QProgressBar` 和 `QCalendarWidget`。

### QCheckBox

`QCheckBox` 组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, a QCheckBox widget
is used to toggle the title of a window.
 
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()


    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子中，有一个能切换窗口标题的单选框。

```
cb = QCheckBox('Show title', self)
```

这个是 `QCheckBox` 的构造器。

```
cb.toggle()
```

要设置窗口标题，我们就要检查单选框的状态。默认情况下，窗口没有标题，单选框未选中。

```
cb.stateChanged.connect(self.changeTitle)
```

把 `changeTitle()` 方法和 `stateChanged` 信号关联起来。这样，`changeTitle()` 就能切换窗口标题了。

```
def changeTitle(self, state):

    if state == Qt.Checked:
        self.setWindowTitle('QCheckBox')
    else:
        self.setWindowTitle('')
```

控件的状态是由 `changeTitle()` 方法控制的，如果空间被选中，我们就给窗口添加一个标题，如果没被选中，就清空标题。

程序展示：

![QCheckBox](https://maicss.gitbooks.io/pyqt5/content/images/6-qcheckbox.png)

### 切换按钮

切换按钮就是 `QPushButton` 的一种特殊模式。 它只有两种状态：按下和未按下。我们再点击的时候切换两种状态，有很多场景会使用到这个功能。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create three toggle buttons.
They will control the background color of a 
QFrame. 
 
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.col = QColor(0, 0, 0)       

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()


    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)                
        elif source.text() == "Green":
            self.col.setGreen(val)             
        else:
            self.col.setBlue(val) 

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个切换按钮和一个 `QWidget`，并把 `QWidget` 的背景设置为黑色。点击不同的切换按钮，背景色会在红、绿、蓝之间切换（而且能看到颜色合成的效果，而不是单纯的颜色覆盖）。

```
self.col = QColor(0, 0, 0)
```

设置颜色为黑色。

```
redb = QPushButton('Red', self)
redb.setCheckable(True)
redb.move(10, 10)
```

创建一个 `QPushButton`，然后调用它的 `setCheckable()` 的方法就把这个按钮编程了切换按钮。

```
redb.clicked[bool].connect(self.setColor)
```

把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值。

```
source = self.sender()
```

获取被点击的按钮。

```
if source.text() == "Red":
    self.col.setRed(val)
```

如果是标签为 “red” 的按钮被点击，就把颜色更改为预设好的对应颜色。

```
self.square.setStyleSheet("QFrame { background-color: %s }" %
    self.col.name())
```

使用样式表（就是 CSS 的 SS）改变背景色

程序展示：

![toggle button](https://maicss.gitbooks.io/pyqt5/content/images/6-togglebutton.png)

### 滑块

`QSlider` 是个有一个小滑块的组件，这个小滑块能拖着前后滑动，这个经常用于修改一些具有范围的数值，比文本框或者点击增加减少的文本框（spin box）方便多了。

本例用一个滑块和一个标签展示。标签为一个图片，滑块控制标签（的值）。

> 先弄个叫 mute.png 的静音图标准备着。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows a QSlider widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这里是模拟的音量控制器。拖动滑块，能改变标签位置的图片。

```
sld = QSlider(Qt.Horizontal, self)
```

创建一个水平的 `QSlider`。

```
self.label = QLabel(self)
self.label.setPixmap(QPixmap('mute.png'))
```

创建一个 `QLabel` 组件并给它设置一个静音图标。

```
sld.valueChanged[int].connect(self.changeValue)
```

把 `valueChanged` 信号跟 `changeValue()` 方法关联起来。

```
if value == 0:
    self.label.setPixmap(QPixmap('mute.png'))
...
```

根据音量值的大小更换标签位置的图片。这段代码是：如果音量为 0，就把图片换成 mute.png。

程序展示：

![QSlider widget](https://maicss.gitbooks.io/pyqt5/content/images/6-qslider.png)

### 进度条

进度条是用来展示任务进度的（我也不想这样说话）。它的滚动能让用户了解到任务的进度。`QProgressBar` 组件提供了水平和垂直两种进度条，进度条可以设置最大值和最小值，默认情况是 0~99。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows a QProgressBar widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们创建了一个水平的进度条和一个按钮，这个按钮控制进度条的开始和停止。

```
self.pbar = QProgressBar(self)
```

新建一个 `QProgressBar` 构造器。

```
self.timer = QtCore.QBasicTimer()
```

用时间控制进度条。

```
self.timer.start(100, self)
```

调用 `start()` 方法加载一个时间事件。这个方法有两个参数：过期时间和事件接收者。

```
def timerEvent(self, e):

    if self.step >= 100:

        self.timer.stop()
        self.btn.setText('Finished')
        return

    self.step = self.step + 1
    self.pbar.setValue(self.step)
```

每个 `QObject` 和又它继承而来的对象都有一个 `timerEvent()` 事件处理函数。为了触发事件，我们重载了这个方法。

```
def doAction(self):

    if self.timer.isActive():
        self.timer.stop()
        self.btn.setText('Start')

    else:
        self.timer.start(100, self)
        self.btn.setText('Stop')
```

里面的 `doAction()` 方法是用来控制开始和停止的。

程序展示：

![QProgressBar](https://maicss.gitbooks.io/pyqt5/content/images/6-qprogressbar.png)

### 日历

`QCalendarWidget` 提供了基于月份的日历插件，十分简易而且直观。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows a QCalendarWidget widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget, 
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):     

        self.lbl.setText(date.toString())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个例子有日期组件和标签组件组成，标签显示被选中的日期。

```
cal = QCalendarWidget(self)
```

创建一个 `QCalendarWidget`。

```
cal.clicked[QDate].connect(self.showDate)
```

选择一个日期时，`QDate` 的点击信号就触发了，把这个信号和我们自己定义的 `showDate()` 方法关联起来。

```
def showDate(self, date):     

    self.lbl.setText(date.toString())
```

使用 `selectedDate()` 方法获取选中的日期，然后把日期对象转成字符串，在标签里面显示出来。

程序展示：

![calendar](https://maicss.gitbooks.io/pyqt5/content/images/6-calendar.png)



### 图片

`QPixmap` 是处理图片的组件。本例中，我们使用 `QPixmap` 在窗口里显示一张图片。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we dispay an image
on the window. 
 
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
pixmap = QPixmap("redrock.png")
```

创建一个 `QPixmap` 对象，接收一个文件作为参数。

```
lbl = QLabel(self)
lbl.setPixmap(pixmap)
```

把 `QPixmap` 实例放到 `QLabel` 组件里。

程序展示：

![pixmap](https://maicss.gitbooks.io/pyqt5/content/images/7-pixmap.png)

### 行编辑

`QLineEdit` 组件提供了编辑文本的功能，自带了撤销、重做、剪切、粘贴、拖拽等功能。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows text which 
is entered in a QLineEdit
in a QLabel widget.
 
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

例子中展示了一个编辑组件和一个标签，我们在输入框里键入的文本，会立即在标签里显示出来。

```
qle = QLineEdit(self)
```

创建一个 `QLineEdit` 对象。

```
qle.textChanged[str].connect(self.onChanged)
```

如果输入框的值有变化，就调用 `onChanged()` 方法。

```
def onChanged(self, text):

    self.lbl.setText(text)
    self.lbl.adjustSize()
```

在 `onChanged()` 方法内部，我们把文本框里的值赋值给了标签组件，然后调用 `adjustSize()` 方法让标签自适应文本内容。

程序展示：

![QLineEdit](https://maicss.gitbooks.io/pyqt5/content/images/7-qlineedit.png)

### QSplitter

`QSplitter` 组件能让用户通过拖拽分割线的方式改变子窗口大小的组件。本例中我们展示用两个分割线隔开的三个 `QFrame` 组件。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows
how to use QSplitter widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, 
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

三个窗口和两个分割线的布局创建完成了，但是要注意，有些主题下，分割线的显示效果不太好。

```
topleft = QFrame(self)
topleft.setFrameShape(QFrame.StyledPanel)
```

为了更清楚的看到分割线，我们使用了设置好的子窗口样式。

```
splitter1 = QSplitter(Qt.Horizontal)
splitter1.addWidget(topleft)
splitter1.addWidget(topright)
```

创建一个 `QSplitter` 组件，并在里面添加了两个框架。

```
splitter2 = QSplitter(Qt.Vertical)
splitter2.addWidget(splitter1)
```

也可以在分割线里面再进行分割。

程序展示：

![QSplitter widget](https://maicss.gitbooks.io/pyqt5/content/images/7-qsplitter.png)

### 下拉选框

`QComboBox` 组件能让用户在多个选择项中选择一个。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows how to use 
a QComboBox widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

本例包含了一个 `QComboBox` 和一个 `QLabel`。下拉选择框有五个选项，都是 Linux 的发行版名称，标签内容为选定的发行版名称。

```
combo = QComboBox(self)
combo.addItem("Ubuntu")
combo.addItem("Mandriva")
combo.addItem("Fedora")
combo.addItem("Arch")
combo.addItem("Gentoo")
```

创建一个 `QComboBox` 组件和五个选项。

```
combo.activated[str].connect(self.onActivated)
```

在选中的条目上调用 `onActivated()` 方法。

```
def onActivated(self, text):

    self.lbl.setText(text)
    self.lbl.adjustSize()
```

在方法内部，设置标签内容为选定的字符串，然后设置自适应文本大小。

程序展示：

![QComboBox](https://maicss.gitbooks.io/pyqt5/content/images/7-qcombobox.png)



## 拖拽

在 GUI 里，拖放是指用户点击一个虚拟的对象，拖动，然后放置到另外一个对象上面的动作。一般情况下，需要调用很多动作和方法，创建很多变量。

拖放能让用户很直观的操作很复杂的逻辑。

一般情况下，我们可以拖放两种东西：数据和图形界面。把一个图像从一个应用拖放到另外一个应用上的实质是操作二进制数据。把一个表格从 Firefox 上拖放到另外一个位置 的实质是操作一个图形组。

### 简单的拖放

本例使用了 `QLineEdit` 和 `QPushButton`。把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a simple drag and
drop example. 

"""

from PyQt5.QtWidgets import (QPushButton, QWidget, 
    QLineEdit, QApplication)
import sys

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)


    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):

        self.setText(e.mimeData().text()) 


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)
```

为了完成预定目标，我们要重构一些方法。首先用 `QPushButton` 上构造一个按钮实例。

```
self.setAcceptDrops(True)
```

激活组件的拖拽事件。

```
def dragEnterEvent(self, e):

    if e.mimeData().hasFormat('text/plain'):
        e.accept()
    else:
        e.ignore()
```

首先，我们重构了 `dragEnterEvent()` 方法。设定好接受拖拽的数据类型（plain text）。

```
def dropEvent(self, e):

    self.setText(e.mimeData().text())
```

然后重构 `dropEvent()` 方法，更改按钮接受鼠标的释放事件的默认行为。

```
edit = QLineEdit('', self)
edit.setDragEnabled(True)
```

`QLineEdit` 默认支持拖拽操作，所以我们只要调用 `setDragEnabled()` 方法使用就行了。

程序展示：

![drag & drop](https://maicss.gitbooks.io/pyqt5/content/images/8-dragdrop.png)

### 拖放按钮组件

这个例子展示怎么拖放一个 button 组件。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this program, we can press on a button with a left mouse
click or drag and drop the button with  the right mouse click. 

"""

from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)


    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)


    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)


    def dragEnterEvent(self, e):

        e.accept()


    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
```

上面的例子中，窗口上有一个 `QPushButton` 组件。左键点击按钮，控制台就会输出 `press`。右键可以点击然后拖动按钮。

```
class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
```

从 `QPushButton` 继承一个 `Button` 类，然后重构 `QPushButton` 的两个方法:`mouseMoveEvent()` 和 `mousePressEvent()`.`mouseMoveEvent()` 是拖拽开始的事件。

```
if e.buttons() != Qt.RightButton:
    return
```

我们只劫持按钮的右键事件，左键的操作还是默认行为。

```
mimeData = QMimeData()

drag = QDrag(self)
drag.setMimeData(mimeData)
drag.setHotSpot(e.pos() - self.rect().topLeft())
```

创建一个 `QDrag` 对象，用来传输 MIME-based 数据。

```
dropAction = drag.exec_(Qt.MoveAction)
```

拖放事件开始时，用到的处理函数式 `start()`.

```
def mousePressEvent(self, e):

    QPushButton.mousePressEvent(self, e)

    if e.button() == Qt.LeftButton:
        print('press')
```

左键点击按钮，会在控制台输出 “press”。注意，我们在父级上也调用了 `mousePressEvent()` 方法，不然的话，我们是看不到按钮按下的效果的。

```
position = e.pos()
self.button.move(position)
```

在 `dropEvent()` 方法里，我们定义了按钮按下后和释放后的行为，获得鼠标移动的位置，然后把按钮放到这个地方。

```
e.setDropAction(Qt.MoveAction)
e.accept()
```

指定放下的动作类型为 moveAction。

程序展示：

这个就一个按钮，没啥可展示的，弄 GIF 太麻烦了。





## 绘图

PyQt5 绘图系统能渲染矢量图像、位图图像和轮廓字体文本。一般会使用在修改或者提高现有组件的功能，或者创建自己的组件。使用 PyQt5 的绘图 API 进行操作。

绘图由 `paintEvent()` 方法完成，绘图的代码要放在 `QPainter` 对象的 `begin()` 和 `end()` 方法之间。是低级接口。

### 文本涂鸦

我们从画一些 Unicode 文本开始。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we draw text in Russian Cylliric.
 
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')
        self.show()


    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()


    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

写了一些文本上下居中对齐的俄罗斯 Cylliric 语言的文字。

```
def paintEvent(self, event):
...
```

在绘画事件内完成绘画动作。

```
qp = QPainter()
qp.begin(self)
self.drawText(event, qp)
qp.end()
```

`QPainter` 是低级的绘画类。所有的绘画动作都在这个类的 `begin()` 和 `end()` 方法之间完成，绘画动作都封装在 `drawText()` 内部了。

```
qp.setPen(QColor(168, 34, 3))
qp.setFont(QFont('Decorative', 10))
```

为文字绘画定义了笔和字体。

```
qp.drawText(event.rect(), Qt.AlignCenter, self.text)
```

`drawText()` 方法在窗口里绘制文本，`rect()` 方法返回要更新的矩形区域。

程序展示：

![drawing text](https://maicss.gitbooks.io/pyqt5/content/images/9-drawtext.png)

### 点的绘画

点是最简单的绘画了。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In the example, we draw randomly 1000 red points 
on the window.
 
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):

        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)     


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们在窗口里随机的画出了 1000 个点。

```
qp.setPen(Qt.red)
```

设置笔的颜色为红色，使用的是预定义好的颜色。

```
size = self.size()
```

每次更改窗口大小，都会产生绘画事件，从 `size()` 方法里获得当前窗口的大小，然后把产生的点随机的分配到窗口的所有位置上。

```
qp.drawPoint(x, y)
```

`drawPoint()` 方法绘图。

程序展示：

![points](https://maicss.gitbooks.io/pyqt5/content/images/9-points.png)



## 颜色

颜色是一个物体显示的 RGB 的混合色。RBG 值的范围是 0~255。我们有很多方式去定义一个颜色，最常见的方式就是 RGB 和 16 进制表示法，也可以使用 RGBA，增加了一个透明度的选项，透明度值的范围是 0~1，0 代表完全透明。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example draws three rectangles in three
#different colours. 
 
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, qp):

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们画出了三个颜色的矩形。

```
color = QColor(0, 0, 0)
color.setNamedColor('#d4d4d4')
```

使用 16 进制的方式定义一个颜色。

```
qp.setBrush(QColor(200, 0, 0))
qp.drawRect(10, 15, 90, 60)
```

定义了一个笔刷，并画出了一个矩形。笔刷是用来画一个物体的背景。`drawRect()` 有四个参数，分别是矩形的 x、y、w、h。 然后用笔刷和矩形进行绘画。

程序展示：

![colours](https://maicss.gitbooks.io/pyqt5/content/images/9-colours.png)

### QPen

`QPen` 是基本的绘画对象，能用来画直线、曲线、矩形框、椭圆、多边形和其他形状。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example we draw 6 lines using
different pen styles. 
 
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()


    def drawLines(self, qp):

        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

在这个例子里，我们用不同的笔画了 6 条直线。PyQt5 有五个预定义的笔，另外一个笔的样式使我们自定义的。

```
pen = QPen(Qt.black, 2, Qt.SolidLine)
```

新建一个 `QPen` 对象，设置颜色黑色，宽 2 像素，这样就能看出来各个笔样式的区别。`Qt.SolidLine` 是预定义样式的一种。

```
pen.setStyle(Qt.CustomDashLine)
pen.setDashPattern([1, 4, 5, 4])
qp.setPen(pen)
```

这里我们自定义了一个笔的样式。定义为 `Qt.CustomDashLine` 然后调用 `setDashPattern()` 方法。数字列表是线的样式，要求必须是个数为奇数，奇数位定义的是空格，偶数位为线长，数字越大，空格或线长越大，比如本例的就是 1 像素线，4 像素空格，5 像素线，4 像素空格。

程序展示：

![pen styles](https://maicss.gitbooks.io/pyqt5/content/images/9-penstyles.png)

### QBrush

`QBrush` 也是图像的一个基本元素。是用来填充一些物体的背景图用的，比如矩形，椭圆，多边形等。有三种类型：预定义、渐变和纹理。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example draws nine rectangles in different
brush styles.
 
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()


    def drawBrushes(self, qp):

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

我们画了 9 个不同的矩形。

```
brush = QBrush(Qt.SolidPattern)
qp.setBrush(brush)
qp.drawRect(10, 15, 90, 60)
```

创建了一个笔刷对象，添加笔刷样式，然后调用 `drawRect()` 方法画图。

程序展示：

![brushes](https://maicss.gitbooks.io/pyqt5/content/images/9-brushes.png)

### 贝塞尔曲线

噩梦可以使用 PyQt5 的 `QPainterPath` 创建贝塞尔曲线。绘画路径是由许多构建图形的对象，具体表现就是一些线的形状，比如矩形，椭圆，线和曲线。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program draws a Bézier curve with 
QPainterPath.
 
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()


    def drawBezierCurve(self, qp):

        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        qp.drawPath(path)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这个示例中，我们画出了一个贝塞尔曲线。

```python
path = QPainterPath()
path.moveTo(30, 30)
path.cubicTo(30, 30, 200, 350, 350, 30)
```

用 `QPainterPath` 路径创建贝塞尔曲线。使用 `cubicTo()` 方法生成，分别需要三个点：起始点，控制点和终止点。

```python
qp.drawPath(path)
```

`drawPath()` 绘制最后的图像。



## 自定义控件

PyQt5 有丰富的组件，但是肯定满足不了所有开发者的所有需求，PyQt5 只提供了基本的组件，像按钮，文本，滑块等。如果你还需要其他的模块，应该尝试自己去自定义一些。

自定义组件使用绘画工具创建，有两个基本方式：根据已有的创建或改进；通过自己绘图创建。

### Burning widget

这个组件我们会在 Nero，K3B，或者其他 CD/DVD 烧录软件中见到。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create a custom widget.
 
"""

from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
    QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import sys

class Communicate(QObject):

    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):

    def __init__(self):      
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def drawWidget(self, qp):

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))


        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)


        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):

            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        OVER_CAPACITY = 750

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()        
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()


    def changeValue(self, value):

        self.c.updateBW.emit(value)        
        self.wid.repaint()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

本例中，我们使用了 `QSlider` 和一个自定义组件，由进度条控制。显示的有物体（也就是 CD/DVD）的总容量和剩余容量。进度条的范围是 1~750。如果值达到了 700（OVER_CAPACITY），就显示为红色，代表了烧毁了的意思。

烧录组件在窗口的底部，这个组件是用 `QHBoxLayout` 和 `QVBoxLayout` 组成的。

```python
class BurningWidget(QWidget):

    def __init__(self):      
        super().__init__()
```

基于 `QWidget` 组件。

```
self.setMinimumSize(1, 30)
```

修改组件进度条的高度，默认的有点小。

```
font = QFont('Serif', 7, QFont.Light)
qp.setFont(font)
```

使用比默认更小一点的字体，这样更配。

```
size = self.size()
w = size.width()
h = size.height()

step = int(round(w / 10.0))


till = int(((w / 750.0) * self.value))
full = int(((w / 750.0) * 700))
```

动态的渲染组件，随着窗口的大小而变化，这就是我们计算窗口大小的原因。最后一个参数决定了组件的最大范围，进度条的值是由窗口大小按比例计算出来的。最大值的地方填充的是红色。注意这里使用的是浮点数，能提高计算和渲染的精度。

绘画由三部分组成，黄色或红色区域和黄色矩形，然后是分割线，最后是添上代表容量的数字。

```
metrics = qp.fontMetrics()
fw = metrics.width(str(self.num[j]))
qp.drawText(i-fw/2, h/2, str(self.num[j]))
```

这里使用字体去渲染文本。必须要知道文本的宽度，这样才能让文本的中间点正好落在竖线上。

```
def changeValue(self, value):

    self.c.updateBW.emit(value)        
    self.wid.repaint()
```

拖动滑块的时候，调用了 `changeValue()` 方法。这个方法内部，我们自定义了一个可以传参的 updateBW 信号。参数就是滑块的当前位置。这个数值之后还用来于 Burning 组件，然后重新渲染 Burning 组件。

![burning widget](https://maicss.gitbooks.io/pyqt5/content/images/10-burning.png)



## 俄罗斯方块游戏

本章我们要制作一个俄罗斯方块游戏。

### Tetris

> 译注：称呼：方块是由四个小方格组成的

俄罗斯方块游戏是世界上最流行的游戏之一。是由一名叫 Alexey Pajitnov 的俄罗斯程序员在 1985 年制作的，从那时起，这个游戏就风靡了各个游戏平台。

俄罗斯方块归类为下落块迷宫游戏。游戏有 7 个基本形状：S、Z、T、L、反向 L、直线、方块，每个形状都由 4 个方块组成，方块最终都会落到屏幕底部。所以玩家通过控制形状的左右位置和旋转，让每个形状都以合适的位置落下，如果有一行全部被方块填充，这行就会消失，并且得分。游戏结束的条件是有形状接触到了屏幕顶部。

方块展示：

![tetrominoes](https://maicss.gitbooks.io/pyqt5/content/images/11-tetrominoes.png)

PyQt5 是专门为创建图形界面产生的，里面一些专门为制作游戏而开发的组件，所以 PyQt5 是能制作小游戏的。

制作电脑游戏也是提高自己编程能力的一种很好的方式。

### 开发

没有图片，所以就自己用绘画画出来几个图形。每个游戏里都有数学模型的，这个也是。

开工之前：

- 用 `QtCore.QBasicTimer()` 创建一个游戏循环
- 模型是一直下落的
- 模型的运动是以小块为基础单位的，不是按像素
- 从数学意义上来说，模型就是就是一串数字而已

代码由四个类组成：Tetris, Board, Tetrominoe 和 Shape。Tetris 类创建游戏，Board 是游戏主要逻辑。Tetrominoe 包含了所有的砖块，Shape 是所有砖块的代码。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a Tetris game clone.
 
"""

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys, random

class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):    
        '''initiates application UI'''

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()        
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')        
        self.show()


    def center(self):
        '''centers the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)


class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()


    def initBoard(self):     
        '''initiates board'''

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()


    def shapeAt(self, x, y):
        '''determines shape at the board position'''

        return self.board[(y * Board.BoardWidth) + x]


    def setShapeAt(self, x, y, shape):
        '''sets a shape at the board'''

        self.board[(y * Board.BoardWidth) + x] = shape


    def squareWidth(self):
        '''returns the width of one square'''

        return self.contentsRect().width() // Board.BoardWidth


    def squareHeight(self):
        '''returns the height of one square'''

        return self.contentsRect().height() // Board.BoardHeight


    def start(self):
        '''starts game'''

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)


    def pause(self):
        '''pauses game'''

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()


    def paintEvent(self, event):
        '''paints all shapes of the game'''

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):

                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())


    def keyPressEvent(self, event):
        '''processes key press events'''

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)


    def timerEvent(self, event):
        '''handles timer event'''

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)


    def clearBoard(self):
        '''clears shapes from the board'''

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)


    def dropDown(self):
        '''drops down a shape'''

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()


    def oneLineDown(self):
        '''goes one line down with a shape'''

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()


    def pieceDropped(self):
        '''after dropping shape, remove full lines and create new shape'''

        for i in range(4):

            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()


    def removeFullLines(self):
        '''removes all full lines from the board'''

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()


        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:

            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()


    def newPiece(self):
        '''creates a new shape'''

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):

            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")



    def tryMove(self, newPiece, newX, newY):
        '''tries to move a shape'''

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True


    def drawSquare(self, painter, x, y, shape):
        '''draws a square of a shape'''        

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):

    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):

        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)


    def shape(self):
        '''returns shape'''

        return self.pieceShape


    def setShape(self, shape):
        '''sets a shape'''

        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape


    def setRandomShape(self):
        '''chooses a random shape'''

        self.setShape(random.randint(1, 7))


    def x(self, index):
        '''returns x coordinate'''

        return self.coords[index][0]


    def y(self, index):
        '''returns y coordinate'''

        return self.coords[index][1]


    def setX(self, index, x):
        '''sets x coordinate'''

        self.coords[index][0] = x


    def setY(self, index, y):
        '''sets y coordinate'''

        self.coords[index][1] = y


    def minX(self):
        '''returns min x value'''

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m


    def maxX(self):
        '''returns max x value'''

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m


    def minY(self):
        '''returns min y value'''

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m


    def maxY(self):
        '''returns max y value'''

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m


    def rotateLeft(self):
        '''rotates shape to the left'''

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):

            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result


    def rotateRight(self):
        '''rotates shape to the right'''

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):

            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':

    app = QApplication([])
    tetris = Tetris()    
    sys.exit(app.exec_())
```

游戏很简单，所以也就很好理解。程序加载之后游戏也就直接开始了，可以用 P 键暂停游戏，空格键让方块直接落到最下面。游戏的速度是固定的，并没有实现加速的功能。分数就是游戏中消除的行数。

```
self.tboard = Board(self)
self.setCentralWidget(self.tboard)
```

创建了一个 Board 类的实例，并设置为应用的中心组件。

```
self.statusbar = self.statusBar()        
self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
```

创建一个 `statusbar` 来显示三种信息：消除的行数，游戏暂停状态或者游戏结束状态。`msg2Statusbar` 是一个自定义的信号，用在（和）Board 类（交互），`showMessage()` 方法是一个内建的，用来在 statusbar 上显示信息的方法。

```
self.tboard.start()
```

初始化游戏：

```
class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)
...
```

创建了一个自定义信号 `msg2Statusbar`，当我们想往 `statusbar` 里显示信息的时候，发出这个信号就行了。

```
BoardWidth = 10
BoardHeight = 22
Speed = 300
```

这些是 `Board` 类的变量。`BoardWidth` 和 `BoardHeight` 分别是 board 的宽度和高度。`Speed` 是游戏的速度，每 300ms 出现一个新的方块。

```
...
self.curX = 0
self.curY = 0
self.numLinesRemoved = 0
self.board = []
...
```

在 `initBoard()` 里初始化了一些重要的变量。`self.board` 定义了方块的形状和位置，取值范围是 0-7。

```
def shapeAt(self, x, y):
    return self.board[(y * Board.BoardWidth) + x]
```

`shapeAt()` 决定了 board 里方块的的种类。

```
def squareWidth(self):
    return self.contentsRect().width() // Board.BoardWidth
```

board 的大小可以动态的改变。所以方格的大小也应该随之变化。`squareWidth()` 计算并返回每个块应该占用多少像素 -- 也即 `Board.BoardWidth`。

```
def pause(self):
    '''pauses game'''

    if not self.isStarted:
        return

    self.isPaused = not self.isPaused

    if self.isPaused:
        self.timer.stop()
        self.msg2Statusbar.emit("paused")

    else:
        self.timer.start(Board.Speed, self)
        self.msg2Statusbar.emit(str(self.numLinesRemoved))

    self.update()
```

`pause()` 方法用来暂停游戏，停止计时并在 `statusbar` 上显示一条信息。

```
def paintEvent(self, event):
    '''paints all shapes of the game'''

    painter = QPainter(self)
    rect = self.contentsRect()
...
```

渲染是在 paintEvent () 方法里发生的 `QPainter` 负责 PyQt5 里所有低级绘画操作。

```
for i in range(Board.BoardHeight):
    for j in range(Board.BoardWidth):
        shape = self.shapeAt(j, Board.BoardHeight - i - 1)

        if shape != Tetrominoe.NoShape:
            self.drawSquare(painter,
                rect.left() + j * self.squareWidth(),
                boardTop + i * self.squareHeight(), shape)
```

渲染游戏分为两步。第一步是先画出所有已经落在最下面的的图，这些保存在 `self.board` 里。可以使用 `shapeAt()` 查看这个这个变量。

```
if self.curPiece.shape() != Tetrominoe.NoShape:

    for i in range(4):

        x = self.curX + self.curPiece.x(i)
        y = self.curY - self.curPiece.y(i)
        self.drawSquare(painter, rect.left() + x * self.squareWidth(),
            boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
            self.curPiece.shape())
```

第二步是画出更在下落的方块。

```
elif key == Qt.Key_Right:
    self.tryMove(self.curPiece, self.curX + 1, self.curY)
```

在 `keyPressEvent()` 方法获得用户按下的按键。如果按下的是右方向键，就尝试把方块向右移动，说尝试是因为有可能到边界不能移动了。

```
elif key == Qt.Key_Up:
    self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
```

上方向键是把方块向左旋转一下

```
elif key == Qt.Key_Space:
    self.dropDown()
```

空格键会直接把方块放到底部

```
elif key == Qt.Key_D:
    self.oneLineDown()
```

D 键是加速一次下落速度。

```
def tryMove(self, newPiece, newX, newY):

    for i in range(4):

        x = newX + newPiece.x(i)
        y = newY - newPiece.y(i)

        if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
            return False

        if self.shapeAt(x, y) != Tetrominoe.NoShape:
            return False

    self.curPiece = newPiece
    self.curX = newX
    self.curY = newY
    self.update()
    return True
```

`tryMove()` 是尝试移动方块的方法。如果方块已经到达 board 的边缘或者遇到了其他方块，就返回 False。否则就把方块下落到想要

```
def timerEvent(self, event):

    if event.timerId() == self.timer.timerId():

        if self.isWaitingAfterLine:
            self.isWaitingAfterLine = False
            self.newPiece()
        else:
            self.oneLineDown()

    else:
        super(Board, self).timerEvent(event)
```

在计时器事件里，要么是等一个方块下落完之后创建一个新的方块，要么是让一个方块直接落到底（move a falling piece one line down）。

```
def clearBoard(self):

    for i in range(Board.BoardHeight * Board.BoardWidth):
        self.board.append(Tetrominoe.NoShape)
```

`clearBoard(`) 方法通过 `Tetrominoe.NoShape` 清空 `broad`。

```
def removeFullLines(self):

    numFullLines = 0
    rowsToRemove = []

    for i in range(Board.BoardHeight):

        n = 0
        for j in range(Board.BoardWidth):
            if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                n = n + 1

        if n == 10:
            rowsToRemove.append(i)

    rowsToRemove.reverse()


    for m in rowsToRemove:

        for k in range(m, Board.BoardHeight):
            for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

    numFullLines = numFullLines + len(rowsToRemove)
 ...
```

如果方块碰到了底部，就调用 `removeFullLines()` 方法，找到所有能消除的行消除它们。消除的具体动作就是把符合条件的行消除掉之后，再把它上面的行下降一行。注意移除满行的动作是倒着来的，因为我们是按照重力来表现游戏的，如果不这样就有可能出现有些方块浮在空中的现象。

```
def newPiece(self):

    self.curPiece = Shape()
    self.curPiece.setRandomShape()
    self.curX = Board.BoardWidth // 2 + 1
    self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

    if not self.tryMove(self.curPiece, self.curX, self.curY):

        self.curPiece.setShape(Tetrominoe.NoShape)
        self.timer.stop()
        self.isStarted = False
        self.msg2Statusbar.emit("Game over")
```

`newPiece()` 方法是用来创建形状随机的方块。如果随机的方块不能正确的出现在预设的位置，游戏结束。

```
class Tetrominoe(object):

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7
```

`Tetrominoe` 类保存了所有方块的形状。我们还定义了一个 `NoShape` 的空形状。

Shape 类保存类方块内部的信息。

```
class Shape(object):

    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ...
    )
...
```

coordsTable 元组保存了所有的方块形状的组成。是一个构成方块的坐标模版。

```
self.coords = [[0,0] for i in range(4)]
```

上面创建了一个新的空坐标数组，这个数组将用来保存方块的坐标。

坐标系示意图：

![coordinates](https://maicss.gitbooks.io/pyqt5/content/images/11-coordinates.png)

上面的图片可以帮助我们更好的理解坐标值的意义。比如元组 `(0, -1), (0, 0), (-1, 0), (-1, -1)` 代表了一个 Z 形状的方块。这个图表就描绘了这个形状。

```
def rotateLeft(self):

    if self.pieceShape == Tetrominoe.SquareShape:
        return self

    result = Shape()
    result.pieceShape = self.pieceShape

    for i in range(4):

        result.setX(i, self.y(i))
        result.setY(i, -self.x(i))

    return result
```

`rotateLeft()` 方法向右旋转一个方块。正方形的方块就没必要旋转，就直接返回了。其他的是返回一个新的，能表示这个形状旋转了的坐标。

程序展示：

![Tetris](https://maicss.gitbooks.io/pyqt5/content/images/11-tetris.png)