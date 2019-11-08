# 配置GitHub SSH

## 1. 生成新的SSH密钥并将其添加到ssh-agent

检查现有SSH密钥后，可以生成一个新的SSH密钥用于身份验证，然后将其添加到ssh-agent中。

如果您还没有SSH密钥，则必须[生成一个新的SSH密钥](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)。如果不确定是否已有SSH密钥，请检查[现有密钥](https://help.github.com/en/enterprise/2.16/user/articles/checking-for-existing-ssh-keys)。

如果不想每次使用SSH密钥时都重新输入密码，则可以[将密钥添加到SSH代理中](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)，该[代理](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)管理SSH密钥并记住密码。

### 1.1  [生成新的SSH密钥](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

1. 打开终端。

2. 粘贴以下文本，替换为您的GitHub Enterprise电子邮件地址。

   ```shell
   $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

   使用提供的电子邮件作为标签，这将创建一个新的ssh密钥。

   ```shell
   > Generating public/private rsa key pair.
   ```

3. 当系统提示您“输入要在其中保存密钥的文件”时，请按Enter。这接受默认文件位置。

   ```shell
   > Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
   ```

4. 在提示符下，键入一个安全密码。有关更多信息，请参阅[“使用SSH密钥密码短语”](https://help.github.com/en/enterprise/2.16/user/articles/working-with-ssh-key-passphrases)。

   ```shell
   > Enter passphrase (empty for no passphrase): [Type a passphrase]> Enter same passphrase again: [Type passphrase again]
   ```

### 1.2 [将SSH密钥添加到ssh-agent](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

在将新的SSH密钥添加到ssh-agent来管理密钥之前，您应该已经[检查了现有的SSH密钥](https://help.github.com/en/enterprise/2.16/user/articles/checking-for-existing-ssh-keys)并[生成了一个新的SSH密钥](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)。

1. 在后台启动ssh-agent。

   ```shell
   $ eval "$(ssh-agent -s)"
   > Agent pid 59566
   ```

2. 将SSH私钥添加到ssh-agent。如果您使用其他名称创建密钥，或者要添加具有其他名称的现有密钥，请使用私有密钥文件的名称替换命令中的*id_rsa*。

   ```shell
   $ ssh-add ~/.ssh/id_rsa
   ```



**完整操作实例：**

```shell
(base) lichenguang@chen-SurfaceLaptop:~$ ssh-keygen -t rsa -b 4096 -C "2725162388@qq.com"
> Generating public/private rsa key pair.
> Enter file in which to save the key (/home/lichenguang/.ssh/id_rsa): 
> Enter passphrase (empty for no passphrase): 
> Enter same passphrase again: 
> Your identification has been saved in /home/lichenguang/.ssh/id_rsa.
> Your public key has been saved in /home/lichenguang/.ssh/id_rsa.pub.
> The key fingerprint is:
> SHA256:/A5v5i7r8FdOB9+SxH5ohP3IfP6epPsVBjZgDMqM6p0 2725162388@qq.com
> The key's randomart image is:
        +---[RSA 4096]----+
        |         .oo     |
        |      + . ...    |
        |     . +     B   |
        |    .  .    + B  |
        |   .    S    O O |
        |  . . .  .  o & *|
        |   . E. . .+ o *.|
        |       o.++ . o +|
        |       .+O=  oo++|
        +----[SHA256]-----+
(base) lichenguang@chen-SurfaceLaptop:~$ eval "$(ssh-agent -s)"
> Agent pid 5251
(base) lichenguang@chen-SurfaceLaptop:~$  ssh-add ~/.ssh/id_rsa
> Enter passphrase for /home/lichenguang/.ssh/id_rsa: 
> Identity added: /home/lichenguang/.ssh/id_rsa (/home/lichenguang/.ssh/id_rsa)
```



## 2. 向您的GitHub帐户添加新的SSH密钥

要配置GitHub Enterprise帐户以使用新的（或现有的）SSH密钥，您还需要将其添加到GitHub Enterprise帐户中。

在将新的SSH密钥添加到GitHub Enterprise帐户之前，您应该具有：

- [检查现有的SSH密钥](https://help.github.com/en/enterprise/2.16/user/articles/checking-for-existing-ssh-keys)
- [生成一个新的SSH密钥并将其添加到ssh-agent](https://help.github.com/en/enterprise/2.16/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

将新的SSH密钥添加到GitHub Enterprise帐户后，您可以重新配置任何本地存储库以使用SSH。有关更多信息，请参阅“将[远程URL从HTTPS切换到SSH”](https://help.github.com/en/enterprise/2.16/user/articles/changing-a-remote-s-url/#switching-remote-urls-from-https-to-ssh)。

**注意：** OpenSSH 7.0中不推荐使用DSA密钥。如果您的操作系统使用OpenSSH，则在设置SSH时需要使用其他类型的密钥，例如RSA密钥。例如，如果您的操作系统是MacOS Sierra，则可以使用RSA密钥设置SSH。

1. 将SSH密钥复制到剪贴板。

   如果您的SSH密钥文件的名称与示例代码的名称不同，请修改文件名以匹配当前设置。复制密钥时，请勿添加任何换行符或空格。

   ```shell
   $ sudo apt-get install xclip
   # Downloads and installs xclip. If you don't have `apt-get`, you might need to use another installer (like `yum`)
   
   $ xclip -sel clip < ~/.ssh/id_rsa.pub
   # Copies the contents of the id_rsa.pub file to your clipboard
   ```

   **提示：**如果`xclip`不起作用，则可以找到隐藏的`.ssh`文件夹，在您喜欢的文本编辑器中打开文件，然后将其复制到剪贴板。

2. 在任何页面的右上角，点击您的个人资料照片，然后点击**设置**。

   ![用户栏中的设置图标](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/userbar-account-settings.png)

   

3. 在用户设置边栏中，点击**SSH和GPG密钥**。

   ![认证密钥](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/settings-sidebar-ssh-keys.png)

   

4. 单击“ **新建SSH密钥”**或“ **添加SSH密钥”**。

   ![SSH密钥按钮](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/ssh-add-ssh-key.png)

   

5. 在“标题”字段中，为新密钥添加一个描述性标签。例如，如果您使用的是个人Mac，则可以将此键称为“个人MacBook Air”。

6. 将您的密钥粘贴到“密钥”字段中。

   ![关键领域](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/ssh-key-paste.png)

   

7. 单击**添加SSH密钥**。

   ![添加键按钮](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/ssh-add-key.png)

   

8. 如果出现提示，请确认您的GitHub Enterprise密码。

   ![Sudo模式对话框](https://github-images.s3.amazonaws.com/enterprise/2.16/assets/images/help/settings/sudo_mode_popup.png)

## 3. 配置global参数

```shell
*** 请告诉我你是谁。

运行

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

来设置您账号的缺省身份标识。
如果仅在本仓库设置身份标识，则省略 --global 参数。


```

