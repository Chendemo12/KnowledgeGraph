# Python os.stat() 和文件目录方法
## 1. os.stat () 方法

### 概述

os.stat () 方法用于在给定的路径上执行一个系统 stat 的调用。

### 语法

**stat()** 方法语法格式如下：

```python
os.stat(path)
```

### 参数

+  **path** -- 指定路径

### 返回值

stat 结构:

+  **st_mode:** inode 保护模式
+  **st_ino:** inode 节点号。
+  **st_dev:** inode 驻留的设备。
+  **st_nlink:** inode 的链接数。
+  **st_uid:** 所有者的用户 ID。
+  **st_gid:** 所有者的组 ID。
+  **st_size:** 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
+  **st_atime:** 上次访问的时间。
+  **st_mtime:** 最后一次修改的时间。
+  **st_ctime:** 由操作系统报告的 "ctime"。在某些系统上（如 Unix）是最新的元数据更改的时间，在其它系统上（如 Windows）是创建时间（详细信息参见平台的文档）。

### 实例

以下实例演示了 stat () 方法的使用：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 显示文件 "a2.py" 信息
statinfo = os.stat('a2.py')

print statinfo
```

执行以上程序输出结果为：

```python
posix.stat_result(st_mode=33188, st_ino=3940649674337682L, st_dev=277923425L, st
_nlink=1, st_uid=400, st_gid=401, st_size=335L, st_atime=1330498089, st_mtime=13
30498089, st_ctime=1330498089)
```



## 2. Python OS 文件 / 目录方法

**os** 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：

| 序号 | 方法及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [os.access(path, mode)](http://www.runoob.com/python/os-access.html) <br>检验权限模式 |
| 2    | [os.chdir(path)](http://www.runoob.com/python/os-chdir.html) <br/>改变当前工作目录 |
| 3    | [os.chflags(path, flags)](http://www.runoob.com/python/os-chflags.html) <br/>设置路径的标记为数字标记。 |
| 4    | [os.chmod(path, mode)](http://www.runoob.com/python/os-chmod.html) <br/>更改权限 |
| 5    | [os.chown(path, uid, gid)](http://www.runoob.com/python/os-chown.html) <br/>更改文件所有者 |
| 6    | [os.chroot(path)](http://www.runoob.com/python/os-chroot.html) <br/>改变当前进程的根目录 |
| 7    | [os.close(fd)](http://www.runoob.com/python/os-close.html) <br/>关闭文件描述符 fd |
| 8    | [os.closerange(fd_low, fd_high)](http://www.runoob.com/python/os-closerange.html) <br/>关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
| 9    | [os.dup(fd)](http://www.runoob.com/python/os-dup.html) <br/>复制文件描述符 fd |
| 10   | [os.dup2(fd, fd2)<br/>](http://www.runoob.com/python/os-dup2.html) 将一个文件描述符 fd 复制到另一个 fd2 |
| 11   | [os.fchdir(fd)](http://www.runoob.com/python/os-fchdir.html) <br/>通过文件描述符改变当前工作目录 |
| 12   | [os.fchmod(fd, mode)](http://www.runoob.com/python/os-fchmod.html) <br/>改变一个文件的访问权限，该文件由参数 fd 指定，参数 mode 是 Unix 下的文件访问权限。 |
| 13   | [os.fchown(fd, uid, gid)](http://www.runoob.com/python/os-fchown.html) <br/>修改一个文件的所有权，这个函数修改一个文件的用户 ID 和用户组 ID，该文件由文件描述符 fd 指定。 |
| 14   | [os.fdatasync(fd)](http://www.runoob.com/python/os-fdatasync.html) <br/>强制将文件写入磁盘，该文件由文件描述符 fd 指定，但是不强制更新文件的状态信息。 |
| 15   | [os.fdopen(fd[, mode[, bufsize\]])](http://www.runoob.com/python/os-fdopen.html) <br/>通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
| 16   | [os.fpathconf(fd, name)](http://www.runoob.com/python/os-fpathconf.html) <br/>返回一个打开的文件的系统配置信息。name 为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
| 17   | [os.fstat(fd)](http://www.runoob.com/python/os-fstat.html) <br/>返回文件描述符 fd 的状态，像 stat ()。 |
| 18   | [os.fstatvfs(fd)](http://www.runoob.com/python/os-fstatvfs.html) <br/>返回包含文件描述符 fd 的文件的文件系统的信息，像 statvfs () |
| 19   | [os.fsync(fd)](http://www.runoob.com/python/os-fsync.html) <br/>强制将文件描述符为 fd 的文件写入硬盘。 |
| 20   | [os.ftruncate(fd, length)](http://www.runoob.com/python/os-ftruncate.html) <br/>裁剪文件描述符 fd 对应的文件，所以它最大不能超过文件大小。 |
| 21   | [os.getcwd()](http://www.runoob.com/python/os-getcwd.html) <br/>返回当前工作目录 |
| 22   | [os.getcwdu()](http://www.runoob.com/python/os-getcwdu.html) <br/>返回一个当前工作目录的 Unicode 对象 |
| 23   | [os.isatty(fd)](http://www.runoob.com/python/os-isatty.html) <br/>如果文件描述符 fd 是打开的，同时与 tty (-like) 设备相连，则返回 true, 否则 False。 |
| 24   | [os.lchflags(path, flags)](http://www.runoob.com/python/os-lchflags.html) <br/>设置路径的标记为数字标记，类似 chflags ()，但是没有软链接 |
| 25   | [os.lchmod(path, mode)](http://www.runoob.com/python/os-lchmod.html) <br/>修改连接文件权限 |
| 26   | [os.lchown(path, uid, gid)](http://www.runoob.com/python/os-lchown.html) <br/>更改文件所有者，类似 chown，但是不追踪链接。 |
| 27   | [os.link(src, dst)](http://www.runoob.com/python/os-link.html) <br/>创建硬链接，名为参数 dst，指向参数 src |
| 28   | [os.listdir(path)](http://www.runoob.com/python/os-listdir.html) <br/>返回 path 指定的文件夹包含的文件或文件夹的名字的列表。 |
| 29   | [os.lseek(fd, pos, how)](http://www.runoob.com/python/os-lseek.html) <br/>设置文件描述符 fd 当前位置为 pos, how 方式修改: SEEK_SET 或者 0 设置从文件开始的计算的 pos; SEEK_CUR 或者 1 则从当前位置计算；os.SEEK_END 或者 2 则从文件尾部开始。在 unix，Windows 中有效 |
| 30   | [os.lstat(path)](http://www.runoob.com/python/os-lstat.html) <br/>像 stat (), 但是没有软链接 |
| 31   | [os.major(device)](http://www.runoob.com/python/os-major.html) <br/>从原始的设备号中提取设备 major 号码 (使用 stat 中的 st_dev 或者 st_rdev field)。 |
| 32   | [os.makedev(major, minor)](http://www.runoob.com/python/os-makedev.html) <br/>以 major 和 minor 设备号组成一个原始设备号 |
| 33   | [os.makedirs(path[, mode\])](http://www.runoob.com/python/os-makedirs.html) <br/>递归文件夹创建函数。像 mkdir (), 但创建的所有 intermediate-level 文件夹需要包含子文件夹。 |
| 34   | [os.minor(device)](http://www.runoob.com/python/os-minor.html) <br/>从原始的设备号中提取设备 minor 号码 (使用 stat 中的 st_dev 或者 st_rdev field)。 |
| 35   | [os.mkdir(path[, mode\])](http://www.runoob.com/python/os-mkdir.html) <br/>以数字 mode 的 mode 创建一个名为 path 的文件夹。默认的 mode 是 0777 (八进制)。 |
| 36   | [os.mkfifo(path[, mode\])](http://www.runoob.com/python/os-mkfifo.html) <br/>创建命名管道，mode 为数字，默认为 0666 (八进制) |
| 37   | [os.mknod(filename[, mode=0600, device\])](http://www.runoob.com/python/os-mknod.html) <br/>创建一个名为 filename 文件系统节点（文件，设备特别文件或者命名 pipe）。 |
| 38   | [os.open(file, flags[, mode\])](http://www.runoob.com/python/os-open.html) <br/>打开一个文件，并且设置需要的打开选项，mode 参数是可选的 |
| 39   | [os.openpty()](http://www.runoob.com/python/os-openpty.html) <br/>打开一个新的伪终端对。返回 pty 和 tty 的文件描述符。 |
| 40   | [os.pathconf(path, name)](http://www.runoob.com/python/os-pathconf.html) <br/>返回相关文件的系统配置信息。 |
| 41   | [os.pipe()](http://www.runoob.com/python/os-pipe.html) <br/>创建一个管道。返回一对文件描述符 (r, w) 分别为读和写 |
| 42   | [os.popen(command[, mode[, bufsize\]])](http://www.runoob.com/python/os-popen.html) <br/>从一个 command 打开一个管道 |
| 43   | [os.read(fd, n)](http://www.runoob.com/python/os-read.html) <br/>从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd 对应文件已达到结尾，返回一个空字符串。 |
| 44   | [os.readlink(path)](http://www.runoob.com/python/os-readlink.html) <br/>返回软链接所指向的文件 |
| 45   | [os.remove(path)](http://www.runoob.com/python/os-remove.html) <br/>删除路径为 path 的文件。如果 path 是一个文件夹，将抛出 OSError; 查看下面的 rmdir () 删除一个 directory。 |
| 46   | [os.removedirs(path)](http://www.runoob.com/python/os-removedirs.html) <br/>递归删除目录。 |
| 47   | [os.rename(src, dst)](http://www.runoob.com/python/os-rename.html) <br/>重命名文件或目录，从 src 到 dst |
| 48   | [os.renames(old, new)](http://www.runoob.com/python/os-renames.html) <br/>递归地对目录进行更名，也可以对文件进行更名。 |
| 49   | [os.rmdir(path)](http://www.runoob.com/python/os-rmdir.html) <br/>删除 path 指定的空目录，如果目录非空，则抛出一个 OSError 异常。 |
| 50   | [os.stat(path)](http://www.runoob.com/python/os-stat.html) <br/>获取 path 指定的路径的信息，功能等同于 C API 中的 stat () 系统调用。 |
| 51   | [os.stat_float_times([newvalue\])](http://www.runoob.com/python/os-stat_float_times.html) <br/>决定 stat_result 是否以 float 对象显示时间戳 |
| 52   | [os.statvfs(path)](http://www.runoob.com/python/os-statvfs.html) <br/>获取指定路径的文件系统统计信息 |
| 53   | [os.symlink(src, dst)](http://www.runoob.com/python/os-symlink.html) <br/>创建一个软链接 |
| 54   | [os.tcgetpgrp(fd)](http://www.runoob.com/python/os-tcgetpgrp.html) <br/>返回与终端 fd（一个由 os.open () 返回的打开的文件描述符）关联的进程组 |
| 55   | [os.tcsetpgrp(fd, pg)](http://www.runoob.com/python/os-tcsetpgrp.html) <br/>设置与终端 fd（一个由 os.open () 返回的打开的文件描述符）关联的进程组为 pg。 |
| 56   | [os.tempnam([dir[, prefix\]])](http://www.runoob.com/python/os-tempnam.html) <br/>返回唯一的路径名用于创建临时文件。 |
| 57   | [os.tmpfile()](http://www.runoob.com/python/os-tmpfile.html) <br/>返回一个打开的模式为 (w+b) 的文件对象。这文件对象没有文件夹入口，没有文件描述符，将会自动删除。 |
| 58   | [os.tmpnam()](http://www.runoob.com/python/os-tmpnam.html) <br/>为创建一个临时文件返回一个唯一的路径 |
| 59   | [os.ttyname(fd)](http://www.runoob.com/python/os-ttyname.html) <br/>返回一个字符串，它表示与文件描述符 fd 关联的终端设备。如果 fd 没有与终端设备关联，则引发一个异常。 |
| 60   | [os.unlink(path)](http://www.runoob.com/python/os-unlink.html) <br/>删除文件路径 |
| 61   | [os.utime(path, times)](http://www.runoob.com/python/os-utime.html) <br/>返回指定的 path 文件的访问和修改的时间。 |
| 62   | [os.walk(top [, topdown=True [, onerror=None [, followlinks=False]]])[#](http://www.runoob.com/python/os-walk.html) <br/>输出在文件夹中的文件名通过在树中游走，向上或者向下。 |
| 63   | [os.write(fd, str)](http://www.runoob.com/python/os-write.html) <br/>写入字符串到文件描述符 fd 中。返回实际写入的字符串长度 |
| 64   | [os.path 模块](http://www.runoob.com/python/python-os-path.html) <br/>获取文件的属性信息。 |