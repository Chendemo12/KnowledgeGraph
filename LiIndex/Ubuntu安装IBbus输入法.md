Ubuntu安装IBus中文输入法

## 1. im-config 设置说明

设置 用户设置` /home/username/.xinputrc `为 default。
自动设置选择: ibus
IBus 智能输入法

 * 必需组件：ibus
 * 输入特定语言所需的组件：
   * 简体中文拼音：ibus-pinyin 或 ibus-sunpinyin 或 ibus-googlepinyin
   * 简体中文五笔：ibus-table-wubi
   * 繁体中文：ibus-chewing 或 ibus-table-quick 或 ibus-table-cangjie
   * 日文：ibus-mozc (最佳)或 ibus-anthy 或 ibus-skk
   * 韩文：ibus-hangul
   * 泰文：ibus-table-thai
   * 越南文：ibus-unikey 或 ibus-table-viqr
   * X 键盘仿真: ibus-xkbc
   * 通用的输入法码表: ibus-m17n 或 ibus-table* packages
 * 应用程序支持：
   * GNOME/GTK+：ibus-gtk 和 ibus-gtk3 (强烈建议同时安装)
   * KDE/Qt：ibus-qt4
   * Clutter：ibus-clutter
   * EMACS：ibus-el

用户设置 已被 im-config 修改。

请重新启动 X 会话管理器以激活新的 用户设置。
如果使用旧配置的守护进程被 X 会话管理器重启，您可能需要使用 kill(1) 手工将其杀死。
请参考 im-config(8) 和 /usr/share/doc/im-config/README.Debian.gz





## 2. IBus输入法安装和设置

