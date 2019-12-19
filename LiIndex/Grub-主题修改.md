## Grub 主题修改

1.到这个网站上去下载自己喜欢的主题包：https://www.gnome-look.org/browse/cat/109

2.打开Linux的终端，创建themes主题文件夹，在终端中输入（接下来的命令都是在一个终端内完成的）

```bash
sudo mkdir /boot/grub/themes
```

3.将刚才下载的安装包解压。

4.将解压后的主题包移动到themes路径下:

```bash
sudo cp 主题包的名字 /boot/grub/themes/
```


5.在上步完成后，接下来需要修改配置文件并更新

+ 修改配置文件，其命令是：

  ```bash
  sudo gedit /etc/grub.d/00_header
  ```

+  打开这个文件后，在注释下添加如下代码：

  ```bash
  GRUB_THEME="/boot/grub/themes/主题包名/theme.txt"
  GRUB_GFXMODE="1920x1080x32"
  ```


  注意第一行代码中theme.txt的路径

6.最后一步，更新配置文件：

```bash
sudo update-grub
```


这样就OK了！


