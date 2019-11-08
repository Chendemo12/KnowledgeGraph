# Pandas速查手册

## 关键缩写和包导入

在这个速查手册中，我们使用如下缩写：

df：任意的 Pandas DataFrame 对象

同时我们需要做如下的引入：

import pandas as pd

## 导入数据

+  pd.read_csv (filename)：从 CSV 文件导入数据
+  pd.read_table (filename)：从限定分隔符的文本文件导入数据
+  pd.read_excel (filename)：从 Excel 文件导入数据
+  pd.read_sql (query, connection_object)：从 SQL 表 / 库导入数据
+  pd.read_json (json_string)：从 JSON 格式的字符串导入数据
+  pd.read_html (url)：解析 URL、字符串或者 HTML 文件，抽取其中的 tables 表格
+  pd.read_clipboard ()：从你的粘贴板获取内容，并传给 read_table ()
+  pd.DataFrame (dict)：从字典对象导入数据，Key 是列名，Value 是数据

## 导出数据

+  df.to_csv (filename)：导出数据到 CSV 文件
+  df.to_excel (filename)：导出数据到 Excel 文件
+  df.to_sql (table_name, connection_object)：导出数据到 SQL 表
+  df.to_json (filename)：以 Json 格式导出数据到文本文件

## 创建测试对象

+  pd.DataFrame (np.random.rand (20,5))：创建 20 行 5 列的随机数组成的 DataFrame 对象
+  pd.Series (my_list)：从可迭代对象 my_list 创建一个 Series 对象
+  df.index = pd.date_range ('1900/1/30', periods=df.shape [0])：增加一个日期索引

## 查看、检查数据

