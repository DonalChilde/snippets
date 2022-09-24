https://solarianprogrammer.com/2017/06/30/building-python-ubuntu-wsl-debian/

Building Python 3.7 from source on Ubuntu and Debian Linux
Posted on June 30, 2017 by Paul
Updated 27 Nov 2018

This is a short article about building Python 3.7 from source on Ubuntu 18.04 or Debian 9 Linux. At the time of this writing Ubuntu LTS default is Python 3.6 and Debian stable default is Python 3.5. Python 3.7 comes with many more improvements vs the old 3.5 or 3.6 versions. You can read more about what’s new in Python 3.7 here. The procedure described in this tutorial also works with Windows Subsystem for Linux, WSL, aka Bash on Ubuntu on Windows.

As a side note, you should be able to use the same procedure on other Debian based systems, like Raspbian on Raspberry Pi, just replace apt with apt-get and you are good to go.

First, make sure your system is fully updated:

1 sudo apt update
2 sudo apt upgrade
Next, install the default GCC toolchain with:

1 sudo apt install build-essential
Next, we need to install a few prerequisites for building Python:

1 sudo apt install libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev
2 sudo apt install libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev
 <!-- Added -->
3 sudo apt install uuid-dev

At the time of this writing, the latest stable version of Python is 3.7.1, if you want to use a newer version change the next instructions accordingly:

1 wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz
2 tar xf Python-3.7.1.tar.xz
3 cd Python-3.7.1
4 ./configure --enable-optimizations
5 make -j 8
6 sudo make altinstall
Please note the use of sudo make altinstall instead of the typical Linux/Unix sudo make install. Using altinstall will ensure that you don’t mess with the default system Python.

Once the above is finished, you could invoke the new Python interpreter with:

1 python3.7
python3 will invoke the system Python version.

## important: check messages for missing modules. This does not install tkinker
