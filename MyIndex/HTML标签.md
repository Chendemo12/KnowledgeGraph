##  1. HTML标签

```html
<img src="the full url or path of the pic" alt="description while the pic cannot find" />
<a >can only show on the same line.</a>

<!--区域标签，进行区域划分-->
<div id="container" align="center">
    <p>
        <!--所有内容都居中显示,align属性，设置对齐方式-->
    </p>
    <div id="content">
        <a>主要内容</a>
    </div>
</div>

<!--unorder list无序列表-->
<ul>
    <li>每一个标签项</li>
</ul>

<!--order list有序列表-->
<ol>
    <li>每一个标签项</li>
</ol>

<!--table表格-->
<table>
    <tr>
    	<th>table header</th>
        <th>table header</th>
    </tr>
    <tr> <!--lines-->
        <td>columns</td>
        <td>columns</td>
	</tr>
</table>

<!--Form表单,action表示该表单交由那个网页来处理-->
<form action="数据处理网页">
	<!--文本输入框-->
    <input type="text|password" value="text/password" name=""/>
    <!--提交按钮,value为显示在按钮上的文字-->
    <input type="submit" value="提交" name="submit" />
    <!--重置按钮-->
    <input type="reset" value="重置" mame="reset" />
    <!--单选框|复选框,value表示要提交到后端的数据,name表示当前项的名称：其中单选框的值要相同,checked="checked"表示默认选中-->
    <input type="radio|checkbox" value="值" name="名称" checked="checked" /> 
</form>

<!--select option下拉列表框-->
<select>
    <option>选项一</option>
    <!--属性selected="selected"表示被选择的那一项-->
    <option selected="selected">选项二</option> 
</select>

<!--Textarea文本域-->
<textarea rows="行数" clos="列数">显示在文本编辑域里的提示性文本</textarea>
```



## 2. Web语义化

+   让页面具有良好的结构和含义，

```html
<div id="header">
	<a>网页页眉</a>
</div>
<!--等同于如下写法-->
<header>网页页眉</header>

<p>
    <em>强调</em>
    <i>斜体,无语义</i>
    <strong>重点强调</strong>
    <b>粗体,无语义</b>
</p>

<!--自定义列表dl,列表项dt,描述dd,效果如右图-->
<dl>
    <dt>HTML</dt>				HTML
    <dd>超文本标记语言</dd>			超文本标记语言
    <dt>CSS</dt>				CSS
    <dd>层叠样式表</dd>				 层叠样式表
</dl>
```



## 3. CSS

+   网页的内容和样式相分离,便于修改样式.

### 3.1 CSS语法

```css
p{	/*选择器*/
    font-size:12px;	/*字号*/
    color:blue;		/*字体颜色*/
}
```

### 3.2 CSS添加方法

```html
<!--1.行内样式-->
<p style="color:red">CSS的添加方法一,内嵌样式</p>

<!--2.内嵌样式,由style标签标示,注意写在head标签内-->
<head>
    <style type="text/css">
        p{
            color:red;
        }
    </style>
</head>

<!--3.单独文件方法-->
<!--将CSS文件放在专属的'/CSS/'文件夹内-->
<head>
    <!--链接样式,写在head标签内-->
    <link rel="stylesheet" href="css/style.css"/>
</head>
```

+   多重样式可以层叠, 可以覆盖; 样式的优先级按照“就近原则”:行内样式>内嵌样式>链接样式>浏览器默认样式.

### 3.3 CSS选择器

+   标签选择器

```CSS
p{	/*作用于所有的P标签*/
    font-size:12px;	/*字号*/
    color:blue;		/*字体颜色*/
}
```

+   类别选择器

```CSS
<style type="text/css">
    p{font-size:12px;}
    .one{font-size:16px;}
    .two{font-size:22px;}
</style>
```

类别选择器以`.`开头, `{}`之内仍是属性的设置.

```html
<body>
    <p class="one">
        引用类别one
    </p>
    <p class="two">
        引用类别two
    </p>
</body>

<!--
类别选择器的引用方法:
	在对应的标签内利用`class`属性来进行样式表的引用, class的属性值为样式表引用类别的名称,不需要`.`
-->
```

+   ID选择器

```CSS
<style type="text/css">
    p{font-size:12px;}
    #one{font-size:16px;}
    #two{font-size:22px;}
</style>
```

ID选择器以`#`定义, `{}`之内是属性的设置.

```HTML
<body>
    <p id="one">
        引用类别one
    </p>
    <p id="two">
        引用类别two
    </p>
</body>

<!--
区别:
	ID选择器定义的样式具有唯一性,在该网页中,只能被引用一次, class类别选择器则可以多次引用.
-->
```

### 3.4 选择器的叠加用法

+   嵌套声明

```CSS
<style type="text/css">
    p span{
        color:red;
    }
</style>
/*特殊规定的样式用span标签定义*/
```

```HTML
<body>
    <p>
       <span>天使投资</span>是投资方式的一种.
    </p>
</body>
```

+   集体声明

```CSS
<style>
    h1,p{color:red;}
</style>
```

+   全局声明

```CSS
<style>
    *{color:red;}
</style>
```

+   混合引用

```HTML
<div class="one yello left">
    <a>多个class选择器混用时, 用空格将多个取值隔开</a>
</div>

<div id="my" class="one ,left">
    <a>id和class混合使用, ID类型不可以多次或多个ID选择器同时引用</a>
</div>
```



## 4. CSS样式

### 4.1 文本与文字样式

+   基础单位

| 单位 | 描述                                               |
| ---- | -------------------------------------------------- |
| px   | 像素                                               |
| em   | 字符<br/>1em:一个字符<br/>自动适应用户所使用的字体 |
| %    | 百分比                                             |

+   颜色

| 颜色            | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| red, blue,green | 颜色名                                                       |
| rgb(x,x,x)      | RGB值<br/>每个颜色值取值区间[0,255]<br>红色(255,0,0)<br>灰色(66,66,66) |
| rgb(x%,x%,x%)   | RGB百分比值,取值[0%,100%]<br>红色(100%,0%,0%)                |
| rgba(x,x,x,x)   | RGB,透明度[0.0,1.0] (完全透明,完全不透明)<br>红色半透明rgba(255,0,0,0.5) |
| #rrggbb         | 十六进制色值<br>红色:#ff00000<br>相邻两位重复,则可去掉重复位:<u>ff</u> –>f ;<u>00</u>–>0;<u>00</u>–>0 |

+   属性

| 属性            | 描述     | 取值                                 |
| --------------- | -------- | ------------------------------------ |
| color           | 文本描述 | rgb                                  |
| letter-spacing  | 字符间距 | 2px                                  |
| line-height     | 行高     | 12px,1.5em,120%                      |
| text-align      | 对齐方式 | center,left,right,justify            |
| text-decoration | 装饰线   | none,overline,underline,line-through |
| text-indent     | 首行缩进 | 2em(2字符)                           |