+  df.head (n)：查看 DataFrame 对象的前 n 行
+  df.tail (n)：查看 DataFrame 对象的最后 n 行
+  df.shape ()：查看行数和列数
+  [http:// df.info()](https://link.zhihu.com/?target=http%3A//df.info())：查看索引、数据类型和内存信息
+  df.describe ()：查看数值型列的汇总统计
+  s.value_counts (dropna=False)：查看 Series 对象的唯一值和计数
+  df.apply (pd.Series.value_counts)：查看 DataFrame 对象中每一列的唯一值和计数

## 数据选取

+  df [col]：根据列名，并以 Series 的形式返回列
+  df [[col1, col2]]：以 DataFrame 形式返回多列
+  s.iloc [0]：按位置选取数据
+  s.loc ['index_one']：按索引选取数据
+  df.iloc [0,:]：返回第一行
+  df.iloc [0,0]：返回第一列的第一个元素

## 数据清理

+  df.columns = ['a','b','c']：重命名列名
+  pd.isnull ()：检查 DataFrame 对象中的空值，并返回一个 Boolean 数组
+  pd.notnull ()：检查 DataFrame 对象中的非空值，并返回一个 Boolean 数组
+  df.dropna ()：删除所有包含空值的行
+  df.dropna (axis=1)：删除所有包含空值的列
+  df.dropna (axis=1,thresh=n)：删除所有小于 n 个非空值的行
+  df.fillna (x)：用 x 替换 DataFrame 对象中所有的空值
+  s.astype (float)：将 Series 中的数据类型更改为 float 类型
+  s.replace (1,'one')：用‘one’代替所有等于 1 的值
+  s.replace ([1,3],['one','three'])：用 'one' 代替 1，用 'three' 代替 3
+  df.rename (columns=lambda x: x + 1)：批量更改列名
+  df.rename (columns={'old_name': 'new_ name'})：选择性更改列名
+  df.set_index ('column_one')：更改索引列
+  df.rename (index=lambda x: x + 1)：批量重命名索引

## 数据处理：Filter、Sort 和 GroupBy

+  df [df [col] > 0.5]：选择 col 列的值大于 0.5 的行
+  df.sort_values (col1)：按照列 col1 排序数据，默认升序排列
+  df.sort_values (col2, ascending=False)：按照列 col1 降序排列数据
+  df.sort_values ([col1,col2], ascending=[True,False])：先按列 col1 升序排列，后按 col2 降序排列数据
+  df.groupby (col)：返回一个按列 col 进行分组的 Groupby 对象
+  df.groupby ([col1,col2])：返回一个按多列进行分组的 Groupby 对象
+  df.groupby (col1)[col2]：返回按列 col1 进行分组后，列 col2 的均值
+  df.pivot_table (index=col1, values=[col2,col3], aggfunc=max)：创建一个按列 col1 进行分组，并计算 col2 和 col3 的最大值的数据透视表
+  df.groupby (col1).agg (np.mean)：返回按列 col1 分组的所有列的均值
+  data.apply (np.mean)：对 DataFrame 中的每一列应用函数 np.mean
+  data.apply (np.max,axis=1)：对 DataFrame 中的每一行应用函数 np.max

## 数据合并

+  df1.append (df2)：将 df2 中的行添加到 df1 的尾部
+  df.concat ([df1, df2],axis=1)：将 df2 中的列添加到 df1 的尾部
+  df1.join (df2,on=col1,how='inner')：对 df1 的列和 df2 的列执行 SQL 形式的 join

## 数据统计

+  df.describe ()：查看数据值列的汇总统计
+  df.mean ()：返回所有列的均值
+  df.corr ()：返回列与列之间的相关系数
+  df.count ()：返回每一列中的非空值的个数
+  df.max ()：返回每一列的最大值
+  df.min ()：返回每一列的最小值
+  df.median ()：返回每一列的中位数
+  df.std ()：返回每一列的标准差





#  Pandas 十分钟入门教程（中文翻译）


导入 pandas、numpy、matplotlib

```
In [1]: import pandas as pd

In [2]: import numpy as np

In [3]: import matplotlib.pyplot as plt
```



## 创造对象

Series 是一个值的序列，它只有一个列，以及索引。下面的例子中，就用默认的整数索引

```
In [4]: s = pd.Series([1,3,5,np.nan,6,8])

In [5]: s
Out[5]: 
0     1
1     3
2     5
3   NaN
4     6
5     8
dtype: float64
```

DataFrame 是有多个列的数据表，每个列拥有一个 label，当然，DataFrame 也有索引

```
In [6]: dates = pd.date_range('20130101', periods=6)

In [7]: dates
Out[7]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [8]: df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

In [9]: df
Out[9]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

如果参数是一个 dict，每个 dict 的 value 会被转化成一个 Series

```
In [10]: df2 = pd.DataFrame({ 'A' : 1.,
   ....:                      'B' : pd.Timestamp('20130102'),
   ....:                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
   ....:                      'D' : np.array([3] * 4,dtype='int32'),
   ....:                      'E' : pd.Categorical(["test","train","test","train"]),
   ....:                      'F' : 'foo' })
   ....: 

In [11]: df2
Out[11]: 
   A          B  C  D      E    F
0  1 2013-01-02  1  3   test  foo
1  1 2013-01-02  1  3  train  foo
2  1 2013-01-02  1  3   test  foo
3  1 2013-01-02  1  3  train  foo
```

每列的格式用 dtypes 查看

```
In [12]: df2.dtypes
Out[12]: 
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

你可以认为，DataFrame 是由 Series 组成的

```
In [13]: df2.A
Out[13]: 
0    1
1    1
2    1
3    1
Name: A, dtype: float64
```

## 查看数据

用 head 和 tail 查看顶端和底端的几列

```
In [14]: df.head()
Out[14]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401

In [15]: df.tail(3)
Out[15]: 
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

实际上，DataFrame 内部用 numpy 格式存储数据。你也可以单独查看 index 和 columns

```
In [16]: df.index
Out[16]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [17]: df.columns
Out[17]: Index(['A', 'B', 'C', 'D'], dtype='object')

In [18]: df.values
Out[18]: 
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
```

`describe()` 显示数据的概要。

```
In [19]: df.describe()
Out[19]: 
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
```

和 numpy 一样，可以方便的得到转置

```
In [20]: df.T
Out[20]: 
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

对 axis 按照 index 排序（`axis=1` 是指第二个维度，即：列）

```
In [21]: df.sort_index(axis=1, ascending=False)
Out[21]: 
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

按值排序

```
In [22]: df.sort_values(by='B')
Out[22]: 
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```

## 选择

>  注意，以下这些对交互式环境很友好，但是作为 production code 请用优化过的 `.at`, `.iat`, `.loc`, `.iloc` 和 `.ix`

## 获取行 / 列

从 DataFrame 选择一个列，就得到了 Series

```
In [23]: df['A']
Out[23]: 
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
```

和 numpy 类似，这里也能用 `[]`

```
In [24]: df[0:3]
Out[24]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

In [25]: df['20130102':'20130104']
Out[25]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

### 通过 label 选择

刚刚那个 DataFrame 可以通过时间戳的下标（`dates[0] = Timestamp('20130101')`）来访问

```
In [26]: df.loc[dates[0]]
Out[26]: 
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
```

还可以多选

```
In [27]: df.loc[:,['A','B']]
Out[27]: 
                   A         B
2013-01-01  0.469112 -0.282863
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
2013-01-06 -0.673690  0.113648
```

注意那个冒号，用法和 MATLAB 或 NumPy 是一样的！所以也可以这样

```
In [28]: df.loc['20130102':'20130104',['A','B']]
Out[28]: 
                   A         B
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
```

依旧和 MATLAB 一样，当有一个维度是标量（而不是范围或序列）的时候，选择出的矩阵维度会减少

```
In [29]: df.loc['20130102',['A','B']]
Out[29]: 
A    1.212112
B   -0.173215
Name: 2013-01-02 00:00:00, dtype: float64
```

如果对所有的维度都写了标量，不就是选出一个元素吗？

```
In [30]: df.loc[dates[0],'A']
Out[30]: 0.46911229990718628
```

这种情况通常用 `at` ，速度更快

```
In [31]: df.at[dates[0],'A']
Out[31]: 0.46911229990718628
```

### 通过整数下标选择

>  和 MATLAB 完全一样

这个就和数组类似啦，直接看例子。选出第 3 行：

```
In [32]: df.iloc[3]
Out[32]: 
A    0.721555
B   -0.706771
C   -1.039575
D    0.271860
Name: 2013-01-04 00:00:00, dtype: float64
```

选出 34 行，01 列：

```
In [33]: df.iloc[3:5,0:2]
Out[33]: 
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
```

也能用 list 选择

```
In [34]: df.iloc[[1,2,4],[0,2]]
Out[34]: 
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
```

也能用 slice

```
In [35]: df.iloc[1:3,:]
Out[35]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
In [36]: df.iloc[:,1:3]
Out[36]: 
                   B         C
2013-01-01 -0.282863 -1.509059
2013-01-02 -0.173215  0.119209
2013-01-03 -2.104569 -0.494929
2013-01-04 -0.706771 -1.039575
2013-01-05  0.567020  0.276232
2013-01-06  0.113648 -1.478427
```

对应单个元素

```
In [37]: df.iloc[1,1]
Out[37]: -0.17321464905330858
In [38]: df.iat[1,1]
Out[38]: -0.17321464905330858
```

### 布尔值下标

>  和 MATLAB 类似

基本用法

```
In [39]: df[df.A > 0]
Out[39]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

没有填充的值等于 NaN

```
In [40]: df[df > 0]
Out[40]: 
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```

`isin()` 函数：是否在集合中

```
In [41]: df2 = df.copy()

In [42]: df2['E'] = ['one', 'one','two','three','four','three']

In [43]: df2
Out[43]: 
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three

In [44]: df2[df2['E'].isin(['two','four'])]
Out[44]: 
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
```

### Setting

为 DataFrame 增加新的列，按 index 对应

```
In [45]: s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))

