# 用conda创建python虚拟环境

1、首先在所在系统中安装Anaconda。可以打开命令行输入`conda -V`检验是否安装以及当前conda的版本。



## 1. conda常用的命令。

+ `conda list` 查看安装了哪些包。

+ `conda env list` 或 `conda info -e` 查看当前存在哪些虚拟环境

+ `conda update conda` 检查更新当前conda

  

## 2. 创建python虚拟环境。

```shell
conda create -n your_env_name python=X.X
```

+ 创建python版本为X.X，名字为`your_env_name`的虚拟环境。

+ `your_env_name`文件可以在Anaconda安装目录`/envs/`文件下找到。

  

## 3. 使用激活(或切换不同python版本)的虚拟环境。

+ 打开命令行输入`python --version`可以检查当前python的版本，

使用如下命令即可 激活你的虚拟环境(即将python的版本改变)。

```shell
Linux:   			source activate your_env_name (虚拟环境名称)
Windows: 	   activate your_env_name (虚拟环境名称)
```


这时再使用`python --version`可以检查当前python版本是否为想要的。



## 4. 对虚拟环境中安装额外的包。

```shell
conda install -n your_env_name [package]
```

+ 安装`package`到`your_env_name`中

  

## 5. 关闭虚拟环境

+ **即从当前环境退出，返回使用PATH环境中的默认python版本。**

 ```shell
   Linux: source deactivate / conda deactivate
   Windows: deactivate
 ```



## 6. 删除虚拟环境。

  ```shell
conda remove -n your_env_name --all
  ```

+ `your_env_name` ：虚拟环境名称

  

## 7. 删除环境中的某个包。

   ```shell
conda remove --name your_env_name  package_name
   ```

+ `your_env_name` ：虚拟环境名称
+ `package_name`：包名
