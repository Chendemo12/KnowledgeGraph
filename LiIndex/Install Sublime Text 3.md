# Install Sublime Text 3 in Ubuntu 16.04 & Higher The Official Way



[![sublime-text-logo](http://tipsonubuntu.com/wp-content/uploads/2015/03/sublime-text-logo-610x302.jpg)](http://tipsonubuntu.com/wp-content/uploads/2015/03/sublime-text-logo.jpg)

The popular cross-platform [Sublime Text](https://www.sublimetext.com/) editor finally offers **official Linux apt repository** to make it easy to install and receive update in Ubuntu.

Sublime Text is a proprietary source code editor with a Python API. It supports many programming languages and markup languages, and its functionality can be extended by users with plugins.

It’s available to download and use for free, but you’re supposed to buy a license if you plan on using it full-time.

#### Install Sublime Text 3 via the official apt repository:

**1.** Open terminal via Ctrl+Alt+T or by searching for “Terminal” from desktop app launcher. When it opens, run command to install the key:

```shell
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

![sublimetext-apt-key](http://tipsonubuntu.com/wp-content/uploads/2017/05/sublimetext-apt-key-610x86.jpg)

**2.** Then add the apt repository via command:

```shell
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

![sublime text apt repository](http://tipsonubuntu.com/wp-content/uploads/2017/05/sublime-text-apt-repo-610x93.jpg)

**3.** Finally check updates and install **sublime-text** via your system package manager:

[![install-sublime-text](http://tipsonubuntu.com/wp-content/uploads/2017/05/install-sublime-text-400x269.jpg)](http://tipsonubuntu.com/wp-content/uploads/2017/05/install-sublime-text.jpg)

or by running commands:

```shell
sudo apt-get update

sudo apt-get install sublime-text
```

Once installed, launch it from your desktop app launcher and enjoy!

#### Uninstall:

To uninstall the editor, either use your system package manager or simply run command:

```shell
sudo apt-get remove sublime-text && sudo apt-get autoremove
```

And the official Sublime Text apt repository can be removed by going to System Settings -> Software & Updates -> Other Software tab.

