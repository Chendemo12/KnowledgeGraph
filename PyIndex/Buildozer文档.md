# 欢迎使用Buildozer的文档！

Buildozer是旨在轻松打包手机应用程序的工具。它会自动执行整个构建过程，下载python-for-android，Android SDK，NDK等先决条件。

Buildozer 在您的应用程序目录中管理一个名为`buildozer.spec`的文件，描述您的应用程序要求和设置，例如标题，图标，随附的模块等。它将使用规范文件来创建适用于Android，iOS等的程序包。

当前，Buildozer支持以下包装：

-   Android：通过[适用于Android的Python进行](https://github.com/kivy/python-for-android)。您必须具有Linux或OSX计算机才能针对Android进行编译。
-   iOS：通过[Kivy iOS](https://github.com/kivy/kivy-ios)。您必须有一台OSX计算机才能针对iOS进行编译。
-   路线图中支持其他平台（例如Windows的.exe，OSX的.dmg等）

如果您对Buildozer有任何疑问，请参阅[Kivy的用户邮件列表](https://groups.google.com/forum/#!forum/kivy-users)。



## 安装

Buildozer本身不依赖任何Python> = 3.3的库。根据要定位的平台，可能需要安装更多工具。Buildozer会尝试为您提供提示或尝试为您安装一些东西，但是并不能涵盖所有情况。

首先，使用以下命令安装buildozer项目：

```
pip3 install --user --upgrade buildozer
```

### 定位

#### Ubuntu 18.04（64bit）上的

（预期在以后的版本中也能正常工作，但仅在最新的LTS中进行定期测试）

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev
pip3 install --user --upgrade cython virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/
```

#### 故障排除

##### Buildozer坚持“必要时安装/更新SDK平台工具”

按“ y”，然后输入以继续，许可证接受系统正在静默等待您的输入

##### 找不到Aidl，请安装它。

Buildozer没有安装必要的软件包

```bash
~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager "build-tools;29.0.0"
```

然后按“ y”，然后输入以接受许可证。

##### python-for-android相关错误

请参阅专用的[p4a故障排除文档](https://python-for-android.readthedocs.io/en/latest/troubleshooting/)。

#### 定位

安装XCode和命令行工具（通过AppStore）

安装自制软件（https://brew.sh）

```bash
brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer autoconf automake
```

安装pip和virtualenv

```bash
python -m pip install --user --upgrade pip virtualenv kivy-ios
```



## 快速入门

让我们开始使用Buildozer！

### 初始化并为Android构建

1.  Buildozer会尝试猜测您的应用程序的版本，通过搜索这样一行__version__ =“1.0.3”在您的main.py。确保您的应用程序开始时只有一个。它不是强制性的，但建议量很大。

2.  使用以下命令创建一个buildozer.spec文件：

    ```bash
    buildozer init
    ```

3.  根据规范编辑buildozer.spec。你至少应该改变标题，package.name和package.domain在 [应用]部分。

4.  使用以下命令启动Android /调试版本：

    ```bash
    buildozer -v android debug
    ```

5.  现在是时候喝咖啡/茶了，如果您的电脑速度较慢，则该晚饭了。首次构建会很慢，因为它将下载Android SDK，NDK以及编译所需的其他工具。不用担心，这些文件将保存在全局目录中，并将在您将通过Buildozer管理的不同项目中共享。

6.  最后，您应该在bin /目录中有一个APK文件。

### 运行我的应用程序

Buildozer能够在您的移动设备上部署，运行该应用程序，甚至可以将日志返回控制台。仅当您已至少编译一次应用程序时，它才有效：

```bash
buildozer android deploy run logcat
```

对于iOS，它看起来是一样的：

```bash
buildozer ios deploy run
```

您可以将编译与部署结合起来：

```bash
buildozer -v android debug deploy run logcat
```

您还可以在默认命令中将此行设置为在不带任何参数的情况下启动Buildozer时执行的操作：

```bash
buildozer setdefault android debug deploy run logcat

# now just type buildozer, and it will do the default command
buildozer
```

要将logcat输出保存到名为my_log.txt的文件中（该文件将出现在当前目录中）：

```bash
buildozer -v android debug deploy run logcat > my_log.txt
```

### 在未连接的设备上安装

如果您已经编译了一个程序包，并希望与其他设备轻松共享它，则可能对serve命令感兴趣。它将通过HTTP 服务 bin /目录。然后，您只需从手机访问控制台中显示的URL：

```bash
buildozer serve
```



## 规格

本文档详细说明了您可以在buildozer.spec中使用的所有配置令牌 。

### [app]部分

-   title：字符串，您的应用程序的标题。

    根据目标平台的不同，某些字符可能无法正常工作。最好尝试看看一切是否按预期进行。尽量避免标题太长，因为它们也将不适合图标下方显示的标题。

-   package.name：字符串，软件包名称。

    软件包名称是一个仅包含ASCII字符和/或数字的单词。它不应包含任何特殊字符。例如，如果您的应用程序名为Flat Jewels，则包名称可以为flatjewels。

-   package.domain：字符串，包域。

    包域是引用执行该应用程序的公司或个人的字符串。域名和域名都将成为您的Android和iOS应用程序标识符，请谨慎选择。例如，当Kivy的团队发布应用程序时，域以org.kivy开始。

-   source.dir：字符串，应用程序源的位置。

    该位置必须是包含main.py文件的目录。它默认为buildozer.spec所在的目录。

-   source.include_exts：列表，要包含的文件扩展名。

    默认情况下，不包括source.dir中的所有文件，而是仅包括其中一些文件（py，png，jpg，kv，atlas），具体取决于扩展名。随意添加自己的扩展名，如果要包括所有内容，则使用空值。

-   source.exclude_exts：列表，要排除的文件扩展名。

    与source.include_exts相反，您可以包括所有想要的文件，但以该令牌中列出的扩展名结尾的文件除外。如果为空，则不会根据文件扩展名排除文件。

-   source.exclude_dirs：列表，要排除的目录。

    与source.exclude_exts相同，但用于目录。您可以使用以下命令排除 测试和bin目录：

    ```bash
    source.exclude_dirs = tests, bin
    ```

-   source.exclude_patterns：列出文件，如果它们与模式匹配则要排除。

    如果您的应用程序布局更复杂，则可能需要一种模式来排除文件。如果您没有图案，它也可以使用。例如：

    ```bash
    source.exclude_patterns = license,images/originals/*
    ```

-   version.regex：正则表达式，用于捕获version.filename中版本的正则表达式 。

    应用程序版本的默认捕获方法是通过grep这样的一行：

    ```bash
    __version__ = "1.0"
    ```

    的1.0将被用作一个版本。

-   version.filename：字符串，默认为main.py。

    用于使用version.regex捕获版本的文件。

-   version：字符串，手动应用程序版本。

    如果您不想捕获版本，请注释掉version.regex 和version.filename，然后将所需的版本直接放在 版本令牌中：

    ```bash
    # version.regex =
    # version.filename =
    version = 1.0
    ```

-   要求：列出您的应用程序所需的Python模块或扩展。

    要求可以是Android专用Python项目中配方的名称，也可以是纯Python包。例如，如果您的应用程序需要Kivy和请求，则需要编写：

    ```bash
    requirements = kivy,requests
    ```

    如果您的应用程序尝试安装Python扩展程序（即需要编译的Python包），并且该扩展程序没有与Android专用Python关联的配方，则它将无法正常工作。我们在此处明确禁用了编译。如果要使其工作，请通过创建配方为Android专用Python项目做出贡献。请参阅[贡献](index.html#document-contribute)。

-   garden_requirements：列表，要包括的花园套餐。

    在此处添加要包括的Kivy花园包装清单。例如：

    ```bash
    garden_requirements = graph
    ```

    请注意，如果它不起作用，可能是因为花园包装本身。如果软件包的作者已经在您的目标平台（而非我们）上对其进行了测试，请咨询该软件包的作者。

-   presplash.filename：字符串，应用程序的加载屏幕。

    预闪屏是加载应用程序期间设备上显示的图像。在Android上称为presplash，在iOS上称为Loading image。根据平台的不同，映像可能会有不同的要求。目前，Buildozer仅与Android兼容，iOS对它的支持不是很好。

    该图像必须是JPG或PNG，最好具有2的幂数，例如512x512的图像非常适合定位所有设备。图像未在设备上安装，缩放或任何其他内容。如果提供的图像太大，则可能无法在小屏幕上显示。

-   icon.filename：字符串，应用程序的图标。

    您的应用程序的图标。它必须是512x512大小的PNG，才能满足所有各种平台要求。

-   orientation：字符串，应用程序的方向。

    指示您的应用程序支持的方向。默认为 横向，但可以更改为纵向或全部。

-   fullscreen：布尔值，全屏模式。

    默认值为true，您的应用程序将以全屏模式运行。表示状态栏将被隐藏。如果要让用户访问状态栏，小时，通知，请使用0作为值。



## 贡献

### 编写自己的食谱

配方可让您为移动设备编译库/ python扩展。在大多数情况下，默认编译指令对目标不起作用，因为ARM编译器/ Android NDK会引入所需的库无法正确处理的特性，因此您需要对其进行修补。另外，由于Android平台最多只能加载64个内联动态库，因此我们提供了一种将所有动态库捆绑在一起的机制，以确保您不会遇到此限制。

要通过Buildozer测试自己的配方，您需要：

1.  Fork [Python for Android](http://github.com/kivy/python-for-android)，并克隆您自己的版本（以后可以轻松添加）：

    ```bash
    git clone http://github.com/YOURNAME/python-for-android
    ```

2.  更改您的buildozer.spec以引用您的版本：

    ```bash
    p4a.source_dir = /path/to/your/python-for-android
    ```

3.  将您的食谱复制到python-for-android / recipes / YOURLIB / recipe.sh

4.  重建。

当您正确地获得编译结果并且您的配方有效时，您可以通过发出Pull Request要求我们将其包括在python-for-android项目中：

1.  创建一个分支：

    ```bash
    git checkout --track -b recipe-YOURLIB origin/master
    ```

2.  添加并提交：

    ```bash
    git add python-for-android/recipes/YOURLIB/*
    git commit -am 'Add support for YOURLIB`
    ```

3.  推送到Github

    >   git push origin master

4.  转到http://github.com/YOURNAME/python-for-android，您应该看到新的分支和上面的“ Pull Request”按钮。使用它，写您所做的描述，然后发送！

# 指数和表格

-   [指数](genindex.html)
-   [模块索引](py-modindex.html)
-   [搜索页面](search.html)