# Matplotlib 基础手册

[链接地址](<https://www.matplotlib.org.cn/index.html>)

这些教程介绍了使用 Matplotlib 创建可视化效果的基础知识，以及有效使用该包的一些最佳实践。

## 使用指南

本教程介绍一些基本的使用模式和最佳实践，以帮助您开始使用 Matplotlib。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#一般概念)一般概念

matplotlib 有一个广泛的代码库，对于许多新用户来说，这个代码库可能会让人望而生畏。然而，大多数 Matplotlib 可以用相当简单的概念框架和几个要点的知识来理解。

打印需要在一系列级别上执行操作，从最一般的级别 (例如 “轮廓此二维阵列”) 到最具体的级别 (例如 “将此屏幕像素涂成红色”)。绘图软件包的目的是通过所有必要的控制，帮助您尽可能轻松地可视化您的数据 - 也就是说，在大多数情况下使用相对较高级别的命令，并且在需要时仍然能够使用低级别命令。

因此，matplotlib 中的所有内容都是按照层次结构组织的。层次结构的顶部是 matplotlib “状态机环境”，它是由 [matplotlib.pylot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 模块提供的。在这个级别上，使用简单的函数来添加打印元素 (线、图像、文本等)。到当前地物中的当前轴。

注意：Pyplot 的状态机环境的行为类似于 MATLAB，并且对于具有 MATLAB 经验的用户来说应该是最熟悉的。

层次结构中的下一级是面向对象的接口的第一级，其中 pyplot 仅用于少数功能，例如图形创建，并且用户显式创建并跟踪图形和轴对象。 在此级别，用户使用 pyplot 来创建图形，并且通过这些图形，可以创建一个或多个轴对象。 然后，这些轴对象用于大多数绘图操作。

对于更多的控制 - 这对于在 GUI 应用程序中嵌入 matplotlib 图表这一点至关重要 - 可以完全删除 pyplot 级别，从而留下纯粹面向对象的方法。

```python
# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#一个图的一部分)一个图的一部分

![图示](https://www.matplotlib.org.cn/static/images/tutorials/anatomy.png)

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#Figure)Figure

该**图 \** 记录了所有子轴，一些 “特殊” 的艺术家（标题，图形图例等）和** 画布 **。（不要过于担心画布，它是至关重要的，因为它实际上是绘图的对象，以获得你绘制的图像，但作为用户它或多或少是你不可见的）。一个数字可以有任意数量的 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes)，但是有用的应该至少有一个。

创建一个图像的最简单方法是使用 pylot：

```python
fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
```

![空图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_001.png)

![空图2](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_002.png)

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#Axes对象)Axes 对象

这就是你想象中的 “一幅图”，它是具有数据空间的图像区域。给定的图形可以包含许多轴，但给定的 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 对象只能在 [一个图](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)中。 Axes 包含两个（或 3D 的三个） [Axis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Axis) 对象（注意 **Axes** 和 **Axis** 之间的差异），它们负责数据限制（数据限制也可以通过 [set_xlim()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim) 和 [set_ylim()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim) 来设置 Axes 方法）。每个 Axes 都有一个标题（通过 [set_title()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title) 设置），一个 x 标签（通过 [set_xlabel()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel) 设置）和一个通过 [set_ylabel()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel) 设置的 y 标签。

Axis 类及其成员函数是使用 OO 接口的主要入口点。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#Axis对象)Axis 对象

这些是类似数字的对象。它们负责设置图形限制并生成刻度线（轴上的标记）和 ticklabels（标记刻度线的字符串）。刻度线的位置由 [Locator](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.Locator) 对象确定，ticklabel 字符串由 [Formatter](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.Formatter) 格式化。正确的定位器和格式化器的组合可以非常精确地控制刻度位置和标签。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#Artist对象)Artist 对象

基本上你在图上看到的一切都是艺术家（Artist）对象（甚至是图，轴和轴对象）。这包括 Text 对象，Line2D 对象，集合对象，Patch 对象......（现在你明白了）。渲染图形时，所有艺术家都被绘制到**画布**（canvas）上。大多数艺术家（Artist）都与轴有关；这样的艺术家（Artist）不能被多个轴共享，也不能从一个轴移动到另一个轴。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#绘制函数的输入类型)绘制函数的输入类型

所有绘图函数都需要 np.array 或 np.ma.masked_array 对象作为输入类型。如果是 “类数组（array-like）” 对象（如 [pandas](http://www.pypandas.cn/) 数据对象和 `np.matrix`）可能会或可能不会按预期工作。最好在绘图之前将它们转换为 np.array 对象。

例如，要转换 [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame)

```python
a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values
```

以及转换 np.matrix

```python
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#Matplotlib，pyplot和pylab：它们之间有什么关系？)Matplotlib，pyplot 和 pylab：它们之间有什么关系？

Matplotlib 是整个包；[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 是 matplotlib 中的一个模块；和 pylab 是一个与 `matplotlib` 一起安装的模块。

Pyplot 为底层面向对象的绘图库提供状态机接口。 状态机隐式地自动创建图形和轴以实现所需的图形。例如：

```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
```

![简单图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_003.png)

第一次调用 `plt.plot` 将自动创建必要的图形和轴以实现所需的绘图。随后对 plt.plot 的调用会重新使用当前轴，并且每次都会添加另一行。设置标题，图例和轴标签还会自动使用当前轴并设置标题，创建图例并分别标记轴。

`pylab` 是一个便利模块，它在单个名称空间中批量导入 [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)（用于绘图）和 [numpy](https://www.numpy.org.cn/) 一样（用于数学和使用数组）。不过不推荐使用 pylab，并且由于命名空间污染而强烈建议不要使用它。请改用 pyplot。

对于非交互式绘图，建议使用 pyplot 创建图形，然后使用 OO 界面进行绘图。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#代码风格)代码风格

查看此文档和示例时，您将找到不同的代码样式和使用模式。这些风格完全没有问题，各有利弊。几乎所有示例都可以转换为另一种样式并实现相同的结果。唯一需要注意的是避免为自己的代码混合了别的代码风格，尽量保持风格的统一。

**注意** ：matplotlib 的开发人员必须遵循特定的编程风格和指导原则。请参见 [Matplotlib 开发人员手册](https://matplotlib.org/devel/index.html#developers-guide-index)。

在不同的风格中，有两种是官方支持的。因此，这些是使用 matplotlib 的首选方法。

对于 pyplot 样式，脚本顶部的通常导入：

```python
import matplotlib.pyplot as plt
import numpy as np
```

然后调用一次，例如，np.arange，np.zeros，np.pi，plt.figure，plt.plot，plt.show 等。使用 pyplot 接口创建图像，然后使用对象方法：

```python
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

![简单图2](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_004.png)

那么，为什么所有都是额外的类型而不是 MATLAB 样式 (依赖于全局状态和平面名称空间) 呢？对于像这个例子这样非常简单的事情，唯一的好处是学术性的：更冗长的风格更明确，更清楚地说明事物从何而来，以及正在发生的事情。对于更复杂的应用程序，这种明确性和明确性变得越来越有价值，而更丰富和更完整的面向对象接口可能会使程序更易于编写和维护。

```python
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
```

![简单图3](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_005.png)

或者如果你想有两个小子图：

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
```

![简单图4](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_usage_006.png)

同样，对于这些简单的例子来说，这种风格看起来有点过头了，但是一旦图形变得稍微复杂一些，就会有回报。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#后端(Backends))后端 (Backends)

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#什么是后端？)什么是后端？

网站和邮件列表中的许多文档都提到了 “后端（Backends）”，许多新用户对这个术语感到困惑。matplotlib 针对许多不同的用例和输出格式。有些人在 python shell 中以交互方式使用 matplotlib，并在键入命令时弹出绘图窗口。有些人运行 [Jupyter](https://jupyter.org/) 笔记本并绘制内联图以进行快速数据分析。其他人将 matplotlib 嵌入到图形用户界面（如 wxpython 或 pygtk）中以构建丰富的应用程序。有些人在批处理脚本中使用 matplotlib 从数值模拟生成 postscript 图像，还有一些人运行 Web 应用程序服务器来动态提供图形。

为了支持所有这些用例，matplotlib 可以针对不同的输出，并且这些功能中的每一个都称为后端（Backends）; “前端（frontend）” 是面向用户的代码，即绘图代码，而 “后端（Backends）” 完成幕后的所有艰苦工作以制作图形。 有两种类型的后端：用户界面后端（用于 pygtk，wxpython，tkinter，qt4 或 macosx; 也称为 “交互式后端”）和硬拷贝后端来制作图像文件（PNG，SVG，PDF，PS; 也被称为 “非交互式后端”）。

配置后端有四种方法。如果它们彼此冲突，将使用以下列表中最后提到的方法，例如，调用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use) 将覆盖 `matplotlibrc` 中的设置。

1. matplotlibrc 文件中的后端参数（请参阅[使用样式表和 rcParams 自定义 Matplotlib](https://matplotlib.org/tutorials/introductory/customizing.html)）：

```python
backend : WXAgg   # use wxpython with antigrain (agg) rendering
```

1. 在 Unix 系统上，为当前 shell 或单个脚本设置 [MPLBACKEND](https://matplotlib.org/faq/environment_variables_faq.html#envvar-MPLBACKEND) 环境变量：

```python
> export MPLBACKEND=module://my_backend
> python simple_plot.py

> MPLBACKEND="module://my_backend" python simple_plot.py
```

在 Windows 上，只有前者是可用的：

```python
> set MPLBACKEND=module://my_backend
> python simple_plot.py
```

设置此环境变量将覆盖任何 `matplotlibrc` 中的后端参数，即使当前工作目录中存在 matplotlibrc 也是如此。 因此，全局设置 [MPLBACKEND](https://matplotlib.org/faq/environment_variables_faq.html#envvar-MPLBACKEND) ，例如 在`.bashrc` 或 `.profile` 中，不鼓励它，因为它可能导致反常的行为。

1. 如果您的脚本依赖于特定的后端，则可以使用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use) 函数：

```python
import matplotlib
matplotlib.use('PS')   # generate postscript output by default
```

如果使用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use) 函数，则必须在输入 [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 之前完成此操作。导入 pyplot 后调用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use) 将不起作用。如果用户希望使用不同的后端，则使用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use) 将需要更改代码。因此，除非绝对必要，否则应避免显式调用 [use()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.use)。

**注意**：后端名称规范不区分大小写；例如，‘GTK3Agg’ 和 ‘gtk3agg’ 是等效的。

通过典型的方式安装 matplotlib，例如：从二进制安装程序或 Linux 发行包安装的话，可以设置好一个默认的后端，允许交互式工作和从脚本绘图，输出到屏幕和 / 或文件，所以至少一开始的时候你不需要使用上面给出的任何方法。

但是，如果您想编写图形用户界面或 Web 应用程序服务器（[Web 应用程序服务器中的 Matplotlib](https://matplotlib.org/faq/howto_faq.html#howto-webapp)），或者需要更好地了解正在发生的事情，请继续阅读。为了使图形用户界面可以更加自定义，matplotlib 将画布（绘图所在的位置）中的渲染器（实际绘制的东西）的概念分开。用户界面的规范渲染器是 Agg，它使用 [Anti-Grain Geometry](http://antigrain.com/) C++ 库来制作图形的光栅（像素）图像。除 macosx 之外的所有用户界面都可以与 agg 渲染一起使用，例如 WXAgg，GTK3Agg，QT4Agg，QT5Agg，TkAgg。此外，一些用户界面支持其他渲染引擎。 例如，使用 GTK + 3，您还可以选择 Cairo 渲染（后端 GTK3Cairo）。

对于渲染引擎，还可以区分[矢量](https://en.wikipedia.org/wiki/Vector_graphics) (vector) 或[光栅](https://en.wikipedia.org/wiki/Raster_graphics) (raster) 渲染器。矢量图形语言发出绘图命令，例如 “从此点到此点绘制线”，因此无标度，并且栅格后端生成线的像素表示，其精度取决于 DPI 设置。

下面是 matplotlib 渲染器的摘要 (每个渲染器都有一个同名的后端；它们是非交互式后端，能够写入文件)：

| 渲染格式                                                     | 文件类型                                                     | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [AGG](https://matplotlib.org/glossary/index.html#term-agg)   | [png](https://matplotlib.org/glossary/index.html#term-png)   | [raster graphics](https://matplotlib.org/glossary/index.html#term-raster-graphics) -- 使用[反纹理几何（Anti-Grain Geometry）](http://antigrain.com/)引擎的高质量图像。 |
| PS                                                           | [ps](https://matplotlib.org/glossary/index.html#term-ps) [eps](https://matplotlib.org/glossary/index.html#term-eps) | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics) -- [Postscript](https://en.wikipedia.org/wiki/PostScript) output |
| PDF                                                          | [pdf](https://matplotlib.org/glossary/index.html#term-pdf)   | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics) -- [Portable Document Format](https://en.wikipedia.org/wiki/Portable_Document_Format) |
| SVG                                                          | [svg](https://matplotlib.org/glossary/index.html#term-svg)   | [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics) -- [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) |
| [Cairo](https://matplotlib.org/glossary/index.html#term-cairo) | [png](https://matplotlib.org/glossary/index.html#term-png) [ps](https://matplotlib.org/glossary/index.html#term-ps) [pdf](https://matplotlib.org/glossary/index.html#term-pdf) [svg](https://matplotlib.org/glossary/index.html#term-svg) | [raster graphics](https://matplotlib.org/glossary/index.html#term-raster-graphics) 和 [vector graphics](https://matplotlib.org/glossary/index.html#term-vector-graphics) -- 使用 [Cairo 图形库 (Cairo graphics)](https://www.cairographics.org/) 库 |

以下是支持的用户界面和渲染器组合；这些是交互式后端，能够显示到屏幕并使用上表中的适当渲染器写入文件：

| 后端      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| Qt5Agg    | 在 [Qt5](https://matplotlib.org/glossary/index.html#term-qt5) 画布中进行 Agg 渲染 (需要 [PyQt5](https://riverbankcomputing.com/software/pyqt/intro))。可以在 IPython 中使用 `%matplotlib qt5` 激活此后端。 |
| ipympl    | 嵌入在 Jupyter 小部件中的 Agg 渲染。（需要 ipympl）。这个后端可以在带有`％matplotlib ipympl` 的 Jupyter 笔记本中启用。 |
| GTK3Agg   | Agg 渲染到 [GTK](https://matplotlib.org/glossary/index.html#term-gtk) 3.x 画布（需要 [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject)，[pycairo](https://www.cairographics.org/pycairo/) 或 [cairocffi](https://pythonhosted.org/cairocffi/)）。 可以使用`％matplotlib gtk3` 在 IPython 中激活此后端。 |
| macosx    | 将 AGG 渲染到 OSX 中的 Cocoa 画布中。可以在 IPython 中使用 % matplotlib OSX 激活此后端。 |
| TkAgg     | Agg 渲染到 [Tk](https://matplotlib.org/glossary/index.html#term-tk) 画布（需要 [TkInter](https://wiki.python.org/moin/TkInter)）。可以使用 `％matplotlib tk` 在 IPython 中激活此后端。 |
| nbAgg     | 在经典的 Jupyter 笔记本中嵌入一个交互式界面。 可以通过％matplotlib `笔记本` 在 Jupyter 笔记本中启用此后端。 |
| WebAgg    | `show()` 将启动一个带有交互式图形的 tornado 服务。           |
| GTK3Cairo | 在 [GTK](https://matplotlib.org/glossary/index.html#term-gtk) 3.x 画布上呈现 cairo (需要 [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject) 和 [pycairo](https://www.cairographics.org/pycairo/) 或 [cairocffi](https://pythonhosted.org/cairocffi/) )。 |
| Qt4Agg    | Agg 渲染到 [Qt4](https://matplotlib.org/glossary/index.html#term-qt4) 画布（需要 [PyQt4](https://riverbankcomputing.com/software/pyqt/intro) 或 pyside）。可以使用 `％matplotlib qt4` 在 IPython 中激活此后端。 |
| WXAgg     | Agg 渲染到 [wxWidgets](https://matplotlib.org/glossary/index.html#term-wxwidgets) 画布（需要 [wxPython](https://www.wxpython.org/) 4）。可以使用 `％matplotlib wx` 在 IPython 中激活此后端。 |

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#ipympl)ipympl

Jupyter 小部件生态系统的移动速度太快，无法直接在 Matplotlib 中支持。安装 ipympl

```python
pip install ipympl
jupyter nbextension enable --py --sys-prefix ipympl
```

或者

```python
conda install ipympl -c conda-forge
```

请参阅 [jupyter-matplotlib](https://github.com/matplotlib/jupyter-matplotlib) 了解更多细节。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#GTK-和-Cairo)GTK 和 Cairo

`GTK3` 后端 (*包括* `GTK3Agg` 和 `GTK3Cairo`) 依赖于 Cairo (pycairo>=1.11.0 或 cairocffi).

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#如何选择PyQt4或PySide？)如何选择 PyQt4 或 PySide？

QT_API 环境变量可以设置为 `pyqt` 或 `pyside`，分别使用 `PyQt4` 或 `PySide`。

由于要使用的绑定的默认值是 `PyQt4`，`matplotlib` 首先尝试导入它，如果导入失败，它会尝试导入 `PySide`。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#什么是交互模式？)什么是交互模式？

使用交互式后端（请参阅[什么是后端？](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#什么是后端？)）允许但本身并不需要或确保绘制到屏幕上。是否以及何时绘制到屏幕，以及在屏幕上绘制绘图后是否继续脚本或 shell 会话取决于调用的函数和方法，以及确定 matplotlib 是否处于 “交互模式” 的状态变量”。默认的布尔值由 matplotlibrc 文件设置，并且可以像任何其他配置参数一样进行自定义（请参阅[使用样式表和 rcParams 自定义 Matplotlib](https://matplotlib.org/tutorials/introductory/customizing.html)）。它也可以通过 [matplotlib.interactive()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.interactive) 设置，并且可以通过 [matplotlib.is_interactive()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.is_interactive) 查询其值。无论是在脚本还是在 shell 中，在绘图命令流的中间打开和关闭交互模式很少需要并且可能令人困惑，因此在下文中我们将假设所有绘图都是以交互模式打开或关闭。

**注意** ：与交互性相关的主要更改，特别是 [show()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show) 的角色和行为，在向 matplotlib 1.0 版的过渡中进行了更改，并在 1.0.1 中修复了错误。这里我们描述主要交互式后端的 1.0.1 版行为，但 MacOSX 除外。

交互模式也可以通过 matplotlib.pyplot.ion () 打开，并通过 matplotlib.pyplot.ioff () 关闭。

**注意**：交互模式在 ipython 和普通的 python shell 中使用合适的后端，但它在 IDLE IDE 中不起作用。如果默认后端不支持交互性，则通过 “[可以使用什么是后端？](https://matplotlib.org/tutorials/introductory/usage.html#id4)” 这个话题中讨论的任何方法显式激活交互式后端。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#交互例子)交互例子

从普通的 python 提示符，或者在没有选项的情况下调用 ipython 之后，试试这个：

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
```

假设您运行的是 1.0.1 或更高版本，并且默认情况下安装并选择了交互式后端，您应该看到一个图，并且您的终端提示也应该是活动的；您可以键入其他命令，例如：

```python
plt.title("interactive test")
plt.xlabel("index")
```

然后你会看到每一行后都要更新绘图。从版本 1.5 开始，通过其他方式修改绘图也应该自动更新大多数后端的显示。获取对 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 实例的引用，并调用该实例的方法：

```python
ax = plt.gca()
ax.plot([3.1, 2.2])
```

如果你使用的是某些后端（如 macosx）或旧版本的 matplotlib，则可能无法立即将新行添加到绘图中。在这种情况下，您需要显式调用 [draw()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw) 以更新绘图：

```python
plt.draw()
```

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#非交互式示例)非交互式示例

像上一个示例中一样开始一个新会话，但现在关闭交互模式：

```python
import matplotlib.pyplot as plt
plt.ioff()
plt.plot([1.6, 2.7])
```

什么都没发生 - 或者至少没有任何东西出现在屏幕上（除非你使用 macosx 后端，这是异常的）。要显示绘图，您需要执行以下操作：

```python
plt.show()
```

现在你看到图像，但你的终端命令行没有响应；show () 命令会阻止其他命令的输入，直到您手动终止绘图窗口。

被迫使用阻塞功能？这有什么用，假设您需要一个脚本，将文件内容绘制到屏幕上。您想查看该图，然后结束脚本。如果没有一些阻塞命令（如 show ()），脚本会闪现图像，然后立即结束，屏幕上不显示任何内容。

此外，非交互模式会将所有图形延迟到调用 show ()；这比每次在脚本中添加新功能时重新绘制打印更有效。

在版本 1.0 之前，show () 通常不能在单个脚本中调用多次 (尽管有时可以不受限制)；对于版本 1.0.1 及更高版本，此限制已解除，因此可以编写如下脚本：

```python
import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
```

这就形成了三个阴谋，一次一个。即。第一个地块关闭后，将显示第二个地块。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#摘要)摘要

在交互模式下，pyplot 功能会自动绘制到屏幕上。

交互式绘制时，如果除了 pyplot 函数之外还使用对象方法调用，则只要想要刷新绘图，就调用 [draw()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw) 。

在要生成一个或多个图形的脚本中使用非交互模式，并在结束或生成一组新图形之前显示它们。在这种情况下，使用 [show()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show) 显示图形并阻止执行，直到您手动销毁它们。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#性能)性能

无论是以交互模式探索数据还是以编程方式保存大量绘图，渲染性能都可能成为您管道中的一个痛苦瓶颈。Matplotlib 提供了几种方法来大大减少渲染时间，但代价是绘图外观略有变化（达到可设置的容差）。可用于缩短渲染时间的方法取决于正在创建的绘图类型。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#线段简化)线段简化

对于具有直线段的打印 (例如，典型的直线打印、多边形轮廓等)，渲染性能可以由 matplotLibrc 文件中的 path.Simplify 和 path.Simplify_Threshold 参数控制 (有关 matplotlib 文件的详细信息，请参见[使用样式表和 rcParams 自定义 Matplotlib](https://matplotlib.org/tutorials/introductory/customizing.html))。Simplify 参数是一个布尔值，用于指示是否简化了直线段。path.Simplify_Threshold 参数控制简化线段的程度；阈值越高，渲染速度越快。

以下脚本将首先显示数据而不进行任何简化，然后简化显示相同的数据。 尝试与它们互动：

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
```

Matplotlib 目前默认为 `1/9` 的保守简化阈值。如果要更改默认设置以使用其他值，可以更改 matplotlibrc 文件。或者，您可以为交互式绘图（具有最大简化）创建新样式，并为出版质量绘图创建另一种样式（最小化简化）并根据需要激活它们。有关如何执行这些操作的说明，请参阅[使用样式表和 rcParams 自定义 Matplotlib](https://matplotlib.org/tutorials/introductory/customizing.html)。

简化通过将线段迭代地合并为单个矢量直到下一个线段与矢量的垂直距离（在显示坐标空间中测量）大于 `path.simplify_threshold` 参数来工作。

**注意**：与版本细分如何简化相关的更改在版本 2.1 中进行。 2.1 之前的这些参数仍将改善渲染时间，但 2.1 版及更高版本的某些类型数据的渲染时间将大大改善。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#标记简化)标记简化

标记也可以简化，尽管不如线段强大。标记简化仅适用于 [Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) 对象（通过市场营销属性）。无论在哪里传递 [Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) 构造参数，例如 [matplotlib.pyplot.plot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 和 [matplotlib.axes.Axes.plot()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot)，都可以使用 markevery 参数：

```python
plt.plot(x, y, markevery=10)
```

市场营销论证允许天真的子采样，或尝试均匀间隔（沿 x 轴）采样。 有关更多信息，请参阅 Markevery 演示。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#将线分割成较小的块)将线分割成较小的块

如果您正在使用 Agg 后端（请参阅[什么是后端？](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#什么是后端？)），那么您可以使用 `agg.path.chunksize` rc 参数。这允许您指定块大小，并且任何具有大于该多个顶点的行将被分割成多行，每行不超过 `agg.path.chunksize` 许多顶点。（除非 `agg.path.chunksize` 为零，在这种情况下没有分块。）对于某种类型的数据，将线条分成合理的大小可以大大减少渲染时间。

以下脚本将首先显示没有任何块大小限制的数据，然后显示块大小为 10,000 的相同数据。当数字很大时，可以最好地看到差异，尝试最大化 GUI 然后与它们进行交互：

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1,np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()
```

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#图例)图例

轴的默认图例行为尝试查找覆盖最少数据点的位置`（loc ='best'）`。 如果有大量数据点，这可能是非常昂贵的计算。 在这种情况下，您可能希望提供特定位置。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/usage.html#使用快速的风格)使用快速的风格

快速样式可用于自动将简化和分块参数设置为合理的设置，以加快绘制大量数据的速度。它可以通过运行简单地使用：

```python
import matplotlib.style as mplstyle
mplstyle.use('fast')
```

它的重量非常轻，因此它可以很好地与其他风格配合使用，只需确保最后应用快速样式，以便其他样式不会覆盖设置：

```python
mplstyle.use(['dark_background', 'ggplot', 'fast'])
```



## Pyplot 教程

关于 pylot 接口的介绍。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#pyplot-简介)pyplot 简介

[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 是命令样式函数的集合，使 matplotlib 像 MATLAB 一样工作。 每个 pyplot 函数对图形进行一些更改：例如，创建图形，在图形中创建绘图区域，在绘图区域中绘制一些线条，用标签装饰图形等。

在 [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 中，各种状态在函数调用中保留，以便跟踪当前图形和绘图区域等内容，并且绘图函数指向当前轴（请注意 “轴” 在此处以及在大多数位置 文档是指 [图形的轴部分](https://matplotlib.org/tutorials/introductory/usage.html#figure-parts)，而不是多个轴的严格数学术语。

**注意**: pyplot API 通常不如面向对象的 API 灵活。您在此处看到的大多数函数调用也可以作为 Axes 对象中的方法调用。 我们建议您浏览教程和示例以了解其工作原理。

使用 pyplot 生成可视化非常快速：

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

![绘制的一张图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_001.png)

您可能想知道为什么 x 轴的范围是 0-3，y 轴的范围是 1-4。如果为 [plot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 命令提供单个列表或数组，则 matplotlib 假定它是一系列 y 值，并自动为您生成 x 值。由于 python 范围以 0 开头，因此默认的 x 向量与 y 具有相同的长度，但从 0 开始。因此 x 数据为 `[0,1,2,3]`。

[plot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 是一个多功能命令，将采用任意数量的参数。 例如，要绘制 x 与 y 的关系，您可以发出命令：

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

![绘制的一张折线图2](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_002.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#格式化绘图的样式)格式化绘图的样式

对于每对 x，y 对的参数，有一个可选的第三个参数，它是指示绘图的颜色和线型的格式字符串。格式字符串的字母和符号来自 MATLAB，您可以将颜色字符串与线型字符串连接起来。默认格式字符串为 “b-”，为蓝色实线。例如，要用红色圆圈绘制上述内容，您将发出：

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

![绘制的一张散点图3](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_003.png)

有关线型和格式字符串的完整列表，请参阅 [plot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 文档。 上例中的 [axis()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis) 命令采用 `[xmin, xmax, ymin, ymax]` 列表并指定轴的视口。

如果 matplotlib 仅限于使用列表，那么数字处理将毫无用处。通常，您将使用 numpy 数组。实际上，所有序列都在内部转换为 numpy 数组。 下面的示例说明了使用数组在一个命令中绘制具有不同格式样式的多行。

```python
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

![绘制的一张符号散点图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_004.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#使用关键字字符串绘图)使用关键字字符串绘图

在某些情况下，您可以使用允许您使用字符串访问特定变量的格式的数据。例如，使用 [numpy.recarray](https://docs.scipy.org/doc/numpy/reference/generated/numpy.recarray.html#numpy.recarray) 或 [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame)。

Matplotlib 允许您使用 data 关键字参数提供此类对象。如果提供，那么您可以生成包含与这些变量对应的字符串的图。

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```

![绘制的一张大小不一散点图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_005.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#用分类变量绘图)用分类变量绘图

也可以使用分类变量创建绘图。Matplotlib 允许您将分类变量直接传递给许多绘图函数。例如：

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

![绘制子图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_006.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#控制线的属性)控制线的属性

线可以设置许多属性：linewidth，dash style，antialiased 等；请参阅 [matplotlib.lines.Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)。 有几种方法可以设置线属性。

+  使用关键字 args：

   ```python
     plt.plot(x, y, linewidth=2.0)
   ```

+  使用 Line2D 实例的 setter 方法。 plot 返回 Line2D 对象列表；例如，line1，line2 = plot（x1，y1，x2，y2）。 在下面的代码中，我们假设我们只有一行，因此返回的列表的长度为 1. 我们使用 tuple 解压缩为 line，以获取该列表的第一个元素：

   ```python
     line, = plt.plot(x, y, '-')
     line.set_antialiased(False) # turn off antialising
   ```

+  使用

    

   setp()

    

   命令。 下面的示例使用 MATLAB 样式命令在行列表上设置多个属性。setp 透明地使用对象列表或单个对象。您可以使用 python 关键字参数或 MATLAB 样式的字符串 / 值对：

   ```python
     lines = plt.plot(x1, y1, x2, y2)
     # use keyword args
     plt.setp(lines, color='r', linewidth=2.0)
     # or MATLAB style string value pairs
     plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
   ```

以下是可用的 [Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) 属性。

| 属性                   | 值类型                                            |
| ---------------------- | ------------------------------------------------- |
| alpha                  | float                                             |
| animated               | [True \| False]                                   |
| antialiased 或 aa      | [True \| False]                                   |
| clip_box               | matplotlib.transform.Bbox 实例                    |
| clip_on                | [True \| False]                                   |
| clip_path              | 路径实例和变换实例 (修补程序)                     |
| color 或 c             | 任何 Matplotlib 颜色                              |
| contains               | the hit testing function                          |
| dash_capstyle          | ['butt' \| 'round' \| 'projecting']               |
| dash_joinstyle         | ['miter' \| 'round' \| 'bevel']                   |
| dashes                 | 以点为单位的开 / 关油墨顺序                       |
| data                   | (np.array xdata, np.array ydata)                  |
| figure                 | matplotlib.quire.Figure 实例                      |
| label                  | 任何字符串                                        |
| linestyle or ls        | [ '-' \| '--' \| '-.' \| ':' \| 'steps' \| ...]   |
| linewidth or lw        | 浮点值                                            |
| lod                    | [True \| False]                                   |
| marker                 | [ '+' \| ',' \| '.' \| '1' \| '2' \| '3' \| '4' ] |
| markeredgecolor or mec | 任何 Matplotlib 颜色                              |
| markeredgewidth or mew | 浮点值                                            |
| markerfacecolor or mfc | 任何 Matplotlib 颜色                              |
| markersize or ms       | 浮点数                                            |
| markevery              | [ None \| integer \| (startind, stride) ]         |
| picker                 | 用于交互式选线                                    |
| pickradius             | 线拾取选择半径                                    |
| solid_capstyle         | ['butt' \| 'round' \| 'projecting']               |
| solid_joinstyle        | ['miter' \| 'round' \| 'bevel']                   |
| transform              | matplotlib.transforms.Transform 实例              |
| visible                | [True \| False]                                   |
| xdata                  | np.array                                          |
| ydata                  | np.array                                          |
| zorder                 | 任意数字                                          |

若要获取可设置行属性的列表，请使用一行或多行作为参数调用 [setp()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp) 函数。

```python
In [69]: lines = plt.plot([1, 2, 3])

In [70]: plt.setp(lines)
  alpha: float
  animated: [True | False]
  antialiased or aa: [True | False]
  ...snip
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#使用多个图形和轴)使用多个图形和轴

MATLAB 和 [pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)，都有当前图形和当前轴的概念。所有打印命令都适用于当前轴。函数 [gca()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca) 返回当前轴 ([matplotlib.axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 实例)，[gcf()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf) 返回当前地物 ([matplotlib.figure.Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 实例)。通常情况下，你不必担心这一点，因为这一切都是在幕后处理的。下面是创建两个子图的脚本。

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

![图例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_007.png)

这里的 [figure()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure) 命令是可选的，因为默认情况下将创建 `figure(1)`，就像默认情况下创建 `subplot(111)` 一样，如果不手动指定任何轴。[subplot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot) 命令指定 `numrows`, `numcols`, `plot_number`，其中 `plot_number`的范围 `从1到numrows*numcols`。如果 `numrows * numcols <10`，则 subplot 命令中的逗号是可选的。因此 `subplot(211)` 与 `subplot(2, 1, 1)` 相同。

您可以创建任意数量的子图和轴。如果要手动放置轴，即不在矩形网格上，请使用 axes () 命令，该命令允许您将位置指定为 `axes([left，bottom，width，height])`，其中所有值均为小数（0 到 1）坐标。有关手动放置轴的示例，请参阅 [Axes Demo](https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html); 有关具有大量子图的示例，请参阅 [Basic Subplot Demo](https://matplotlib.org/gallery/subplots_axes_and_figures/subplot_demo.html)。

您可以使用具有增加的图号的多个 [figure()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure) 调用来创建多个数字。当然，每个图形可以包含您心中所需的轴和子图：

```python
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
```

您可以使用 [clf()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf) 清除当前图形，使用 [cla()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla) 清除当前轴。如果您发现在幕后为您维护状态（特别是当前图像，图形和轴）很烦人，请不要绝望：这只是围绕面向对象 API 的瘦状态包装器，您可以使用它（见 [Artist tutorial](https://matplotlib.org/tutorials/intermediate/artists.html)）

如果你要制作大量的图像，你还需要注意一件事：在用 [close()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close) 显式关闭数字之前，数字所需的内存不会完全释放。删除对图的所有引用，和 / 或使用窗口管理器来杀死屏幕上出现图形的窗口是不够的，因为 pyplot 会保持内部引用，直到调用 [close()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close)。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#使用文本)使用文本

[text()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text) 命令可用于在任意位置添加文本，而 [xlabel()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel), [ylabel()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel) 和 [title()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title) 用于在指定位置添加文本 (有关更详细的示例，请参见 Matplotlib 图中的文本)

```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

![图例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_008.png)

所有 [text()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text) 命令都返回一个 [matplotlib.text.Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text) 实例。与上面的行一样，您可以通过将关键字参数传递给文本函数或使用 [setp()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp) 来自定义属性：

```python
t = plt.xlabel('my data', fontsize=14, color='red')
```

[文本属性和布局](https://matplotlib.org/tutorials/text/text_props.html)中更详细地介绍了这些属性。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#在文本中使用数学表达式)在文本中使用数学表达式

matplotlib 在任何文本表达式中接受 TeX 方程表达式。 例如，要在标题中写入表达式 σi= 15，您可以编写由美元符号包围的 TeX 表达式：

```python
plt.title(r'$\sigma_i=15$')
```

标题字符串前面的 r 很重要 - 它表示该字符串是一个原始字符串，而不是将反斜杠视为 python 转义。matplotlib 有一个内置的 TeX 表达式解析器和布局引擎，并提供自己的数学字体 - 有关详细信息，请参阅编写[数学表达式](https://matplotlib.org/tutorials/text/mathtext.html)。因此，您可以跨平台使用数学文本，而无需安装 TeX。 对于安装了 LaTeX 和 dvipng 的用户，您还可以使用 LaTeX 格式化文本并将输出直接合并到显示图或保存的 postscript 中 - 请参阅使用 [LaTeX](https://matplotlib.org/tutorials/text/usetex.html) 进行文本渲染。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#注释文本)注释文本

上面的基本 [text()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text) 命令的使用将文本放在 Axes 上的任意位置。文本的常见用途是注释绘图的某些功能，而 [annotate()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate) 方法提供帮助功能以使注释变得容易。在注释中，有两点需要考虑：由参数 xy 表示的注释位置和文本 xytext 的位置。 这两个参数都是（x，y）元组。

```python
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
```

![图例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_009.png)

在此基本示例中，xy（箭头提示）和 xytext 位置（文本位置）都在数据坐标中。 可以选择各种其他坐标系 - 有关详细信息，请参阅[基本注释](https://matplotlib.org/tutorials/text/annotations.html#annotations-tutorial)和[高级注释](https://matplotlib.org/tutorials/text/annotations.html#plotting-guide-annotation)。更多示例可以在 [Annotating Plots](https://matplotlib.org/gallery/text_labels_and_annotations/annotation_demo.html) 中找到。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/pyplot.html#对数和其他非线性轴)对数和其他非线性轴

[matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 不仅支持线性轴刻度，还支持对数和 logit 刻度。 如果数据跨越许多数量级，则通常使用此方法。 更改轴的比例很容易：

```python
plt.xscale('log')
```

下面显示了具有相同数据和 y 轴不同比例的四个图的示例。

```python
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
```

![图例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pyplot_010.png)

您也可以添加自己的比例，有关详细信息，请[参阅开发人员指南](https://matplotlib.org/devel/add_new_projection.html#adding-new-scales)以创建比例和转换。



## Matplotlib 中的示例图

在这里，您将发现一系列带有生成它们的代码的示例图，在这里，您将发现一系列带有生成它们的代码的示例图。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#线段图)线段图

以下是使用 [plot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) 创建带有文本标签的折线图的方法。

![简单的线段图示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_simple_plot_0011.png)

简单的线段图示例

[点此进入查看源码](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#让一个图中有多个子图)让一个图中有多个子图

使用 [subplot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot) 函数创建多个轴（即子图）：

![简单子图示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_subplot_0011.png)

简单子图示例

[点此进入查看源码](https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#显示图像)显示图像

Matplotlib 可以使用 [imshow()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow) 函数显示图像（假设水平尺寸相等）。

![使用imshow()显示CT扫描的示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_image_demo_0031.png)

使用 [imshow()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow) 显示 CT 扫描的示例

[点此进入查看源码](https://matplotlib.org/gallery/images_contours_and_fields/image_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#轮廓和伪彩色)轮廓和伪彩色

即使水平尺寸不均匀，[pcolormesh()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh) 函数也可以制作二维数组的彩色表示。 [contour()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour) 函数是表示相同数据的另一种方式：

![比较pcolormesh()和contour()以绘制二维数据的示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pcolormesh_levels_0011.png)

比较 [pcolormesh()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh) 和 [contour()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour) 以绘制二维数据的示例。

[点此进入查看源码](https://matplotlib.org/gallery/images_contours_and_fields/image_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#直方图)直方图

[hist()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist) 函数自动生成直方图并返回 bin 计数或概率：

![直方图特性演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_histogram_features_0011.png)

直方图特性演示

[点此进入查看源码](https://matplotlib.org/gallery/statistics/histogram_features.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#路径)路径

您可以使用 [matplotlib.path](https://matplotlib.org/api/path_api.html#module-matplotlib.path) 模块在 Matplotlib 中添加任意路径：

![路径补丁](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_path_patch_0011.png)

路径补丁

[点此进入查看源码](https://matplotlib.org/gallery/shapes_and_collections/path_patch.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#三维绘图)三维绘图

mplot3d 工具包（参见[入门](https://matplotlib.org/tutorials/toolkits/mplot3d.html#toolkit-mplot3d-tutorial)和 [3D 绘图](https://matplotlib.org/gallery/index.html#mplot3d-examples-index)）支持简单的三维图形，包括曲面，线框，散点图和条形图。

![平面3d图](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_surface3d_0011.png)

平面 3d 图

感谢 John Porter，Jonathon Taylor，Reinier Heeres 和 Ben Root 的 mplot3d 工具包。 此工具包包含在所有标准 Matplotlib 安装中。

[点此进入查看源码](https://matplotlib.org/gallery/mplot3d/surface3d.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#流图)流图

[streamplot()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot) 函数绘制矢量场的流线。除了简单地绘制流线图之外，它还允许您将流线的颜色和 / 或线宽映射到单独的参数，例如矢量场的速度或局部强度。

![Streamplot有各种绘图选项](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_plot_streamplot_0011.png)

Streamplot 有各种绘图选项

此功能补充了用于绘制矢量场的 [quiver()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver) 函数。 感谢 Tom Flannaghan 和 Tony Yu 添加了 streamplot 功能。

[点此进入查看源码](https://matplotlib.org/gallery/images_contours_and_fields/plot_streamplot.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#椭圆)椭圆

为了支持[菲尼克斯](http://www.jpl.nasa.gov/news/phoenix/main.php)火星任务（使用 Matplotlib 显示航天器的地面跟踪），Michael Droettboom 建立在 Charlie Moad 的工作基础上，为椭圆弧（参见 [Arc](https://matplotlib.org/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc)）提供极其精确的 8 样条近似，这对缩放不敏感 水平。

![椭圆演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_ellipse_demo_0011.png)

椭圆演示

[点此进入查看源码](https://matplotlib.org/gallery/shapes_and_collections/ellipse_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#条形图)条形图

Use the [bar()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar) function to make bar charts, which includes customizations such as error bars:

![条形图演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_barchart_demo_0011.png)

条形图演示

您还可以创建堆叠条形（bar_stacked.py）或水平条形图（barh.py）。

[点此进入查看源码](https://matplotlib.org/gallery/statistics/barchart_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#饼状图)饼状图

[pie()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie) 函数允许您创建饼图。可选功能包括自动标记区域的百分比，从饼图中心爆炸一个或多个楔形，以及阴影效果。 仔细查看附加的代码，只需几行代码即可生成此图。

![饼状图特性](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_pie_features_0011.png)

饼状图特性

[点此进入查看源码](https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#表格)表格

[table()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table) 函数将一个文本表添加到轴。

![表格演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_table_demo_0011.png)

表格演示

[点此进入查看源码](https://matplotlib.org/gallery/misc/table_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#散点图)散点图

[scatter()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter) 函数使用（可选）大小和颜色参数创建散点图。此示例绘制了 Google 股票价格的变化，标记尺寸反映了交易量和颜色随时间变化。这里，alpha 属性用于制作半透明圆圈标记。

![散点图演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_scatter_demo2_0011.png)

散点图

[点此进入查看源码](https://matplotlib.org/gallery/lines_bars_and_markers/scatter_demo2.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#GUI小部件)GUI 小部件

Matplotlib 具有独立于您正在使用的图形用户界面的基本 GUI 小部件，允许您编写跨 GUI 图形和小部件。 请参阅 [matplotlib.widgets](https://matplotlib.org/api/widgets_api.html#module-matplotlib.widgets) 和 [小部件示例](https://matplotlib.org/gallery/index.html).。

![滑块和单选按钮GUI](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_slider_demo_0011.png)

滑块和单选按钮 GUI。

[点此进入查看源码](https://matplotlib.org/gallery/widgets/slider_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#填充曲线)填充曲线

[fill()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill) 函数可以绘制填充的曲线和多边形：

![填充曲线](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_fill_0011.png)

填充曲线

感谢 Andrew Straw 添加此功能。

[点此进入查看源码](https://matplotlib.org/gallery/lines_bars_and_markers/fill.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#日期处理)日期处理

您可以绘制带有主要和次要刻度的时间序列数据以及两者的自定义刻度格式化程序。

![日期处理演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_date_0011.png)

日期处理演示

有关详细信息和用法，请参阅 [matplotlib.ticker](https://matplotlib.org/api/ticker_api.html#module-matplotlib.ticker) 和 [matplotlib.dates](https://matplotlib.org/api/dates_api.html#module-matplotlib.dates)。

[点此进入查看源码](https://matplotlib.org/gallery/text_labels_and_annotations/date.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#log函数图)log 函数图

[semilogx()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx)，[semilogy()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy) 和 [loglog()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog) 函数简化了对数图的创建。

![log函数图演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_log_demo_0011.png)

log 函数图演示

感谢 Andrew Straw，Darren Dale 和 Gregory Lielens 提供的日志扩展基础架构。

[点此进入查看源码](https://matplotlib.org/gallery/scales/log_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#极坐标图)极坐标图

[polar()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib.pyplot.polar) 函数生成极坐标图。

![极坐标图演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_polar_demo_0011.png)

极坐标图演示

[点此进入查看源码](https://matplotlib.org/gallery/pie_and_polar_charts/polar_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#图例)图例

[legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend) 函数自动生成图形图例，具有 MATLAB 兼容的图例放置功能。

![图例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_legend_0011.png)

图例

感谢 Charles Twardy 对图例功能的输入。

[点此进入查看源码](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#文本对象的TeX符号)文本对象的 TeX 符号

下面是 Matplotlib 内部 mathtext 引擎现在支持的许多 TeX 表达式的示例。mathtext 模块使用 [FreeType](https://www.freetype.org/) 和 DejaVu，BaKoMa 计算机现代或 [STIX](http://www.stixfonts.org/) 字体提供 TeX 样式的数学表达式。有关其他详细信息，请参阅 [matplotlib.mathtext](https://matplotlib.org/api/mathtext_api.html#module-matplotlib.mathtext) 模块。

![Mathtext示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_mathtext_examples_0011.png)

Mathtext 示例

Matplotlib 的 mathtext 基础结构是一个独立的实现，不需要在您的计算机上安装 TeX 或任何外部软件包。请参阅[编写数学表达式的教程](https://matplotlib.org/tutorials/text/mathtext.html)。

[点此进入查看源码](https://matplotlib.org/gallery/text_labels_and_annotations/mathtext_examples.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#原生纹理渲染)原生纹理渲染

虽然 Matplotlib 的内部数学渲染引擎非常强大，但有时候你需要 TeX。Matplotlib 支持使用 usetex 选项对字符串进行外部 TeX 渲染。

![tex演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_tex_demo_0011.png)

Tex 演示

[点此进入查看源码](https://matplotlib.org/gallery/text_labels_and_annotations/tex_demo.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#EEG-GUI)EEG GUI

您可以将 Matplotlib 嵌入到 pygtk，wx，Tk 或 Qt 应用程序中。 这是一个名为 [pbrain](https://github.com/nipy/pbrain) 的 EEG 查看器的屏幕截图。

![小型egg演示](https://www.matplotlib.org.cn/static/images/tutorials/eeg_small.png)

低轴使用 [specgram()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram) 绘制其中一个 EEG 通道的频谱图。

有关如何在不同工具包中嵌入 Matplotlib 的示例，请参阅：

+  [Embedding In GTK3](https://matplotlib.org/gallery/user_interfaces/embedding_in_gtk3_sgskip.html)
+  [Embedding In Wx2](https://matplotlib.org/gallery/user_interfaces/embedding_in_wx2_sgskip.html)
+  [Matplotlib With Glade 3](https://matplotlib.org/gallery/user_interfaces/mpl_with_glade3_sgskip.html)
+  [Embedding in Qt](https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html)
+  [Embedding In Tk](https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#XKCD风格的草图)XKCD 风格的草图

只是为了好玩，Matplotlib 支持 xkcd 风格的绘图。

![小型egg演示](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_xkcd_0011.png)

Xkcd

[点此进入查看源码](https://matplotlib.org/gallery/showcase/xkcd.html)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#子图示例)子图示例

许多绘图类型可以组合在一个图中，以创建强大而灵活的数据表示。

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
```

![子图示例](https://www.matplotlib.org.cn/static/images/tutorials/sphx_glr_sample_plots_001.png)

## 图像教程

有关使用 Matplotlib 打印图像的简短教程。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#启动方式)启动方式

首先，让我们从 IPython 开始。它是对标准 Python 提示的最佳增强，它与 Matplotlib 有着很好的兼容性。现在可以在 shell 或 IPython Notebook 上启动 IPython。

随着 IPython 的启动，我们现在需要连接到 GUI 事件循环。这告诉 IPython 在哪里（和如何）显示图像。要连接到 GUI 循环，请在 IPython 提示符下执行 **%matplotlib** magic。 关于它在 [IPython 的 GUI 事件循环](http://ipython.org/ipython-doc/2/interactive/reference.html#gui-event-loop-support)文档中的确切含义有更详细的说明。

如果您使用的是 IPython Notebook，则可以使用相同的命令，但人们通常使用特定的参数来使用 % matplotlib 技法：

```python
In [1]: %matplotlib inline
```

这将打开内联打印，其中打印图形将显示在笔记本中。这对互动有重要的影响。对于内联打印，单元格下方输出打印的单元中的命令不会影响打印。例如，无法从创建打印的单元格下方的单元格更改颜色贴图。但是，对于打开单独窗口的其他后端 (如 Qt5)，创建打印的单元格将更改打印 - 它是内存中的活动对象。

本教程将使用 matplotlib 的命令式打印界面 pylot。此界面保持全局状态，对于快速轻松地尝试各种打印设置非常有用。另一种选择是面向对象的接口，它也非常强大，通常更适合大型应用程序开发。如果您想了解面向对象的接口，我们的[使用指南](https://matplotlib.org/tutorials/introductory/usage.html)是一个很好的起点。现在，让我们继续使用命令式方法：

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#将图像数据导入Numpy数组)将图像数据导入 Numpy 数组

枕形库支持加载图像数据。在本地，Matplotlib 仅支持 PNG 图像。如果本机读取失败，下面显示的命令将返回 [Pillow](https://pillow.readthedocs.io/en/latest/)。

此示例中使用的图像是一个 PNG 文件，但请记住对您自己的数据的枕头要求。

下面是我们要操作的图片：

![黑白图片](pictures/Matplotlib 中文手册.assets/stinkbug.png)

这是一个 24 位的 RGB PNG 图像 (R、G、B 每个 8 位)。根据您获取数据的位置，您最可能遇到的其他类型的图像是 RGBA 图像 (允许透明) 或单通道灰度 (亮度) 图像。您可以右键单击它并选择 “将图像另存为”，将其下载到您的计算机上，以便完成本教程的其余部分。

我们开始吧.。

```python
img = mpimg.imread('../../doc/_static/stinkbug.png')
print(img)
```

输出：

```python
[[[0.40784314 0.40784314 0.40784314]
  [0.40784314 0.40784314 0.40784314]
  [0.40784314 0.40784314 0.40784314]
  ...
  [0.42745098 0.42745098 0.42745098]
  [0.42745098 0.42745098 0.42745098]
  [0.42745098 0.42745098 0.42745098]]

 [[0.4117647  0.4117647  0.4117647 ]
  [0.4117647  0.4117647  0.4117647 ]
  [0.4117647  0.4117647  0.4117647 ]
  ...
  [0.42745098 0.42745098 0.42745098]
  [0.42745098 0.42745098 0.42745098]
  [0.42745098 0.42745098 0.42745098]]

 [[0.41960785 0.41960785 0.41960785]
  [0.41568628 0.41568628 0.41568628]
  [0.41568628 0.41568628 0.41568628]
  ...
  [0.43137255 0.43137255 0.43137255]
  [0.43137255 0.43137255 0.43137255]
  [0.43137255 0.43137255 0.43137255]]

 ...

 [[0.4392157  0.4392157  0.4392157 ]
  [0.43529412 0.43529412 0.43529412]
  [0.43137255 0.43137255 0.43137255]
  ...
  [0.45490196 0.45490196 0.45490196]
  [0.4509804  0.4509804  0.4509804 ]
  [0.4509804  0.4509804  0.4509804 ]]

 [[0.44313726 0.44313726 0.44313726]
  [0.44313726 0.44313726 0.44313726]
  [0.4392157  0.4392157  0.4392157 ]
  ...
  [0.4509804  0.4509804  0.4509804 ]
  [0.44705883 0.44705883 0.44705883]
  [0.44705883 0.44705883 0.44705883]]

 [[0.44313726 0.44313726 0.44313726]
  [0.4509804  0.4509804  0.4509804 ]
  [0.4509804  0.4509804  0.4509804 ]
  ...
  [0.44705883 0.44705883 0.44705883]
  [0.44705883 0.44705883 0.44705883]
  [0.44313726 0.44313726 0.44313726]]]
```

注意这里的 dtype-Float32。Matplotlib 已将每个通道的 8 位数据重新缩放为 0.0 到 1.0 之间的浮点数据。另外，Pillow 可以使用的唯一数据类型是 uint8。Matplotlib 绘图可以处理 Float32 和 uint8，但 PNG 以外的任何格式的图像读 / 写仅限于 uint8 数据。为什么是 8 位？大多数显示器只能渲染每通道 8 位的颜色渐变。为什么它们只能呈现 8 位 / 通道？因为这是人眼所能看到的。更多在这里 (从摄影的角度)：[发光景观位深度教程](https://luminous-landscape.com/bit-depth/)。

每个内部列表代表一个像素。在这里，对于 RGB 图像，有 3 个值。由于是黑白图像，R、G 和 B 都是相似的。RGBA (其中 A 是 Alpha 或透明度)，每个内部列表有 4 个值，一个简单的亮度图像只有一个值 (因此只是一个 2-D 数组，而不是 3-D 数组)。对于 RGB 和 RGBA 图像，matplotlib 支持 Float32 和 uint8 数据类型。对于灰度，matplotlib 仅支持 Float32。如果数组数据不符合这些描述之一，则需要重新缩放它。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#将数字数组绘制为图像)将数字数组绘制为图像

因此，您将数据放在一个 numpy 数组中（通过导入或生成它）。 让我们渲染吧。 在 Matplotlib 中，这是使用 [imshow()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow) 函数执行的。 在这里，我们将抓住绘图对象。 此对象为您提供了一种从提示中操作绘图的简便方法。

```python
imgplot = plt.imshow(img)
```

![使用matplotlib打印的图片](pictures/Matplotlib 中文手册.assets/sphx_glr_images_001.png)

你也可以绘制任何 numpy 数组。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#将伪彩色方案应用于图像图)将伪彩色方案应用于图像图

Pseudocolor 可以成为增强对比度和更容易可视化数据的有用工具。这在使用投影仪进行数据演示时尤其有用 - 它们的对比度通常非常差。

伪彩色仅与单通道，灰度，亮度图像相关。 我们目前有一个 RGB 图像。由于 R，G 和 B 都是相似的（请参阅上面或您的数据），我们可以选择一个数据通道：

```python
lum_img = img[:, :, 0]

# This is array slicing.  You can read more in the `Numpy tutorial
# <https://docs.scipy.org/doc/numpy/user/quickstart.html>`_.

plt.imshow(lum_img)
```

![伪彩色方案](pictures/Matplotlib 中文手册.assets/sphx_glr_images_002.png)

现在，使用亮度（2D，无颜色）图像，应用默认色图（也称为查找表，LUT）。 默认名称为 viridis。 还有很多其他选择。

```python
plt.imshow(lum_img, cmap="hot")
```

![伪彩色方案2](pictures/Matplotlib 中文手册.assets/sphx_glr_images_003.png)

注意：您还可以使用 set_cmap () 方法更改现有绘图对象上的颜色映射：

```python
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
```

![伪彩色方案3](pictures/Matplotlib 中文手册.assets/sphx_glr_images_004.png)

注意：但是，请记住，在具有内联后端的 IPython 笔记本中，您无法更改已经呈现的绘图。 如果你在一个单元格中创建 imgplot，则不能在稍后的单元格中调用 set_cmap () 并期望更早的绘图。 确保在一个单元格中一起输入这些命令。 plt 命令不会更改早期单元格的图形。

还有许多其他色彩方案可用。 查看[色彩映射的列表和图像](https://matplotlib.org/tutorials/colors/colormaps.html)。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#颜色比例参考)颜色比例参考

了解颜色代表什么价值是有帮助的。 我们可以通过添加彩条来实现。

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```

![伪彩色方案4](pictures/Matplotlib 中文手册.assets/sphx_glr_images_005.png)

这会为您现有的图形添加一个颜色条。 如果您更改切换到不同的色彩映射，则不会自动更改 - 您必须重新创建绘图，然后再次添加颜色栏。

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#检查特定数据范围)检查特定数据范围

有时，您希望增强图像的对比度，或者扩大特定区域的对比度，同时牺牲颜色的细节，这些颜色不会有太大变化，或者无关紧要。 找到有趣区域的好工具是直方图。要创建图像数据的直方图，我们使用 [hist()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist) 函数。

```python
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
```

![直方图](pictures/Matplotlib 中文手册.assets/sphx_glr_images_006.png)

最常见的情况是，图像的 “有趣” 部分位于峰值附近，您可以通过剪裁峰值上方和 / 或下方的区域来获得额外的对比度。在我们的直方图中，看起来高端中没有太多有用的信息 (图像中没有很多白色的东西)。让我们调整上限，以便有效地 “放大” 直方图的一部分。我们通过将 clim 参数传递给 imshow 来实现这一点。也可以通过调用图像打印对象的 “set_clim ()” 方法来实现这一点，但是在使用 IPython Notebook 时，请确保在与 PLOT 命令相同的单元格中执行此操作 - 它不会更改以前单元格中的打印。

可以在打印调用中指定客户端。

```python
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
```

![伪彩色图](pictures/Matplotlib 中文手册.assets/sphx_glr_images_007.png)

还可以使用返回的对象指定客户端。

```python
fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
```

![伪彩色图](pictures/Matplotlib 中文手册.assets/sphx_glr_images_008.png)

#### [#](https://www.matplotlib.org.cn/tutorials/introductory/images.html#数组插值方案)数组插值方案

根据不同的数学方案，插值计算像素 “应该” 的颜色或值。 发生这种情况的一个常见地方是调整图像大小。 像素数会发生变化，但您需要相同的信息。 由于像素是离散的，因此缺少空间。 插值就是你填充那个空间的方式。 这就是为什么当你把它们炸掉时，你的图像有时看起来像是像素化的原因。 当原始图像和扩展图像之间的差异更大时，效果更明显。 让我们拍摄我们的照片并缩小它。 我们有效地丢弃像素，只保留少数像素。 现在，当我们绘制它时，数据会被炸成屏幕上的大小。 旧像素不再存在，计算机必须以像素绘制以填充该空间。

我们将使用我们用于加载图像的 Pillow 库来调整图像大小。

```python
from PIL import Image

img = Image.open('../../doc/_static/stinkbug.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)
```

![伪彩色图子图](pictures/Matplotlib 中文手册.assets/sphx_glr_images_009.png)

这里我们有默认的插值，双线性，因为我们没有给 imshow () 任何插值参数。

我们试试其他一些。 这里是 “最近的”，没有插值。

```python
imgplot = plt.imshow(img, interpolation="nearest")
```

![模糊图](pictures/Matplotlib 中文手册.assets/sphx_glr_images_010.png)

和双三次：

```python
imgplot = plt.imshow(img, interpolation="bicubic")
```

![模糊图2](pictures/Matplotlib 中文手册.assets/sphx_glr_images_011.png)

在吹制照片时经常使用双立方插值 - 人们往往更喜欢模糊而不是像素化。



## Plot 的生命周期

本教程旨在使用 Matplotlib 显示单个可视化的开始，中间和结尾。 我们将从一些原始数据开始，最后保存一个自定义可视化图形。 在此过程中，我们将尝试使用 Matplotlib 突出一些简洁的功能和最佳实践。

**注意**：本教程基于 Chris Moffitt 撰写的[这篇优秀博客文章](http://pbpython.com/effective-matplotlib.html))。它由 Chris Holdgraf 转换成本教程。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#关于面向对象的API与Pyplot的说明)关于面向对象的 API 与 Pyplot 的说明

Matplotlib 有两个接口。第一个是面向对象（OO）接口。在这种情况下，我们利用 [axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 的实例，以便在 [figure.Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 的实例上呈现可视化。

第二种是基于 MATLAB 并使用基于状态的接口。这封装在 pyplot 模块中。请参阅 [pyplot 教程](https://matplotlib.org/tutorials/introductory/pyplot.html)，以深入了解 pyplot 界面。

大多数条款都很简单，但要记住的主要是：

+  该图是可能包含 1 个或更多轴的最终图像。
+  轴代表一个单独的图（不要将其与 “轴” 这个词混淆，后者指的是图的 x /y 轴）。

我们称之为直接从 Axes 进行绘图的方法，这使我们在定制绘图方面具有更大的灵活性和强大功能。

**注意**：通常，尝试在 pyplot 接口上使用面向对象的接口。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#我们的数据)我们的数据

我们将使用本教程派生的帖子中的数据。它包含许多公司的销售信息。

```python
# sphinx_gallery_thumbnail_number = 10
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#快速开始)快速开始

这些数据自然可视化为条形图，每组一个条形图。要使用面向对象的方法，我们将首先生成一个图形实例。[figure.Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 和 [axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes)。图就像一个画布，Axes 是画布的一部分，我们将在其上进行特定的可视化。

**注意** ：图字上可以有多个轴。 有关如何执行此操作的信息，请参阅 [“紧密布局” 教程](https://matplotlib.org/tutorials/intermediate/tight_layout_guide.html)。

```python
fig, ax = plt.subplots()
```

![生命周期示例](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_001-1565507123851.png)

现在我们有了一个 Axes 实例，我们可以在它上面进行绘图。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```

![生命周期示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_002-1565507123834.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#控制风格)控制风格

Matplotlib 中有许多样式可供您根据需要定制可视化。要查看样式列表，我们可以使用 pyplot.style。

```python
print(plt.style.available)
```

输出：

```python
['seaborn-dark', 'dark_background', 'seaborn-pastel', 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', '_classic_test', 'ggplot', 'seaborn-white', 'classic', 'Solarize_Light2', 'seaborn-paper', 'fast', 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']
```

您可以使用以下内容激活样式：

```python
plt.style.use('fivethirtyeight')
```

现在让我们重新制作上面的图像，看看它的样子：

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```

![生命周期示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_003-1565507123857.png)

样式控制很多东西，比如颜色，线宽，背景等。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#自定义绘制)自定义绘制

现在我们已经得到了一个我们想要的一般外观的绘制，所以让我们对它进行微调，以便它可以打印出来。 首先让我们旋转 x 轴上的标签，使它们更清晰地显示出来。使用 [axes.Axes.get_xticklabels()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels) 方法将这些标签：

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
```

![生命周期示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_004-1565507123885.png)

如果我们想一次设置多个项的属性，那么使用 [pyplot.setp()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp) 函数会很有用。 这将获取 Matplotlib 对象的列表（或许多列表），并尝试设置每个对象的一些样式元素。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

![生命周期示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_005-1565507123853.png)

看起来这样会切断底部的一些标签。我们可以告诉 Matplotlib 自动为我们创建的图中的元素腾出空间。为此，我们将设置 rcParams 的 autolayout 值。有关使用 rcParams 控制图的样式，布局和其他功能的更多信息，请参阅[使用样式表和 rcParams 自定义 Matplotlib](https://matplotlib.org/tutorials/introductory/customizing.html)。

```python
plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

![生命周期示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_006-1565507123876.png)

接下来，我们将为图添加标签。 要使用 OO 接口执行此操作，我们可以使用 [axes.Axes.set()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set) 方法设置此 Axes 对象的属性。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```

![生命周期示例6](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_007-1565507123979.png)

我们还可以使用 [pyplot.subplots()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots) 函数调整此图的大小。我们可以用 figsize kwarg 做到这一点。

**注意**：虽然 NumPy 中的索引遵循形式（行，列），但 figsize kwarg 遵循形式（宽度，高度）。这遵循可视化中的惯例，遗憾的是它们与线性代数的惯例不同。

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```

![生命周期示例7](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_008-1565507123956.png)

对于标签，我们可以使用 [ticker.FuncFormatter](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.FuncFormatter) 类以函数的形式指定自定义格式指南。 下面我们将定义一个以整数作为输入的函数，并返回一个字符串作为输出。

```python
def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currency)
```

然后我们可以将此格式化程序应用于我们的绘图上的标签。为此，我们将使用轴的 xaxis 属性。这使您可以在我们的绘图上对特定轴执行操作。

```python
fig, ax = plt.subplots(figsize=(6, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)
```

![生命周期示例8](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_009-1565507123970.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#结合多个可视化)结合多个可视化

可以在 [axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 的同一个实例上绘制多个绘图元素。为此，我们只需要在该轴对象上调用另一个绘图方法。

```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we'll move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(right=.1)

plt.show()
```

![生命周期示例9](pictures/Matplotlib 中文手册.assets/sphx_glr_lifecycle_010-1565507124004.png)

### [#](https://www.matplotlib.org.cn/tutorials/introductory/lifecycle.html#保存我们的绘制)保存我们的绘制

现在我们对我们的绘制结果感到满意，我们希望将其保存到磁盘。我们可以在 Matplotlib 中保存许多文件格式。要查看可用选项列表，请使用：

```python
print(fig.canvas.get_supported_filetypes())
```

输出：

```python
{'ps': 'Postscript', 'eps': 'Encapsulated Postscript', 'pdf': 'Portable Document Format', 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap', 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 'jpg': 'Joint Photographic Experts Group', 'jpeg': 'Joint Photographic Experts Group', 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format'}
```

然后我们可以使用 [figure.Figure.savefig()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.savefig) 来将数字保存到磁盘。请注意，我们将在下面显示几个有用的标志：

+  transparent = True 如果格式支持，则使保存的图形的背景透明。
+  dpi = 80 控制输出的分辨率（每平方英寸的点数）。
+  bbox_inches = "tight" 符合图中我们绘制的界限。

```python
# Uncomment this line to save the figure.
# fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```



## 使用样式表和 rcparams 自定义 Matplotlib

自定义 Matplotlib 的属性和默认样式的提示。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#使用样式表)使用样式表

`样式`包添加了对易于切换绘制 “样式” 的支持，其具有与 [matplotlib rc](https://matplotlib.org/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files) 文件相同的参数（在启动时读取以配置 matplotlib）。

Matplotlib 提供了许多[预定义的样式](https://github.com/matplotlib/matplotlib/tree/master/lib/matplotlib/mpl-data/stylelib)。例如，有一种名为 “gglot” 的预定义样式，它模拟了 [ggplot](http://ggplot2.org/)（一种流行的 [R](https://www.r-project.org/) 绘图软件包）的美感。要使用此样式，只需添加：

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('ggplot')
data = np.random.randn(50)
```

要列出所有可用的样式，请使用：

```python
print(plt.style.available)
```

输出：

```python
['seaborn-dark', 'dark_background', 'seaborn-pastel', 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', '_classic_test', 'ggplot', 'seaborn-white', 'classic', 'Solarize_Light2', 'seaborn-paper', 'fast', 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#定义自己的风格)定义自己的风格

您可以通过调用 `style.use`` 以及样式表的路径或 URL 来创建自定义样式并使用它们。此外，如果将 `<style-name>.mplstyle` 文件添加到 mpl_configdir /stylelib，则可以通过调用 `style.use(<style-name>)`重用自定义样式表。 默认情况下，`mpl_configdir` 应为 `~/.config/matplotlib` ，但您可以使用 matplotlib.get_configdir () 来检查您的位置。您可能需要创建此目录。您还可以通过设置 MPLCONFIGDIR 环境变量 来更改 matplotlib 查找 stylelib/ 文件夹的目录，请参阅 [matplotlib 配置和缓存目录位置](https://matplotlib.org/faq/troubleshooting_faq.html#locating-matplotlib-config-dir)。

请注意，如果样式具有相同的名称，`mpl_configdir / stylelib` 中的自定义样式表将覆盖 matplotlib 定义的样式表。

例如，您可能希望使用以下命令创建 `mpl_configdir/stylelib/presentation.mplstyle`：

```python
axes.titlesize : 24
axes.labelsize : 20
lines.linewidth : 3
lines.markersize : 10
xtick.labelsize : 16
ytick.labelsize : 16
```

然后，当您想要将针对纸张设计的绘图调整为在演示文稿中看起来很好的绘图时，您可以添加：

```python
>>> import matplotlib.pyplot as plt
>>> plt.style.use('presentation')
```

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#构图风格)构图风格

样式表旨在组合在一起。因此，您可以拥有一个自定义颜色的样式表和一个可以改变演示文稿元素大小的单独样式表。通过传递样式列表可以轻松组合这些样式：

```python
>>> import matplotlib.pyplot as plt
>>> plt.style.use(['dark_background', 'presentation'])
```

请注意，右侧的样式将覆盖左侧样式已定义的值。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#临时样式)临时样式

如果您只想为特定代码块使用样式但不想更改全局样式，则样式包提供上下文管理器，用于将更改限制为特定范围。要隔离样式更改，可以编写如下内容：

```python
with plt.style.context(('dark_background')):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()
```

![临时样式](pictures/Matplotlib 中文手册.assets/sphx_glr_customizing_001-1565507152765.png)

## [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#matplotlib-rcParams)matplotlib rcParams

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#动态rc设置)动态 rc 设置

您还可以在 python 脚本中动态更改默认的 rc 设置，或者从 python shell 以交互方式更改。 所有 rc 设置都存储在一个名为 [matplotlib.rcParams](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rcParams) 的类字典变量中，该变量对于 matplotlib 包是全局的。rcParams 可以直接修改，例如：

```python
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'
plt.plot(data)
```

![折线图](pictures/Matplotlib 中文手册.assets/sphx_glr_customizing_002-1565507152779.png)

Matplotlib 还提供了一些用于修改 rc 设置的便捷功能。[matplotlib.rc()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rc) 命令可用于使用关键字参数一次修改单个组中的多个设置：

```python
mpl.rc('lines', linewidth=4, color='g')
plt.plot(data)
```

![折线图2](pictures/Matplotlib 中文手册.assets/sphx_glr_customizing_003-1565507152801.png)

[matplotlib.rcdefaults()](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rcdefaults) 命令将恢复标准的 matplotlib 默认设置。

设置 rcParams 的值时有一定程度的验证，有关详细信息，请参阅 [matplotlib.rcsetup](https://matplotlib.org/api/rcsetup_api.html#module-matplotlib.rcsetup)。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#matplotlibrc文件)matplotlibrc 文件

matplotlib 使用 `matplotlibrc` 配置文件来自定义各种属性，我们称之为 `rc设置或rc参数`。您可以控制 matplotlib 中几乎每个属性的默认值：图形大小和 dpi，线宽，颜色和样式，轴，轴和网格属性，文本和字体属性等。matplotlib 按以下顺序在四个位置查找 `matplotlibrc`：

1. 当前工作目录中的 `matplotlibrc`，通常用于您不希望在其他地方应用的特定自定义。
2. `$ MATPLOTLIBRC` 如果是文件，否则 `$MATPLOTLIBRC/matplotlibrc`。
3. 它接下来是在特定于用户的位置，具体取决于您的平台：
   +  在 Linux 和 FreeBSD 上，如果您已经自定义环境，它会查看.config/matplotlib/matplotlibrc（或 $ XDG_CONFIG_HOME/matplotlib/matplotlibrc）。On Linux and FreeBSD, it looks in .config/matplotlib/matplotlibrc (or $XDG_CONFIG_HOME/matplotlib/matplotlibrc) if you've customized your environment.
   +  在其他平台上，它查找.matplotlib/matplotlibrc。
      请参阅 [matplotlib 配置和缓存目录位置](https://matplotlib.org/faq/troubleshooting_faq.html#locating-matplotlib-config-dir)。
4. `INSTALL/matplotlib/mpl-data/matplotlibrc`，其中 *INSTALL* 类似于 Linux 上的 `/usr/lib/python3.5/site-packages`，可能是 Windows 上的 `C:\Python35\Lib\site-packages`。每次安装 matplotlib 时，都会覆盖此文件，因此如果要保存自定义项，请将此文件移动到特定于用户的 matplotlib 目录。

一旦找到 `matplotlibrc` 文件，它就不会搜索任何其他路径。

要显示当前活动的 matplotlibrc 文件的加载位置，可以执行以下操作：

```python
>>> import matplotlib
>>> matplotlib.matplotlib_fname()
'/home/foo/.config/matplotlib/matplotlibrc'
```

请参阅下面的示例 [matplotlibrc 文件](https://matplotlib.org/tutorials/introductory/customizing.html#matplotlibrc-sample)。虽然所有参数都是可选的，但您应该几乎总是设置后端，否则 matplotlib 将选择 Agg，一个非交互式后端。 这可能会导致意外行为，因为如果您没有 `matplotlibrc` 文件，它通常会回退到 `INSTALL/matplotlib/mpl-data/matplotlibrc`，它通常由软件包维护者设置为交互式后端。

### [#](https://www.matplotlib.org.cn/tutorials/introductory/customizing.html#一个示例matplotlibrc文件)一个示例 matplotlibrc 文件

```python
#### MATPLOTLIBRC FORMAT

## This is a sample matplotlib configuration file - you can find a copy
## of it on your system in
## site-packages/matplotlib/mpl-data/matplotlibrc.  If you edit it
## there, please note that it will be overwritten in your next install.
## If you want to keep a permanent local copy that will not be
## overwritten, place it in the following location:
## unix/linux:
##      $HOME/.config/matplotlib/matplotlibrc or
##      $XDG_CONFIG_HOME/matplotlib/matplotlibrc (if $XDG_CONFIG_HOME is set)
## other platforms:
##      $HOME/.matplotlib/matplotlibrc
##
## See http://matplotlib.org/users/customizing.html#the-matplotlibrc-file for
## more details on the paths which are checked for the configuration file.
##
## This file is best viewed in a editor which supports python mode
## syntax highlighting. Blank lines, or lines starting with a comment
## symbol, are ignored, as are trailing comments.  Other lines must
## have the format
##     key : val ## optional comment
##
## Colors: for the color values below, you can either use - a
## matplotlib color string, such as r, k, or b - an rgb tuple, such as
## (1.0, 0.5, 0.0) - a hex string, such as ff00ff - a scalar
## grayscale intensity such as 0.75 - a legal html color name, e.g., red,
## blue, darkslategray

##### CONFIGURATION BEGINS HERE

## The default backend. If you omit this parameter, the first
## working backend from the following list is used:
## MacOSX Qt5Agg Qt4Agg Gtk3Agg GTK3Cairo TkAgg WxAgg Agg Cairo
##
## Other choices include: WX PS PDF SVG Template.
##
## You can also deploy your own backend outside of matplotlib by
## referring to the module name (which must be in the PYTHONPATH) as
## 'module://my_backend'.
#backend      : Agg

## Note that this can be overridden by the environment variable
## QT_API used by Enthought Tool Suite (ETS); valid values are
## "pyqt" and "pyside".  The "pyqt" setting has the side effect of
## forcing the use of Version 2 API for QString and QVariant.

## The port to use for the web server in the WebAgg backend.
#webagg.port : 8988

## The address on which the WebAgg web server should be reachable
#webagg.address : 127.0.0.1

## If webagg.port is unavailable, a number of other random ports will
## be tried until one that is available is found.
#webagg.port_retries : 50

## When True, open the webbrowser to the plot that is shown
#webagg.open_in_browser : True

## if you are running pyplot inside a GUI and your backend choice
## conflicts, we will automatically try to find a compatible one for
## you if backend_fallback is True
#backend_fallback: True

#interactive  : False
#toolbar      : toolbar2   ## None | toolbar2  ("classic" is deprecated)
#timezone     : UTC        ## a pytz timezone string, e.g., US/Central or Europe/Paris

## Where your matplotlib data lives if you installed to a non-default
## location.  This is where the matplotlib fonts, bitmaps, etc reside
#datapath : /home/jdhunter/mpldata


#### LINES
## See http://matplotlib.org/api/artist_api.html#module-matplotlib.lines for more
## information on line properties.
#lines.linewidth   : 1.5     ## line width in points
#lines.linestyle   : -       ## solid line
#lines.color       : C0      ## has no affect on plot(); see axes.prop_cycle
#lines.marker      : None    ## the default marker
#lines.markerfacecolor  : auto    ## the default markerfacecolor
#lines.markeredgecolor  : auto    ## the default markeredgecolor
#lines.markeredgewidth  : 1.0     ## the line width around the marker symbol
#lines.markersize  : 6            ## markersize, in points
#lines.dash_joinstyle : round        ## miter|round|bevel
#lines.dash_capstyle : butt          ## butt|round|projecting
#lines.solid_joinstyle : round       ## miter|round|bevel
#lines.solid_capstyle : projecting   ## butt|round|projecting
#lines.antialiased : True         ## render lines in antialiased (no jaggies)

## The three standard dash patterns.  These are scaled by the linewidth.
#lines.dashed_pattern : 3.7, 1.6
#lines.dashdot_pattern : 6.4, 1.6, 1, 1.6
#lines.dotted_pattern : 1, 1.65
#lines.scale_dashes : True

#markers.fillstyle: full ## full|left|right|bottom|top|none

#### PATCHES
## Patches are graphical objects that fill 2D space, like polygons or
## circles.  See
## http://matplotlib.org/api/artist_api.html#module-matplotlib.patches
## information on patch properties
#patch.linewidth        : 1        ## edge width in points.
#patch.facecolor        : C0
#patch.edgecolor        : black   ## if forced, or patch is not filled
#patch.force_edgecolor  : False   ## True to always use edgecolor
#patch.antialiased      : True    ## render patches in antialiased (no jaggies)

#### HATCHES
#hatch.color     : black
#hatch.linewidth : 1.0

#### Boxplot
#boxplot.notch       : False
#boxplot.vertical    : True
#boxplot.whiskers    : 1.5
#boxplot.bootstrap   : None
#boxplot.patchartist : False
#boxplot.showmeans   : False
#boxplot.showcaps    : True
#boxplot.showbox     : True
#boxplot.showfliers  : True
#boxplot.meanline    : False

#boxplot.flierprops.color           : black
#boxplot.flierprops.marker          : o
#boxplot.flierprops.markerfacecolor : none
#boxplot.flierprops.markeredgecolor : black
#boxplot.flierprops.markersize      : 6
#boxplot.flierprops.linestyle       : none
#boxplot.flierprops.linewidth       : 1.0

#boxplot.boxprops.color     : black
#boxplot.boxprops.linewidth : 1.0
#boxplot.boxprops.linestyle : -

#boxplot.whiskerprops.color     : black
#boxplot.whiskerprops.linewidth : 1.0
#boxplot.whiskerprops.linestyle : -

#boxplot.capprops.color     : black
#boxplot.capprops.linewidth : 1.0
#boxplot.capprops.linestyle : -

#boxplot.medianprops.color     : C1
#boxplot.medianprops.linewidth : 1.0
#boxplot.medianprops.linestyle : -

#boxplot.meanprops.color           : C2
#boxplot.meanprops.marker          : ^
#boxplot.meanprops.markerfacecolor : C2
#boxplot.meanprops.markeredgecolor : C2
#boxplot.meanprops.markersize      :  6
#boxplot.meanprops.linestyle       : --
#boxplot.meanprops.linewidth       : 1.0


#### FONT

## font properties used by text.Text.  See
## http://matplotlib.org/api/font_manager_api.html for more
## information on font properties.  The 6 font properties used for font
## matching are given below with their default values.
##
## The font.family property has five values: 'serif' (e.g., Times),
## 'sans-serif' (e.g., Helvetica), 'cursive' (e.g., Zapf-Chancery),
## 'fantasy' (e.g., Western), and 'monospace' (e.g., Courier).  Each of
## these font families has a default list of font names in decreasing
## order of priority associated with them.  When text.usetex is False,
## font.family may also be one or more concrete font names.
##
## The font.style property has three values: normal (or roman), italic
## or oblique.  The oblique style will be used for italic, if it is not
## present.
##
## The font.variant property has two values: normal or small-caps.  For
## TrueType fonts, which are scalable fonts, small-caps is equivalent
## to using a font size of 'smaller', or about 83%% of the current font
## size.
##
## The font.weight property has effectively 13 values: normal, bold,
## bolder, lighter, 100, 200, 300, ..., 900.  Normal is the same as
## 400, and bold is 700.  bolder and lighter are relative values with
## respect to the current weight.
##
## The font.stretch property has 11 values: ultra-condensed,
## extra-condensed, condensed, semi-condensed, normal, semi-expanded,
## expanded, extra-expanded, ultra-expanded, wider, and narrower.  This
## property is not currently implemented.
##
## The font.size property is the default font size for text, given in pts.
## 10 pt is the standard value.

#font.family         : sans-serif
#font.style          : normal
#font.variant        : normal
#font.weight         : normal
#font.stretch        : normal
## note that font.size controls default text sizes.  To configure
## special text sizes tick labels, axes, labels, title, etc, see the rc
## settings for axes and ticks. Special text sizes can be defined
## relative to font.size, using the following values: xx-small, x-small,
## small, medium, large, x-large, xx-large, larger, or smaller
#font.size           : 10.0
#font.serif          : DejaVu Serif, Bitstream Vera Serif, Computer Modern Roman, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif     : DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
#font.cursive        : Apple Chancery, Textile, Zapf Chancery, Sand, Script MT, Felipa, cursive
#font.fantasy        : Comic Sans MS, Chicago, Charcoal, ImpactWestern, Humor Sans, xkcd, fantasy
#font.monospace      : DejaVu Sans Mono, Bitstream Vera Sans Mono, Computer Modern Typewriter, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace

#### TEXT
## text properties used by text.Text.  See
## http://matplotlib.org/api/artist_api.html#module-matplotlib.text for more
## information on text properties
#text.color          : black

#### LaTeX customizations. See http://wiki.scipy.org/Cookbook/Matplotlib/UsingTex
#text.usetex         : False  ## use latex for all text handling. The following fonts
                              ## are supported through the usual rc parameter settings:
                              ## new century schoolbook, bookman, times, palatino,
                              ## zapf chancery, charter, serif, sans-serif, helvetica,
                              ## avant garde, courier, monospace, computer modern roman,
                              ## computer modern sans serif, computer modern typewriter
                              ## If another font is desired which can loaded using the
                              ## LaTeX \usepackage command, please inquire at the
                              ## matplotlib mailing list
#text.latex.preamble :      ## IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
                            ## AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
                            ## IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
                            ## preamble is a comma separated list of LaTeX statements
                            ## that are included in the LaTeX document preamble.
                            ## An example:
                            ## text.latex.preamble : \usepackage{bm},\usepackage{euler}
                            ## The following packages are always loaded with usetex, so
                            ## beware of package collisions: color, geometry, graphicx,
                            ## type1cm, textcomp. Adobe Postscript (PSSNFS) font packages
                            ## may also be loaded, depending on your font settings
#text.latex.preview : False

#text.hinting : auto   ## May be one of the following:
                       ##   none: Perform no hinting
                       ##   auto: Use FreeType's autohinter
                       ##   native: Use the hinting information in the
                       #              font file, if available, and if your
                       #              FreeType library supports it
                       ##   either: Use the native hinting information,
                       #              or the autohinter if none is available.
                       ## For backward compatibility, this value may also be
                       ## True === 'auto' or False === 'none'.
#text.hinting_factor : 8 ## Specifies the amount of softness for hinting in the
                         ## horizontal direction.  A value of 1 will hint to full
                         ## pixels.  A value of 2 will hint to half pixels etc.
#text.antialiased : True ## If True (default), the text will be antialiased.
                         ## This only affects the Agg backend.

## The following settings allow you to select the fonts in math mode.
## They map from a TeX font name to a fontconfig font pattern.
## These settings are only used if mathtext.fontset is 'custom'.
## Note that this "custom" mode is unsupported and may go away in the
## future.
#mathtext.cal : cursive
#mathtext.rm  : sans
#mathtext.tt  : monospace
#mathtext.it  : sans:italic
#mathtext.bf  : sans:bold
#mathtext.sf  : sans
#mathtext.fontset : dejavusans ## Should be 'dejavusans' (default),
                               ## 'dejavuserif', 'cm' (Computer Modern), 'stix',
                               ## 'stixsans' or 'custom'
#mathtext.fallback_to_cm : True  ## When True, use symbols from the Computer Modern
                                 ## fonts when a symbol can not be found in one of
                                 ## the custom math fonts.
#mathtext.default : it ## The default font to use for math.
                       ## Can be any of the LaTeX font names, including
                       ## the special name "regular" for the same font
                       ## used in regular text.

#### AXES
## default face and edge color, default tick sizes,
## default fontsizes for ticklabels, and so on.  See
## http://matplotlib.org/api/axes_api.html#module-matplotlib.axes
#axes.facecolor      : white   ## axes background color
#axes.edgecolor      : black   ## axes edge color
#axes.linewidth      : 0.8     ## edge linewidth
#axes.grid           : False   ## display grid or not
#axes.grid.axis      : both    ## which axis the grid should apply to
#axes.grid.which     : major   ## gridlines at major, minor or both ticks
#axes.titlesize      : large   ## fontsize of the axes title
#axes.titleweight    : normal  ## font weight of title
#axes.titlepad       : 6.0     ## pad between axes and title in points
#axes.labelsize      : medium  ## fontsize of the x any y labels
#axes.labelpad       : 4.0     ## space between label and axis
#axes.labelweight    : normal  ## weight of the x and y labels
#axes.labelcolor     : black
#axes.axisbelow      : line    ## draw axis gridlines and ticks below
                               ## patches (True); above patches but below
                               ## lines ('line'); or above all (False)
#axes.formatter.limits : -7, 7 ## use scientific notation if log10
                               ## of the axis range is smaller than the
                               ## first or larger than the second
#axes.formatter.use_locale : False ## When True, format tick labels
                                   ## according to the user's locale.
                                   ## For example, use ',' as a decimal
                                   ## separator in the fr_FR locale.
#axes.formatter.use_mathtext : False ## When True, use mathtext for scientific
                                     ## notation.
#axes.formatter.min_exponent: 0 ## minimum exponent to format in scientific notation
#axes.formatter.useoffset      : True    ## If True, the tick label formatter
                                         ## will default to labeling ticks relative
                                         ## to an offset when the data range is
                                         ## small compared to the minimum absolute
                                         ## value of the data.
#axes.formatter.offset_threshold : 4     ## When useoffset is True, the offset
                                         ## will be used when it can remove
                                         ## at least this number of significant
                                         ## digits from tick labels.
#axes.spines.left   : True   ## display axis spines
#axes.spines.bottom : True
#axes.spines.top    : True
#axes.spines.right  : True
#axes.unicode_minus  : True    ## use unicode for the minus symbol
                               ## rather than hyphen.  See
                               ## http://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes
#axes.prop_cycle    : cycler('color', ['1f77b4', 'ff7f0e', '2ca02c', 'd62728', '9467bd', '8c564b', 'e377c2', '7f7f7f', 'bcbd22', '17becf'])
                      ## color cycle for plot lines  as list of string
                      ## colorspecs: single letter, long name, or web-style hex
                      ## Note the use of string escapes here ('1f77b4', instead of 1f77b4)
                      ## as opposed to the rest of this file.
#axes.autolimit_mode : data ## How to scale axes limits to the data.
                            ## Use "data" to use data limits, plus some margin
                            ## Use "round_number" move to the nearest "round" number
#axes.xmargin        : .05  ## x margin.  See `axes.Axes.margins`
#axes.ymargin        : .05  ## y margin See `axes.Axes.margins`
#polaraxes.grid      : True    ## display grid on polar axes
#axes3d.grid         : True    ## display grid on 3d axes

#### DATES
## These control the default format strings used in AutoDateFormatter.
## Any valid format datetime format string can be used (see the python
## `datetime` for details).  For example using '%%x' will use the locale date representation
## '%%X' will use the locale time representation and '%%c' will use the full locale datetime
## representation.
## These values map to the scales:
##     {'year': 365, 'month': 30, 'day': 1, 'hour': 1/24, 'minute': 1 / (24 * 60)}

#date.autoformatter.year     : %Y
#date.autoformatter.month    : %Y-%m
#date.autoformatter.day      : %Y-%m-%d
#date.autoformatter.hour     : %m-%d %H
#date.autoformatter.minute   : %d %H:%M
#date.autoformatter.second   : %H:%M:%S
#date.autoformatter.microsecond   : %M:%S.%f

#### TICKS
## see http://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick
#xtick.top            : False  ## draw ticks on the top side
#xtick.bottom         : True   ## draw ticks on the bottom side
#xtick.labeltop       : False  ## draw label on the top
#xtick.labelbottom    : True   ## draw label on the bottom
#xtick.major.size     : 3.5    ## major tick size in points
#xtick.minor.size     : 2      ## minor tick size in points
#xtick.major.width    : 0.8    ## major tick width in points
#xtick.minor.width    : 0.6    ## minor tick width in points
#xtick.major.pad      : 3.5    ## distance to major tick label in points
#xtick.minor.pad      : 3.4    ## distance to the minor tick label in points
#xtick.color          : black  ## color of the tick labels
#xtick.labelsize      : medium ## fontsize of the tick labels
#xtick.direction      : out    ## direction: in, out, or inout
#xtick.minor.visible  : False  ## visibility of minor ticks on x-axis
#xtick.major.top      : True   ## draw x axis top major ticks
#xtick.major.bottom   : True   ## draw x axis bottom major ticks
#xtick.minor.top      : True   ## draw x axis top minor ticks
#xtick.minor.bottom   : True   ## draw x axis bottom minor ticks
#xtick.alignment      : center ## alignment of xticks

#ytick.left           : True   ## draw ticks on the left side
#ytick.right          : False  ## draw ticks on the right side
#ytick.labelleft      : True   ## draw tick labels on the left side
#ytick.labelright     : False  ## draw tick labels on the right side
#ytick.major.size     : 3.5    ## major tick size in points
#ytick.minor.size     : 2      ## minor tick size in points
#ytick.major.width    : 0.8    ## major tick width in points
#ytick.minor.width    : 0.6    ## minor tick width in points
#ytick.major.pad      : 3.5    ## distance to major tick label in points
#ytick.minor.pad      : 3.4    ## distance to the minor tick label in points
#ytick.color          : black  ## color of the tick labels
#ytick.labelsize      : medium ## fontsize of the tick labels
#ytick.direction      : out    ## direction: in, out, or inout
#ytick.minor.visible  : False  ## visibility of minor ticks on y-axis
#ytick.major.left     : True   ## draw y axis left major ticks
#ytick.major.right    : True   ## draw y axis right major ticks
#ytick.minor.left     : True   ## draw y axis left minor ticks
#ytick.minor.right    : True   ## draw y axis right minor ticks
#ytick.alignment      : center_baseline ## alignment of yticks

#### GRIDS
#grid.color       :   b0b0b0    ## grid color
#grid.linestyle   :   -         ## solid
#grid.linewidth   :   0.8       ## in points
#grid.alpha       :   1.0       ## transparency, between 0.0 and 1.0

#### Legend
#legend.loc           : best
#legend.frameon       : True     ## if True, draw the legend on a background patch
#legend.framealpha    : 0.8      ## legend patch transparency
#legend.facecolor     : inherit  ## inherit from axes.facecolor; or color spec
#legend.edgecolor     : 0.8      ## background patch boundary color
#legend.fancybox      : True     ## if True, use a rounded box for the
                                 ## legend background, else a rectangle
#legend.shadow        : False    ## if True, give background a shadow effect
#legend.numpoints     : 1        ## the number of marker points in the legend line
#legend.scatterpoints : 1        ## number of scatter points
#legend.markerscale   : 1.0      ## the relative size of legend markers vs. original
#legend.fontsize      : medium
#legend.title_fontsize    : None ## None sets to the same as the default axes.  
## Dimensions as fraction of fontsize:
#legend.borderpad     : 0.4      ## border whitespace
#legend.labelspacing  : 0.5      ## the vertical space between the legend entries
#legend.handlelength  : 2.0      ## the length of the legend lines
#legend.handleheight  : 0.7      ## the height of the legend handle
#legend.handletextpad : 0.8      ## the space between the legend line and legend text
#legend.borderaxespad : 0.5      ## the border between the axes and legend edge
#legend.columnspacing : 2.0      ## column separation

#### FIGURE
## See http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure
#figure.titlesize : large      ## size of the figure title (Figure.suptitle())
#figure.titleweight : normal   ## weight of the figure title
#figure.figsize   : 6.4, 4.8   ## figure size in inches
#figure.dpi       : 100        ## figure dots per inch
#figure.facecolor : white      ## figure facecolor
#figure.edgecolor : white      ## figure edgecolor
#figure.frameon : True         ## enable figure frame
#figure.max_open_warning : 20  ## The maximum number of figures to open through
                               ## the pyplot interface before emitting a warning.
                               ## If less than one this feature is disabled.
## The figure subplot parameters.  All dimensions are a fraction of the
#figure.subplot.left    : 0.125  ## the left side of the subplots of the figure
#figure.subplot.right   : 0.9    ## the right side of the subplots of the figure
#figure.subplot.bottom  : 0.11   ## the bottom of the subplots of the figure
#figure.subplot.top     : 0.88   ## the top of the subplots of the figure
#figure.subplot.wspace  : 0.2    ## the amount of width reserved for space between subplots,
                                 ## expressed as a fraction of the average axis width
#figure.subplot.hspace  : 0.2    ## the amount of height reserved for space between subplots,
                                 ## expressed as a fraction of the average axis height

## Figure layout
#figure.autolayout : False     ## When True, automatically adjust subplot
                               ## parameters to make the plot fit the figure
                               ## using `tight_layout`
#figure.constrained_layout.use: False ## When True, automatically make plot
                                      ## elements fit on the figure. (Not compatible
                                      ## with `autolayout`, above).
#figure.constrained_layout.h_pad : 0.04167 ## Padding around axes objects. Float representing
#figure.constrained_layout.w_pad : 0.04167 ##  inches. Default is 3./72. inches (3 pts)
#figure.constrained_layout.hspace : 0.02   ## Space between subplot groups. Float representing
#figure.constrained_layout.wspace : 0.02   ##  a fraction of the subplot widths being separated.

#### IMAGES
#image.aspect : equal             ## equal | auto | a number
#image.interpolation  : nearest   ## see help(imshow) for options
#image.cmap   : viridis           ## A colormap name, gray etc...
#image.lut    : 256               ## the size of the colormap lookup table
#image.origin : upper             ## lower | upper
#image.resample  : True
#image.composite_image : True     ## When True, all the images on a set of axes are
                                  ## combined into a single composite image before
                                  ## saving a figure as a vector graphics file,
                                  ## such as a PDF.

#### CONTOUR PLOTS
#contour.negative_linestyle : dashed ## string or on-off ink sequence
#contour.corner_mask        : True   ## True | False | legacy

#### ERRORBAR PLOTS
#errorbar.capsize : 0             ## length of end cap on error bars in pixels

#### HISTOGRAM PLOTS
#hist.bins : 10                   ## The default number of histogram bins.
                                  ## If Numpy 1.11 or later is
                                  ## installed, may also be `auto`

#### SCATTER PLOTS
#scatter.marker : o               ## The default marker type for scatter plots.

#### Agg rendering
#### Warning: experimental, 2008/10/10
#agg.path.chunksize : 0           ## 0 to disable; values in the range
                                  ## 10000 to 100000 can improve speed slightly
                                  ## and prevent an Agg rendering failure
                                  ## when plotting very large data sets,
                                  ## especially if they are very gappy.
                                  ## It may cause minor artifacts, though.
                                  ## A value of 20000 is probably a good
                                  ## starting point.
#### PATHS
#path.simplify : True   ## When True, simplify paths by removing "invisible"
                        ## points to reduce file size and increase rendering
                        ## speed
#path.simplify_threshold : 0.111111111111  ## The threshold of similarity below which
                                           ## vertices will be removed in the
                                           ## simplification process
#path.snap : True ## When True, rectilinear axis-aligned paths will be snapped to
                  ## the nearest pixel when certain criteria are met.  When False,
                  ## paths will never be snapped.
#path.sketch : None ## May be none, or a 3-tuple of the form (scale, length,
                    ## randomness).
                    ## *scale* is the amplitude of the wiggle
                    ## perpendicular to the line (in pixels).  *length*
                    ## is the length of the wiggle along the line (in
                    ## pixels).  *randomness* is the factor by which
                    ## the length is randomly scaled.
#path.effects : []  ##

#### SAVING FIGURES
## the default savefig params can be different from the display params
## e.g., you may want a higher resolution, or to make the figure
## background white
#savefig.dpi         : figure   ## figure dots per inch or 'figure'
#savefig.facecolor   : white    ## figure facecolor when saving
#savefig.edgecolor   : white    ## figure edgecolor when saving
#savefig.format      : png      ## png, ps, pdf, svg
#savefig.bbox        : standard ## 'tight' or 'standard'.
                                ## 'tight' is incompatible with pipe-based animation
                                ## backends but will workd with temporary file based ones:
                                ## e.g. setting animation.writer to ffmpeg will not work,
                                ## use ffmpeg_file instead
#savefig.pad_inches  : 0.1      ## Padding to be used when bbox is set to 'tight'
#savefig.jpeg_quality: 95       ## when a jpeg is saved, the default quality parameter.
#savefig.directory   : ~        ## default directory in savefig dialog box,
                                ## leave empty to always use current working directory
#savefig.transparent : False    ## setting that controls whether figures are saved with a
                                ## transparent background by default
#savefig.frameon : True            ## enable frame of figure when saving
#savefig.orientation : portrait    ## Orientation of saved figure

### tk backend params
#tk.window_focus   : False    ## Maintain shell focus for TkAgg

### ps backend params
#ps.papersize      : letter   ## auto, letter, legal, ledger, A0-A10, B0-B10
#ps.useafm         : False    ## use of afm fonts, results in small files
#ps.usedistiller   : False    ## can be: None, ghostscript or xpdf
                                          ## Experimental: may produce smaller files.
                                          ## xpdf intended for production of publication quality files,
                                          ## but requires ghostscript, xpdf and ps2eps
#ps.distiller.res  : 6000      ## dpi
#ps.fonttype       : 3         ## Output Type 3 (Type3) or Type 42 (TrueType)

### pdf backend params
#pdf.compression   : 6   ## integer from 0 to 9
                         ## 0 disables compression (good for debugging)
#pdf.fonttype       : 3         ## Output Type 3 (Type3) or Type 42 (TrueType)
#pdf.use14corefonts : False
#pdf.inheritcolor : False

### svg backend params
#svg.image_inline : True       ## write raster image data directly into the svg file
#svg.fonttype :   path         ## How to handle SVG fonts:
   ##     none: Assume fonts are installed on the machine where the SVG will be viewed.
   ##     path: Embed characters as paths -- supported by most SVG renderers
   ##     svgfont: Embed characters as SVG fonts -- supported only by Chrome,
   ##                Opera and Safari
#svg.hashsalt : None           ## if not None, use this string as hash salt
                               ## instead of uuid4
### pgf parameter
#pgf.rcfonts : True
#pgf.preamble :
#pgf.texsystem : xelatex

### docstring params
##docstring.hardcopy = False  ## set this when you want to generate hardcopy docstring

## Event keys to interact with figures/plots via keyboard.
## Customize these settings according to your needs.
## Leave the field(s) empty if you don't need a key-map. (i.e., fullscreen : '')
#keymap.fullscreen : f, ctrl+f       ## toggling
#keymap.home : h, r, home            ## home or reset mnemonic
#keymap.back : left, c, backspace    ## forward / backward keys to enable
#keymap.forward : right, v           ##   left handed quick navigation
#keymap.pan : p                      ## pan mnemonic
#keymap.zoom : o                     ## zoom mnemonic
#keymap.save : s, ctrl+s             ## saving current figure
#keymap.help : f1                    ## display help about active tools
#keymap.quit : ctrl+w, cmd+w, q      ## close the current figure
#keymap.quit_all : W, cmd+W, Q       ## close all figures
#keymap.grid : g                     ## switching on/off major grids in current axes
#keymap.grid_minor : G               ## switching on/off minor grids in current axes
#keymap.yscale : l                   ## toggle scaling of y-axes ('log'/'linear')
#keymap.xscale : k, L                ## toggle scaling of x-axes ('log'/'linear')
#keymap.all_axes : a                 ## enable all axes
#keymap.copy : ctrl+c, cmd+c         ## Copy figure to clipboard

###ANIMATION settings
#animation.html :  none            ## How to display the animation as HTML in
                                   ## the IPython notebook. 'html5' uses
                                   ## HTML5 video tag; 'jshtml' creates a
                                   ## Javascript animation
#animation.writer : ffmpeg         ## MovieWriter 'backend' to use
#animation.codec : h264            ## Codec to use for writing movie
#animation.bitrate: -1             ## Controls size/quality tradeoff for movie.
                                   ## -1 implies let utility auto-determine
#animation.frame_format:  png      ## Controls frame format used by temp files
#animation.html_args:              ## Additional arguments to pass to html writer
#animation.ffmpeg_path:  ffmpeg    ## Path to ffmpeg binary. Without full path
                                   ## $PATH is searched
#animation.ffmpeg_args:            ## Additional arguments to pass to ffmpeg
#animation.avconv_path:  avconv    ## Path to avconv binary. Without full path
                                   ## $PATH is searched
#animation.avconv_args:            ## Additional arguments to pass to avconv
#animation.convert_path:  convert  ## Path to ImageMagick's convert binary.
                                   ## On Windows use the full path since convert
                                   ## is also the name of a system tool.
#animation.convert_args:           ## Additional arguments to pass to convert
#animation.embed_limit : 20.0
```



# matplotlib 进阶

这些教程涵盖了 Matplotlib 中一些更复杂的类和函数。它们可用于特定的自定义和复杂可视化。

## 艺术家对象教程

使用 Artist 对象在画布上渲染。

matplotlib API 有三层。

+  `matplotlib.backend_bases.FigureCanvas` 是绘制图形的区域。
+  `matplotlib.backend_bases.Renderer` 是知道如何在 FigureCanvas 上绘制的对象。
+  [matplotlib.artist.Artist](https://matplotlib.org/api/artist_api.html#matplotlib.artist.Artist) 是知道如何使用渲染器绘制到画布上的对象。

`FigureCanvas` 和 Renderer 处理与 [wxPython](https://www.wxpython.org/) 等用户界面工具包或 PostScript® 等绘图语言交谈的所有细节，而 `Artist` 处理所有高级构造，如表示和布置图形，文本和线条。典型的用户将花费 95％的时间与 `Artists` 合作。

`Artists` 有两种类型：基元和容器。基元代表我们想要在画布上绘制的标准图形对象：[Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D), [Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle), [Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text), [AxesImage](https://matplotlib.org/api/image_api.html#matplotlib.image.AxesImage) 等，容器是放置它们的位置（[Axis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Axis), [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 和 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)）。 标准用法是创建一个 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 实例，使用 Figure 创建一个或多个 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 或 Subplot 实例，并使用 Axes 实例辅助方法创建基元。 在下面的示例中，我们使用 [matplotlib.pyplot.figure()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure) 创建一个 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 实例，这是一个方便的方法，用于实例化图实例并将它们与您的用户界面或绘图工具包 FigureCanvas 连接。正如我们将在下面讨论的那样，这不是必需的 - 你可以直接使用 PostScript，PDF Gtk + 或 wxPython FigureCanvas 实例，直接实例化你的数字并自己连接它们 - 但是因为我们专注于 Artist API 我们将会 让 [pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 为我们处理一些细节：

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2,1,1) # two rows, one column, first plot
```

[Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 可能是 matplotlib API 中最重要的类，也是您大部分时间都在使用的类。 这是因为 Axes 是大多数对象所在的绘图区域，Axes 有许多特殊的辅助方法（[plot()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot), [text()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text), [hist()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist), [imshow()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow)）来创建最常见的图形基元（[Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D), [Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text), [Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle)，Image，分别）。这些辅助方法将获取您的数据（例如，numpy 数组和字符串）并根据需要创建原始 Artist 实例（例如，Line2D），将它们添加到相关容器，并在请求时绘制它们。 你们大多数人可能都熟悉 Subplot，这只是一个 Axe 的一个特例，它存在于 Subplot 实例的逐行列网格中。 如果要在任意位置创建 Axes，只需使用 [add_axes()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_axes) 方法，该方法采用 0-1 相对图形坐标中的 [left，bottom，width，height] 值列表：

```python
fig2 = plt.figure()
ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])
```

继续我们的例子：

```python
import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)
```

在这个例子中，`ax` 是上面的 `fig.add_subplot` 调用创建的 Axes 实例（记住 Subplot 只是 Axes 的子类），当你调用 `ax.plot` 时，它会创建一个 `Line2D` 实例并将其添加到 Axes.lines 列表中。在下面的交互式 [ipython](http://ipython.org/) 会话中，您可以看到 `Axes.lines` 列表的长度为 1，并且包含该行返回的 `line, = ax.plot...`，调用：

```python
In [101]: ax.lines[0]
Out[101]: <matplotlib.lines.Line2D instance at 0x19a95710>

In [102]: line
Out[102]: <matplotlib.lines.Line2D instance at 0x19a95710>
```

如果您对 ax.plot 进行后续调用（并且保持状态为 “on”，这是默认值），则会向列表中添加其他行。您可以稍后通过调用 list 方法删除行；其中任何一个都可行：

```python
del ax.lines[0]
ax.lines.remove(line)  # one or the other, not both!
```

Axes 还有辅助方法来配置和装饰 x 轴和 y 轴刻度线，刻度标签和轴标签：

```python
xtext = ax.set_xlabel('my xdata') # returns a Text instance
ytext = ax.set_ylabel('my ydata')
```

当您调用 [ax.set_xlabel](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel) 时，它会传递 [XAxis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.XAxis) 的 [Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text) 实例上的信息。每个 Axes 实例都包含一个 [XAxis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.XAxis) 和一个 [YAxis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.YAxis) 实例，用于处理刻度，刻度标签和轴标签的布局和绘图。

尝试创建下图。

```python
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

# Fixing random state for reproducibility
np.random.seed(19680801)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50,
                            facecolor='yellow', edgecolor='yellow')
ax2.set_xlabel('time (s)')

plt.show()
```

![艺术家对象教程示例](pictures/Matplotlib 中文手册.assets/sphx_glr_artists_001.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#自定义对象)自定义对象

图中的每个元素都由 matplotlib [Artist](https://matplotlib.org/api/artist_api.html#matplotlib.artist.Artist) 表示，每个元素都有一个广泛的属性列表来配置它的外观。 图形本身包含一个与图形大小完全相同的矩形，您可以使用它来设置图形的背景颜色和透明度。同样，每个 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 边界框（典型 matplotlib 图中带有黑色边的标准白色框，都有一个 [Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle) 实例，用于确定 Axes 的颜色，透明度和其他属性。这些实例存储为成员变量 Figure.patch 和 Axes.patch（“Patch” 是一个继承自 MATLAB 的名称，是图中颜色的 2D “补丁”，例如矩形，圆形和多边形）。每个 matplotlib Artist 都具有以下属性

| 属性       | 描述                                                 |
| ---------- | ---------------------------------------------------- |
| alpha      | 透明度 - 0-1 的标量                                  |
| animated   | 一种用于促进动画绘制的布尔值。                       |
| axes       | Artist 对象载体轴，可能是 None。                     |
| clip_box   | 一种裁剪 Artist 对象的边界边框。                     |
| clip_on    | 是否启用剪裁                                         |
| clip_path  | Artist 剪辑的路径                                    |
| contains   | 用于测试 Artist 是否包含拾取点的拾取功能             |
| figure     | Artist 对象实例的载体，可能是 None。                 |
| label      | 文本标签（例如，用于自动标记）。                     |
| picker     | 控制对象拾取的 python 对象                           |
| transform  | 转化                                                 |
| visible    | 一个布尔值是否应该绘制 Artist                        |
| zorder     | 确定绘图顺序的数字                                   |
| rasterized | 布尔；将矢量转换为栅格图形：(用于压缩和 eps 透明度） |

每个属性都使用老式的 setter 或 getter 访问（是的，我们知道这会激怒 Pythonistas，我们计划通过属性或特性支持直接访问，但尚未完成）。例如，要将当前的 alpha 乘以一半：

```python
a = o.get_alpha()
o.set_alpha(0.5*a)
```

如果要一次设置多个属性，还可以将 set 方法与关键字参数一起使用。例如：

```python
o.set(alpha=0.5, zorder=2)
```

如果你在 python shell 上以交互方式工作，检查 Artist 属性的一种方便方法是使用 [matplotlib.artist.getp()](https://matplotlib.org/api/_as_gen/matplotlib.artist.getp.html#matplotlib.artist.getp) 函数（简单地在 pyplot 中使用 getp ()），它列出了属性及其值。从 Artist 派生的类，例如，图和矩形。以下是上面提到的图形矩形属性：

```python
In [149]: matplotlib.artist.getp(fig.patch)
    alpha = 1.0
    animated = False
    antialiased or aa = True
    axes = None
    clip_box = None
    clip_on = False
    clip_path = None
    contains = None
    edgecolor or ec = w
    facecolor or fc = 0.75
    figure = Figure(8.125x6.125)
    fill = 1
    hatch = None
    height = 1
    label =
    linewidth or lw = 1.0
    picker = None
    transform = <Affine object at 0x134cca84>
    verts = ((0, 0), (0, 1), (1, 1), (1, 0))
    visible = True
    width = 1
    window_extent = <Bbox object at 0x134acbcc>
    x = 0
    y = 0
    zorder = 1
```

所有类的文档字符串也包含 Artist 属性，因此您可以查看交互式 “帮助” 或 [artist](https://matplotlib.org/api/artist_api.html#artist-api) 以获取给定对象的属性列表。

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#对象容器)对象容器

现在我们知道如何检查和设置我们想要配置的给定对象的属性，我们需要知道如何获取该对象。 如介绍中所述，有两种对象：基元和容器。 基元通常是你想要配置的东西（[Text](https://matplotlib.org/api/text_api.html#matplotlib.text.Text) 实例的字体，[Line2D](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) 的宽度），虽然容器也有一些属性 - 例如 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) [Artist](https://matplotlib.org/api/artist_api.html#matplotlib.artist.Artist) 是一个包含许多基元的容器 你的情节，但它也有像 xscale 这样的属性来控制 x 轴是 “线性” 还是 “日志”。 在本节中，我们将回顾各种容器对象存储您想要获得的艺术家的位置。

#### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#图容器)图容器

顶级容器 Artist 是 [matplotlib.figure.Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)，它包含图中的所有内容。图的背景是一个存储在 Figure.patch 中的 [Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle)。在向图中添加子图（[add_subplot()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot)）和轴（[add_axes()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_axes)）时，这些将附加到 [Figure.axes](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.axes)。 这些也由创建它们的方法返回：

```python
In [156]: fig = plt.figure()

In [157]: ax1 = fig.add_subplot(211)

In [158]: ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

In [159]: ax1
Out[159]: <matplotlib.axes.Subplot instance at 0xd54b26c>

In [160]: print(fig.axes)
[<matplotlib.axes.Subplot instance at 0xd54b26c>, <matplotlib.axes.Axes instance at 0xd3f0b2c>]
```

因为该图保持了 “当前轴” 的概念（参见 [Figure.gca](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.gca) 和 [Figure.sca](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.sca)）以支持 pylab/pyplot 状态机，所以不应直接从轴列表中插入或删除轴，而应使用 [add_subplot()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot) 和 [add_axes()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_axes) 方法插入，以及 [delaxes()](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.delaxes) 方法删除。但是，您可以自由地遍历轴列表或索引到其中以访问要自定义的 Axes 实例。这是一个打开所有轴网格的示例：

```python
for ax in fig.axes:
    ax.grid(True)
```

该图还有自己的文本，线条，面片和图像，您可以使用它们直接添加图元。`Figure` 的默认坐标系统将以像素为单位（通常不是您想要的），但您可以通过设置要添加到图中的 `Artist` 的 transform 属性来控制它。

更有用的是 “图形坐标”，其中 (0, 0) 是图的左下角， (1, 1) 是图的右上角，您可以通过将 `Artist` 变换设置为 `fig.transFigure` 来获得：

```python
import matplotlib.lines as lines

fig = plt.figure()

l1 = lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
l2 = lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)
fig.lines.extend([l1, l2])

plt.show()
```

![艺术家对象教程示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_artists_002.png)

以下是该图所包含的 Artists 的摘要。

| 图属性  | 描述                                              |
| ------- | ------------------------------------------------- |
| axes    | Axes 实例列表（包括 Subplot）                     |
| patch   | 矩形背景                                          |
| images  | ImageImages 补丁列表 - 对原始像素显示很有用       |
| legends | 图例实例列表（与 Axes.legends 不同）              |
| lines   | 图 Line2D 实例列表（很少使用，请参阅 Axes.lines） |
| patches | 图补丁列表（很少使用，请参阅 Axes.patches）       |
| texts   | 列表图文本实例                                    |

#### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#轴容器)轴容器

[matplotlib.axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 是 matplotlib 宇宙的中心 - 它包含绝大多数在图中使用的艺术家，其中包含许多辅助方法来创建和添加这些艺术家，以及帮助方法来访问和自定义 它包含的艺术家。 与 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 一样，它包含一个 [Patch](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch) 补丁，它是一个用于笛卡尔坐标的 [Rectangle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle) 和一个用于极坐标的 [Circle](https://matplotlib.org/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle); 此补丁确定绘图区域的形状，背景和边框：

```python
ax = fig.add_subplot(111)
rect = ax.patch  # a Rectangle instance
rect.set_facecolor('green')
```

当您调用绘图方法（例如，规范 [plot()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot) 并传入数组或值列表）时，该方法将创建一个 [matplotlib.lines.Line2D()](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D)实例，使用作为关键字参数传递的所有 Line2D 属性更新该行， 将该行添加到 Axes.lines 容器中，并将其返回给您：

```python
In [213]: x, y = np.random.rand(2, 100)

In [214]: line, = ax.plot(x, y, '-', color='blue', linewidth=2)
```

plot 返回一个行列表，因为你可以传递多个 x，y 对来绘图，我们将长度为一个列表的第一个元素解压缩到行变量中。 该行已添加到 Axes.lines 列表中：

```python
In [229]: print(ax.lines)
[<matplotlib.lines.Line2D instance at 0xd378b0c>]
```

类似地，创建补丁的方法（如 [bar()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar)）会创建一个矩形列表，将补丁添加到 Axes.patches 列表中：

```python
In [233]: n, bins, rectangles = ax.hist(np.random.randn(1000), 50, facecolor='yellow')

In [234]: rectangles
Out[234]: <a list of 50 Patch objects>

In [235]: print(len(ax.patches))
```

除非您确切知道自己在做什么，否则不应将对象直接添加到 `Axes.lines` 或 `Axes.patches` 列表中，因为 Axes 在创建和添加对象时需要执行一些操作。它设置 `Artist` 的 figure 和 axes 属性，以及默认的 Axes 转换（除非设置了转换）。它还检查 Artist 中包含的数据以更新控制自动缩放的数据结构，以便可以调整视图限制以包含绘制的数据。 尽管如此，您可以自己创建对象，并使用 [add_line()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line) 和 [and add_patch()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch) 等辅助方法将它们直接添加到 Axes 中。 这是一个带注释的交互式会话，说明了正在发生的事情：

```python
In [262]: fig, ax = plt.subplots()

# create a rectangle instance
In [263]: rect = matplotlib.patches.Rectangle( (1,1), width=5, height=12)

# by default the axes instance is None
In [264]: print(rect.get_axes())
None

# and the transformation instance is set to the "identity transform"
In [265]: print(rect.get_transform())
<Affine object at 0x13695544>

# now we add the Rectangle to the Axes
In [266]: ax.add_patch(rect)

# and notice that the ax.add_patch method has set the axes
# instance
In [267]: print(rect.get_axes())
Axes(0.125,0.1;0.775x0.8)

# and the transformation has been set too
In [268]: print(rect.get_transform())
<Affine object at 0x15009ca4>

# the default axes transformation is ax.transData
In [269]: print(ax.transData)
<Affine object at 0x15009ca4>

# notice that the xlimits of the Axes have not been changed
In [270]: print(ax.get_xlim())
(0.0, 1.0)

# but the data limits have been updated to encompass the rectangle
In [271]: print(ax.dataLim.bounds)
(1.0, 1.0, 5.0, 12.0)

# we can manually invoke the auto-scaling machinery
In [272]: ax.autoscale_view()

# and now the xlim are updated to encompass the rectangle
In [273]: print(ax.get_xlim())
(1.0, 6.0)

# we have to manually force a figure draw
In [274]: ax.figure.canvas.draw()
```

有许多 `Axes` 辅助方法可用于创建原始 `Artists` 并将它们添加到各自的容器中。下表总结了一小部分样本，他们创建的 `Artist` 种类以及他们存储的位置

| 辅助方法                 | Artist（艺术家对象） | 容器                    |
| ------------------------ | -------------------- | ----------------------- |
| ax.annotate - 文字注释   | 注视                 | ax.texts                |
| ax.bar - 条形图          | Rectangle            | ax.patches              |
| ax.errorbar - 误差条形图 | Line2D and Rectangle | ax.lines and ax.patches |
| ax.fill - 共享区域       | Polygon              | ax.patches              |
| ax.hist - 直方图         | Rectangle            | ax.patches              |
| ax.imshow - 图像数据     | AxesImage            | ax.images               |
| ax.legend - 轴图例       | Legend               | ax.legends              |
| ax.plot - xy 图          | Line2D               | ax.lines                |
| ax.scatter - 散点图      | PolygonCollection    | ax.collections          |
| ax.text - 文本           | Text                 | ax.texts                |

除了所有这些 `Artists` 之外，Axes 还包含两个重要的 `Artist` 容器：[XAxis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.XAxis) 和 [YAxis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.YAxis)，用于处理刻度和标签的绘制。它们存储为实例变量 `xaxis` 和 `yaxis`。下面将详细介绍 `xaxis` 和 `yaxis` 容器，但请注意，Axes 包含许多帮助方法，这些方法将调用转发到 [Axis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Axis) 实例，因此除非您愿意，否则通常不需要直接使用它们。例如，您可以使用 Axes 辅助方法设置 XAxis ticklabels 的字体颜色：

```python
for label in ax.get_xticklabels():
    label.set_color('orange')
```

以下是 Axes 包含的 Artists 的摘要

| 轴属性      | 描述                       |
| ----------- | -------------------------- |
| artists     | Artist 实例列表            |
| patch       | 轴背景的矩形实例           |
| collections | Collection 实例列表        |
| images      | AxesImage 列表             |
| legends     | Legend 实例列表            |
| lines       | Line2D 实例列表            |
| patches     | 补丁实例列表               |
| texts       | 文本实例列表               |
| xaxis       | matplotlib.axis.XAxis 实例 |
| yaxis       | matplotlib.axis.YAxis 实例 |

#### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#轴容器)轴容器

[matplotlib.axis.Axis](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Axis) 实例处理刻度线，网格线，刻度标签和轴标签的绘制。您可以分别为 y 轴配置左和右刻度，为 x 轴分别配置上下刻度。Axis 还存储用于自动缩放，平移和缩放的数据和视图间隔，以及 [Locator](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.Locator) 和 [Formatter](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.Formatter) 实例，它们控制刻度线的放置位置以及它们如何表示为字符串。

每个 Axis 对象都包含一个 label 属性（这是 [pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) 在调用 [xlabel()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel) 和 [ylabel()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel) 时修改的内容）以及主要和次要刻度列表。刻度线是 [XTick](https://matplotlib.org/api/axis_api.html#matplotlib.axis.XTick) 和 [YTick](https://matplotlib.org/api/axis_api.html#matplotlib.axis.YTick) 实例，它们包含渲染刻度线和刻度线标签的实际线和文本基元。 因为滴答是根据需要动态创建的（例如，在平移和缩放时），您应该通过其访问器方法 [get_major_ticks()](https://matplotlib.org/api/_as_gen/matplotlib.axis.Axis.get_major_ticks.html#matplotlib.axis.Axis.get_major_ticks) 和 [get_minor_ticks()](https://matplotlib.org/api/_as_gen/matplotlib.axis.Axis.get_minor_ticks.html#matplotlib.axis.Axis.get_minor_ticks) 访问主要和次要刻度的列表。 尽管 ticks 包含所有原语并将在下面介绍，但是 Axis 实例具有访问方法，这些方法返回刻度线，刻度标签，刻度位置等：

```python
fig, ax = plt.subplots()
axis = ax.xaxis
axis.get_ticklocs()
```

![艺术家对象教程示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_artists_003.png)

```python
axis.get_ticklabels()
```

请注意，标签的间距是标签的两倍，因为默认情况下，顶部和底部有刻度线，但只有 x 轴下方的刻度标签；这可以定制：

```python
axis.get_ticklines()
```

默认情况下，你可以得到主要刻度。

```python
axis.get_ticklines()
```

但是你也可以获取次要刻度。

```python
axis.get_ticklines(minor=True)

# Here is a summary of some of the useful accessor methods of the ``Axis``
# (these have corresponding setters where useful, such as
# set_major_formatter)
#
# ======================  =========================================================
# Accessor method         Description
# ======================  =========================================================
# get_scale               The scale of the axis, e.g., 'log' or 'linear'
# get_view_interval       The interval instance of the axis view limits
# get_data_interval       The interval instance of the axis data limits
# get_gridlines           A list of grid lines for the Axis
# get_label               The axis label - a Text instance
# get_ticklabels          A list of Text instances - keyword minor=True|False
# get_ticklines           A list of Line2D instances - keyword minor=True|False
# get_ticklocs            A list of Tick locations - keyword minor=True|False
# get_major_locator       The matplotlib.ticker.Locator instance for major ticks
# get_major_formatter     The matplotlib.ticker.Formatter instance for major ticks
# get_minor_locator       The matplotlib.ticker.Locator instance for minor ticks
# get_minor_formatter     The matplotlib.ticker.Formatter instance for minor ticks
# get_major_ticks         A list of Tick instances for major ticks
# get_minor_ticks         A list of Tick instances for minor ticks
# grid                    Turn the grid on or off for the major or minor ticks
# ======================  =========================================================
#
# Here is an example, not recommended for its beauty, which customizes
# the axes and tick properties

# plt.figure creates a matplotlib.figure.Figure instance
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')


for label in ax1.xaxis.get_ticklabels():
    # label is a Text instance
    label.set_color('red')
    label.set_rotation(45)
    label.set_fontsize(16)

for line in ax1.yaxis.get_ticklines():
    # line is a Line2D instance
    line.set_color('green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)

plt.show()
```

![艺术家对象教程示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_artists_004.png)

#### [#](https://www.matplotlib.org.cn/tutorials/intermediate/artists.html#刻度容器)刻度容器

[matplotlib.axis.Tick](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick) 是我们从 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 到 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 到 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 到 [Tick](https://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick) 的下降的最终容器对象。Tick 包含刻度线和网格线实例，以及上部和下部刻度的标签实例。 其中每个都可以直接作为 Tick 的属性访问。 此外，还有一些布尔变量可确定 x 轴上的上标签和刻度是否打开，y 轴的右标签和刻度是否打开。

| 刻度属性  | 描述                                |
| --------- | ----------------------------------- |
| tick1line | Line2D 实例                         |
| tick2line | Line2D 实例                         |
| gridline  | Line2D 实例                         |
| label1    | Text 实例                           |
| label2    | Text 实例                           |
| gridOn    | boolean，决定是否绘制网格线         |
| tick1On   | boolean 决定是否绘制第一个刻度线    |
| tick2On   | boolean 决定是否绘制第二个刻度线    |
| label1On  | boolean，决定是否绘制第一个刻度标签 |
| label2On  | boolean，决定是否绘制第二个刻度标签 |

下面是一个示例，它设置右侧刻度的格式化程序，带有美元符号，颜色为 y 轴右侧的绿色。

```python
import matplotlib.ticker as ticker

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))

formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)

for tick in ax.yaxis.get_major_ticks():
    tick.label1On = False
    tick.label2On = True
    tick.label2.set_color('green')

plt.show()
```

![艺术家对象教程示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_artists_005.png)

## 图例指南

在 Matplotlib 中灵活地生成图例。

此图例指南是 [legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend) 中提供的文档的扩展 - 请确保您在继续本指南之前熟悉该文档的内容。

本指南使用了一些常用术语，为清楚起见，这些术语在此处记录：

+  图例入口：图例由一个或多个图例条目组成。 条目由一个密钥和一个标签组成。
+  图例键：每个图例标签左侧的彩色 / 图案标记。
+  图例标签：描述密钥表示的句柄的文本。
+  图例处理：原始对象，用于在图例中生成适当的条目。

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#控制图例条目)控制图例条目

调用不带参数的 [legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend) 会自动获取图例句柄及其关联的标签。此功能相当于：

```python
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
```

[get_legend_handles_labels()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html#matplotlib.axes.Axes.get_legend_handles_labels) 函数返回 Axes 上存在的 handles/artists 列表，可用于生成结果图例的条目 - 值得注意的是，并非所有艺术家都可以添加到图例中，此时必须创建 "proxy"（有关更多详细信息，请参阅 [创建专门用于添加到图例的艺术家（也称为代理艺术家）](https://matplotlib.org/tutorials/intermediate/legend_guide.html#proxy-legend-handles)）。

要完全控制添加到图例的内容，通常将相应的句柄直接传递给 [legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend)：

```python
line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend(handles=[line_up, line_down])
```

在某些情况下，无法设置句柄的标签，因此可以将标签列表传递给 [legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend)：

```python
line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend([line_up, line_down], ['Line Up', 'Line Down'])
```

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#创建专门用于添加到图例的artists（也叫-Proxy-artists）)创建专门用于添加到图例的 artists（也叫 Proxy artists）

并非所有句柄都可以自动转换为图例条目，因此通常需要创建一个可以的艺术家对象。图或轴上不必存在图例句柄以便使用。

假设我们想要创建一个图例，其中包含一些由红色表示的数据条目：

```python
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

red_patch = mpatches.Patch(color='red', label='The red data')
plt.legend(handles=[red_patch])

plt.show()
```

![图例指南示例](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_001.png)

有许多支持的图例句柄，而不是创建一个颜色的补丁我们可以创建一个带标记的行：

```python
import matplotlib.lines as mlines

blue_line = mlines.Line2D([], [], color='blue', marker='*',
                          markersize=15, label='Blue stars')
plt.legend(handles=[blue_line])

plt.show()
```

![图例指南示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_002.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#图例位置)图例位置

可以通过关键字参数 loc 指定图例的位置。有关更多详细信息，请参见 [legend()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend) 上的文档。

`bbox_to_anchor` 关键字为手动图例放置提供了很大程度的控制。 例如，如果您希望轴图例位于图的右上角而不是轴的角，只需指定角的位置以及该位置的坐标系：

```python
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)
```

自定义图例展示的更多示例：

```python
plt.subplot(211)
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")

# Place a legend above this subplot, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(223)
plt.plot([1, 2, 3], label="test1")
plt.plot([3, 2, 1], label="test2")
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.show()
```

![图例指南示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_003.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#同一轴上的多个图例)同一轴上的多个图例

有时，在多个图例中拆分图例条目更为明确。虽然这样做的本能方法可能是多次调用 legend () 函数，但您会发现 Axes 上只存在一个图例。 这样做是为了可以反复调用 legend () 来将图例更新为 Axes 上的最新句柄，因此为了保留旧的图例实例，我们必须手动将它们添加到 Axes：

```python
line1, = plt.plot([1, 2, 3], label="Line 1", linestyle='--')
line2, = plt.plot([3, 2, 1], label="Line 2", linewidth=4)

# Create a legend for the first line.
first_legend = plt.legend(handles=[line1], loc='upper right')

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# Create another legend for the second line.
plt.legend(handles=[line2], loc='lower right')

plt.show()
```

![图例指南示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_004.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#图例处理程序)图例处理程序

为了创建图例条目，句柄作为适当的 HandlerBase 子类的参数给出。处理程序子类的选择由以下规则确定：

1. 使用 handler_map 关键字中的值更新 get_legend_handler_map ()。
2. 检查句柄是否在新创建的 handler_map 中。
3. 检查句柄的类型是否在新创建的 handler_map 中。
4. 检查句柄的 mro 中的任何类型是否在新创建的 handler_map 中。

为了完整起见，此逻辑主要在 get_legend_handler () 中实现。

所有这些灵活性意味着我们拥有必要的钩子来为我们自己的图例键实现自定义处理程序。

使用自定义处理程序的最简单示例是实例化一个现有的 HandlerBase 子类。为简单起见，让我们选择接受 numpoints 参数的 matplotlib.legend_handler.HandlerLine2D（为方便起见，注意 numpoints 是 legend () 函数的关键字）。然后，我们可以将实例的映射作为关键字传递给 Handler。

```python
from matplotlib.legend_handler import HandlerLine2D

line1, = plt.plot([3, 2, 1], marker='o', label='Line 1')
line2, = plt.plot([1, 2, 3], marker='o', label='Line 2')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
```

![图例指南示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_005.png)

如您所见，“Line 1” 现在有 4 个标记点，其中 “Line 2” 有 2 个（默认值）。 尝试上面的代码，只将 map 的键从 line1 更改为 type（line1）。注意现在两个 Line2D 实例如何获得 4 个标记。

除了处理复杂绘图类型（如误差条形图，词干图和直方图）的处理程序外，默认的 handler_map 还有一个特殊的元组处理程序（HandlerTuple），它只是为给定元组中的每个项目绘制彼此重叠的句柄。以下示例演示了将两个图例键组合在一起：

```python
from numpy.random import randn

z = randn(10)

red_dot, = plt.plot(z, "ro", markersize=15)
# Put a white cross over some of the data.
white_cross, = plt.plot(z[:5], "w+", markeredgewidth=3, markersize=15)

plt.legend([red_dot, (red_dot, white_cross)], ["Attr A", "Attr A+B"])
```

![图例指南示例6](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_006.png)

HandlerTuple 类还可用于将多个图例键分配给同一条目：

```python
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple

p1, = plt.plot([1, 2.5, 3], 'r-d')
p2, = plt.plot([3, 2, 1], 'k-o')

l = plt.legend([(p1, p2)], ['Two keys'], numpoints=1,
               handler_map={tuple: HandlerTuple(ndivide=None)})
```

![图例指南示例7](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_007.png)

#### [#](https://www.matplotlib.org.cn/tutorials/intermediate/legend_guide.html#实现自定义图例处理程序)实现自定义图例处理程序

可以实现自定义处理程序将任何句柄转换为图例键（句柄不一定需要是 matplotlib 艺术家对象）。处理程序必须实现 “legend_artist” 方法，该方法返回单个艺术家以供图例使用。 有关 “legend_artist” 的签名详细信息记录在 legend_artist () 中。

```python
import matplotlib.patches as mpatches


class AnyObject(object):
    pass


class AnyObjectHandler(object):
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle([x0, y0], width, height, facecolor='red',
                                   edgecolor='black', hatch='xx', lw=3,
                                   transform=handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch


plt.legend([AnyObject()], ['My first handler'],
           handler_map={AnyObject: AnyObjectHandler()})
```

![图例指南示例8](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_008.png)

或者，如果我们想要全局接受 AnyObject 实例而不需要一直手动设置 handler_map 关键字，我们可以使用以下命令注册新的处理程序：

```python
from matplotlib.legend import Legend
Legend.update_default_handler_map({AnyObject: AnyObjectHandler()})
```

虽然这里的功能很明确，但请记住，已经实现了许多处理程序，并且现有类可能已经很容易实现您想要实现的功能。例如，要生成椭圆图例键，而不是矩形图例：

```python
from matplotlib.legend_handler import HandlerPatch


class HandlerEllipse(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse(xy=center, width=width + xdescent,
                             height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]


c = mpatches.Circle((0.5, 0.5), 0.25, facecolor="green",
                    edgecolor="red", linewidth=3)
plt.gca().add_patch(c)

plt.legend([c], ["An ellipse, not a rectangle"],
           handler_map={mpatches.Circle: HandlerEllipse()})
```

![图例指南示例9](pictures/Matplotlib 中文手册.assets/sphx_glr_legend_guide_009.png)

## 使用循环器设置样式

演示自定义属性循环设置，以控制多线图的颜色和其他样式属性。

**注意：** 可以在[此处](http://matplotlib.org/cycler/)找到有关 cycler API 的更完整文档。

此示例演示了两种不同的 API：

1. 设置指定属性循环的默认 rc 参数。 这会影响所有后续轴（但不会影响已创建的轴）。
2. 设置一对轴的属性循环。

```python
from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt
```

首先，我们将生成一些样本数据，在本例中为四条偏移正弦曲线。

```python
x = np.linspace(0, 2 * np.pi, 50)
offsets = np.linspace(0, 2 * np.pi, 4, endpoint=False)
yy = np.transpose([np.sin(x + phi) for phi in offsets])
```

现在你已经成型了

```python
print(yy.shape)
```

输出：

```python
(50, 4)
```

所以 yy [:, i] 会给你第 i 个偏移正弦曲线。让我们使用 [matplotlib.pyplot.rc()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc) 设置默认的 prop_cycle。我们将通过添加 (+) 两个循环仪来组合颜色循环仪和线型循环仪。有关组合不同循环仪的更多信息，请参阅本教程的底部。

```python
default_cycler = (cycler(color=['r', 'g', 'b', 'y']) +
                  cycler(linestyle=['-', '--', ':', '-.']))

plt.rc('lines', linewidth=4)
plt.rc('axes', prop_cycle=default_cycler)
```

现在我们将生成一个有两个轴的图形，一个在另一个上面。在第一个轴上，我们将使用默认的循环器进行绘图。在第二个轴上，我们将使用 [matplotlib.axes.Axes.set_prop_cycle()](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle) 设置 prop_cycler，它只会为此 [matplotlib.axes.Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 实例设置 prop_cycle。我们将使用第二台循环仪，它结合了色循环仪和线宽循环仪。

```python
custom_cycler = (cycler(color=['c', 'm', 'y', 'k']) +
                 cycler(lw=[1, 2, 3, 4]))

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.plot(yy)
ax0.set_title('Set default color cycle to rgby')
ax1.set_prop_cycle(custom_cycler)
ax1.plot(yy)
ax1.set_title('Set axes color cycle to cmyk')

# Add a bit more space between the two plots.
fig.subplots_adjust(hspace=0.3)
plt.show()
```

![用cycler定型示例](pictures/Matplotlib 中文手册.assets/sphx_glr_color_cycle_001.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/color_cycle.html#在matplotlibrc文件或样式文件中设置prop_cycler)在 matplotlibrc 文件或样式文件中设置 prop_cycler

请记住，如果要在.matplotlibrc 文件或样式文件（style.mplstyle）中设置自定义 prop_cycler，可以设置 axes.prop_cycle 属性：

```python
axes.prop_cycle    : cycler(color='bgrcmyk')
```

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/color_cycle.html#循环访问多个属性)循环访问多个属性

您可以添加以下循环器：

```python
from cycler import cycler
cc = (cycler(color=list('rgb')) +
      cycler(linestyle=['-', '--', '-.']))
for d in cc:
    print(d)
```

结果：

```python
{'color': 'r', 'linestyle': '-'}
{'color': 'g', 'linestyle': '--'}
{'color': 'b', 'linestyle': '-.'}
```

你可以使用多个循环器：

```python
from cycler import cycler
cc = (cycler(color=list('rgb')) *
      cycler(linestyle=['-', '--', '-.']))
for d in cc:
    print(d)
```

结果：

```python
{'color': 'r', 'linestyle': '-'}
{'color': 'r', 'linestyle': '--'}
{'color': 'r', 'linestyle': '-.'}
{'color': 'g', 'linestyle': '-'}
{'color': 'g', 'linestyle': '--'}
{'color': 'g', 'linestyle': '-.'}
{'color': 'b', 'linestyle': '-'}
{'color': 'b', 'linestyle': '--'}
{'color': 'b', 'linestyle': '-.'}
```



## 使用 GridSpec 和其他功能自定义图布局

如何创建网格的轴组合。

+  [subplots()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots): 可能是用来创建图形和轴的主要函数。它也类似于 matplotlib.pyplot.subplot ()，但同时创建并放置地物上的所有轴。另请参见 matplotlib.Figure.subplots。
+  [GridSpec()](https://matplotlib.org/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec): 指定将放置子图的网格的几何。需要设置网格的行数和列数。可选地，可以调整子图布局参数（例如，左，右等）。
+  [SubplotSpec()](https://matplotlib.org/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec): 指定给定 GridSpec 中子图的位置。
+  [subplot2grid()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid): 一个辅助函数，类似于 subplot ()，但使用基于 0 的索引并让子图占据多个单元格。本教程不涉及此功能。

```python
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
```

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/gridspec.html#基本快速入门指南)基本快速入门指南

前两个示例显示了如何使用 [subplots()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots) 和 [gridspec](https://matplotlib.org/api/gridspec_api.html#module-matplotlib.gridspec) 创建基本的 2×2 网格。

使用 [subplots()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots) 非常简单。它返回一个 [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) 实例和一个 [Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) 对象数组。

```python
fig1, f1_axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
```

![用cycler定型示例](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_001.png)

对于像这样的简单用例，gridspec 可能过于冗长。您必须单独创建图形和 GridSpec 实例，然后将 gridspec 实例的元素传递给 add_subplot () 方法以创建轴对象。gridspec 的元素通常以与 numpy 数组相同的方式访问。

```python
fig2 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig2)
f2_ax1 = fig2.add_subplot(spec2[0, 0])
f2_ax2 = fig2.add_subplot(spec2[0, 1])
f2_ax3 = fig2.add_subplot(spec2[1, 0])
f2_ax4 = fig2.add_subplot(spec2[1, 1])
```

![用cycler定型示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_002.png)

gridspec 的强大之处在于能够创建跨越行和列的子图。 注意 Numpy 切片语法用于选择每个子图将占用的 gridspec 部分。

请注意，我们还使用了方便方法 Figure.add_gridspec 而不是 gridspec.GridSpec，可能会为用户保存导入，并保持名称空间更清晰。

```python
fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)
f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax1.set_title('gs[0, :]')
f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('gs[-1, 0]')
f3_ax5 = fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')
```

![用cycler定型示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_003.png)

gridspec 对于通过几种方法创建不同宽度的子图也是必不可少的。

此处显示的方法类似于上面的方法并初始化统一的网格规范，然后使用 numpy 索引和切片为给定的子图分配多个 “单元”。

```python
fig4 = plt.figure(constrained_layout=True)
spec4 = fig4.add_gridspec(ncols=2, nrows=2)
anno_opts = dict(xy=(0.5, 0.5), xycoords='axes fraction',
                 va='center', ha='center')

f4_ax1 = fig4.add_subplot(spec4[0, 0])
f4_ax1.annotate('GridSpec[0, 0]', **anno_opts)
fig4.add_subplot(spec4[0, 1]).annotate('GridSpec[0, 1:]', **anno_opts)
fig4.add_subplot(spec4[1, 0]).annotate('GridSpec[1:, 0]', **anno_opts)
fig4.add_subplot(spec4[1, 1]).annotate('GridSpec[1:, 1:]', **anno_opts)
```

![用cycler定型示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_004.png)

另一种选择是使用 `width_ratios` 和 `height_ratios` 参数。这些关键字参数是数字列表。请注意，绝对值是没有意义的，只有它们的相对比率很重要。 这意味着 `width_ratios = [2,4,8]` 相当于 `width_ratios = [1,2,4]` 在同样宽的数字内。为了演示，我们将在 for 循环中盲目地创建轴，因为我们以后不再需要它们。

```python
fig5 = plt.figure(constrained_layout=True)
widths = [2, 3, 1.5]
heights = [1, 3, 2]
spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios=widths,
                          height_ratios=heights)
for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(spec5[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
```

![用cycler定型示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_005.png)

学习使用 width_ratios 和 height_ratios 特别有用，因为顶级函数 subplots () 在 gridspec_kw 参数中接受它们。就此而言，GridSpec 接受的任何参数都可以通过 gridspec_kw 参数传递给 subplots ()。此示例在不直接使用 gridspec 实例的情况下重新创建上一个图。

```python
gs_kw = dict(width_ratios=widths, height_ratios=heights)
fig6, f6_axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
        gridspec_kw=gs_kw)
for r, row in enumerate(f6_axes):
    for c, ax in enumerate(row):
        label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
```

![用cycler定型示例6](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_006.png)

可以组合子图和 gridspec 方法，因为有时使用子图制作大多数子图更方便，然后删除一些子图并将它们组合起来。在这里，我们创建一个布局，其中最后一列中的底部两个轴组合在一起。

```python
fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
gs = f7_axs[1, 2].get_gridspec()
# remove the underlying axes
for ax in f7_axs[1:, -1]:
    ax.remove()
axbig = fig7.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
               xycoords='axes fraction', va='center')

fig7.tight_layout()
```

![用cycler定型示例7](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_007.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/gridspec.html#对Gridspec布局的精细调整)对 Gridspec 布局的精细调整

显式使用 GridSpec 时，可以调整从 GridSpec 创建的子图的布局参数。请注意，此选项与 constrained_layout 或 [Figure.tight_layout](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.tight_layout) 不兼容，后者均调整子图大小以填充图形。

```python
fig8 = plt.figure(constrained_layout=False)
gs1 = fig8.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48, wspace=0.05)
f8_ax1 = fig8.add_subplot(gs1[:-1, :])
f8_ax2 = fig8.add_subplot(gs1[-1, :-1])
f8_ax3 = fig8.add_subplot(gs1[-1, -1])
```

![用cycler定型示例8](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_008.png)

这类似于 [subplots_adjust()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust)，但它只影响从给定 GridSpec 创建的子图。

这类似于 [subplots_adjust()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust)，但它只影响从给定的 GridSpec 创建的子图。

例如，比较这个图像的左边和右侧：

```python
fig9 = plt.figure(constrained_layout=False)
gs1 = fig9.add_gridspec(nrows=3, ncols=3, left=0.05, right=0.48,
                        wspace=0.05)
f9_ax1 = fig9.add_subplot(gs1[:-1, :])
f9_ax2 = fig9.add_subplot(gs1[-1, :-1])
f9_ax3 = fig9.add_subplot(gs1[-1, -1])

gs2 = fig9.add_gridspec(nrows=3, ncols=3, left=0.55, right=0.98,
                        hspace=0.05)
f9_ax4 = fig9.add_subplot(gs2[:, :-1])
f9_ax5 = fig9.add_subplot(gs2[:-1, -1])
f9_ax6 = fig9.add_subplot(gs2[-1, -1])
```

![用cycler定型示例9](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_009.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/gridspec.html#使用SubplotSpec的GridSpec)使用 SubplotSpec 的 GridSpec

您可以从 SubplotSpec 创建 GridSpec，在这种情况下，它的布局参数设置为给定 SubplotSpec 的位置。

注意，这也可以从更详细的 gridspec.GridspecFromSubplotSpec 获得。

```python
fig10 = plt.figure(constrained_layout=True)
gs0 = fig10.add_gridspec(1, 2)

gs00 = gs0[0].subgridspec(2, 3)
gs01 = gs0[1].subgridspec(3, 2)

for a in range(2):
    for b in range(3):
        fig10.add_subplot(gs00[a, b])
        fig10.add_subplot(gs01[b, a])
```

![用cycler定型示例10](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_010.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/gridspec.html#基于SubplotSpec的复杂嵌套GridSpec)基于 SubplotSpec 的复杂嵌套 GridSpec

这是一个更复杂的嵌套 GridSpec 示例，我们在外部 4x4 网格的每个单元格周围放置一个框，方法是在每个内部 3x3 网格中隐藏适当的数据区域边界。

```python
import numpy as np
from itertools import product


def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)


fig11 = plt.figure(figsize=(8, 8), constrained_layout=False)

# gridspec inside gridspec
outer_grid = fig11.add_gridspec(4, 4, wspace=0.0, hspace=0.0)

for i in range(16):
    inner_grid = outer_grid[i].subgridspec(3, 3, wspace=0.0, hspace=0.0)
    a, b = int(i/4)+1, i % 4+1
    for j, (c, d) in enumerate(product(range(1, 4), repeat=2)):
        ax = plt.Subplot(fig11, inner_grid[j])
        ax.plot(*squiggle_xy(a, b, c, d))
        ax.set_xticks([])
        ax.set_yticks([])
        fig11.add_subplot(ax)

all_axes = fig11.get_axes()

# show only the outside spines
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
    if ax.is_first_row():
        ax.spines['top'].set_visible(True)
    if ax.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ax.is_first_col():
        ax.spines['left'].set_visible(True)
    if ax.is_last_col():
        ax.spines['right'].set_visible(True)

plt.show()
```

![用cycler定型示例11](pictures/Matplotlib 中文手册.assets/sphx_glr_gridspec_011.png)

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/gridspec.html#References)References

此示例中显示了以下函数和方法的用法：

```python
matplotlib.pyplot.subplots
matplotlib.figure.Figure.add_gridspec
matplotlib.figure.Figure.add_subplot
matplotlib.gridspec.GridSpec
matplotlib.gridspec.SubplotSpec.subgridspec
matplotlib.gridspec.GridSpecFromSubplotSpec
Total running time of the script: ( 0 minutes 2.021 seconds)
```



## 约束布局指南

如何使用约束布局干净地拟合图中的图形。

`constrained_layout` 自动调整子图和装饰，如图例和颜色条，以便它们适合图形窗口，同时仍尽可能保留用户请求的逻辑布局。

`constrained_layout` 类似于 tight_layout，但使用约束求解器来确定允许它们拟合的轴的大小。

在将任何轴添加到图形之前，需要激活 `constrained_layout`。 这样做有两种方法：

使用 subplots () 或 figure () 的相应参数，例如：

```python
plt.subplots(constrained_layout=True)
```

通过 rcParams 激活它，如：

```python
plt.rcParams['figure.constrained_layout.use'] = True
```

以下各节将详细介绍这些内容。

**警告**： 目前，约束布局是实验性的。 行为和 API 可能会发生变化，或者可以在没有弃用期的情况下删除整个功能。 如果您需要绘图绝对可重复，请在运行 Constrained Layout 后获取 Axes 位置，并在您的代码中使用 axined_layout = False 的 ax.set_position ()。

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#简单的例子)简单的例子

在 Matplotlib 中，轴（包括子图）的位置在标准化的图形坐标中指定。您的轴标签或标题（有时甚至是标签标签）可能会超出图形区域，因此会被裁剪。

```python
# sphinx_gallery_thumbnail_number = 18

#import matplotlib
#matplotlib.use('Qt5Agg')

import warnings

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec

import matplotlib._layoutbox as layoutbox

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 4.5, 4.


def example_plot(ax, fontsize=12, nodec=False):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    if not nodec:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)
    else:
        ax.set_xticklabels('')
        ax.set_yticklabels('')


fig, ax = plt.subplots(constrained_layout=False)
example_plot(ax, fontsize=24)
```

![约束布局指南示例](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_001-1565508652698.png)

为防止这种情况，需要调整轴的位置。对于子图，可以通过调整子图参数（[移动轴的边缘以为刻度标签腾出空间](https://matplotlib.org/faq/howto_faq.html#howto-subplots-adjust)）来完成。 但是，使用 constrained_layout = True kwarg 指定您的图形将自动进行调整。

```python
fig, ax = plt.subplots(constrained_layout=True)
example_plot(ax, fontsize=24)
```

![约束布局指南示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_002-1565508652720.png)

当您有多个子图时，通常会看到不同轴的标签彼此重叠。

```python
fig, axs = plt.subplots(2, 2, constrained_layout=False)
for ax in axs.flatten():
    example_plot(ax)
```

![约束布局指南示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_003-1565508652713.png)

`constrained_layout=True`在调用中指定`plt.subplots`会导致布局被正确约束。

```python
fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    example_plot(ax)
```

![约束布局指南示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_004-1565508652709.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Colorbars)Colorbars

如果使用 colorbar（）命令创建颜色条，则需要为其腾出空间。constrained_layout 自动执行此操作。请注意，如果指定 use_gridspec = True，则会忽略该选项，因为此选项用于通过 tight_layout 改进布局。

**注意：**对于 pcolormesh kwargs（pc_kwargs），我们使用字典。下面我们将一个颜色条分配给多个轴，每个轴包含一个 ScalarMappable; 指定 norm 和 colormap 可确保所有轴的颜色条都准确。

```python
arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)
# see note above: this makes all pcolormesh calls consistent:
pc_kwargs = {'rasterized': True, 'cmap': 'viridis', 'norm': norm}
fig, ax = plt.subplots(figsize=(4, 4), constrained_layout=True)
im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=ax, shrink=0.6)
```

![约束布局指南示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_005-1565508653365.png)

如果为 colorbar 的 ax 参数指定轴列表（或其他可迭代容器），则 constrained_layout 将从指定的轴中获取空间。

```python
fig, axs = plt.subplots(2, 2, figsize=(4, 4), constrained_layout=True)
for ax in axs.flatten():
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs, shrink=0.6)
```

![约束布局指南示例6](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_006-1565508653375.png)

如果从轴网格内部指定轴列表，则颜色条将适当地窃取空间，并留下间隙，但所有子图仍将具有相同的大小。

```python
fig, axs = plt.subplots(3, 3, figsize=(4, 4), constrained_layout=True)
for ax in axs.flatten():
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs[1:, ][:, 1], shrink=0.8)
fig.colorbar(im, ax=axs[:, -1], shrink=0.6)
```

![约束布局指南示例7](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_007-1565508653379.png)

请注意，将单个轴指定为父轴时会有一些细微之处。在下文中，颜色条排列可能是理想的和预期的，但它们不是因为与底部轴配对的颜色条与轴的子图谱规格相关联，因此当添加了 gridspec 级颜色条时收缩。

```python
fig, axs = plt.subplots(3, 1, figsize=(4, 4), constrained_layout=True)
for ax in axs[:2]:
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs[:2], shrink=0.6)
im = axs[2].pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs[2], shrink=0.6)
```

![约束布局指南示例8](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_008-1565508653360.png)

使单轴行为像轴列表的 API 是将其指定为列表（或其他可迭代容器），如下所示：

```python
fig, axs = plt.subplots(3, 1, figsize=(4, 4), constrained_layout=True)
for ax in axs[:2]:
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs[:2], shrink=0.6)
im = axs[2].pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=[axs[2]], shrink=0.6)
```

![约束布局指南示例9](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_009-1565508653359.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Suptitle)Suptitle

`constrained_layout` 也可以为 suptitle 腾出空间。

```python
fig, axs = plt.subplots(2, 2, figsize=(4, 4), constrained_layout=True)
for ax in axs.flatten():
    im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=axs, shrink=0.6)
fig.suptitle('Big Suptitle')
```

![约束布局指南示例10](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_010-1565508653455.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Legends)传奇

图例可以放在父轴之外。Constrained-layout 旨在为 Axes.legend（）处理此问题。但是，约束布局不会处理通过 Figure.legend（）（还）创建的图例。

```python
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(np.arange(10), label='This is a plot')
ax.legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
```

![约束布局指南示例11](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_011-1565508653466.png)

但是，这将从子图布局中窃取空间：

```python
fig, axs = plt.subplots(1, 2, figsize=(4, 2), constrained_layout=True)
axs[0].plot(np.arange(10))
axs[1].plot(np.arange(10), label='This is a plot')
axs[1].legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
```

![约束布局指南示例12](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_012-1565508653484.png)

为了使图例或其他艺术家不从子图布局中窃取空间，我们可以 leg.set_in_layout（False）。当然，这可能意味着图例最终被裁剪，但如果随后使用 fig.savefig（'outname.png'，bbox_inches ='tight'）调用该图可能很有用。但请注意，必须再次切换图例的 get_in_layout 状态才能使保存的文件正常工作，如果我们希望 constrained_layout 在打印前调整轴的大小，则必须手动触发绘图。

```python
fig, axs = plt.subplots(1, 2, figsize=(4, 2), constrained_layout=True)

axs[0].plot(np.arange(10))
axs[1].plot(np.arange(10), label='This is a plot')
leg = axs[1].legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
leg.set_in_layout(False)
# trigger a draw so that constrained_layout is executed once
# before we turn it off when printing....
fig.canvas.draw()
# we want the legend included in the bbox_inches='tight' calcs.
leg.set_in_layout(True)
# we don't want the layout to change at this point.
fig.set_constrained_layout(False)
fig.savefig('CL01.png', bbox_inches='tight', dpi=100)
```

![约束布局指南示例13](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_013-1565508653495.png)

保存的文件如下所示：

![约束布局指南示例cl01](pictures/Matplotlib 中文手册.assets/CL01-1565508653530.png)

解决这种尴尬的更好方法是简单地使用 Figure.legend 提供的图例方法：

```python
fig, axs = plt.subplots(1, 2, figsize=(4, 2), constrained_layout=True)
axs[0].plot(np.arange(10))
lines = axs[1].plot(np.arange(10), label='This is a plot')
labels = [l.get_label() for l in lines]
leg = fig.legend(lines, labels, loc='center left',
                 bbox_to_anchor=(0.8, 0.5), bbox_transform=axs[1].transAxes)
fig.savefig('CL02.png', bbox_inches='tight', dpi=100)
```

![约束布局指南示例14](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_014-1565508653524.png)

保存的文件如下所示：

![约束布局指南示例cl02](pictures/Matplotlib 中文手册.assets/CL02-1565508653590.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Padding-and-Spacing)填充和间距

对于 constrained_layout，我们在每个轴的边缘周围实现了填充。此填充设置距图的边缘的距离，以及相邻图之间的最小距离。它由关键字参数 w_pad 和 h_pad 以英寸为单位指定为函数 set_constrained_layout_pads：

```python
fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    example_plot(ax, nodec=True)
    ax.set_xticklabels('')
    ax.set_yticklabels('')
fig.set_constrained_layout_pads(w_pad=4./72., h_pad=4./72.,
        hspace=0., wspace=0.)

fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    example_plot(ax, nodec=True)
    ax.set_xticklabels('')
    ax.set_yticklabels('')
fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72.,
        hspace=0., wspace=0.)
```

![约束布局指南示例15](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_015-1565508653595.png)

![约束布局指南示例16](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_016-1565508653600.png)

子图之间的间距由 wspace 和 hspace 设置。作为整体，指定为子图组大小的一部分。如果图形的大小发生变化，则这些空间会按比例变化。请注意，边缘处的空间如何不会从上面改变，但是子图之间的空间确实如此。

```python
fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    example_plot(ax, nodec=True)
    ax.set_xticklabels('')
    ax.set_yticklabels('')
fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72.,
        hspace=0.2, wspace=0.2)
```

![约束布局指南示例17](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_017-1565508653611.png)

#### [＃使用色条](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Spacing-with-colorbars)间距

色块将放置在 wspace 和 hsapce 之外，与其他子图分开。颜色条与其连接的轴之间的填充将永远不会小于 w_pad（对于垂直颜色条）或 h_pad（对于水平颜色条）。注意在 colorbar 调用中使用 pad kwarg。它默认为附加轴的大小的 0.02。

```python
fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    pc = ax.pcolormesh(arr, **pc_kwargs)
    fig.colorbar(pc, ax=ax, shrink=0.6, pad=0)
    ax.set_xticklabels('')
    ax.set_yticklabels('')
fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72.,
        hspace=0.2, wspace=0.2)
```

![约束布局指南示例18](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_018-1565508653627.png)

在上面的例子中，颜色条与图的距离不会超过 2 点，但如果我们想要它更远一点，我们可以指定它的值为非零值。

```python
fig, axs = plt.subplots(2, 2, constrained_layout=True)
for ax in axs.flatten():
    pc = ax.pcolormesh(arr, **pc_kwargs)
    fig.colorbar(im, ax=ax, shrink=0.6, pad=0.05)
    ax.set_xticklabels('')
    ax.set_yticklabels('')
fig.set_constrained_layout_pads(w_pad=2./72., h_pad=2./72.,
        hspace=0.2, wspace=0.2)
```

![约束布局指南示例19](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_019-1565508653683.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#rcParams)rcParams

可以在脚本或 matplotlibrc 文件中设置五个 rcParams。它们都有前缀 figure.constrained_layout：

+  use：是否使用 constrained_layout。默认值为 False
+  w_pad，h_pad：围绕轴对象填充。
   浮动代表英寸。默认值为 3./72。英寸（3 分）
+  wspace，hspace：子图组之间的空格。
   浮点表示被分离的子图宽度的一小部分。默认值为 0.02。

```python
plt.rcParams['figure.constrained_layout.use'] = True
fig, axs = plt.subplots(2, 2, figsize=(3, 3))
for ax in axs.flatten():
    example_plot(ax)
```

![约束布局指南示例20](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_020-1565508653690.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Use-with-GridSpec)与 GridSpec 一起使用

constrained_layout 用于 subplots（）或 GridSpec（）和 add_subplot（）。

请注意，以下内容为 constrained_layout = True

```python
fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1, figure=fig)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)
```

![约束布局指南示例21](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_021-1565508653693.png)

更复杂的 gridspec 布局是可能的。请注意，我们使用了传递函数 add_gridspec 和 subgridspec

```python
fig = plt.figure()

gs0 = fig.add_gridspec(1, 2)

gs1 = gs0[0].subgridspec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs2 = gs0[1].subgridspec(3, 1)

for ss in gs2:
    ax = fig.add_subplot(ss)
    example_plot(ax)
    ax.set_title("")
    ax.set_xlabel("")

ax.set_xlabel("x-label", fontsize=12)
```

![约束布局指南示例22](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_022-1565508653722.png)

请注意，在上面左侧和列中没有相同的垂直范围。如果我们希望两个网格的顶部和底部对齐，那么它们需要在相同的 gridspec 中：

```python
fig = plt.figure()

gs0 = fig.add_gridspec(6, 2)

ax1 = fig.add_subplot(gs0[:3, 0])
ax2 = fig.add_subplot(gs0[3:, 0])

example_plot(ax1)
example_plot(ax2)

ax = fig.add_subplot(gs0[0:2, 1])
example_plot(ax)
ax = fig.add_subplot(gs0[2:4, 1])
example_plot(ax)
ax = fig.add_subplot(gs0[4:, 1])
example_plot(ax)
```

![约束布局指南示例23](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_023-1565508653730.png)

此示例使用两个 gridspecs 使颜色条仅适用于一组 pcolors。请注意左列是如何比这两个右列宽。当然，如果您希望子图的大小相同，则只需要一个 gridspec。

```python
def docomplicated(suptitle=None):
    fig = plt.figure()
    gs0 = fig.add_gridspec(1, 2, figure=fig, width_ratios=[1., 2.])
    gsl = gs0[0].subgridspec(2, 1)
    gsr = gs0[1].subgridspec(2, 2)

    for gs in gsl:
        ax = fig.add_subplot(gs)
        example_plot(ax)
    axs = []
    for gs in gsr:
        ax = fig.add_subplot(gs)
        pcm = ax.pcolormesh(arr, **pc_kwargs)
        ax.set_xlabel('x-label')
        ax.set_ylabel('y-label')
        ax.set_title('title')

        axs += [ax]
    fig.colorbar(pcm, ax=axs)
    if suptitle is not None:
        fig.suptitle(suptitle)

docomplicated()
```

![约束布局指南示例24](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_024-1565508653766.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Manually-setting-axes-positions)手动设置轴位置

可以有充分的理由手动设置轴位置。手动调用 set_position 将设置轴，因此 constrained_layout 不再对其产生影响。（请注意，constrained_layout 仍然为移动的轴留下空间）。

```python
fig, axs = plt.subplots(1, 2)
example_plot(axs[0], fontsize=12)
axs[1].set_position([0.2, 0.2, 0.4, 0.4])
```

![约束布局指南示例25](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_025-1565508653781.png)

如果要在数据空间中使用插入轴，则需要使用 fig.execute_constrained_layout（）调用手动执行布局。然后将插图正确定位。但是，如果随后更改了图形的大小，则无法正确定位。同样，如果将图形打印到另一个后端，由于后端渲染字体的方式差异很小，位置可能会略有变化。

```python
from matplotlib.transforms import Bbox

fig, axs = plt.subplots(1, 2)
example_plot(axs[0], fontsize=12)
fig.execute_constrained_layout()
# put into data-space:
bb_data_ax2 = Bbox.from_bounds(0.5, 1., 0.2, 0.4)
disp_coords = axs[0].transData.transform(bb_data_ax2)
fig_coords_ax2 = fig.transFigure.inverted().transform(disp_coords)
bb_ax2 = Bbox(fig_coords_ax2)
ax2 = fig.add_axes(bb_ax2)
```

![约束布局指南示例26](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_026-1565508653794.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Manually-turning-off-constrained_layout)手动关闭 constrained_layout

`constrained_layout`通常调整图形每次绘制时的轴位置。如果你想获得所提供的间距`constrained_layout`但没有更新，那么先进行初始绘制，然后调用 fig.set_constrained_layout（False）。这对于刻度标签可能会改变长度的动画非常有用。

请注意，`constrained_layout`对于使用工具栏的后端的 ZOOM 和 PAN GUI 事件，它处于关闭状态。这可以防止轴在变焦和平移期间改变位置。

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Limitations)限制

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Incompatible-functions)不兼容的功能

constrained_layout 不适用于通过 subplot 命令创建的子图。原因是这些命令中的每一个都创建了一个单独的 GridSpec 实例，而 constrained_layout 使用（嵌套的）gridspec 来执行布局。所以以下无法产生一个漂亮的布局：

```python
fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
```

![约束布局指南示例27](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_027-1565508653835.png)

当然可以使用 gridspec 进行布局：

```python
fig = plt.figure()
gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, 1])

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
```

![约束布局指南示例28](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_028-1565508653854.png)

同样，subplot2grid（）由于同样的原因不起作用：每次调用都会创建不同的父 gridspec。

```python
fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
```

![约束布局指南示例29](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_029-1565508653903.png)

使该图与 constrained_layout 兼容的方法是再次直接使用 gridspec

```python
fig = plt.figure()
gs = fig.add_gridspec(3, 3)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1:])
ax3 = fig.add_subplot(gs[1:, 0:2])
ax4 = fig.add_subplot(gs[1:, -1])

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
```

![约束布局指南示例30](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_030-1565508653911.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Other-Caveats)其他警告

+  constrained_layout 仅考虑 ticklabels，axis 标签，标题和图例。因此，其他艺术家可能被剪裁并且也可能重叠。
+  它假定刻度标签，轴标签和标题所需的额外空间与轴的原始位置无关。这通常是正确的，但在极少数情况下并非如此。
+  后端处理渲染字体的方式差异很小，因此结果不会像素相同。

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Debugging)调试

约束布局可能会以某种意外的方式失败。因为它使用约束求解器，求解器可以找到数学上正确的解，但根本不是用户想要的解。通常的故障模式是将所有尺寸折叠到其最小允许值。如果发生这种情况，原因有两个：

1. 您要求绘制的元素没有足够的空间。
2. 有一个错误 - 在这种情况下在[https://github.com/matplotlib/matplotlib/issues 上](https://github.com/matplotlib/matplotlib/issues)打开一个问题。

如果存在错误，请使用不需要外部数据或依赖项（numpy 除外）的自包含示例进行报告。

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Notes-on-the-algorithm)算法说明

约束的算法相对简单，但由于我们可以通过复杂的方式布局图形而具有一定的复杂性。

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Figure-layout)图布局

数字按层次排列：

1. 图：fig = plt.figure（）

   ```
    1. Gridspec gs0 = gridspec.GridSpec(1, 2, figure=fig)
            1. Subplotspec: ss = gs[0, 0]
                    1. Axes: ax0 = fig.add_subplot(ss)
            1. Subplotspec: ss = gs[0, 1]
                    1. Gridspec: gsR = gridspec.GridSpecFromSubplotSpec(2, 1, ss)
                            - Subplotspec: ss = gsR[0, 0]
                                    - Axes: axR0 = fig.add_subplot(ss)
                            - Subplotspec: ss = gsR[1, 0]
                                    - Axes: axR1 = fig.add_subplot(ss)
   ```

每个项目都有一个与之关联的布局框。使用 GridSpecFromSubplotSpec 创建的 gridspec 的嵌套可以任意深度。

每个 Axes 都有两个布局框。第一个，ax._layoutbox 表示轴的外部及其所有装饰（即刻度标签，轴标签等）。第二个布局框对应于 Axes 的 ax.position，它设置了图中刺的位置。

为什么这么多堆叠的容器？理想情况下，所有需要的是 Axes 布局框。对于 Gridspec 案例，如果 Gridspec 通过 GridSpecFromSubplotSpec 嵌套，则需要一个容器。在顶层，它是理想的对称性，但它也为 suptitle 腾出空间。

对于 Subplotspec / Axes 情况，Axes 通常有颜色条或其他注释需要打包在 Subplotspec 中，因此需要外层。

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Simple-case:-one-Axes)简单案例：一个轴

对于单个轴，布局是直截了当的。图和外部 Gridspec 布局框重合。Subplotspec 和 Axes 框也重合，因为 Axes 没有颜色条。请注意，红色 pos 框和绿色轴框之间的差异由 Axes 周围的装饰大小设置。

在代码中，这是通过 do_constrained_layout（）中的条目完成的，如：

```python
ax._poslayoutbox.edit_left_margin_min(-bbox.x0 + pos.x0 + w_padt)
from matplotlib._layoutbox import plot_children

fig, ax = plt.subplots(constrained_layout=True)
example_plot(ax, fontsize=24)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例31](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_031-1565508653922.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Simple-case:-two-Axes)简单案例：两个轴

对于这种情况，Axes 布局框和 Subplotspec 框仍然是共同的。但是，由于右侧绘图中的装饰比左侧小，所以右侧布局框较小。

Subplotspec 框在子例程 arange_subplotspecs（）中的代码中布局，它只是检查代码中的子图规对象并相应地堆叠它们。

两个 pos 轴排成一列。因为它们具有相同的最小行，所以它们排列在顶部。因为它们具有相同的最大行，所以它们排列在底部。在代码中，这是通过调用 layoutbox.align 来完成的。如果有多行，则行之间会出现相同的水平对齐。

两个 pos 轴的宽度相同，因为 subplotspecs 占据相同的列数。这是在将 dcols0 与 dcolsC 进行比较的代码中完成的。如果它们相等，则它们的宽度被限制为相等。

虽然在这种情况下它有点微妙，但请注意 Subplotspecs 之间的划分不是居中，而是已向右移动以为左侧绘图中的较大标签腾出空间。

```python
fig, ax = plt.subplots(1, 2, constrained_layout=True)
example_plot(ax[0], fontsize=32)
example_plot(ax[1], fontsize=8)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例32](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_032-1565508653926.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Two-Axes-and-colorbar)两个轴和颜色条

添加颜色条可以清楚地说明为什么 Subplotspec 布局框必须与轴布局框不同。在这里，我们看到左侧 subplotspec 有更多空间容纳颜色条，并且 ss 框内有两个绿色轴箱。

请注意，pos 框的宽度仍然相同，因为它们的宽度受到限制，因为它们的 subplotspecs 占用相同数量的列（在本例中为一列）。

colorbar 布局逻辑包含在 make_axes 中，它为连接到单个轴的 cbars 调用*约束*layout.layoutcolorbarsingle（），如果 colorbar 与 gridspec 关联，则*约束*layout.layoutcolorbargridspec（）。

```python
fig, ax = plt.subplots(1, 2, constrained_layout=True)
im = ax[0].pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=ax[0], shrink=0.6)
im = ax[1].pcolormesh(arr, **pc_kwargs)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例33](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_033-1565508653980.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Colorbar-associated-with-a-Gridspec)与 Gridspec 关联的 Colorbar

此示例显示 Subplotspec 布局框由颜色栏布局框缩小。colorbar 布局框的大小设置为小于 gridspec 中 pos 布局框的垂直范围的缩小，并使其在这两个点之间居中。

```python
fig, ax = plt.subplots(2, 2, constrained_layout=True)
for a in ax.flatten():
    im = a.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=ax, shrink=0.6)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例34](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_034-1565508654017.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Uneven-sized-Axes)大小不均匀的轴

在 Gridspec 布局中，有两种方法可以使轴具有不均匀的尺寸，方法是指定它们以跨越 Gridspecs 行或列，或者指定宽度和高度比。

这里使用第一种方法。使高度正确的约束是在 drowsC <drows0（在这种情况下为 1）小于 2 的代码中。因此我们将 1 行轴的高度约束为小于 2 的高度的一半。行轴。

**注意：**如果附加到较小轴的装饰非常大，则此算法可能是错误的，因此存在未解释的边缘情况。

```python
fig = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(2, 2, figure=fig)
ax = fig.add_subplot(gs[:, 0])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[0, 1])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[1, 1])
im = ax.pcolormesh(arr, **pc_kwargs)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例35](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_035-1565508654012.png)

高度和宽度比率与代码的相同部分相适应，较小的轴总是被约束为尺寸小于较大的轴。

```python
fig = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(3, 2, figure=fig,
    height_ratios=[1., 0.5, 1.5],
    width_ratios=[1.2, 0.8])
ax = fig.add_subplot(gs[:2, 0])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[2, 0])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[0, 1])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[1:, 1])
im = ax.pcolormesh(arr, **pc_kwargs)
plot_children(fig, fig._layoutbox, printit=False)
```

![约束布局指南示例36](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_036-1565508654051.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Empty-gridspec-slots)清空 gridspec 插槽

未解释的最后一段代码是如果有一个空的 gridspec 开头会发生什么。在这种情况下，添加一个假的不可见轴，我们像以前一样继续。空的 gridspec 没有装饰，但轴的位置与占用的轴位置大小相同。

这是在*约束* layout.do_constrained_layout（）（hassubplotspec）开始时完成的。

```python
fig = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(1, 3, figure=fig)
ax = fig.add_subplot(gs[0])
im = ax.pcolormesh(arr, **pc_kwargs)
ax = fig.add_subplot(gs[-1])
im = ax.pcolormesh(arr, **pc_kwargs)
plot_children(fig, fig._layoutbox, printit=False)
plt.show()
```

![约束布局指南示例37](pictures/Matplotlib 中文手册.assets/sphx_glr_constrainedlayout_guide_037-1565508654037.png)

#### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/constrainedlayout_guide.html#Other-notes)其他说明

布局只调用一次。如果原始布局非常接近（在大多数情况下应该是这样），这是可以的。但是，如果布局从默认布局改变很多，那么装饰器可以改变大小。特别是 x 和 ytick 标签可以改变。如果发生这种情况，那么我们应该将整个例程调用两次。

**脚本总运行时间：**（0 分 3.780 秒）



## 紧密布局指南

如何使用紧密布局以清晰地拟合图中的图形。

tight_layout 自动调整子图参数，以便子图符合图形区域。这是一个实验性功能，可能不适用于某些情况。它仅检查 ticklabels，轴标签和标题的范围。

另一种方法`tight_layout`是 constrained_layout。

### [#](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#简单例子)简单例子

在 matplotlib 中，轴（包括子图）的位置在标准化的图形坐标中指定。您的轴标签或标题（有时甚至是标签标签）可能会出现在图形区域之外，因此会被剪裁。

```python
# sphinx_gallery_thumbnail_number = 7

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"


def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)

plt.close('all')
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)
```

![紧密布局指南示例](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_001.png)

为防止这种情况，需要调整轴的位置。对于子图，可以通过调整子图参数（移动轴的边缘以为刻度标签腾出空间）来完成。Matplotlib v1.1 引入了一个新命令 tight_layout（），它会自动为您执行此操作。

```python
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)
plt.tight_layout()
```

![紧密布局指南示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_002.png)

请注意，matplotlib.pyplot.tight_layout（）仅在调用时调整子图 params。为了在每次重绘图形时执行此调整，您可以调用 fig.set_tight_layout（True），或者等效地将 figure.autolayout rcParam 设置为 True。

当您有多个子图时，通常会看到不同轴的标签彼此重叠。

```python
plt.close('all')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
```

![紧密布局指南示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_003.png)

tight_layout（）还将调整子图之间的间距以最小化重叠。

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
plt.tight_layout()
```

![紧密布局指南示例4](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_004.png)

tight_layout（）可以获取 pad，w_pad 和 h_pad 的关键字参数。它们控制图形边界周围和子图之间的额外填充。焊盘以字体大小的分数指定。

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
```

![紧密布局指南示例5](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_005.png)

即使子图的大小不同，只要它们的网格规范兼容，tight_layout（）也会起作用。在下面的示例中，ax1 和 ax2 是 2x2 网格的子图，而 ax3 是 1x2 网格。

```python
plt.close('all')
fig = plt.figure()

ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)

plt.tight_layout()
```

![紧密布局指南示例6](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_006.png)

它适用于使用 subplot2grid（）创建的子图。通常，从 gridspec 创建的子图（使用 GridSpec 和其他函数自定义图布局）将起作用。

```python
plt.close('all')
fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0))
ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

plt.tight_layout()
```

![紧密布局指南示例7](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_007.png)

虽然未经过全面测试，但它似乎适用于具有方面的子图！=“自动”（例如，带有图像的轴）。

```python
arr = np.arange(100).reshape((10, 10))

plt.close('all')
fig = plt.figure(figsize=(5, 4))

ax = plt.subplot(111)
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()
```

![紧密布局指南示例8](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_008.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#Caveats)警告

+  tight_layout（）仅考虑 ticklabels，轴标签和标题。因此，其他艺术家可能被剪裁并且也可能重叠。
+  它假定刻度标签，轴标签和标题所需的额外空间与轴的原始位置无关。这通常是正确的，但在极少数情况下并非如此。
+  pad = 0 用几个像素剪辑一些文本。这可能是当前算法的错误或限制，并且不清楚它为什么会发生。同时，建议使用至少大于 0.3 的垫。

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#Use-with-GridSpec)与 GridSpec 一起使用

GridSpec 有自己的 tight_layout（）方法（pyplot api tight_layout（）也有效）。

```python
import matplotlib.gridspec as gridspec

plt.close('all')
fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig)
```

![紧密布局指南示例9](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_009.png)

您可以提供一个可选的 rect 参数，该参数指定子图将适合的边界框。坐标必须是标准化的图形坐标，默认值为（0,0,1,1）。

```python
fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig, rect=[0, 0, 0.5, 1])
```

![紧密布局指南示例10](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_010.png)

例如，这可以用于具有多个网格规格的图形。

```python
fig = plt.figure()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig, rect=[0, 0, 0.5, 1])

gs2 = gridspec.GridSpec(3, 1)

for ss in gs2:
    ax = fig.add_subplot(ss)
    example_plot(ax)
    ax.set_title("")
    ax.set_xlabel("")

ax.set_xlabel("x-label", fontsize=12)

gs2.tight_layout(fig, rect=[0.5, 0, 1, 1], h_pad=0.5)

# We may try to match the top and bottom of two grids ::
top = min(gs1.top, gs2.top)
bottom = max(gs1.bottom, gs2.bottom)

gs1.update(top=top, bottom=bottom)
gs2.update(top=top, bottom=bottom)
plt.show()
```

![紧密布局指南示例11](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_011.png)

虽然这应该足够好，但调整顶部和底部也可能需要调整 hspace。要更新 hspace 和 vspace，我们再次使用更新的 rect 参数调用 tight_layout（）。请注意，rect 参数指定包含 ticklabels 等的区域。因此，我们将通过每个 gridspec 的上方和底部之间的差异来增加底部（对于正常情况为 0）。顶部也一样。

```python
fig = plt.gcf()

gs1 = gridspec.GridSpec(2, 1)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

example_plot(ax1)
example_plot(ax2)

gs1.tight_layout(fig, rect=[0, 0, 0.5, 1])

gs2 = gridspec.GridSpec(3, 1)

for ss in gs2:
    ax = fig.add_subplot(ss)
    example_plot(ax)
    ax.set_title("")
    ax.set_xlabel("")

ax.set_xlabel("x-label", fontsize=12)

gs2.tight_layout(fig, rect=[0.5, 0, 1, 1], h_pad=0.5)

top = min(gs1.top, gs2.top)
bottom = max(gs1.bottom, gs2.bottom)

gs1.update(top=top, bottom=bottom)
gs2.update(top=top, bottom=bottom)

top = min(gs1.top, gs2.top)
bottom = max(gs1.bottom, gs2.bottom)

gs1.tight_layout(fig, rect=[None, 0 + (bottom-gs1.bottom),
                            0.5, 1 - (gs1.top-top)])
gs2.tight_layout(fig, rect=[0.5, 0 + (bottom-gs2.bottom),
                            None, 1 - (gs2.top-top)],
                 h_pad=0.5)
```

![紧密布局指南示例12](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_012.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#Legends-and-Annotations)图例和注解

Pre Matplotlih 2.2，图例和注释被排除在决定布局的边界框计算之外。随后，这些艺术家被添加到计算中，但有时不包括它们。例如，在这种情况下，让轴稍微移动以为图例腾出空间可能是件好事：

```python
fig, ax = plt.subplots(figsize=(4, 3))
lines = ax.plot(range(10), label='A simple plot')
ax.legend(bbox_to_anchor=(0.7, 0.5), loc='center left',)
fig.tight_layout()
plt.show()
```

![紧密布局指南示例13](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_013.png)

但是，有时这是不可取的（通常在使用 fig.savefig（'outname.png'，bbox_inches ='tight'）时）。为了从边界框计算中删除图例，我们只需设置其边界 leg.set_in_layout（False），图例将被忽略。

```python
fig, ax = plt.subplots(figsize=(4, 3))
lines = ax.plot(range(10), label='B simple plot')
leg = ax.legend(bbox_to_anchor=(0.7, 0.5), loc='center left',)
leg.set_in_layout(False)
fig.tight_layout()
plt.show()
```

![紧密布局指南示例14](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_014.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#Use-with-AxesGrid1)与 AxesGrid1 一起使用

虽然有限，但也支持 axes_grid1 工具包。

```python
from mpl_toolkits.axes_grid1 import Grid

plt.close('all')
fig = plt.figure()
grid = Grid(fig, rect=111, nrows_ncols=(2, 2),
            axes_pad=0.25, label_mode='L',
            )

for ax in grid:
    example_plot(ax)
ax.title.set_visible(False)

plt.tight_layout()
```

![紧密布局指南示例15](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_015.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/tight_layout_guide.html#Colorbar)彩条

如果使用 colorbar（）命令创建颜色栏，则创建的颜色栏是 Axes 的实例，而不是 Subplot，因此 tight_layout 不起作用。使用 Matplotlib v1.1，您可以使用 gridspec 创建一个颜色条作为子图。

```python
plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

plt.colorbar(im, use_gridspec=True)

plt.tight_layout()
```

![紧密布局指南示例16](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_016.png)

另一种选择是使用 AxesGrid1 工具包显式创建颜色条的轴。

```python
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

plt.tight_layout()
```

![紧密布局指南示例17](pictures/Matplotlib 中文手册.assets/sphx_glr_tight_layout_guide_017.png)

**脚本总运行时间：**（0 分 1.488 秒）



## 原点和范围在 imshow

imshow（）允许您渲染一个图像（一个 2D 数组，它将被颜色映射（基于 norm 和 cmap）或 3D RGB（A）数组，它将按原样使用）到数据空间中的矩形区域。最终渲染中图像的方向由原点和范围 kwargs（以及生成的 AxesImage 实例上的属性）和轴的数据限制控制。

范围 kwarg 控制**数据坐标**中的边界框，图像将在**数据坐标**中指定为（左，右，底部，顶部），原始 kwarg 控制图像填充边界框的方式，以及最终渲染图像中的方向也受轴限制的影响。

**提示：以下**大部分代码用于向图表添加标签和信息性文本。可以在图中看到所描述的起源和范围的影响，而无需遵循所有代码细节。为了快速理解，您可能希望跳过下面的代码详细信息，并直接继续讨论结果。

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def index_to_coordinate(index, extent, origin):
    """Return the pixel center of an index."""
    left, right, bottom, top = extent

    hshift = 0.5 * np.sign(right - left)
    left, right = left + hshift, right - hshift
    vshift = 0.5 * np.sign(top - bottom)
    bottom, top = bottom + vshift, top - vshift

    if origin == 'upper':
        bottom, top = top, bottom

    return {
        "[0, 0]": (left, bottom),
        "[M', 0]": (left, top),
        "[0, N']": (right, bottom),
        "[M', N']": (right, top),
    }[index]


def get_index_label_pos(index, extent, origin, inverted_xindex):
    """
    Return the desired position and horizontal alignment of an index label.
    """
    if extent is None:
        extent = lookup_extent(origin)
    left, right, bottom, top = extent
    x, y = index_to_coordinate(index, extent, origin)

    is_x0 = index[-2:] == "0]"
    halign = 'left' if is_x0 ^ inverted_xindex else 'right'
    hshift = 0.5 * np.sign(left - right)
    x += hshift * (1 if is_x0 else -1)
    return x, y, halign


def get_color(index, data, cmap):
    """Return the data color of an index."""
    val = {
        "[0, 0]": data[0, 0],
        "[0, N']": data[0, -1],
        "[M', 0]": data[-1, 0],
        "[M', N']": data[-1, -1],
    }[index]
    return cmap(val / data.max())


def lookup_extent(origin):
    """Return extent for label positioning when not given explicitly."""
    if origin == 'lower':
        return (-0.5, 6.5, -0.5, 5.5)
    else:
        return (-0.5, 6.5, 5.5, -0.5)


def set_extent_None_text(ax):
    ax.text(3, 2.5, 'equals\nextent=None', size='large',
            ha='center', va='center', color='w')


def plot_imshow_with_labels(ax, data, extent, origin, xlim, ylim):
    """Actually run ``imshow()`` and add extent and index labels."""
    im = ax.imshow(data, origin=origin, extent=extent)

    # extent labels (left, right, bottom, top)
    left, right, bottom, top = im.get_extent()
    if xlim is None or top > bottom:
        upper_string, lower_string = 'top', 'bottom'
    else:
        upper_string, lower_string = 'bottom', 'top'
    if ylim is None or left < right:
        port_string, starboard_string = 'left', 'right'
        inverted_xindex = False
    else:
        port_string, starboard_string = 'right', 'left'
        inverted_xindex = True
    bbox_kwargs = {'fc': 'w', 'alpha': .75, 'boxstyle': "round4"}
    ann_kwargs = {'xycoords': 'axes fraction',
                  'textcoords': 'offset points',
                  'bbox': bbox_kwargs}
    ax.annotate(upper_string, xy=(.5, 1), xytext=(0, -1),
                ha='center', va='top', **ann_kwargs)
    ax.annotate(lower_string, xy=(.5, 0), xytext=(0, 1),
                ha='center', va='bottom', **ann_kwargs)
    ax.annotate(port_string, xy=(0, .5), xytext=(1, 0),
                ha='left', va='center', rotation=90,
                **ann_kwargs)
    ax.annotate(starboard_string, xy=(1, .5), xytext=(-1, 0),
                ha='right', va='center', rotation=-90,
                **ann_kwargs)
    ax.set_title('origin: {origin}'.format(origin=origin))

    # index labels
    for index in ["[0, 0]", "[0, N']", "[M', 0]", "[M', N']"]:
        tx, ty, halign = get_index_label_pos(index, extent, origin,
                                             inverted_xindex)
        facecolor = get_color(index, data, im.get_cmap())
        ax.text(tx, ty, index, color='white', ha=halign, va='center',
                bbox={'boxstyle': 'square', 'facecolor': facecolor})
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)


def generate_imshow_demo_grid(extents, xlim=None, ylim=None):
    N = len(extents)
    fig = plt.figure(tight_layout=True)
    fig.set_size_inches(6, N * (11.25) / 5)
    gs = GridSpec(N, 5, figure=fig)

    columns = {'label': [fig.add_subplot(gs[j, 0]) for j in range(N)],
               'upper': [fig.add_subplot(gs[j, 1:3]) for j in range(N)],
               'lower': [fig.add_subplot(gs[j, 3:5]) for j in range(N)]}
    x, y = np.ogrid[0:6, 0:7]
    data = x + y

    for origin in ['upper', 'lower']:
        for ax, extent in zip(columns[origin], extents):
            plot_imshow_with_labels(ax, data, extent, origin, xlim, ylim)

    for ax, extent in zip(columns['label'], extents):
        text_kwargs = {'ha': 'right',
                       'va': 'center',
                       'xycoords': 'axes fraction',
                       'xy': (1, .5)}
        if extent is None:
            ax.annotate('None', **text_kwargs)
            ax.set_title('extent=')
        else:
            left, right, bottom, top = extent
            text = ('left: {left:0.1f}\nright: {right:0.1f}\n' +
                    'bottom: {bottom:0.1f}\ntop: {top:0.1f}\n').format(
                        left=left, right=right, bottom=bottom, top=top)

            ax.annotate(text, **text_kwargs)
        ax.axis('off')
    return columns
```

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/imshow_extent.html#Default-extent)默认范围

首先，让我们看看默认范围 = 无

```python
generate_imshow_demo_grid(extents=[None])
```

![imshow中的原点和范围示例](pictures/Matplotlib 中文手册.assets/sphx_glr_imshow_extent_001.png)

通常，对于形状（M，N）的数组，第一个索引沿垂直方向运行，第二个索引沿水平方向延伸。像素中心位于整数位置，水平范围为 0 到 N'= N-1，垂直方向为 0 到 M'= M-1。origin 确定如何在边界框中填充数据。

用于`origin='lower'`：

+  [0,0] 位于（左，下）
+  [M'，0] 位于（左，上）
+  [0，N'] 位于（右，下）
+  [M'，N'] 在（右，上）

`origin='upper'` 反转垂直轴方向和填充：

+  [0,0] 位于（左，上）
+  [M'，0] 位于（左，下）
+  [0，N'] 在（右，上）
+  [M'，N'] 位于（右，下）

总之，[0,0] 索引的位置以及范围受原点的影响：

| 起源 | [0,0] 位置 | 程度                                     |
| ---- | ---------- | ---------------------------------------- |
| 上   | 左上方     | （-0.5，numcols-0.5，numrows-0.5，-0.5） |
| 降低 | 左下方     | （-0.5，numcols-0.5，-0.5，numrows-0.5） |

origin 的默认值由 rcParams [“image.origin”] 设置，默认为 “upper” 以匹配数学和计算机图形图像索引约定中的矩阵索引约定。

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/imshow_extent.html#Explicit-extent)明确范围

通过设置范围，我们定义图像区域的坐标。对基础图像数据进行插值 / 重采样以填充该区域。

如果将轴设置为自动缩放，则将轴的视图限制设置为与确保由（左，下）设置的坐标位于轴左下角的范围匹配！但是，这可能会使轴反转，因此它们不会在 “自然” 方向上增加。

```python
extents = [(-0.5, 6.5, -0.5, 5.5),
           (-0.5, 6.5, 5.5, -0.5),
           (6.5, -0.5, -0.5, 5.5),
           (6.5, -0.5, 5.5, -0.5)]

columns = generate_imshow_demo_grid(extents)
set_extent_None_text(columns['upper'][1])
set_extent_None_text(columns['lower'][0])
```

![imshow中的原点和范围示例2](pictures/Matplotlib 中文手册.assets/sphx_glr_imshow_extent_002.png)

### [＃](https://www.matplotlib.org.cn/tutorials/intermediate/imshow_extent.html#Explicit-extent-and-axes-limits)显式范围和轴限制

如果我们通过显式设置 set_xlim /set_ylim 来修复轴限制，我们会强制轴的某个大小和方向。这可以将图像的 “左右” 和 “上下” 感与屏幕上的方向分离。

在下面的示例中，我们选择了略大于范围的限制（请注意轴内的白色区域）。

虽然我们之前的例子中保留了范围，但是坐标（0,0）现在显式地放在左下角，值增加到上和右（从观察者的角度来看）。我们可以看到：

+  坐标（左，下）锚定图像，然后填充框朝向数据空间中的（右，顶）点。
+  第一列始终最接近 “左”。
+  `origin` 控制第一行是否最接近 “顶部” 或 “底部”。
+  图像可以沿任一方向反转。
+  图像的 “左右” 和 “上下” 感可以与屏幕上的方向分离。

```python
generate_imshow_demo_grid(extents=[None] + extents,
                          xlim=(-2, 8), ylim=(-1, 6))
```

![imshow中的原点和范围示例3](pictures/Matplotlib 中文手册.assets/sphx_glr_imshow_extent_003.png)