

# Selenium with Python 中文翻译文档 

| 作者: | [Baiju Muthukadan](https://muthukadan.net/)                  |
| :---- | ------------------------------------------------------------ |
| 翻译: | [caoruiy](http://blog.plcent.com/), 感谢 [yangeren](https://github.com/yangeren) 的参与 |
| 授权: | This document is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)。 |

[TOC]
**【Note】**

这不是一个官方的文档。官方的文档可以 [在此获得](https://seleniumhq.github.io/selenium/docs/api/py/api.html)。

# 1. 安装 

## 1.1. 安装 

`Selenium Python bindings` 提供了一个简单的 API，让你使用 `Selenium WebDriver` 来编写功能 / 校验测试。 通过`Selenium Python` 的 API，你可以非常直观的使用 `Selenium WebDriver` 的所有功能。

`Selenium Python bindings` 使用非常简洁方便的 API 让你去使用像 Firefox, IE, Chrome, Remote 等等 这样的 `Selenium WebDrivers`（Selenium web 驱动器）。当前支持的版本为 2.7, 3.2 及以上。

本文的用来讲解说明 `Selenium 2 WebDriver` 的 API，此文档不包含 Selenium 1 / Selenium RC 的文档。

## 1.2. 下载 Python bindings for Selenium

可以从 PyPI 的官方库中下载该 selenium 支持库， [点此下载](https://pypi.python.org/pypi/selenium) 当然， 更好的方法当然是使用 [pip](https://pip.pypa.io/en/latest/installing/) 命令来安装 selenium 包。 Python3.5 的 [`标准库`]( <https://docs.python.org/3.5/installing/index.html) >中包含 pip 命令。 使用 [`pip`](https://selenium-python-zh.readthedocs.io/en/latest/installation.html#id6)命令，你可以像下面这样安装 selenium:

```python
pip install selenium
```

Note

使用 Python2.x 版本的用户可以手动安装 pip 或者 easy_install，下面是 easy_install 的安装方法:

>  easy_install selenium

你可以考虑使用 [`virtualenv`]( http://www.virtualenv.org/) _创建独立的 Python 环境。Python3.5 中 [`pyvenv`](https://docs.python.org/3.5/using/scripts.html#scripts-pyvenv)  可以提供几乎一样的功能。

## 1.3. Windows 用户的详细说明 

**Note**

请在有网的情况下执行该安装命令。

1. 安装 Python3.5：[官方下载页](http://www.python.org/download).

2. 从开始菜单点击运行（或者 `Windows+R`）输入 `cmd`, 然后执行下列命令安装:

   ```
   C:\Python35\Scripts\pip.exe install selenium
   ```

现在你可以使用 Python 运行测试脚本了。 例如：如果你创建了一个 selenium 的基本示例并且保存在了 ``C:my_selenium_script.py``，你可以如下执行:

```
C:\Python35\python.exe C:\my_selenium_script.py
```

## 1.4. 下载 Selenium 服务器 

Note

如果你想使用一个远程的 WebDriver，Selenium 服务是唯一的依赖， 参见 [使用远程 Selenium WebDriver](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html#selenium-remote-webdriver) 获得更多细节。 如果你只是刚刚开始学习使用 Selenium，你可以忽略该章节直接开始下一节。

Selenium server 是一个 JAVA 工程，Java Runtime Environment (JRE) 1.6 或者更高的版本是推荐的运行环境。

你可以在 [该下载页](http://seleniumhq.org/download/) 下载 2.x 的 Selenium server，这个文件大概长成这个样子：`selenium-server-standalone-2.x.x.jar`， 你可以去下载最新版本的 2.x server。

如果你还没有安装 Java Runtime Environment (JRE) 的话， 呢，[在这下载](http://www.oracle.com/technetwork/java/javase/downloads/index.html)， 如果你是有的是 GNU/Linux 系统，并且巧了，你还有 root 权限，你还可以使用操作系统指令去安装 JRE。

如果你把 `java` 命令放在了 PATH (环境变量) 中的话，使用下面命令安装:

```java
java -jar selenium-server-standalone-2.x.x.jar
```

当然了，把 ``2.x.x`` 换成你下载的实际版本就可以了。

如果是不是 root 用户你或者没有把 JAVA 放到 PATH 中， 你可以使用绝对路径或者相对路径的方式来使用命令， 这个命令大概长这样子:

```
/path/to/java -jar /path/to/selenium-server-standalone-2.x.x.jar
```



# 2. 快速入门 

## 2.1. 简单用例 

如果你已经安装好了 selenium，你可以把下面的 python 代码拷贝到你的编辑器中

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

上面的脚本可以保存到一个文件（如 python_org_search.py），那么可以这样使用

```python
python python_org_search.py
```

你运行的 python 环境中应该已经安装了 selenium 模块。

## 2.2. 示例详解 

selenium.webdriver 模块提供了所有 WebDriver 的实现， 当前支持的 WebDriver 有： Firefox, Chrome, IE and Remote。 [`Keys`](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html#id4) 类提供键盘按键的支持，比如：RETURN, F1, ALT 等

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

接下来，创建一个 Firefox WebDriver 的实例

```python
driver = webdriver.Firefox()
```

driver.get 方法将打开 URL 中填写的地址，WebDriver 将等待，直到页面完全加载完毕（其实是等到”onload” 方法执行完毕），然后返回继续执行你的脚本。值得注意的是，如果你的页面使用了大量的 Ajax 加载， WebDriver 可能不知道什么时候页面已经完全加载:

```python
driver.get("http://www.python.org")
```

下一行是用 assert 的方式确认标题是否包含 “Python” 一词。 (译注：assert 语句将会在之后的语句返回 false 后抛出异常，详细内容可以自行百度)

```python
assert "Python" in driver.title
```

WebDriver 提供了大量的方法让你去查询页面中的元素，这些方法形如： find_element_by_*。 例如：包含 name 属性的 input 输入框可以通过 find_element_by_name 方法查找到， 详细的查找方法可以在第四节元素查找中查看:

```python
elem = driver.find_element_by_name("q")
```

接下来，我们发送了一个关键字，这个方法的作用类似于你用键盘输入关键字。 特殊的按键可以使用 Keys 类来输入，该类继承自 selenium.webdriver.common.keys， 为了安全起见，我们先清除 input 输入框中的任何预填充的文本（例如：”Search”）, 从而避免我们的搜索结果受影响：

```python
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面后，你会得到所有的结果。为了确保某些特定的结果被找到，使用 `assert` 如下:

```python
assert "No results found." not in driver.page_source
```

最后，关闭浏览器窗口，你还可以使用 quit 方法代替 close 方法， quit 将关闭整个浏览器，而_close—— 只会关闭一个标签页， 如果你只打开了一个标签页，大多数浏览器的默认行为是关闭浏览器:

```python
driver.close()
```

## 2.3. 用 Selenium 写测试用例 

Selenium 通常被用来写一些测试用例. selenium 包本身不提供测试工具或者框架。你可以使用 Python 自带的模块 unittest 写测试用例。 The other options for a tool/framework are py.test and nose.

在本章中，我们使用 unittest 来编写测试代码，下面是一个已经写好的用例。 这是一个在 python.org 站点上搜索的案例:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

你可以在 shell 中运行下列代码:

```python
python test_python_org_search.py

----------------------------------------------------------------------
Ran 1 test in 15.566s

OK
```

结果表明这个测试用例已经成功运行。

## 2.4. 逐步解释测试代码 

一开始，我们引入了需要的模块， [unittest](http://docs.python.org/library/unittest.html) 模块是基于 JAVA JUnit 的 Python 内置的模块。 该模块提供了一个框架去组织测试用例。 selenium.webdriver 模块提供了所有 WebDriver 的实现。 现在支持的 WebDriver 有：Firefox, Chrome, IE and Remote. Keys 类提供所有的键盘按键操作，比如像这样的：

>  RETURN, F1, ALT 等。

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

该测试类继承自unittest.TestCase. 继承 TestCase 类是告诉 unittest 模块该类是一个测试用例:

```python
class PythonOrgSearch(unittest.TestCase):
```

setUp 方法是初始化的一部分，该方法会在该测试类中的每一个测试方法被执行前都执行一遍。 下面创建了一个 Firefox WebDriver 的一个实例。

```python
def setUp(self):
    self.driver = webdriver.Firefox()
```

这是一个测试用例实际的测试方法。测试方法始终以 `test` 开头。 在该方法中的第一行创建了一个在 `setUp` 方法中创建的驱动程序对象的本地引用。

```python
def test_search_in_python_org(self):
    driver = self.driver
```

`driver.get`方法将会根据方法中给出的 URL 地址打开该网站。 WebDriver 会等待整个页面加载完成（其实是等待”onload” 事件执行完毕）之后把控制权交给测试程序。 如果你的页面使用大量的 AJAX 技术来加载页面，WebDriver 可能不知道什么时候页面已经加载完成:

```python
driver.get("http://www.python.org")
```

下面一行使用 assert 断言的方法判断在页面标题中是否包含 “Python”

```python
self.assertIn("Python", driver.title)
```

WebDriver 提供很多方法去查找页面值的元素，这些方法都以*find_element_by_* 开头。 例如：包含 name 属性的 input 元素可以使用

>  find_element_by_name:

```python
elem = driver.find_element_by_name("q")
```

接下来我们发送`keys`，这个和使用键盘输入 keys 类似。 特殊的按键可以通过引入 `selenium.webdriver.common.keys` 的 `Keys` 类来输入

```pythoon
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面之后，无论如何你都会得到搜索结果，为了确保某些结果类检索到，可以使用下列断言 After submission of the page, you should get result as per search if

```python
assert "No results found." not in driver.page_source
```

`tearDown` 方法会在每一个测试方法执行之后被执行。 该方法可以用来做一些清扫工作，比如关闭浏览器。 当然你也可以调用 `quit` 方法代替 `close` 方法，

>  `quit` 将关闭整个浏览器，而 `close` 只会关闭一个标签页， 如果你只打开了一个标签页，大多数浏览器的默认行为是关闭浏览器。

```python
def tearDown(self):
    self.driver.close()
```

下面是入口函数:

```python
if __name__ == "__main__":
    unittest.main()
```



## 2.5. 使用远程 Selenium WebDriver

为了使用远程 WebDriver, 你应该拥有一个正在运行的 Selenium 服务器。 通过下列命令运行服务器:

```java
java -jar selenium-server-standalone-2.x.x.jar
```

Selenium 服务运行后，你会看到这样的提示信息:

```
15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
```

上面一行告诉你，你可以通过这个 URL 连接到远程 WebDriver， 下面是一些例子:

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.OPERA)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
```

[`desired_capabilities`](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html#id7) 是一个字典，如果你不想使用默认的字典，你可以明确指定一个值

```python
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
```



# 3. 打开一个页面 

你想做的第一件事也许是使用 WebDriver 打开一个链接。 常规的方法是调用 `get` 方法:

```python
driver.get("http://www.google.com")
```

WebDriver 将等待，直到页面完全加载完毕（其实是等到 `onload` 方法执行完毕）， 然后返回继续执行你的脚本。 值得注意的是，如果你的页面使用了大量的 Ajax 加载， WebDriver 可能不知道什么时候页面已经完全加载。 如果你想确保也 main 完全加载完毕，可以使用`:ref:waits <waits>`

## 3.1. 与页面交互 

只是打开页面其实并没有什么卵用。我们真正想要的是与页面做交互。 更具体地说，对于一个页面中的 HTML 元素，首先我们要找到他。WebDriver 提供了大量的方法帮助你去查找元素，例如：已知一个元素定义如下:

```python
<input type="text" name="passwd" id="passwd-id" />
```

你可以通过下面的方法查找他:

```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```

你还可以通过链接的文本查找他，需要注意的是，这个文本必须完全匹地配。 当你使用 `XPATH` 时，你必须注意，如果匹配超过一个元素，只返回第一个元素。 如果上面也没找到，将会抛出 [`NoSuchElementException`](https://selenium-python-zh.readthedocs.io/en/latest/navigating.html#id3)异常。

WebDriver 有一个"基于对象" 的 API; 我们使用相同的接口表示所有类型的元素。 这就意味着，当你打开你的 IDE 的自动补全的时候，你会有很多可以调用的方法。 但是并不是所有的方法都是有意义或是有效的。不过不要担心！ 当你调用一些毫无意义的方法时，WebDriver 会尝试去做一些正确的事情（例如你对一个"meta"元素调用`setSelected()`方法的时候）。

所以，当你拿到 ige 元素时，你能做什么呢？首先，你可能会想在文本框中输入一些内容:

```python
element.send_keys("some text")
```

你还可以通过”Keys” 类来模式输入方向键:

```python
element.send_keys(" and some", Keys.ARROW_DOWN)
```

对于任何元素，他可能都叫 `send_keys` ，这就使得它可以测试键盘快捷键， 比如当你使用 Gmail 的时候。但是有一个副作用是当你输入一些文本时，这些 输入框中原有的文本不会被自动清除掉，相反，你的输入会继续添加到已存在文本之后。 你可以很方便的使用 `clear()` 方法去清除 input 或者 textarea 元素中的内容:

```python
element.clear()
```

## 3.2. 填写表格 

我们已经知道如何在 input 或 textarea 元素中输入内容，但是其他元素怎么办？ 你可以 “切换” 下拉框的状态，你可以使用 `setSelected`方法去做一些事情，比如 选择下拉列表，处理 `SELECT` 元素其实没有那么麻烦:

```python
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
```

上面这段代码将会寻找页面第一个 “SELECT” 元素，并且循环他的每一个 OPTION 元素， 打印从 utamen 的值，然后按顺序都选中一遍。

正如你说看到的那样，这不是处理 SELECT 元素最好的方法。WebDriver 的支持类包括一个叫做 [`Select`](https://selenium-python-zh.readthedocs.io/en/latest/navigating.html#id6)的类，他提供有用的方法处理这些内容:

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

WebDriver 也提供一些有用的方法来取消选择已经选择的元素:

```python
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

这将取消选择所以的 OPTION。

假设在一个案例中，我们需要列出所有已经选择的选项，Select 类提供了方便的方法来实现这一点:

```python
select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options
```

获得所以选项:

```python
options = select.options
```

一旦你填写完整个表单，你应该想去提交它，有一个方法就是去找到一个 “submit” 按钮然后点击它:

```python
# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()
```

或者，WebDriver 对每一个元素都有一个叫做 `submit()` 的方法，如果你在一个表单内的 元素上使用该方法，WebDriver 会在 DOM 树上就近找到最近的表单，返回提交它。 如果调用的元素不再表单内，将会抛出 `NoSuchElementException` 异常:

```python
element.submit()
```

## 3.3. 拖放 

您可以使用拖放，无论是移动一个元素，或放到另一个元素内:

```python
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```

## 3.4. 在不同的窗口和框架之间移动 

对于现在的 web 应用来说，没有任何 frames 或者只包含一个 window 窗口是比较罕见的。 WebDriver 支持在不同的窗口之间移动，只需要调用 `switch_to_window` 方法即可:

```python
driver.switch_to_window("windowName")
```

所有的 `driver` 将会指向当前窗口，但是你怎么知道当前窗口的名字呢，查看打开他的 javascript 或者连接代码:

```html
<a href="somewhere.html" target="windowName">Click here to open a new window</a>
```

或者，你可以在`switch_to_window ()` 中使用” 窗口句柄” 来打开它， 知道了这些，你就可以迭代所有已经打开的窗口了:

```python
for handle in driver.window_handles:
    driver.switch_to_window(handle)
```

你还可以在不同的 frame 中切换 (or into iframes):

```python
driver.switch_to_frame("frameName")
```

通过 “.” 操作符你还可以获得子 frame，并通过下标指定任意 frame，就像这样:

```python
driver.switch_to_frame("frameName.0.child")
```

如何获取名叫 “frameName” 的 frame 中名叫 “child” 的子 frame 呢？ **来自 top frame 的所有的 frame 都会被评估** （ **All frames are evaluated as if from top.**）

一旦我们完成了 frame 中的工作，我们可以这样返回父 frame:

```python
driver.switch_to_default_content()
```

## 3.5. 弹出对话框 

Selenium WebDriver 内置了对处理弹出对话框的支持。 在你的某些动作之后可能会触发弹出对话框，你可以像下面这样访问对话框:

```python
alert = driver.switch_to_alert()
```

它将返回当前打开的对话框对象。使用此对象，您现在可以接受、排除、读取其内容， 甚至可以在 prompt 对话框中输入 (译注：`prompt()` 是对话框的一种，不同于 `alert()`对话框，不同点可以自行百度)。 这个接口对 alert, confirm， prompt 对话框效果相同。 参考相关的 API 文档获取更多信息。

## 3.6. 访问浏览器历史记录 

在之前的文章中，我们使用 `get` 命令打开一个页面，( `driver.get("http://www.example.com")`)，WebDriver 有很多更小的，以任务为导向的接口， navigation 就是一个有用的任务，打开一个页面你可以使用 `get`:

```python
driver.get("http://www.example.com")
```

在浏览历史中前进和后退你可以使用:

```python
driver.forward()
driver.back()
```

请注意，这个功能完全取决于底层驱动程序。当你调用这些方法的时候，很有可能会发生意想不到的事情， 如果你习惯了浏览器的这些行为于其他的不同。（原文：It’s just possible that something unexpected may happen when you call these methods if you’re used to the behaviour of one browser over another.）

## 3.7. 操作 Cookies

在我们结束这一节之前，或许你对如何操作 Cookies 可能会很感兴趣。 首先，你需要打开一个也面，因为 Cookie 是在某个域名下才生效的:

```python
::
```

>  \# 打开一个页面 driver.get (“[http://www.example.com](http://www.example.com/)”)
>
>  \# 现在设置 Cookies，这个 cookie 在域名根目录下（”/”）生效 cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’} driver.add_cookie (cookie)
>
>  \# 现在获取所有当前 URL 下可获得的 Cookies driver.get_cookies ()


# 4. 查找元素 

在一个页面中有很多不同的策略可以定位一个元素。在你的项目中， 你可以选择最合适的方法去查找元素。Selenium 提供了下列的方法给你:

+  find_element_by_id
+  find_element_by_name
+  find_element_by_xpath
+  find_element_by_link_text
+  find_element_by_partial_link_text
+  find_element_by_tag_name
+  find_element_by_class_name
+  find_element_by_css_selector

**一次查找多个元素 (这些方法会返回一个 list 列表):**

+  find_elements_by_name
+  find_elements_by_xpath
+  find_elements_by_link_text
+  find_elements_by_partial_link_text
+  find_elements_by_tag_name
+  find_elements_by_class_name
+  find_elements_by_css_selector

除了上述的公共方法，下面还有两个私有方法，在你查找也页面元素的时候也许有用。 他们是 find_element 和 find_elements 。

用法示例:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

下面是 By 类的一些可用属性:

```python
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## 4.1. 通过 ID 查找元素 

当你知道一个元素的 id 时，你可以使用本方法。在该策略下，页面中第一个该 id 元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>
```

可以这样查找表单 (form) 元素:

```python
login_form = driver.find_element_by_id('loginForm')
```

## 4.2. 通过 Name 查找元素 

当你知道一个元素的 name 时，你可以使用本方法。在该策略下，页面中第一个该 name 元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>
```

name 属性为 username & password 的元素可以像下面这样查找:

```python
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
```

这会得到 “Login” 按钮，因为他在 “Clear” 按钮之前:

```python
continue = driver.find_element_by_name('continue')
```

## 4.3. 通过 XPath 查找元素 

XPath 是 XML 文档中查找结点的语法。因为 HTML 文档也可以被转换成 XML (XHTML) 文档， Selenium 的用户可以利用这种强大的语言在 web 应用中查找元素。 XPath 扩展了（当然也支持）这种通过 id 或 name 属性获取元素的简单方式，同时也开辟了各种新的可能性， 例如获取页面上的第三个复选框。

使用 XPath 的主要原因之一就是当你想获取一个既没有 id 属性也没有 name 属性的元素时， 你可以通过 XPath 使用元素的绝对位置来获取他（这是不推荐的），或相对于有一个 id 或 name 属性的元素 （理论上的父元素）的来获取你想要的元素。XPath 定位器也可以通过非 id 和 name 属性查找元素。

绝对的 XPath 是所有元素都从根元素的位置（HTML）开始定位，只要应用中有轻微的调整，会就导致你的定位失败。 但是通过就近的包含 id 或者 name 属性的元素出发定位你的元素，这样相对关系就很靠谱， 因为这种位置关系很少改变，所以可以使你的测试更加强大。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>
```

可以这样查找表单 (form) 元素:

```python
login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
```

1. 绝对定位 (页面结构轻微调整就会被破坏)
2. HTML 页面中的第一个 form 元素
3. 包含 id 属性并且其值为 loginForm 的 form 元素

username 元素可以如下获取:

```python
username = driver.find_element_by_xpath("//form[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")
```

1. 第一个 form 元素中包含 name 属性并且其值为 username 的 input 元素
2. id 为 loginForm 的 form 元素的第一个 input 子元素
3. 第一个 name 属性为 username 的 input 元素

“Clear” 按钮可以如下获取:

```python
clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
```

1. Input with attribute named name and the value continue and attribute named type and the value button
2. Fourth input child element of the form element with attribute named id and value loginForm

这些实例都是一些举出用法，为了学习更多有用的东西，下面这些参考资料推荐给你:

+  [W3Schools XPath Tutorial](http://www.w3schools.com/xsl/xpath_intro.asp)
+  [W3C XPath Recommendation](http://www.w3.org/TR/xpath)
+  [XPath Tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html) - with interactive examples.

还有一些非常有用的插件，可以协助发现元素的 XPath:

+  [XPath Checker](https://addons.mozilla.org/en-US/firefox/addon/1095?id=1095) - suggests XPath and can be used to test XPath results.
+  [Firebug](https://addons.mozilla.org/en-US/firefox/addon/1843) - XPath suggestions are just one of the many powerful features of this very useful add-on.
+  [XPath Helper](https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl) - for Google Chrome

## 4.4. 通过链接文本获取超链接 

当你知道在一个锚标签中使用的链接文本时使用这个。 在该策略下，页面中第一个匹配链接内容锚标签 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
<html>
```

continue.html 超链接可以被这样查找到:

```python
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')
```

## 4.5. 通过标签名查找元素 

当你向通过标签名查找元素时使用这个。 在该策略下，页面中第一个匹配该标签名的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <h1>Welcome</h1>
  <p>Site content goes here.</p>
</body>
<html>
```

h1 元素可以如下查找:

```python
heading1 = driver.find_element_by_tag_name('h1')
```

## 4.6. 通过 Class name 定位元素 

当你向通过 class name 查找元素时使用这个。 在该策略下，页面中第一个匹配该 class 属性的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

p 元素可以如下查找:

```python
content = driver.find_element_by_class_name('content')
```

## 4.7. 通过 CSS 选择器查找元素 

当你向通过 CSS 选择器查找元素时使用这个。 在该策略下，页面中第一个匹配该 CSS 选择器的元素 会被匹配并返回。如果找不到任何元素，会抛出 `NoSuchElementException` 异常。

作为示例，页面元素如下所示:

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

p 元素可以如下查找:

```python 
content = driver.find_element_by_css_selector('p.content')
```

[Sauce 实验室有一篇很好的文档来介绍 CSS 选择器](http://saucelabs.com/resources/selenium/css-selectors)



# 5. 等待页面加载完成 (Waits)

现在的大多数的 Web 应用程序是使用 Ajax 技术。当一个页面被加载到浏览器时， 该页面内的元素可以在不同的时间点被加载。这使得定位元素变得困难， 如果元素不再页面之中，会抛出 ElementNotVisibleException 异常。 使用 waits, 我们可以解决这个问题。waits 提供了一些操作之间的时间间隔 - 主要是定位元素或针对该元素的任何其他操作。

Selenium Webdriver 提供两种类型的 waits - 隐式和显式。 显式等待会让 WebDriver 等待满足一定的条件以后再进一步的执行。 而隐式等待让 Webdriver 等待一定的时间后再才是查找某元素。

## 5.1. 显式等待 

显式等待是你在代码中定义等待一定条件发生后再进一步执行你的代码。 最糟糕的案例是使用 time.sleep ()，它将条件设置为等待一个确切的时间段。 这里有一些方便的方法让你只等待需要的时间。WebDriverWait 结合 ExpectedCondition 是实现的一种方式。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```

在抛出 TimeoutException 异常之前将等待 10 秒或者在 10 秒内发现了查找的元素。 WebDriverWait 默认情况下会每 500 毫秒调用一次 ExpectedCondition 直到结果成功返回。 ExpectedCondition 成功的返回结果是一个布尔类型的 true 或是不为 null 的返回值。

**预期的条件**

自动化的 Web 浏览器中一些常用的预期条件，下面列出的是每一个实现， `Selenium Python binding` 都提供了一些方便的方法，这样你就不用去编写 expected_condition 类或是创建至今的工具包去实现他们。 

- title_is - title_contains - presence_of_element_located - visibility_of_element_located - visibility_of - presence_of_all_elements_located - text_to_be_present_in_element - text_to_be_present_in_element_value - frame_to_be_available_and_switch_to_it - invisibility_of_element_located - element_to_be_clickable - 显示并可用. - staleness_of - element_to_be_selected - element_located_to_be_selected - element_selection_state_to_be - element_located_selection_state_to_be - alert_is_present

```python
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
```

expected_conditions 模块提供了一组预定义的条件供 WebDriverWait 使用。

## 5.2. 隐式等待 

如果某些元素不是立即可用的，隐式等待是告诉 WebDriver 去等待一定的时间后去查找元素。 默认等待时间是 0 秒，一旦设置该值，隐式等待是设置该 WebDriver 的实例的生命周期。

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```



# 6. 页面对象 

本章是一个针对页面对象设计模式的教程引导。 一个页面对象表示在你测试的 WEB 应用程序的用户界面上的区域。

使用页面对象模式的好处:

+  创建可复用的代码以便于在多个测试用例间共享
+  减少重复的代码量
+  如果用户界面变化，只需要修改一处

## 6.1. 测试用例 

下面是一个在 python.org 网站搜索一个词并保证一些结果可以找到的测试用例。

```python
import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
            assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

## 6.2. 页面对象类 

页面对象为每个网页模拟创建出一个对象。 按照此技术，在测试代码和技术实施之间的一个分离层被创建。

这个 `page.py` 看起来像这样:

```python
from element import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
```

## 6.3. 页面元素 

这个 `element.py` 看起来像这样:

```python
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
```

## 6.4. 定位器 

其中一个做法是，从它们正在使用的地方分离定位字符。在这个例子中，同一页面的定位器属于同一个类。

这个 `locators.py` 看起来像这样:

```python
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
```



# 7. Selenium Documentation

## 7.1 Common

| modules                                                      | explain                                               |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [`selenium.common.exceptions`](https://seleniumhq.github.io/selenium/docs/api/py/common/selenium.common.exceptions.html#module-selenium.common.exceptions) | Exceptions that may happen in all the webdriver code. |

## 7.2 Webdriver.common

| [`selenium.webdriver.common.action_chains`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#module-selenium.webdriver.common.action_chains) | The ActionChains implementation,         |
| ------------------------------------------------------------ | ---------------------------------------- |
| [`selenium.webdriver.common.alert`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.alert.html#module-selenium.webdriver.common.alert) | The Alert implementation.                |
| [`selenium.webdriver.common.by`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html#module-selenium.webdriver.common.by) | The By implementation.                   |
| [`selenium.webdriver.common.desired_capabilities`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html#module-selenium.webdriver.common.desired_capabilities) | The Desired Capabilities implementation. |
| [`selenium.webdriver.common.keys`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys) | The Keys implementation.                 |
| [`selenium.webdriver.common.touch_actions`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.touch_actions.html#module-selenium.webdriver.common.touch_actions) | The Touch Actions implementation         |
| [`selenium.webdriver.common.utils`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.utils.html#module-selenium.webdriver.common.utils) | The Utils methods.                       |
| [`selenium.webdriver.common.proxy`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.proxy.html#module-selenium.webdriver.common.proxy) | The Proxy implementation.                |
| [`selenium.webdriver.common.service`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.service.html#module-selenium.webdriver.common.service) |                                          |
| [`selenium.webdriver.common.html5.application_cache`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.html5.application_cache.html#module-selenium.webdriver.common.html5.application_cache) | The ApplicationCache implementaion.      |

## 7.3 Webdriver.support

| [`selenium.webdriver.support.abstract_event_listener`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.abstract_event_listener.html#module-selenium.webdriver.support.abstract_event_listener) |
| ------------------------------------------------------------ |
| [`selenium.webdriver.support.color`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.color.html#module-selenium.webdriver.support.color) |
| [`selenium.webdriver.support.event_firing_webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.event_firing_webdriver.html#module-selenium.webdriver.support.event_firing_webdriver) |
| [`selenium.webdriver.support.expected_conditions`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html#module-selenium.webdriver.support.expected_conditions) |
| [`selenium.webdriver.support.select`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select) |
| [`selenium.webdriver.support.wait`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.wait.html#module-selenium.webdriver.support.wait) |



## 7.4 Webdriver.android

[`selenium.webdriver.android.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_android/selenium.webdriver.android.webdriver.html#module-selenium.webdriver.android.webdriver)

## 7.5 Webdriver.chrome

| [`selenium.webdriver.chrome.options`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.options.html#module-selenium.webdriver.chrome.options) |
| ------------------------------------------------------------ |
| [`selenium.webdriver.chrome.service`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.service.html#module-selenium.webdriver.chrome.service) |
| [`selenium.webdriver.chrome.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.webdriver.html#module-selenium.webdriver.chrome.webdriver) |

## 7.6 Webdriver.firefox

| [`selenium.webdriver.firefox.extension_connection`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.extension_connection.html#module-selenium.webdriver.firefox.extension_connection) |
| ------------------------------------------------------------ |
| [`selenium.webdriver.firefox.firefox_binary`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.firefox_binary.html#module-selenium.webdriver.firefox.firefox_binary) |
| [`selenium.webdriver.firefox.options`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html#module-selenium.webdriver.firefox.options) |
| [`selenium.webdriver.firefox.firefox_profile`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.firefox_profile.html#module-selenium.webdriver.firefox.firefox_profile) |
| [`selenium.webdriver.firefox.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.webdriver.html#module-selenium.webdriver.firefox.webdriver) |

## 7.7 Webdriver.ie

| [`selenium.webdriver.ie.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_ie/selenium.webdriver.ie.webdriver.html#module-selenium.webdriver.ie.webdriver) |
| ------------------------------------------------------------ |
|                                                              |

## 7.8 Webdriver.opera

[`selenium.webdriver.opera.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_opera/selenium.webdriver.opera.webdriver.html#module-selenium.webdriver.opera.webdriver)

## 7.9 Webdriver.phantomjs

| [`selenium.webdriver.phantomjs.service`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_phantomjs/selenium.webdriver.phantomjs.service.html#module-selenium.webdriver.phantomjs.service) |
| ------------------------------------------------------------ |
| [`selenium.webdriver.phantomjs.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_phantomjs/selenium.webdriver.phantomjs.webdriver.html#module-selenium.webdriver.phantomjs.webdriver) |

## 7.10 Webdriver.remote

| [`selenium.webdriver.remote.command`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.command.html#module-selenium.webdriver.remote.command) |                               |
| ------------------------------------------------------------ | ----------------------------- |
| [`selenium.webdriver.remote.errorhandler`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.errorhandler.html#module-selenium.webdriver.remote.errorhandler) |                               |
| [`selenium.webdriver.remote.mobile`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.mobile.html#module-selenium.webdriver.remote.mobile) |                               |
| [`selenium.webdriver.remote.remote_connection`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.remote_connection.html#module-selenium.webdriver.remote.remote_connection) |                               |
| [`selenium.webdriver.remote.utils`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.utils.html#module-selenium.webdriver.remote.utils) |                               |
| [`selenium.webdriver.remote.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#module-selenium.webdriver.remote.webdriver) | The WebDriver implementation. |
| [`selenium.webdriver.remote.webelement`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html#module-selenium.webdriver.remote.webelement) |                               |

## 7.11 Webdriver.safari

| [`selenium.webdriver.safari.service`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_safari/selenium.webdriver.safari.service.html#module-selenium.webdriver.safari.service) |
| ------------------------------------------------------------ |
| [`selenium.webdriver.safari.webdriver`](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_safari/selenium.webdriver.safari.webdriver.html#module-selenium.webdriver.safari.webdriver) |

## 7.12 部分类

The By implementation.

+  *class* `selenium.webdriver.common.by`						[[源代码\]](https://seleniumhq.github.io/selenium/docs/api/py/_modules/selenium/webdriver/common/by.html#By)

   Set of supported locator strategies.
   
   ​	`CLASS_NAME` *= 'class name'*
   
   ​	`CSS_SELECTOR` *= 'css selector'*
   
   ​	`ID` *= 'id'*
   ​	`LINK_TEXT` *= 'link text'*
   ​	`NAME` *= 'name'*
   ​	`PARTIAL_LINK_TEXT` *= 'partial link text'*
   ​	`TAG_NAME` *= 'tag name'*
   ​	`XPATH` *= 'xpath'
   
   

![1568818702223](pictures/Selenium with Python 中文翻译文档.assets/1568818702223.png)



![1568818747887](pictures/Selenium with Python 中文翻译文档.assets/1568818747887.png)

![1568818859610](pictures/Selenium with Python 中文翻译文档.assets/1568818859610.png)

![1568818891763](pictures/Selenium with Python 中文翻译文档.assets/1568818891763.png)

![1568818910753](pictures/Selenium with Python 中文翻译文档.assets/1568818910753.png)



![1568818949874](pictures/Selenium with Python 中文翻译文档.assets/1568818949874.png)

![1568818970746](pictures/Selenium with Python 中文翻译文档.assets/1568818970746.png)



![1568818990592](pictures/Selenium with Python 中文翻译文档.assets/1568818990592.png)



![1568819013801](pictures/Selenium with Python 中文翻译文档.assets/1568819013801.png)

![1568819033689](pictures/Selenium with Python 中文翻译文档.assets/1568819033689.png)



# 8. 附录：常见问题 

Another FAQ: https://github.com/SeleniumHQ/selenium/wiki/Frequently-Asked-Questions

## 8.1. 如何使用 ChromeDriver ?

下载最新版本的 [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). 解压缩这个文件:

```
unzip chromedriver_linux32_x.x.x.x.zip
```

你应该会看到一个 `chromedriver` 的可执行文件。现在你可以像这样创建一个 Chrome WebDriver 实例:

```python
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
```

这个示例的其余部分应该在其他的文档中给出。

## 8.2. Selenium 2 是否支持 XPath 2.0 版本？

参考：http://seleniumhq.org/docs/03_webdriver.html#how-xpath-works-in-webdriver

Selenium 代表的 XPath 查询基于浏览器自身的 XPath 引擎，所以 Selenium 支持任何 支持 XPath 的浏览器。在不具备原生的 XPath 引擎（IE6,7,8）的浏览器，Selenium 只支持 XPath 1.0。

## 8.3. 如何向下滚动到页面的底部？

参考: http://blog.varunin.com/2011/08/scrolling-on-pages-using-selenium.html

你可以在加载完成的页面上使用 execute_script 方法执行 js。所以， 你调用 javascript API 滚动到底部或页面的任何位置。

这里是一个滚动到页面底部的例子:

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

该 [window](http://www.w3schools.com/jsref/obj_window.asp) 对象在 DOM 有一个 [scrollTo](http://www.w3schools.com/jsref/met_win_scrollto.asp) 滚动到打开窗口 的任意位置的方法。 该 [scrollHeight](http://www.w3schools.com/jsref/dom_obj_all.asp) 是所有元素的共同属性。 该 document.body.scrollHeight 将给出整个页面体的高度。

## 8.4. 如何使用自定义的 Firefox 配置文件保存文件？

参考: http://stackoverflow.com/questions/1176348/access-to-file-download-dialog-in-firefox

参考: http://blog.codecentric.de/en/2010/07/file-downloads-with-selenium-mission-impossible/

第一步是要确认自动保存文件的类型。

要确定你想要自动下载的内容类型，你可使用 [curl](http://curl.haxx.se/):

```
curl -I URL | grep "Content-Type"
```

找到内容类型的另一种方法是使用 [`](https://selenium-python-zh.readthedocs.io/en/latest/faq.html#id4)requests <[http://python-requests.org](http://python-requests.org/)>` 模块， 你可以像这样使用:

```python
import requests
content_type = requests.head('http://www.python.org').headers['content-type']
print(content_type)
```

一旦内容类型被确认，你可以用它来设置 firefox 配置文件的偏好: `browser.helperApps.neverAsk.saveToDisk` 下面是一个例子:

```python
import os

from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()
```

在上面的例子中，`application/octet-stream` 被当作内容类型。

该 `browser.download.dir` 选项指定了你要下载文件的目录。

## 8.5. 如果上传文件到文件上传控件？

选择 `<input type="file">` 元素并且调用 `send_keys()` 方法传入要上传文件的路径，可以 是对于测试脚本的相对路径，也可以是绝对路径。 请牢记在 Windows 和 Unix 系统之间的路径名的区别。

## 8.6. 如果在 Firefox 中使用 firebug 工具？

首先下载 Firebug 插件的 XPI 文件， 然后调用对于 firefox 的配置提供的 `add_extension` 方法

```python
from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.add_extension(extension=’firebug-1.8.4.xpi’) 
#Avoid startup screen browser = webdriver.Firefox(firefox_profile=fp)
fp.set_preference(“extensions.firebug.currentVersion”, “1.8.4”) 
````

## 8.7. 如果获取当前窗口的截图？

使用 webdriver 提供的 save_screenshot 方法:

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()
```





