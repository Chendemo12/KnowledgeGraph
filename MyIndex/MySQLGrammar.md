# MySQL Grammar

## 1. **CTEATA DATABASE**

```mysql
CREATE DATABASE database_name
[ON
[PRIMARY] [<filespec>  [,...n] 
[,filegroupspec>[,...n]]]
[LOG ON {<filespec>[,...n]}]
]

<filespec>::=
	(
	NAME = logical_filename,
		[,FILENAME = 'os_file_name']
		[,SIZE = size]
		[,MAXSIZE = {max_size|UNLIMITED}]
		[,FILEGROWTH = grow_increment]
	)

	
<filegroupspec>::=
	(
		FILEGROUP filegroup_name[DEFAULT]
		<FILESPEC>
	)
```

1. **注意**

   1、中括号[]表示该项可以省略，省略时各参数取默认值。
   2、大括号{}为必选语法项。
   3、[,...n]指示前面的项可以重复n次，各项之间用逗号隔开。
   4、竖线(|)分隔括号或大括号的语法项，只能使用其中一项。
   5、SQL语句在书写时不区分大小写，为了清晰，一般都用大写书写系统保留字，用小写表示用户自定义名称。
   6、一条语句可以写在多行上，但不能多条语句写在一行上。

   

2. **语法解释**

   ***database_name:***	要建立的数据库名称。
   ***ON:***	指定存储数据库中数据文件的磁盘文件。

   ***PRIMARY:***	定义数据库的主数据文件，若没有指定PRIMARY关键字，则该语句所列的第一个文件成为主文件。
   ***LOG ON:***	指定建立数据库的事务日志文件。
   ***NAME:***	指定数据或事物日志文件的逻辑名称。
   ***FILENAME:***	指定数据和日志的操作系统文件名(包括所在路径)。
   ***SIZE:***	指定数据库的初始文件容量。
   ***MAXSIXE:***	指定操作系统文件能增长到的最大尺寸，如果没有指定长度，文件将一直增长，直到磁盘满为止。
   ***FILEGROWTH:***	指定文件的自动增长量或比例。该值可按MB、KB、GB、TB、或%的形式指定，必须是整数，不能包含小数。默认为MB。如果指定了%，那么文件增量为文件发生增长时文件大小的指定百分比。如果指定的是数据为0，表示文件不增长。如果未指定FILEGROWTH，则文件的默认增长为1MB，日志文件的增长为10%。
   ***FELEGROUP:***	控制文件组属性。
   ***filegroup_name:***	文件组的逻辑名称。filegroup_name在数据库中必须唯一，而且不能使用系统提供的PRIMARY，名称必须符合标识符规则。

   

3. **实例**

   ```mysql
   CREATE DATABASE jifei			--创建一个数据库JIFEI
   ON PRIMARY
   	(
   		NAME = jifei_Data,		--主数据文件逻辑名称
   		FILENAME = 'D:\jifeiDB\jifei_Data.mdf'		
           						--主数据文件存储位置
   		SIZE = 10MB,			--主数据文件初始大小
   		MAXSIXE = 100MB,		--主数据文件最大增长空间
   		FILEGROWTH = 2MB,		--主数据自动增长率
   	)
   
   LOG ON
   	(	
   		NAME = jifei_log,
   		FILEAME = 'D:\jifeiDB\jifei_log.ldf',
   		SIZE = 2MB,
   		MAXSIXE = 50MB,
   		FILEGROWTH = 20%
   	);
   GO
   ```

## 2. **查看数据库信息**

1. **关键字：*EXEC***

2. **语法**

   ```mysql
   USE database_name
   GO
   EXEC sp_helpfile
   ```

## 3. 打开数据库属性面板

1. **语法**

   ```mysql
   USE database_name
   GO
   ```

## 4. 修改数据库初始容量

1. **修改数据库的容量只能比最初分配给数据库的容量要大。**

2. **语法**

   ```mysql
   ALTER DATABASE database_name
   MODIFY FILE
   	(
           NAME = logical_file_name
           [,SIZE = newsize[KB|MB|GB|TB]]
           [,MAXSIZE = {max_size[KB|MB|GB|TB]}]
           [,FILEGROWTH = growth_increment[KB|MB|GB|TB|%]]
          	--“%” 表示增长率
       )
   ```

   

3. **实例**

   ```mysql
   USE jifei
   GO
   ALTER DATABASE jifei
   MODIFY FILE
   	(
           NAME = jifei.data,
           SIZE = 20MB,
           MAXSIZE = 150MB,
           FILEGROWTH = 3MB
   	)
   GO
   EXEC sp_helpfile
   ```

   

## 5. 缩减数据库容量

1. **收缩整个数据库容量**

   1. **收缩后数据库的大小不能小于创建时指定的大小。**

   2. **语法**

      ```mysql
      DBCC
      SHRINKDATABASE (database_name [,target_percent]  
                      [,{NOTRUNCAT|TRUNCAEONLY}])
                      
      /*	说明：
      
      	database name：是要缩减的数据库名称。
      	target_percent：指明要缩减数据库的比例。
      	指定“NOTRUNCATE”时，表示在数据库文件中保留收缩数据库时释放出来的空间；如果未指定，将所释放的文件空间释放给操作系统，数据库文件中不保留这部分释放的空间。因此，指定NOTRUNCATE时，数据库看起来未收缩。NOTRUNCATE选项只适用于数据文件，日志文件不受影响。
      	指定TRUNCATEONLY时数据库文件中未使用的空间释放给操作系统，从而减少数据库文件的大小。使用TRUNCATEONLY时，忽略target_percent参数对应的值。
      	使用权限默认为dbo。
      
      */
      ```

   3. **实例**

      ```mysql
      USE jifei
      GO
      DBCC SHRINKFILE (jifei,20)
      GO
      ```

      