IBus 全称 Intelligent Input Bus是下一代输入法框架（或者说“平台”）。 项目现托管于 [Google Code IBus]( https://code.google.com/p/ibus/) 此项目包含了世界多数语言的文字输入需求——由世界多个国家开发者维护。

IBus是一个框架，支持多种输入法。

### 2.1 安裝IBus框架：

在终端输入命令:

```
sudo apt-get install ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4
```

### 2.2 启用IBus框架：

在终端输入:

```
im-switch -s ibus
```

重新启动X（也可以重启电脑）

### 2.3 安装拼音引擎：

在终端输入:

```
sudo apt-get install ibus-pinyin
```

设置ibus-pinyin，在终端输入:

```
/usr/lib/ibus-pinyin/ibus-setup-pinyin
```

安装sunpinyin模块，在终端输入:

```
sudo apt-get install ibus-sunpinyin
```

设置ibus-sunpinyin，在终端输入:

```
/usr/lib/ibus-sunpinyin/ibus-setup-sunpinyin
```

### 2.4 安装五笔引擎：

在终端输入:

```
sudo apt-get install ibus-table-wubi
```

### 2.5 设置IBus框架：

在终端输入:

```
ibus-setup
```

### 2.6 Kubuntu下使用IBus：

在终端输入:

```
sudo apt-get install gnome-icon-theme
```

其他同上

### 2.7 找回消失的IBus图标：

在终端输入:

```
ibus-daemon -drx
```

### 2.8 其他语言输入法：

安装 ibus-m17n 包即可。

```
sudo apt-get install ibus-m17n
```

这个软件包包含了几乎所有除了英语，中日韩等的其他输入法，如：阿拉伯语，阿姆哈拉语，阿萨姆语，阿萨帕斯坎诸语，奥杰布瓦语，白俄罗斯语，波斯语，藏语，傣语，丹麦语，迪维希语，俄语，法语，梵语，高棉语，格鲁吉亚语，古典希腊语，古吉拉特语，哈萨克语，捷克语，卡纳达语，克里语，克罗地亚语，克什米尔语，老挝语，马拉提语，马拉雅拉姆语，孟加拉语，缅甸语，尼泊尔语，旁遮普语，普什图语，日语，瑞典语，瑞典，塞尔维亚语，僧加罗语，世界语，斯洛伐克语，四川彝族语，泰卢固语，泰米尔语，泰语，维吾尔语，乌兹别克语，乌尔都语，希伯来语，现代希腊语，信德语，亚美尼亚语，伊努伊特语，依地语，印地语，越南，占语，朝鲜，latex输入特殊符号，input-pad等。

如果您使用的是 fcitx，请安装相应的包。

```
sudo apt-get install fcitx-m17n
```



### 2.9 自定义码表输入法及设置：

安装好ibus后,在目录:`/usr/share/`下会有:`ibus,ibus-pinyin,ibus-table`，三个文件夹.

其中`ibus-table`文件夹中用于存放五笔之类的输入法内容.其下

`icons`文件夹用于存放输入法显示的图片,

`tables`文件夹用于存放码表(db格式)(SQlite数据库)

我们可以使用ibus提供的工具把自己的码表和参数生成db文件

导入到ibus中，生成自己的输入法使用,

ibus提供了一个样本文件:`template.txt`

以便参考

其大概格式如下:

```
### 该码表文件必须按UTF-8格式编码保存
### 注释行以### 开头而不是一个#
### 它起源于scim码表格式，所以你可以用scim-tables码表来修改
SCIM_Generic_Table_Phrase_Library_TEXT
VERSION_1_0
### 开始定义
BEGIN_DEFINITION

### License
LICENSE = LGPL
### UUID用于标识该表以便于区分其他的表，你可以在终端中使用
### uuidgen命令产生一个uuid给该表
UUID = c9851827-0abe-12ed-8db5-010b9d51ffed

### 版本号,但不要太长
### For example the last modified date of this file.
### This number must be less than 2^32.
### Just make your table version-able
SERIAL_NUMBER = 20090218

### 输入法图标，可以是pygtk识别的图片格式，一般用png,svg格式
### 该图标放在icons目录
ICON = ibus-table.svg

### 默认的表名，必填
NAME = Table

### 本地名，选添
NAME.zh_CN = 形码
NAME.zh_HK = 形碼
NAME.zh_TW = 形碼

###  描述可填可不填
DESCRIPTION = This is a template engine table for IBus Table.

### 该码表支持的语言
### 只用"zh_CN"则认为是zh_CN
### 但是如果是zh_CN,zh_HK或其他zh_XX则认为是zh
### and "en_US, zh_CN" will be just ignored.
LANGUAGES = zh_CN,zh_SG,zh_TW,zh_HK

### 该表作者
AUTHOR = Z ZZ <XXX@gmail.com> 

### 提示字符，它将被显示在状态栏中，CN会被“中”字代替
STATUS_PROMPT = CN

### 可输入的字符
VALID_INPUT_CHARS = abcdefghijklmnopqrstuvwxyz

### Layout
LAYOUT = us

### 每个字或短语的最大输入长度
MAX_KEY_LENGTH = 4

### 自动上屏功能默认关闭FALSE(TRUE打开)
### 有人说五笔不能自动上屏把这修改成TRUE就好了
AUTO_COMMIT = FALSE

### 标点符号 默认是全角格式
DEF_FULL_WIDTH_PUNCT = TRUE

### 全角字符默认关闭
DEF_FULL_WIDTH_LETTER = FALSE

### 是否允许用户定义词组短语，默认允许
### 但你需要定义构词法则
### 开启后使用该表时定义词组方法:
### 先输入词组中的每一个字,输完选字时用Ctrl+"数字键" 选取
### 词组中的第一个字,然后输入词组中的第二个字,
### 输完选字时用Ctrl+"数字键" 选取
### 直到输入该词组的最后一个字,输完后直接用数字键选则
### 如此,这一词组便录入完闭,以后即可按后面定义的词组法则来输入该词
USER_CAN_DEFINE_PHRASE = TRUE

### 是否允许拼音模式，默认允许，该功能只是为中文设计
### 如果你的输入法不是中文的可以关闭它(似乎没什么用??注音模式?反正我不会用)
PINYIN_MODE = TRUE

### 字,词组,短语频率调节.默认允许
DYNAMIC_ADJUST = TRUE  

### Some characters whose frequencies should be fix all the time, e.g. 
### some punctuations
### NO_CHECK_CHARS = 

### 用户自定义词组后该词输入规则
### ce表示词组长度等于，例如ce2表示词组长度等于2，
### ca表示词组长度等于或大于，
### p21表示词组中第2个字的第一笔（对应的按键）
### 每一个规则用;号隔开
RULES = ce2:p11+p12+p21+p22;ce3:p11+p21+p22+p31;ca4:p11+p21+p31+p41
### 以上规则表示,两字词按每字前2个键输入,3字词按1字1键2字1,2键,3字1键输入...
END_DEFINITION
### 开始码表数据
### 码表格式为：“输入建\t(制表符)字词\t(制表符)频率\n(换行)”
### From left to right, the 1st column are the input key combination that you
### entered via keyboard; the 2nd column are presented character or phrase of
### the key combination you want; the 3rd column are frequency of the character
### or phrase.
BEGIN_TABLE
input_keys	aim_chars	freq
input_keys	aim_chars	freq
input_keys	aim_chars	freq
END_TABlE

### 有些输入法对词组中的字使用不同的码表，例如郑码，它需要定义guocima
### 如果你不许要请把下面的注释掉
### Since some input methods use different table for every character to make
### phrase, such as ZhengMa, they need explict define the goucima (the
### phrase-building code for the given character), the format of every entry is
### "character\tgoucima\n". 
### For the input method which just use the full code as word-building code
### just skip this field. The ibus-table will build the codes needed from
### above TABLE.
### if you don't need different word-building code, please comment out the
### next few lines with ###, just like these lines you are look at now.
BEGIN_GOUCI
character_1	goucima_1
character_1	goucima_2
END_GOUCI
```

去掉注释的样本如下:

```
SCIM_Generic_Table_Phrase_Library_TEXT
VERSION_1_0

BEGIN_DEFINITION

UUID = c88e7342-13ae-498d-9442-fc92ad1d85ee

SERIAL_NUMBER = 1

ICON = wubi98.svg

NAME = WuBi98

NAME.zh_CN = 五笔98
NAME.zh_HK = 五筆98
NAME.zh_TW = 五筆98

LANGUAGES = zh_CN,zh_SG,zh_TW,zh_HK

AUTHOR = SomeBody

STATUS_PROMPT = CN

VALID_INPUT_CHARS = abcdefghijklmnopqrstuvwxy

MAX_KEY_LENGTH = 4

AUTO_COMMIT = TRUE

DEF_FULL_WIDTH_PUNCT = FALSE

DEF_FULL_WIDTH_LETTER = FALSE

USER_CAN_DEFINE_PHRASE = TRUE

PINYIN_MODE = TRUE

DYNAMIC_ADJUST = TRUE 

RULES = ce2:p11+p12+p21+p22;ce3:p11+p21+p31+p32;ca4:p11+p21+p31+p-11

END_DEFINITION

BEGIN_TABLE
abc      工      100
aaa      内置词组      50
bbb      内置短语      101
END_TABLE
```

根据个人喜好写完上述文件,和"BEGIN_TABLE"与"END_TABLE"之间的码表保存好, 然后到终端用命令:

```
ibus-table-createdb -s 你的码表名
```

生成该表的db文件,然后用命令:

```
sudo cp 你的码表名.db /usr/share/ibus-table/tables/ 
```

放到ibus目录中,重启后就可以使用了. 当然了还有输入法的图片:

```
sudo cp 输入法图片 /usr/share/ibus-table/icons/ 
```

# Ubuntu 安装Fcitx输入法

## 1. im-config 设置说明
设置 用户设置 /home/lichenguang/.xinputrc 为 fcitx。
手动设置选择: fcitx
小企鹅输入法(Fcitx)
 * 必需组件：fcitx
 * 输入特定语言所需的组件：
   * 简体中文拼音：fcitx-sunpinyin 或 fcitx-googlepinyin 或 fcitx-pinyin
   * 简体中文五笔：fcitx-table-wubi 或 fcitx-table-wbpy
   * 繁体中文：fcitx-table-cangjie
   * 通用的输入法码表: fcitx-table 套件
 * 应用程序支持：
   * GNOME/GTK+：fcitx-frontend-gtk2 和 fcitx-frontend-gtk3
                  (强烈建议同时安装)
   * KDE/Qt4：fcitx-frontend-qt4

用户设置 已被 im-config 修改。

请重新启动 X 会话管理器以激活新的 用户设置。
如果使用旧配置的守护进程被 X 会话管理器重启，您可能需要使用 kill(1) 手工将其杀死。
请参考 im-config(8) 和 /usr/share/doc/im-config/README.Debian.gz

