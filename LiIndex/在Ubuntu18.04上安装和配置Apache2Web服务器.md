## 如何在Ubuntu 18.04上安装和配置Apache 2 Web服务器

### **1. 什么是Apache Web Server？**

Apache或Apache HTTP服务器是一个免费的开源Web服务器，由Apache软件基金(Apache Software Foundation)开发和维护。它的受欢迎程度可以通过以下事实来判断：全球约有46％的网站由Apache提供支持。 Apache允许网站开发人员通过网络提供他们的内容。

本教程是关于在[Ubuntu](https://www.linuxidc.com/topicnews.aspx?tid=2)系统上安装和配置Apache2的。本文中提到的命令和过程已在Ubuntu 18.04 LTS系统上运行。因为我们在本文中使用了Ubuntu命令行，终端;您可以通过系统Dash或Ctrl + Alt + T快捷方式打开它。

### 2. 在Ubuntu Linux上安装Apache 2

请按照以下步骤通过Ubuntu官方存储库安装Apache2软件。

第1步：更新系统存储库

您可以通过首先更新Ubuntu存储库的本地包索引来下载最新版本的软件。打开终端并输入以下命令以执行此操作：

```bash
 sudo apt update
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519435536.png)

步骤2：使用apt命令安装Apache 2

接下来，输入以下命令作为sudo，以便安装Apache2及其所需的依赖项：

```bash
sudo apt install apache2
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519435755.png)

系统可能会提示您使用`y / n`选项继续安装。 请输入`Y`，然后安装程序将开始。

第3步：验证Apache安装

安装完成后，您可以检查版本号，从而通过输入以下命令验证系统上是否确实安装了Apache2：

```bash
apache2 -version
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519436287.png)

输出如下：

```bash
Server version: Apache/2.4.29 (Ubuntu)
Server built:  2018-10-10T18:59:25
```

### 3. 配置UFW防火墙

为了配置Apache，我们首先需要允许外部访问我们系统的某些Web端口，并在您的UFW防火墙上允许Apache。

第1步：列出UFW应用程序配置文件

为了配置防火墙，让我们首先列出我们启用Apache访问所需的应用程序配置文件。 使用以下命令列出此类可用应用程序：

```bash
sudo ufw app list
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519439261.png)

输出如下：

```bash
可用应用程序：
  Apache
  Apache Full
  Apache Secure
  CUPS
  OpenSSH
  Samba
```

在上面的输出中，您可以看到三个Apache配置文件都提供不同级别的安全性; Apache是一个提供最大限制但端口80仍处于打开状态的Apache。

步骤2：在UFW上允许Apache并验证其状态

在UFW上允许Apache将为网络流量打开端口80，同时为服务器提供最大的安全性。 请通过以下命令配置UFW以允许Apache：

```bash
sudo ufw allow 'Apache'
```

輸出如下:

```bash
防火墙规则已更新
规则已更新(v6)
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519439296.png)

UFW的状态现在将在防火墙上显示启用Apache。

```bash
 sudo ufw status
```

### 4. 配置Apache Web服务器

步骤1：验证Apache服务是否正在运行

第一步是通过以下命令验证Apache2服务是否在您的系统上启动并运行：

```bash
 sudo systemctl status apache2
```

输出如下:

```bash
● apache2.service - The Apache HTTP Server
  Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset:
  Drop-In: /lib/systemd/system/apache2.service.d
          └─apache2-systemd.conf
  Active: active (running) since Sun 2018-11-25 19:26:03 CST; 10min ago
 Main PID: 11590 (apache2)
    Tasks: 6 (limit: 3500)
  CGroup: /system.slice/apache2.service
          ├─11590 /usr/sbin/apache2 -k start
          ├─11610 /usr/sbin/apache2 -k start
          ├─11611 /usr/sbin/apache2 -k start
          ├─11612 /usr/sbin/apache2 -k start
          ├─11616 /usr/sbin/apache2 -k start
          └─11618 /usr/sbin/apache2 -k start

11月 25 19:26:03 linuxidc systemd[1]: Starting The Apache HTTP Server...
11月 25 19:26:03 linuxidc apachectl[11574]: AH00558: apache2: Could not reliably
11月 25 19:26:03 linuxidc systemd[1]: Started The Apache HTTP Server.
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519446015.png)

状态:**active（running）**验证apache2服务是否正在运行。

第2步：验证Apache是否正常运行并侦听您的IP地址

您还可以通过从Apache服务器请求页面来验证Apache是否正在运行。 为此，您可以使用服务器的IP来访问Apache登录页面。

使用以下命令了解服务器的IP：

```bash
 hostname -I
192.168.182.188 172.16.43.1 172.16.238.1 172.17.0.1
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519445638.png)

然后在Web浏览器中逐个尝试IP，如下所示：

http://server_IP

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112519462817.png)

就我而言，http://192.168.182.188和http://172.16.43.1。 这样做将显示Ubuntu的以下Apache网页，验证Apache服务器是否正常工作。

### 5. 在Apache中设置虚拟主机

虚拟主机类似于Nginx中的服务器块。 它用于管理来自一个服务器的多个域的配置。 我们将提供一个如何通过Apache服务器设置虚拟主机的示例。 我们将使用Apache for Ubuntu 18中默认启用的服务器块来建立一个名为`linuxidc.com`的网站。

第1步：设置域名

默认情况下启用的服务器块能够提供来自` /var/www/html`的文档。 但是，我们将在`/var/www/`创建一个目录，保留默认目录。

通过以下命令创建此目录，将linuxidc.com替换为您各自的域名。

```bash
sudo mkdir -p /var/www/linuxidc.com/html
```

然后通过以下命令分配目录的所有权：

```bash
sudo chown -R USER:USER:USER /var/www/linuxidc.com/html
sudo chmod -R 755 /var/www/linuxidc.com
```

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520035980.png)

现在让我们创建一个索引页面，如果Apache运行我们的域名，我们以后可以访问它们进行测试。 通过Nano编辑器或任何您喜欢的文本编辑器创建HTML文件。

```bash
nano /var/www/linuxidc.com/html/index.html
```

为索引页输入以下HTML：

```html
<VirtualHost *:80>
ServerAdmin admin@chenlinux.com
ServerName chenlinux.com
ServerAlias www.chenlinux.com
DocumentRoot /var/www/chenlinux.com/html
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