2. **收缩指定文件的大小**

   1. **语法**

      ```mysql
      DBCC SHRINKFILE
      	(
              file_name {[,EMPTYFILE]|[[,target_size][,{NOTRUNCATE|TRUNCATEONLY}]]}
          )
      
      /*	说明：
      	其中部分参数的含义与收缩数据库类似；
      	file_name:是要缩减的数据库文件的逻辑名称。
      	target_size:指明缩减后文件的目标大小(用整数表示，单位为MB)。如果未指定，则DBCC SHRINKFILE将文件大小减小到创建文件时指定的大小。该语句不会将文件收缩到小于文件中存储数据所需要的大小。例如，如果大小为10MB的数据文件中有6MB的数据，此时将target_size指定为5MB,则该语句也只能将该文件收缩到6MB。因此，在收缩整个数据库的大小时，收缩后的所有文件的大小都不能小于创建这些文件时指定的初始大小，或者是上一次进行收缩文件操作时设置的大小。但当对某个具体的文件进行收缩时则无此限制。不管是哪种收缩方法，收缩后的文件都不能小于其当前存放数据所占空间的大小。
      
      */
      ```

## 6. 创建和更改文件组

1. **定义文件组的主要目的是为了添加新的数据文件。**

2. **语法**

   ```mysql
   ALTER DATABASE database_name
   	{
           |ADD FILEGROUP filegroup_name
           |REMOVE FILEGROUP filegroup_name
           |MODIFY FILEGROUP filegroup_name
           {{READ_ONLY|READ_WRITE}|DEFAULT|NAME = new_filegroup_name}
       }
       
   /*	说明：
   	ADD FILEGROUP filegroup_name：将文件组添加到数据库。
   	REMOVE FILEGROUP filegroup_name：从数据库中删除文件组。
   	MODIFY FILEGROUP filegroup_name ... = new_filegroup_name}：通过将文件组设置为数据的默认文件组或者更改文件组名称来修改文件组。
   	{READ_ONLY|READ_WRITE}：对文件组设置为："只读"或"读/写"属性。其中READ_ONLY 指定文件组为只读，不允许更新其中的对象;主文件组不能设置为只读。
   	READ_WRITE：指定文件组为可读/写，即允许更新文件组中的对象。
   
   */
   	
   ```

   

3. **实例**

   ```mysql
   USE jifei
   GO
   ALTER DATABASE jifei
   ADD FILEGROUP jifei_group1
   GO
   ```

## 7. 增加或删除数据库文件

1. **添加文件**
   1. **语法**
   
      ```mysql
      ALTER DATABASE database_name
      {
      |ADD FILE  <filespec> [,...n] [TO FILEGROUP {filegroup_name}]
      |ADD LOG FILE  <filespec> [,...n]
      |REMOVE FILE logical_file_name
      |REMOVE FILEGROUP filegroup_name
      }
      
      <filespec>::=
      (
          NAME = logical_file_name
          [,FILENAME = 'os_file_name']
          [,SIZE = size[KB|MB|GB|TB]]
          [,MAXSIZE = max_size[KB|MB|GB|TB]]
          [,FILEGROWTH = growth_increment[KB|MB|GB|TB]]
          [,OFFLINE]
      )
      ```
   
      2. **实例**
   
         ```mysql
         /*	
         为JIFEI数据库增加一个新的数据文件jifei_data2.ndf，初始分配空间为6MB，自动增长率为1MB，最大文件空间为20MB，物理文件名为jifei_data2.ndf，物理存储位置为d:\jifeiDB文件夹。
         */
         
         USE jifei
         GO
         ALTER DATABASE jifei
         ADD FILE
         	(
                 NAME = jifei_data2,
                 FILENAME = 'D:\jifeiDB\jifei_data2.ndf',
                 SIZE = 6MB,
                 MAXSIZE = 20MB,
                 FILEGROWTH = 1MB
             )
         ```

2. **删除文件**

   ```mysql
   --删除文件jifeigrp1_data1.ndf
   ALTER DATABASE jifei
   REMOVE FILE jifeigrp1_data1
   
   --删除日志文件jifei_log1.ldf
   ALTER DATABASE jifei
   REMOVE FILE jifei_log1
   
   --删除文件组jifei_group1
   ALTER DATABASE jifei
   REMOVE FILEGROUP jifei_group1
   ```

## 8. 更改数据库名称

1. **语法**

   ```mysql
   DROP DATABASE database_name [,database_name ...]
   ```




## 9. 单表查询



## 10. 选择表中的若干数据

1. **消除取值重复的值**

   1. **关键字**：DISTINCT

   2. **实例**

      ```mysql
      USE student
      GO
      SELECT DISTINCT 学号
      FROM 课程注册
      GO
      ```

      

2. **限制返回的行数**

   1. **关键字：**TOP n(行数)：	***返回前n行***

      ​			  TOP n PERCENT:	***返回前n%条记录***

   2. **实例**

      ```mysql
      USE student
      GO
      SELECT TOP 3 *
      FROM 课程注册
      GO
      ```

3. **查询满足条件的元组**

   1. **比较运算符**

      1. [!]
      2. 

      

   2. **确定范围**

      1. 

      

   3. **确定集合**

      1. 

      

   4. **字符匹配**

      1. 

      

   5. ****

      1. 