In [46]: s1
Out[46]: 
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64

In [47]: df['F'] = s1
```

通过 label 设置

```
In [48]: df.at[dates[0],'A'] = 0
```

通过下标设置

```
In [49]: df.iat[0,1] = 0
```

用 numpy 数组设置

```
df.loc[:,'D'] = np.array([5] * len(df))
```

用布尔值作下标的 set

```
In [53]: df2[df2 > 0] = -df2
```

## 缺失值

pandas 用 `np.nan` 表示缺失值。通常它不会被计算。

Reindexing 允许你改变某个轴的 index（以下代码制造一个示例用的 DataFrame）

```
In [55]: df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

In [56]: df1.loc[dates[0]:dates[1],'E'] = 1

In [57]: df1
Out[57]: 
                   A         B         C  D   F   E
2013-01-01  0.000000  0.000000 -1.509059  5 NaN   1
2013-01-02  1.212112 -0.173215  0.119209  5   1   1
2013-01-03 -0.861849 -2.104569 -0.494929  5   2 NaN
2013-01-04  0.721555 -0.706771 -1.039575  5   3 NaN
```

丢弃有 NaN 的行

```
In [58]: df1.dropna()
Out[58]: 
                   A         B         C  D  F  E
2013-01-02  1.212112 -0.173215  0.119209  5  1  1
```

填充缺失值

```
In [59]: df1.fillna(value=5)
Out[59]: 
                   A         B         C  D  F  E