我们使用nano编辑器来创建HTML文件。

您可以使用`Ctrl + X`将文件保存为`nano`，然后输入`Y`并按`Enter`键。

Apache需要一个虚拟主机文件来提供服务器的内容。 已经创建了用于此目的的默认配置文件，但我们将为自定义配置创建一个新配置文件。

```bash
sudo nano /etc/apache2/sites-available/linuxidc.com.conf
```

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520168535.png)

输入域名的以下自定义配置详细信息：

```bash
<VirtualHost *:80>
ServerAdmin admin@linuxidc.com
ServerName linuxidc.com
ServerAlias www.linuxidc.com
DocumentRoot /var/www/linuxidc.com/html
ErrorLog APACHELOGDIR/error.logCustomLogAPACHELOGDIR/error.logCustomLog{APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

我们正在使用nano编辑器来创建此.conf文件。

您可以使用Ctrl + X将文件保存为nano，然后输入Y并按Enter键。

步骤2：启用域配置文件

让我们启用使用a2ensite工具创建的配置文件：

```bash
sudo a2ensite linuxidc.com.conf
```

输出:

```bash
Enabling site linuxidc.com.
To activate the new configuration, you need to run:
 	systemctl reload apache2
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520164013.png)

输出将建议激活新配置，但我们可以在运行以下禁用原始配置文件的命令后集体执行此操作：

```bash
sudo a2dissite 000-default.conf
Site 000-default disabled.
To activate the new configuration, you need to run:
  systemctl reload apache2
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520164761.png)

现在重启Apache服务：

```bash
 sudo systemctl restart apache2
```

第3步：测试错误

最后，让我们通过以下命令测试是否存在任何配置错误：

```bash
 sudo apache2ctl configtest
```

如果您没有收到任何错误，您将获得以下输出：

`Syntax OK`

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520189313.png)

但是，Ubuntu 18.04中常见以下错误

```bash
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message**
Syntax OK
```

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520161214.png)

解决错误：

输入以下命令以解决上述错误：

```bash
 echo "ServerName linuxidc.com" | sudo tee /etc/apache2/conf-available/servername.conf
```

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520181274.png)

然后：

```bash
sudo a2enconf servername
```

输出:

```bash
Enabling conf servername.
To activate the new configuration, you need to run:
  systemctl reload apache2
```



![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520186388.png)

现在，当您再次检查错误时，您将看到通过以下输出解决了此错误：

```bash
 sudo apache2ctl configtest
```

`Syntax OK`

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112520189313.png)

第4步：测试Apache是否为您的域名提供服务

Apache服务器现在配置为提供您的域名。 这可以通过在系统上运行的任何Web浏览器中输入您的服务器名称来验证：

http://www.linuxidc.com

索引页面应显示如下，表示Apache现在已准备好为您的服务器块提供服务！

通过域名访问您的网站

中文乱码：

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112521174991.png)

Apache 2网页中文乱码的解决方法：

```bash
 sudo nano /etc/apache2/conf-available/charset.conf
```

修改`charset.conf`的`AddDefaultCharset UTF-8`，把`AddDefaultCharset UTF-8`前面的`#`去掉即可。

如下图：

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112521218297.png)

然后重启apache2

```bash
  sudo systemctl restart apache2
```

再次打开，OK，中文网页乱码解决了。

![如何在Ubuntu上安装和配置Apache 2 Web服务器](https://www.linuxidc.com/upload/2018_11/18112521164380.png)

### 6. 一些常见的Apache管理命令

设置Web服务器后，您可能必须在Apache上执行一些基本的管理操作。 以下是您可以在终端应用程序中输入的用于这些操作的命令。

```bash
sudo systemctl start apache2  //将此命令用作sudo以启动Apache服务器。

sudo systemctl stop apache2  //将此命令用作sudo，以便在Apache服务器处于启动模式时停止它。

sudo systemctl restart apache2  //将此命令用作sudo以便停止然后再次启动Apache服务。

sudo systemctl reload apache2  //将此命令用作sudo，以便在不重新启动连接的情况下应用配置更改。

sudo systemctl启用apache2  //将此命令用作sudo，以便在每次启动系统时启用Apache。

sudo systemctl disable apache2  //将Apache设置为每次启动系统时启动

```



### 7. 总结

通过本文，您学习了如何在Ubuntu系统上安装和配置Apache Web服务器。 这包括对您的UFW防火墙进行一些更改，然后为您的IP地址配置Web服务器。 我们还建议您通过Apache设置虚拟主机; 这将为您提供如何使用Apache在Internet上托管文件的基础。 基本的Apache管理命令还可以帮助您作为Web管理员以最佳方式管理Web服务器。

Linux公社的RSS地址：https://www.linuxidc.com/rssFeed.aspx

**本文永久更新链接地址**：https://www.linuxidc.com/Linux/2018-11/155507.htm