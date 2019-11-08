# PyQuery 

[TOC]

## 一、简介：

一款类似于 [jquery](https://tianshimanbu.com/tag/jquery/) 的 [python](https://tianshimanbu.com/tag/python/) 库

PyQuery 允许你像 JQuery 一样对快速对 [xml](https://tianshimanbu.com/tag/xml/)（[lxml](https://tianshimanbu.com/tag/lxml/)） [文档](https://tianshimanbu.com/tag/文档/)进行`元素查询`、`元素操作`的 [python](https://tianshimanbu.com/tag/python/) 库。如果你熟悉 JQuery 的 api，那么掌握 PyQuery 是一件十分容易的事情，因为 PyQuery 的 api 和 JQuery 的 api 基本上一致。PyQuery 是一款基于 [lxml](http://lxml.de/) 的库，而 [lxml](https://tianshimanbu.com/tag/lxml/) 能够快速处理 [xml](https://tianshimanbu.com/tag/xml/) 和 html [文档](https://tianshimanbu.com/tag/文档/)。

起初仅仅是因为我有个想法：想在 [python](https://tianshimanbu.com/tag/python/) 里面使用 [jquery](https://tianshimanbu.com/tag/jquery/) 类似 api 来操作 [xml](https://tianshimanbu.com/tag/xml/) [文档](https://tianshimanbu.com/tag/文档/)，所以 PyQuery 就诞生了。你要明白一点的是，PyQuery 库并不是用 JavaScript 来写的，正如上面所提到，这是一个 python 语言库，它基于 [lxml](https://tianshimanbu.com/tag/lxml/) 快速处理库。

PyQuery 可以用来做很多 xml 相关的事情，下面是我能想到的一些用途：

+  使用 PyQuery 对纯 HTTP 模板（html）进行修改。
+  移除废弃或者不需要的 web 元素。
+  提取程序的主题元素。

PyQuery 被放置在了 [github](https://github.com/gawel/pyquery/) 上，该项目被我设置了一些提交策略和代码审查策略，也就是被允许的人才能够提交和审查代码，如果你想提交你的修改，那么请给我邮件。

另外，请把 [bug](https://tianshimanbu.com/tag/bug/) 提交到 [git](https://tianshimanbu.com/tag/git/)hub 上的 [issue](https://github.com/gawel/pyquery/issues) 面板上。

## 二、快速入门

### 1. 使用 PyQuery 之前应该使用 [pip](https://tianshimanbu.com/tag/pip/) 或者别的工具进行安装：

```python
pip install pyquery
```

一般会自动帮你把依赖库安装上，如 lxml 库。

### 2. 使用 PyQuery 快速加载 xml 文档，加载源可以是以下几个情形：

+  字符串
+  xml 文档
+  文件路径
+  url 链接

代码示例（python 终端）：

```python
>>> from pyquery import PyQuery as pq
>>> from lxml import etree #引入依赖库
>>> import urllib #引入依赖库
>>> d = pq("<html></html>")
>>> d = pq(etree.fromstring("<html></html>"))  #字符串
>>> d = pq(url='http://google.com/')  #url路径
>>> # d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read()) #读流
>>> d = pq(filename=path_to_html_file)  #文件夹
```

加载以后得到变量 `d`, 该变量如 [jquery](https://tianshimanbu.com/tag/jquery/) 里面的 $ 操作符一样，可以对元素进行操作：

```python
>>> d("#hello")  #ID选择器，选择id=hello的元素
[<p#hello.hello>] #打印ID为hello的元素（PyQuery对象）
>>> p = d("#hello")
>>> print(p.html()) #打印p元素
Hello world !
>>> p.html("you know <a href='http://python.org/'>Python</a> rocks") #赋值html内容，相当于innerHtml=xx
[<p#hello.hello>]
>>> print(p.html()) 
you know <a href="http://python.org/">Python</a> rocks
>>> print(p.text()) #提取p标签内的text，不含html标签。
you know Python rocks
```

除此以外，你还可以使用非 c[ss](https://tianshimanbu.com/tag/ss/) 标准的 :first :last :even :odd :eq :lt :gt :checked :selected :file 伪符号来对元素进行定位，如：

```python
>>> d('p:first')
[<p#hello.hello>]
```

更多快速入门请阅读：[PyQuery 快速入门 - 十分钟搞定 PyQuery](http://www.jianshu.com/p/c07f7cd1b548)

### 三、选择器语法

和 JQuery 一样，PyQuery 同样提供了丰富的选择器语法，满足你提取一个或者多个元素。

建立 html 文档并且命名为:`demo.html`

```python
<div>
<tr class="item-0">
<td>first section</td>
<td>第一项</td>
<td>备注</td>
</tr>
<tr class="item-1">
<td>second section</td>
<td>第二项</td>
<td>备注</td>
</tr>
</div>
```

PyQuery 各种选择器语法示例：

```python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq#引入 PyQuery

doc = pq(filename='demo.html')# 传入文件 demo.html

print doc.html() # html()方法获取当前选中的 html 块

print doc('.item-1') # 相当于 class 选择器，选取 class 为 item-1 的 html 块

data = doc('tr') # 选取 <tr> 元素

for tr in data.items():# 遍历 data 中的 <tr> 元素
temp = tr('td').eq(2).text() # 选取第3个 <td> 元素中的文本块
print temp
```


## 四、操作 html 的属性

**操作属性是 PyQuery 比较有魅力的功能，用于清洗网页数据。**

使用类似于 JQuery api 对 html 属性进行操作，实例：

```python
>>> p = pq('<p id="hello" class="hello"></p>')('p')
>>> p.attr("id") #打印p的ID值
'hello'
>>> p.attr("id", "plop") #给p元素的ID重新赋值，赋值后结果为plop
[<p#plop.hello>]
>>> p.attr("id", "hello") 
[<p#hello.hello>]
```

使用更 Python 的语法进行操作，实例：

```python
>>> p.attr.id = "plop"
>>> p.attr.id
'plop'
>>> p.attr["id"] = "ola"
>>> p.attr["id"]
'ola'
>>> p.attr(id='hello', class_='hello2')
[<p#hello.hello2>]
>>> p.attr.class_
'hello2'
>>> p.attr.class_ = 'hello'
```

## 五、操作 CSS

你可以对 html 元素的 c[ss](https://tianshimanbu.com/tag/ss/) 进行操作：

```python
>>> p.addClass("toto") # 添加css
[<p#hello.hello.toto>]
>>> p.toggleClass("titi toto")
[<p#hello.hello.titi>]
>>> p.removeClass("titi") # 移除css
[<p#hello.hello>]
```

添加内联 style 的 c[ss](https://tianshimanbu.com/tag/ss/) 样式：

```python
>>> p.css("font-size", "15px")
[<p#hello.hello>]
>>> p.attr("style")
'font-size: 15px'
>>> p.css({"font-size": "17px"})
[<p#hello.hello>]
>>> p.attr("style")
'font-size: 17px'
```

使用 Python 语法进行编写 (只需要将 - 变成下划线_, 如 font-size 对应名字为 font_size)：

```python
>>> p.css.font_size = "16px" #font_size 对应css的font-size
>>> p.attr.style
'font-size: 16px'
>>> p.css['font-size'] = "15px"
>>> p.attr.style
'font-size: 15px'
>>> p.css(font_size="16px")
[<p#hello.hello>]
>>> p.attr.style
'font-size: 16px'
>>> p.css = {"font-size": "17px"}
>>> p.attr.style
'font-size: 17px'
```

## 六、Manipulating（操作）API

+  append 函数：在元素末尾（元素内部的内容末尾）追加内容，添加的内容仍然在该元素内

```python
>>> d = pq('<p class="hello" id="hello">you know Python rocks</p>')
>>> d('p').append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')  #使用append api追加
[<p#hello.hello>]
>>> print d
<p class="hello" id="hello">you know Python rocks check out <a href="http://reddit.com/r/python"><span>reddit</span></a></p>
```

+  prepend 函数：在元素前面添加内容，添加的内容仍然在该元素内

```python
>>> p = d('p')
>>> p.prepend('check out <a href="http://reddit.com/r/python">reddit</a>') #添加的内容
[<p#hello.hello>]
>>> print p  #查看p标签全部内容
<p class="hello" id="hello">check out <a href="http://reddit.com/r/python">reddit</a>you know Python rocks</p>
>>> p.html()
u'check out <a href="http://reddit.com/r/python">reddit</a>you know Python rocks'
```

+  prependTo 函数：在前面或者末尾添加内容

```python
>>> d = pq('<html><body><div id="test"><a href="http://python.org">python</a> !</div></body></html>')
>>> p.prependTo(d('#test'))
[<p#hello.hello>]
>>> d('#test').html()
u'<p class="hello" id="hello">check out <a href="http://reddit.com/r/python">reddit</a>you know Python rocks</p><a href="http://python.org">python</a> !'
```

这一段逻辑没有那么直观，解释下：

+  初始化一个 d 变量，内容为：`<html><body><div id="test"><a href="http://python.org">python</a> !</div></body></html>`
+  把 p 元素`添加到` (prependTo) d ('#test') 的前面，d ('#test') 的内容为：`<div id="test"><a href="http://python.org">python</a> !</div>`，那么就相当于在 a 标签前面加东西。
+  最后打印 d ('#test') 中的 html 内容：可以看到 a 标签之前多了 p 的内容。

同样的 append 对 p 进行操作：p.append (d ('#test'))，那么得到的结果：

```python
>>> print p
<p class="hello" id="hello">check out <a href="http://reddit.com/r/python">reddit</a>you know Python rocks<div id="test"><a href="http://python.org">python</a> !</div></p>
```

相反的 API 还有 insertBefore 和 insertAfter。

+  remove 函数：移除符合条件的元素

```python
>>> d = pq('<html><body><p id="id">Yeah!</p><p>python rocks !</p></div></html>')
>>> d.remove('p#id') # 移除id=id的p，整个元素都移除，移除后后打印html
[<html>]
>>> d('p#id') # 打印
[]
```

+  empty 函数：置空元素内的 html

```python
>>> d('p').empty() # 置空操作，置空后没有html内容
[<p>]
```

## 七、条件过滤

一些 JQuery 过滤方法同样适用于 PyQuery，下面是几个 API 例子：

+  filter 函数：过滤符合条件（class 或者 id 等）的元素

```python
>>> d = pq('<p id="hello" class="hello"><a/></p><p id="test"><a/></p>')
>>> d('p').filter('.hello') # 提取class=hello的p标签元素
[<p#hello.hello>]
```

+  eq 函数：筛选序号等于 x 的元素

```python
>>> d('p').eq(0)
[<p#hello.hello>]
```

+  find 函数：筛选 x 标签的元素，返回 list 列表

```python
>>> d('p').find('a') # 筛选a标签的元素，返回所有的a元素
[<a>, <a>]
>>> d('p').eq(1).find('a') # 筛选第二个p元素中的所有a元素
[<a>]
```

+  end 函数同样适用于链式筛选

```python
>>> d('p').find('a').end()
[<p#hello.hello>, <p#test>]
>>> d('p').eq(0).end()
[<p#hello.hello>, <p#test>]
>>> d('p').filter(lambda i: i == 1).end()
[<p#hello.hello>, <p#test>]
```

## 八、其它常用 API

`.hasClass(name)` 判断是否包含指定的 class，返回 True 或 False；

`.add()` 将元素添加到匹配元素的集合中。 

`.andSelf()` 把堆栈中之前的元素集添加到当前集合中。 

`.children()` 获得匹配元素集合中每个元素的所有子元素。 

`.closest()` 从元素本身开始，逐级向上级元素匹配，并返回最先匹配的祖先元素。 

`.contents()`  获得匹配元素集合中每个元素的子元素，包括文本和注释节点。 
　
`.each()`  对 jQuery 对象进行迭代，为每个匹配元素执行函数。 
　
`.end()`  结束当前链中最近的一次筛选操作，并将匹配元素集合返回到前一次的状态。 

`.eq()`  将匹配元素集合缩减为位于指定索引的新元素。 
　
`.filter()`  将匹配元素集合缩减为匹配选择器或匹配函数返回值的新元素。 

`.find()`  获得当前匹配元素集合中每个元素的后代，由选择器进行筛选。 

`.first()`  将匹配元素集合缩减为集合中的第一个元素。 

`.has()`  将匹配元素集合缩减为包含特定元素的后代的集合。 

`.is()`  根据选择器检查当前匹配元素集合，如果存在至少一个匹配元素，则返回 true。 

`.last()`  将匹配元素集合缩减为集合中的最后一个元素。 

`.map()`   把当前匹配集合中的每个元素传递给函数，产生包含返回值的新 jQuery 对象。 

`.next()`  获得匹配元素集合中每个元素紧邻的同辈元素。 

`.nextAll()`  获得匹配元素集合中每个元素之后的所有同辈元素，由选择器进行筛选（可选）。 

`.nextUntil()`  获得每个元素之后所有的同辈元素，直到遇到匹配选择器的元素为止。 

`.not()`  从匹配元素集合中删除元素。 

`.offsetParent()`  获得用于定位的第一个父元素。 

`.parent()`  获得当前匹配元素集合中每个元素的父元素，由选择器筛选（可选）。 
　
`.parents()`  获得当前匹配元素集合中每个元素的祖先元素，由选择器筛选（可选）。 

`.parentsUntil()`  获得当前匹配元素集合中每个元素的祖先元素，直到遇到匹配选择器的元素为止。 

`.prev()`  获得匹配元素集合中每个元素紧邻的前一个同辈元素，由选择器筛选（可选）。 

`.prevAll()` 获得匹配元素集合中每个元素之前的所有同辈元素，由选择器进行筛选（可选）。 

`.prevUntil()`  获得每个元素之前所有的同辈元素，直到遇到匹配选择器的元素为止。 

`.siblings()`  获得匹配元素集合中所有元素的同辈元素，由选择器筛选（可选）。 

`.slice()`  将匹配元素集合缩减为指定范围的子集。