2013-01-01  0.000000  0.000000 -1.509059  5  5  1
2013-01-02  1.212112 -0.173215  0.119209  5  1  1
2013-01-03 -0.861849 -2.104569 -0.494929  5  2  5
2013-01-04  0.721555 -0.706771 -1.039575  5  3  5
```

获取布尔值的 mask：哪些值是 NaN

```
In [60]: pd.isnull(df1)
Out[60]: 
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```

## 操作

### 统计

>  通常，操作都会把 NaN 排除在外

平均值

```
In [61]: df.mean()
Out[61]: 
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
```

对另一个维度做平均值，只要加个参数

```
In [62]: df.mean(1)
Out[62]: 
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
```

### Apply

对数据（行或列） Apply 函数

```
In [66]: df.apply(np.cumsum)
Out[66]: 
                   A         B         C   D   F
2013-01-01  0.000000  0.000000 -1.509059   5 NaN
2013-01-02  1.212112 -0.173215 -1.389850  10   1
2013-01-03  0.350263 -2.277784 -1.884779  15   3
2013-01-04  1.071818 -2.984555 -2.924354  20   6
2013-01-05  0.646846 -2.417535 -2.648122  25  10
2013-01-06 -0.026844 -2.303886 -4.126549  30  15

In [67]: df.apply(lambda x: x.max() - x.min())
Out[67]: 
A    2.073961
B    2.671590
C    1.785291
D    0.000000
F    4.000000
dtype: float64
```

### 直方图

```
In [68]: s = pd.Series(np.random.randint(0, 7, size=10))

In [69]: s
Out[69]: 
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int32

In [70]: s.value_counts()
Out[70]: 
4    5
6    2
2    2
1    1
dtype: int64
```

### 字符串函数

Series 自带了很多字符串处理函数，在 `str` 属性中，下面是一个例子

```
In [71]: s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

In [72]: s.str.lower()
Out[72]: 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```

## Merge

### Concat

简单地按行拼接

```
In [73]: df = pd.DataFrame(np.random.randn(10, 4))

In [74]: df
Out[74]: 
          0         1         2         3
0 -0.582002  0.066403  0.917236 -0.214155
1  2.063923  1.930796  0.139574  0.449368
2 -1.348962  0.228120  0.323906  1.280778
3  0.689536 -0.083717  1.436075  0.663250
4 -1.895829 -0.726235 -0.770739  0.192482
5  0.302074  0.228735  1.390550  0.196159
6  0.672059 -1.576747  0.154820  1.218892
7  2.378061  0.280385  1.055607 -0.469225
8 -0.997102 -0.533977  0.311215  0.940570
9 -1.381892 -1.450002  0.562337 -1.195926

# break it into pieces
In [75]: pieces = [df[3:7], df[:3], df[7:]]

In [76]: pd.concat(pieces)
Out[76]: 
          0         1         2         3
