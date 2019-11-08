# PyMySQL官方文档



------

> [TOC]

------



## 用户指南

PyMySQL用户指南解释了如何安装PyMySQL以及如何作为开发人员为库做贡献。



### 安装

最后一个稳定版本可在PyPI上使用，可以安装`pip`：

```python
$ python3 -m pip install PyMySQL
```

要使用“sha256_password”或“caching_sha2_password”进行身份验证，您需要安装其他依赖项：

```python
$ python3 -m pip install PyMySQL[rsa]
```

#### 要求

- Python - 以下之一：
  - [CPython](http://www.python.org/) > = 2.7或> = 3.5
  - 最新的[PyPy](http://pypy.org/)
- MySQL服务器 - 以下之一：
  - [MySQL](http://www.mysql.com/) > = 5.5
  - [MariaDB](https://mariadb.org/) > = 5.5



### 示例

#### CRUD 

以下示例使用简单表

```python
"""
CREATE TABLE users(
    id int(11) NOT NULL AUTO_INCREMENT,
    email varchar(255) COLLATE utf8_bin NOT NULL,
    password varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
	) 
	ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
	AUTO_INCREMENT=1 ;
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

这个例子将打印：

```python
{'password': 'very-secret', 'id': 1}
```





### 资源

DB-API 2.0：[http](http://www.python.org/dev/peps/pep-0249)：[//www.python.org/dev/peps/pep-0249](http://www.python.org/dev/peps/pep-0249)

MySQL参考手册：[http](http://dev.mysql.com/doc/)：[//dev.mysql.com/doc/](http://dev.mysql.com/doc/)

MySQL客户端/服务器协议：[http](http://dev.mysql.com/doc/internals/en/client-server-protocol.html)： [//dev.mysql.com/doc/internals/en/client-server-protocol.html](http://dev.mysql.com/doc/internals/en/client-server-protocol.html)

PyMySQL邮件列表：[https](https://groups.google.com/forum/#!forum/pymysql-users)：//groups.google.com/forum/#!forum/pymysql-users





### 开发

您可以通过[贡献GitHub](https://github.com/PyMySQL/PyMySQL)来帮助开发PyMySQL 。

#### 构建文档

转到`docs`目录并运行。`make html`

#### 测试套件

如果您想运行测试套件，请创建一个用于测试的数据库，如下所示：

```mysql
mysql -e 'create database test_pymysql  DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;'
mysql -e 'create database test_pymysql2 DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;'
```

然后，将文件复制`.travis/database.json`到`pymysql/tests/databases.json` 并编辑新文件以匹配您的MySQL配置：

```mysql
$ cp .travis/database.json pymysql/tests/databases.json
$ $EDITOR pymysql/tests/databases.json
```

要运行所有测试，请执行以下脚本`runtests.py`：

```python
$ python runtests.py
```

`tox.ini`还提供了一个文件，用于在多个Python版本上方便地运行测试：

```python
$ tox
```





## API参考

如果您正在寻找有关特定功能，类或方法的信息，本文档的这一部分适合您。

有关更多信息，请阅读[Python数据库API规范](https://www.python.org/dev/peps/pep-0249)。



### 连接对象

```python
class pymysql.connections.Connection(
    host=None,                                    
    user=None,                                     
    password='',                                     
    database=None,                                     
    port=0,                                     
    unix_socket=None,                                     
    charset='',                                     
    sql_mode=None,                                      
    read_default_file=None,                                      
    conv=None,                                      
    use_unicode=None, 
    client_flag=0,                                    
    cursorclass=<class'pymysql.cursors.Cursor'>,              
    init_command=None,                                     
    connect_timeout=10,     
    ssl=None, 
    read_default_group=None, 
    compress=None, 
    named_pipe=None, 
    autocommit=False, 
    db=None, 
    passwd=None, 
    local_infile=False, 
    max_allowed_packet=16777216, 
    defer_connect=False, 
    auth_plugin_map=None, 
    read_timeout=None, 
    write_timeout=None, 
    bind_address=None, 
    binary_prefix=False, 
    program_name=None, 
    server_public_key=None
)
```

> 用mysql服务器表示套接字。
>
> 获取此类实例的正确方法是调用connect（）。
>
> 建立与MySQL数据库的连接。接受几个论点

> > 参数:
> >
> > - **host** - 数据库服务器所在的主机
> > - **user** - 登录的用户名
> > - **password** - 要使用的密码。
> > - **database** - 要使用的数据库，None不使用特定的数据库。
> > - **port** - 要使用的MySQL端口，默认通常都可以。（默认值：3306）
> > - **bind_address** - 当客户端具有多个网络接口时，请指定从中连接到主机的接口。参数可以是主机名或IP地址。
> > - **unix_socket** - 您可以选择使用unix套接字而不是TCP / IP。
> > - **read_timeout** - 以秒为单位读取连接的超时（默认值：无 - 无超时）
> > - **write_timeout** - 以秒为单位写入连接的超时（默认值：无 - 无超时）
> > - **charset** - 你要使用的Charset。
> > - **sql_mode** - 要使用的默认SQL_MODE。
> > - **read_default_file** - 指定my.cnf文件以从[client]部分下读取这些参数。
> > - **conv** - 使用转换字典而不是默认字典。这用于提供类型的自定义编组和解组。见转换器。
> > - **use_unicode** - 是否默认为unicode字符串。对于Py3k，此选项默认为true。
> > - **client_flag** - 要发送给MySQL的自定义标志。在constants.CLIENT中查找潜在值。
> > - **cursorclass** - 要使用的自定义游标类。
> > - **init_command** - 建立连接时要运行的初始SQL语句。
> > - **connect_timeout** - 连接时抛出异常之前的超时。（默认值：10，最小值：1，最大值：31536000）
> > - **ssl** - 类似于mysql_ssl_set（）参数的参数的dict。
> > - **read_default_group** - 要在配置文件中读取的组。
> > - **压缩** - 不支持
> > - **named_pipe** - 不支持
> > - **autocommit** - **自动**提交模式。无表示使用服务器默认值。（默认值：False）
> > - **local_infile** - 允许使用LOAD DATA LOCAL命令的布尔值。（默认值：False）
> > - **max_allowed_packet** - 发送到服务器的最大数据包大小（以字节为单位）。（默认值：16MB）仅用于限制小于默认值（16KB）的“LOAD LOCAL INFILE”数据包的大小。
> > - **defer_connect** - 不要在构造上显式连接 - 等待连接调用。（默认值：False）
> > - **auth_plugin_map** - 插件名称的一个字典，用于处理该插件的类。该类将Connection对象作为构造函数的参数。该类需要一个认证方法，将认证包作为参数。对于对话框插件，可以使用提示（echo，prompt）方法（如果没有authenticate方法）从用户返回字符串。（实验）
> > - **server_public_key** - SHA256身份验证插件公钥值。（默认：无）
> > - **db** - 数据库的别名。（与MySQLdb兼容）
> > - **passwd** - 密码的别名。（与MySQLdb兼容）
> > - **binary_prefix** - 在字节和bytearray上添加_binary前缀。（默认值：False）



请参阅规范中的[连接](https://www.python.org/dev/peps/pep-0249/#connection-objects)。

> - **`begin（）`**
>
>   开始交易。
>
> - **`close（）`**
>
>   发送退出消息并关闭套接字。请参阅 规范中的[Connection.close（）](https://www.python.org/dev/peps/pep-0249/#Connection.close)。举：**错误** - 如果连接已关闭。
>
> - **`commit（）`**
>
>   提交更改为稳定存储。请参阅 规范中的[Connection.commit（）](https://www.python.org/dev/peps/pep-0249/#commit)。
>
> - **`cursor（cursor = None ）`**
>
>   创建一个新游标以执行查询。参数：**cursor** - 要创建的游标类型; 之一`Cursor`， `SSCursor`，`DictCursor`，或`SSDictCursor`。无意味着使用Cursor。
>
> - **`open`**
>
>   如果连接打开，则返回True
>
> - **`ping（reconnect = True ）`**
>
>   检查服务器是否处于活动状态。参数：**重新连接** - 如果连接已关闭，请重新连接。举：**错误** - 如果连接已关闭且重新连接= False。
>
> - **`rollback（）`**
>
>   回滚当前事务。请参阅 规范中的[Connection.rollback（）](https://www.python.org/dev/peps/pep-0249/#rollback)。
>
> - **`select_db（db ）`**
>
>   设置当前数据库。参数：**db** - **数据库**的名称。
>
> - **`show_warnings（）`**
>
>   发送“SHOW WARNINGS”SQL命令。



### 游标对象

> **`class pymysql.cursors.Cursor` **  **（连接）**

+ 这是您用于与数据库交互的对象。

+ 不要自己创建Cursor实例。调用**connections.Connection.cursor（）**。

+ 请参阅规范中的[Cursor](https://www.python.org/dev/peps/pep-0249/#cursor-objects)。

  

> > - **`callproc（procname，args =（））`**
> >
> >   使用args执行存储过程
> >
> >   **procnameprocname** - 字符串，在服务器上执行的过程的名称
> >
> >   **args** - 与过程一起使用的参数序列
> >
> >   返回原始args。
> >
> >   
> >
> >   兼容性警告：PEP-249指定必须返回任何已修改的参数。这当前是不可能的，因为它们只能通过将它们存储在服务器变量中然后通过查询检索来获得。由于存储过程返回零个或多个结果集，因此没有可靠的方法通过callproc获取OUT或INOUT参数。服务器变量名为@_procname_n，其中procname是上面的参数，n是参数的位置（从零开始）。获取过程生成的所有结果集后，可以使用.execute（）发出SELECT @ _procname_0，...查询以获取任何OUT或INOUT值。
> >
> >   
> >
> >   兼容性警告：调用存储过程本身的行为会创建一个空结果集。在程序生成的任何结果集之后出现。这是关于DB-API的非标准行为。一定要使用nextset（）来推进所有结果集; 否则你可能会断开连接。
> >
> > - **`close（）`**
> >
> >   关闭光标会耗尽所有剩余数据。
> >
> > - **`execute（query，args = None ）`**
> >
> >   执行查询
> >
> >   参数：
> >
> >     > **query**（[*str*](https://docs.python.org/3/library/stdtypes.html#str)） - 要执行的查询。
> >  >
> >   > **args**（[*元组*](https://docs.python.org/3/library/stdtypes.html#tuple)*，*[*列表*](https://docs.python.org/3/library/stdtypes.html#list)*或*[*字典*](https://docs.python.org/3/library/stdtypes.html#dict)） - 与查询一起使用的参数。（可选的）
> > 
> > 返回：受影响的行数
> >
> >   返回类型：[INT](https://docs.python.org/3/library/functions.html#int)
> >
> >   如果args是dict，则％（name）s可以用作查询中的占位符。
> >
> >   
> >
> >   - **`executemany（查询，args）`**
> >
> > 针对一个查询运行多个数据
> >
> >   参数：
> >
> >     > **query** - 要在服务器上执行的查询
> >  >
> >   > **args** - 序列或映射的序列。它用作参数。
> > 
> > 返回：受影响的行数（如果有）。
> >
> >   此方法可提高多行INSERT和REPLACE的性能。否则它等同于使用execute（）循环遍历args。
> >
> >   
> >
> >   - **`fetchall()`**
> >
> > 获取所有行
> >
> >   - **`fetchmany(size = None)`**
> >
> > 获取几行
> >
> >   - **`fetchone()`**
> >
> > 获取下一行
> >
> >   - **`max_stmt_length= 1024000`**
> >
> > [`executemany()`](#pymysql.cursors.Cursor.executemany)生成的最大语句大小。允许语句的最大大小为max_allowed_packet - packet_header_size。max_allowed_packet的默认值是1048576。
> >
> >   - **`mogrify（query，args = None ）`**
> >
> > 通过调用execute（）方法返回发送到数据库的确切字符串。此方法遵循DB API 2.0的扩展，然后是Psycopg。
> >
> >   - **`setinputsizes（ args）`**
> >
> > 没有，DB API要求。
> >
> >   
> >
> >   - **`setoutputsizes（ args）`**
> >
> > 没有，DB API 要求。



> **`class pymysql.cursors.SSCursor`**  **（连接）**

+ **Unbuffered Cursor**，主要用于返回大量数据的查询，或用于通过慢速网络连接到远程服务器。

+ 不是将每行数据复制到缓冲区，而是根据需要获取行。这样做的好处是客户端使用更少的内存，并且当通过慢速网络旅行或者结果集非常大时，返回行的速度要快得多。

+ 但是有一些限制。MySQL协议不支持返回总行数，因此判断有多少行的唯一方法是迭代返回的每一行。此外，它目前无法向后滚动，因为只有当前行保存在内存中

  

> > - **`close（）`**
> >
> >   关闭光标会耗尽所有剩余数据。
> >
> > - **`fetchall（）`**
> >
> >   根据MySQLdb获取所有内容。对于大型查询来说，它是无用的，因为它是缓冲的。如果您想要此方法的无缓冲生成器版本，请参阅fetchall_unbuffered（）。
> >
> > - **`fetchall_unbuffered（）`**
> >
> >   获取全部，作为生成器实现，这不是标准的，但是，返回列表中的所有内容是没有意义的，因为这会对大型结果集使用荒谬的内存。
> >
> > - **`fetchmany（size = None ）`**
> >
> >   取很多
> >
> > - **`fetchone（）`**
> >
> >   获取下一行
> >
> > - **`read_next（）`**
> >
> >   阅读下一行



> **`class pymysql.cursors.DictCursor`（连接）**

+ 将结果作为字典返回的游标

> **``class pymysql.cursors.SSDictCursor`** **（连接）**

+ 一个无缓冲的游标，它将结果作为字典返回





## 指数和表

### [指数](genindex.html)

> # Index
>
> [**B**](https://pymysql.readthedocs.io/en/latest/genindex.html#B) | [**C**](https://pymysql.readthedocs.io/en/latest/genindex.html#C) | [**D**](https://pymysql.readthedocs.io/en/latest/genindex.html#D) | [**E**](https://pymysql.readthedocs.io/en/latest/genindex.html#E) | [**F**](https://pymysql.readthedocs.io/en/latest/genindex.html#F) | [**M**](https://pymysql.readthedocs.io/en/latest/genindex.html#M) | [**O**](https://pymysql.readthedocs.io/en/latest/genindex.html#O) | [**P**](https://pymysql.readthedocs.io/en/latest/genindex.html#P) | [**R**](https://pymysql.readthedocs.io/en/latest/genindex.html#R) | [**S**](https://pymysql.readthedocs.io/en/latest/genindex.html#S)
>
> ## B
>
> 
>
> ## C
>
> | [callproc() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.callproc)[close() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.close)[(pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.close)[(pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.close) | [commit() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.commit)[Connection (class in pymysql.connections)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection)[Cursor (class in pymysql.cursors)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor)[cursor() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.cursor) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## D
>
> 
>
> ## E
>
> | [execute() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.execute) | [executemany() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.executemany) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## F
>
> | [fetchall() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.fetchall)[(pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.fetchall)[fetchall_unbuffered() (pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.fetchall_unbuffered) | [fetchmany() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.fetchmany)[(pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.fetchmany)[fetchone() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.fetchone)[(pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.fetchone) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## M
>
> | [max_stmt_length (pymysql.cursors.Cursor attribute)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.max_stmt_length) | [mogrify() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.mogrify) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## O
>
> 
>
> ## P
>
> | [ping() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.ping) | [pymysql.connections (module)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#module-pymysql.connections)[pymysql.cursors (module)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#module-pymysql.cursors) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## R
>
> | [read_next() (pymysql.cursors.SSCursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor.read_next) | [rollback() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.rollback) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |
>
> ## S
>
> | [select_db() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.select_db)[setinputsizes() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.setinputsizes)[setoutputsizes() (pymysql.cursors.Cursor method)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.setoutputsizes) | [show_warnings() (pymysql.connections.Connection method)](https://pymysql.readthedocs.io/en/latest/modules/connections.html#pymysql.connections.Connection.show_warnings)[SSCursor (class in pymysql.cursors)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSCursor)[SSDictCursor (class in pymysql.cursors)](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.SSDictCursor) |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> |                                                              |                                                              |



### [模块索引](py-modindex.html)

> | **p**                                                        |                                                              |      |
> | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
> | ![- ](https://pymysql.readthedocs.io/en/latest/_static/minus.png) | `pymysql`                                                    |      |
> |                                                              | [`pymysql.connections`](https://pymysql.readthedocs.io/en/latest/modules/connections.html#module-pymysql.connections) |      |
> |                                                              | [`pymysql.cursors`](https://pymysql.readthedocs.io/en/latest/modules/cursors.html#module-pymysql.cursors) |      |



### [搜索页面](search.html)



