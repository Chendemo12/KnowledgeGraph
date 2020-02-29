

#  Python os.walk目录遍历



### 概述

`os.walk() `方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。

`os.walk() `方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。

在Unix，Windows中有效。

`os.walk()`的参数如下:

```python
os.walk(top, topdown=True, onerror=None, followlinks=False)
```

其中：

- <u>top</u> 是要遍历的目录。
- <u>topdown</u> 是代表要从上而下遍历还是从下往上遍历。
- <u>onerror</u> 可以用来设置当便利出现错误的处理函数(该函数接受一个OSError的实例作为参数)，设置为空则不作处理。
- <u>followlinks</u> 表示是否要跟随目录下的链接去继续遍历，要注意的是，os.walk不会记录已经遍历的目录，所以跟随链接遍历的话有可能一直循环调用下去。

os.walk 返回的是一个3个元素的元组 `(root, dirs, files)` ，分别表示<u>遍历的路径名</u>、<u>该路径下的目录列表</u>和<u>该路径下的文件列表</u>。注意目录列表和文件列表不是具体路径，需要具体路径(从root开始的路径)的话可以用 `os.path.join(root,dir)` 和 `os.path.join(root,files)` 。



## 例子

假设现在存在如下的文件和目录结构:

```bash
➜  test_os_walk git:(master) ✗ tree
.
├── a.py
├── b.py
├── c.py
├── dir1
│   ├── dir4
│   │   ├── g.py
│   │   └── h.py
│   ├── dirx
│   │   ├── diry
│   │   │   └── k.py
│   │   └── z.py
│   ├── e.py
│   ├── f.py
│   └── g.py
├── dir2
│   ├── dira
│   │   └── dirb
│   │       └── dirc
│   │           └── aha.py
│   ├── k.py
│   ├── l.py
│   └── m.py
└── dir3
    ├── dir5
    │   └── z.py
    ├── x.py
    └── y.py

10 directories, 17 files
```

### 测试topdown

当我用 `os.walk` 遍历这个目录时，程序和输出如下:

```
import os

path = '/Users/nisen/Projects/python_advanced_class/test/test_os_walk'

for root, dirs, files in os.walk(path, True):
    print 'root: %s' % root
    print 'dirs: %s' % dirs
    print 'files: %s' % files
    print ''
```

结果如下，从root的路径可以看出遍历是自上而下的：

```
➜  test git:(master) ✗ python test11.py
root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk
dirs: ['dir1', 'dir2', 'dir3']
files: ['a.py', 'b.py', 'c.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1
dirs: ['dir4', 'dirx']
files: ['e.py', 'f.py', 'g.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dir4
dirs: []
files: ['g.py', 'h.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dirx
dirs: ['diry']
files: ['z.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dirx/diry
dirs: []
files: ['k.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2
dirs: ['dira']
files: ['k.py', 'l.py', 'm.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira
dirs: ['dirb']
files: []

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira/dirb
dirs: ['dirc']
files: []

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira/dirb/dirc
dirs: []
files: ['aha.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir3
dirs: ['dir5']
files: ['x.py', 'y.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir3/dir5
dirs: []
files: ['z.py']
```

而当设置os.walk的topdown为False时，结果如下, 可以看出他是自上而下遍历的：

```
➜  test git:(master) ✗ python test11.py
root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dir4
dirs: []
files: ['g.py', 'h.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dirx/diry
dirs: []
files: ['k.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1/dirx
dirs: ['diry']
files: ['z.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir1
dirs: ['dir4', 'dirx']
files: ['e.py', 'f.py', 'g.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira/dirb/dirc
dirs: []
files: ['aha.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira/dirb
dirs: ['dirc']
files: []

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2/dira
dirs: ['dirb']
files: []

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir2
dirs: ['dira']
files: ['k.py', 'l.py', 'm.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir3/dir5
dirs: []
files: ['z.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk/dir3
dirs: ['dir5']
files: ['x.py', 'y.py']

root: /Users/nisen/Projects/python_advanced_class/test/test_os_walk
dirs: ['dir1', 'dir2', 'dir3']
files: ['a.py', 'b.py', 'c.py']
```

### 运行时修改遍历目录

当topdown设置为True时，可以在处理时修改返回的 `dirs` 列表，这样可以遍历下面的目录时会根据修改后的 `dirs` 来遍历。比如下面的例子，在遍历的时候不把"CSV"目录包括在内:

```
import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/email'):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
```