3  0.689536 -0.083717  1.436075  0.663250
4 -1.895829 -0.726235 -0.770739  0.192482
5  0.302074  0.228735  1.390550  0.196159
6  0.672059 -1.576747  0.154820  1.218892
0 -0.582002  0.066403  0.917236 -0.214155
1  2.063923  1.930796  0.139574  0.449368
2 -1.348962  0.228120  0.323906  1.280778
7  2.378061  0.280385  1.055607 -0.469225
8 -0.997102 -0.533977  0.311215  0.940570
9 -1.381892 -1.450002  0.562337 -1.195926
```

### Join

和 SQL 的 join 是一个意思

```
In [77]: left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

In [78]: right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

In [79]: left
Out[79]: 
   key  lval
0  foo     1
1  foo     2

In [80]: right
Out[80]: 
   key  rval
0  foo     4
1  foo     5

In [81]: pd.merge(left, right, on='key')
Out[81]: 
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```

### Append

向 DataFrame 增加新的数据行

```
In [82]: df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])

In [83]: df
Out[83]: 
          A         B         C         D
0  1.346061  1.511763  1.627081 -0.990582
1 -0.441652  1.211526  0.268520  0.024580
2 -1.577585  0.396823 -0.105381 -0.532532
3  1.453749  1.208843 -0.080952 -0.264610
4 -0.727965 -0.589346  0.339969 -0.693205
5 -0.339355  0.593616  0.884345  1.591431
6  0.141809  0.220390  0.435589  0.192451
7 -0.096701  0.803351  1.715071 -0.708758

In [84]: s = df.iloc[3]

In [85]: df.append(s, ignore_index=True)
Out[85]: 
          A         B         C         D
0  1.346061  1.511763  1.627081 -0.990582
1 -0.441652  1.211526  0.268520  0.024580
2 -1.577585  0.396823 -0.105381 -0.532532
3  1.453749  1.208843 -0.080952 -0.264610
4 -0.727965 -0.589346  0.339969 -0.693205
5 -0.339355  0.593616  0.884345  1.591431
6  0.141809  0.220390  0.435589  0.192451
7 -0.096701  0.803351  1.715071 -0.708758
8  1.453749  1.208843 -0.080952 -0.264610
```

## Grouping

和 SQL 中的 `GROUP BY` 类似，包括以下这几步：

+  根据某些规则，把数据**分组**
+  对每组应用一个聚集函数，把结果放在一个数据结构中

准备一下测试用的数据集

```
In [86]: df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
   ....:                           'foo', 'bar', 'foo', 'foo'],
   ....:                    'B' : ['one', 'one', 'two', 'three',
   ....:                           'two', 'two', 'one', 'three'],
   ....:                    'C' : np.random.randn(8),
   ....:                    'D' : np.random.randn(8)})
   ....: 

In [87]: df
Out[87]: 
     A      B         C         D
0  foo    one -1.202872 -0.055224
1  bar    one -1.814470  2.395985
2  foo    two  1.018601  1.552825
3  bar  three -0.595447  0.166599
4  foo    two  1.395433  0.047609
5  bar    two -0.392670 -0.136473
6  foo    one  0.007207 -0.561757
7  foo  three  1.928123 -1.623033
```

做 Group 操作并对每组求和

```
In [88]: df.groupby('A').sum()
Out[88]: 
            C        D
A                     
bar -2.802588  2.42611
foo  3.146492 -0.63958
```

可以对两列进行 Group by 并求和

```
In [89]: df.groupby(['A','B']).sum()
Out[89]: 
                  C         D
A   B                        
bar one   -1.814470  2.395985
    three -0.595447  0.166599
    two   -0.392670 -0.136473
foo one   -1.195665 -0.616981
    three  1.928123 -1.623033
    two    2.414034  1.600434
```

## Reshape

### Stack 层叠

准备一下数据

```
In [90]: tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
   ....:                      'foo', 'foo', 'qux', 'qux'],
   ....:                     ['one', 'two', 'one', 'two',
   ....:                      'one', 'two', 'one', 'two']]))
   ....: 

In [91]: index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

In [92]: df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

In [93]: df2 = df[:4]

In [94]: df2
Out[94]: 
                     A         B
first second                    
bar   one     0.029399 -0.542108
      two     0.282696 -0.087302
baz   one    -1.575170  1.771208
      two     0.816482  1.100230
```

`stack()` 把 DataFrame 的列 “压缩” 到 index 里去

```
In [95]: stacked = df2.stack()

In [96]: stacked
Out[96]: 
first  second   
bar    one     A    0.029399
               B   -0.542108
       two     A    0.282696
               B   -0.087302
baz    one     A   -1.575170
               B    1.771208
       two     A    0.816482
               B    1.100230
dtype: float64
```

反之，只要是 `MultiIndex` 都可以用 `unstack()` 恢复出列，默认把最后一个 index 解开

```
In [97]: stacked.unstack()
Out[97]: 
                     A         B
first second                    
bar   one     0.029399 -0.542108
      two     0.282696 -0.087302
baz   one    -1.575170  1.771208
      two     0.816482  1.100230

In [98]: stacked.unstack(1)
Out[98]: 
second        one       two
first                      
bar   A  0.029399  0.282696
      B -0.542108 -0.087302
baz   A -1.575170  0.816482
      B  1.771208  1.100230

In [99]: stacked.unstack(0)
Out[99]: 
first          bar       baz
second                      
one    A  0.029399 -1.575170
       B -0.542108  1.771208
two    A  0.282696  0.816482
       B -0.087302  1.100230
```

### Pivot Table 旋转

准备一下数据

```
In [100]: df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
   .....:                    'B' : ['A', 'B', 'C'] * 4,
   .....:                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
   .....:                    'D' : np.random.randn(12),
   .....:                    'E' : np.random.randn(12)})
   .....: 

In [101]: df
Out[101]: 
        A  B    C         D         E
0     one  A  foo  1.418757 -0.179666
1     one  B  foo -1.879024  1.291836
2     two  C  foo  0.536826 -0.009614
3   three  A  bar  1.006160  0.392149
4     one  B  bar -0.029716  0.264599
5     one  C  bar -1.146178 -0.057409
6     two  A  foo  0.100900 -1.425638
7   three  B  foo -1.035018  1.024098
8     one  C  foo  0.314665 -0.106062
9     one  A  bar -0.773723  1.824375
10    two  B  bar -1.170653  0.595974
11  three  C  bar  0.648740  1.167115
```

pivot 是把原来的数据 (values) 作为新表的行 (index)、列 (columns)

```
In [102]: pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
Out[102]: 
C             bar       foo
A     B                    
one   A -0.773723  1.418757
      B -0.029716 -1.879024
      C -1.146178  0.314665
three A  1.006160       NaN
      B       NaN -1.035018
      C  0.648740       NaN
two   A       NaN  0.100900
      B -1.170653       NaN
      C       NaN  0.536826
```

## 时间序列

pandas 的时间序列功能在金融应用中很有用。

resample 功能：

```
In [103]: rng = pd.date_range('1/1/2012', periods=100, freq='S')

In [104]: ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

In [105]: ts.resample('T', how='sum')
Out[105]: 
2012-01-01 00:00:00    14833
2012-01-01 00:01:00     9246
Freq: T, dtype: int32
```

时区表示

```
In [106]: rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')

In [107]: ts = pd.Series(np.random.randn(len(rng)), rng)

In [108]: ts
Out[108]: 
2012-03-06    0.464000
2012-03-07    0.227371
2012-03-08   -0.496922
2012-03-09    0.306389
2012-03-10   -2.290613
Freq: D, dtype: float64

In [109]: ts_utc = ts.tz_localize('UTC')

In [110]: ts_utc
Out[110]: 
2012-03-06 00:00:00+00:00    0.464000
2012-03-07 00:00:00+00:00    0.227371
2012-03-08 00:00:00+00:00   -0.496922
2012-03-09 00:00:00+00:00    0.306389
2012-03-10 00:00:00+00:00   -2.290613
Freq: D, dtype: float64
```

时区的转换：

```
In [111]: ts_utc.tz_convert('US/Eastern')
Out[111]: 
2012-03-05 19:00:00-05:00    0.464000
2012-03-06 19:00:00-05:00    0.227371
2012-03-07 19:00:00-05:00   -0.496922
2012-03-08 19:00:00-05:00    0.306389
2012-03-09 19:00:00-05:00   -2.290613
Freq: D, dtype: float64
```

从 Timestamp index 转换成 TimePeriod

```
In [112]: rng = pd.date_range('1/1/2012', periods=5, freq='M')

In [113]: ts = pd.Series(np.random.randn(len(rng)), index=rng)

In [114]: ts
Out[114]: 
2012-01-31   -1.134623
2012-02-29   -1.561819
2012-03-31   -0.260838
2012-04-30    0.281957
2012-05-31    1.523962
Freq: M, dtype: float64

In [115]: ps = ts.to_period()

In [116]: ps
Out[116]: 
2012-01   -1.134623
2012-02   -1.561819
2012-03   -0.260838
2012-04    0.281957
2012-05    1.523962
Freq: M, dtype: float64

In [117]: ps.to_timestamp()
Out[117]: 
2012-01-01   -1.134623
2012-02-01   -1.561819
2012-03-01   -0.260838
2012-04-01    0.281957
2012-05-01    1.523962
Freq: MS, dtype: float64
```

## 类别

```
In [122]: df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
```

把上述的文本类型的 raw_grade 转化成类别：

```
In [123]: df["grade"] = df["raw_grade"].astype("category")

In [124]: df["grade"]
Out[124]: 
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): [a, b, e]
```

类别可以 inplace 地赋值：（只是改一下对应的字符串嘛，类别是用 Index 对象存储的）

```
In [125]: df["grade"].cat.categories = ["very good", "good", "very bad"]
```

修改类别时，如果有新的类别，会自动加进去

```
In [126]: df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

In [127]: df["grade"]
Out[127]: 
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): [very bad, bad, medium, good, very good]
```

做 `group by` 的时候，空的类别也会被呈现出来

```
In [129]: df.groupby("grade").size()
Out[129]: 
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

![img](pictures/Pandas速查手册.assets/series_plot_basic.png)

对于 DataFrame，可以直接 plot

```
In [133]: df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
   .....:                   columns=['A', 'B', 'C', 'D'])
   .....: 

In [134]: df = df.cumsum()

In [135]: plt.figure(); df.plot(); plt.legend(loc='best')
Out[135]: <matplotlib.legend.Legend at 0xab53b26c>
```

![img](pictures/Pandas速查手册.assets/frame_plot_basic.png)

## 读取、写入数据

### CSV

写入

```
In [136]: df.to_csv('foo.csv')
```

读取

```
In [137]: pd.read_csv('foo.csv')
Out[137]: 
     Unnamed: 0          A          B         C          D
0    2000-01-01   0.266457  -0.399641 -0.219582   1.186860
1    2000-01-02  -1.170732  -0.345873  1.653061  -0.282953
2    2000-01-03  -1.734933   0.530468  2.060811  -0.515536
3    2000-01-04  -1.555121   1.452620  0.239859  -1.156896
4    2000-01-05   0.578117   0.511371  0.103552  -2.428202
5    2000-01-06   0.478344   0.449933 -0.741620  -1.962409
6    2000-01-07   1.235339  -0.091757 -1.543861  -1.084753
..          ...        ...        ...       ...        ...
993  2002-09-20 -10.628548  -9.153563 -7.883146  28.313940
994  2002-09-21 -10.390377  -8.727491 -6.399645  30.914107
995  2002-09-22  -8.985362  -8.485624 -4.669462  31.367740
996  2002-09-23  -9.558560  -8.781216 -4.499815  30.518439
997  2002-09-24  -9.902058  -9.340490 -4.386639  30.105593
998  2002-09-25 -10.216020  -9.480682 -3.933802  29.758560
999  2002-09-26 -11.856774 -10.671012 -3.216025  29.369368

[1000 rows x 5 columns]
```

### HDF5

```
In [138]: df.to_hdf('foo.h5','df')

In [139]: pd.read_hdf('foo.h5','df')
```

### Excel

```
In [140]: df.to_excel('foo.xlsx', sheet_name='Sheet1')

In [141]: pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
```

## 坑

```
>>> if pd.Series([False, True, False]):
    print("I was true")
Traceback
    ...
ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
```

如上，不能直接把返回值当作布尔值。


