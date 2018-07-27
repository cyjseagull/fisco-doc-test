# 编译安装

## 国密版FISCO BCOS编译安装

  本章详细介绍如何编译并部署国密版FISCO BCOS, 由于国密版FISCO BCOS是在非国密版FISCO BCOS基础上启用了国密算法，因此其部署方法、对机器配置的要求类似于非国密版FISCO BCOS, 详细信息可参考[FISCO BCOS区块链操作手册](manual#%E7%AC%AC%E4%B8%80%E7%AB%A0-%E9%83%A8%E7%BD%B2fisco-bcos%E7%8E%AF%E5%A2%83)。

## 依赖软件部署

<br>

**部署FISCO BCOS依赖软件包：**

可参考[FISCO BCOS区块链操作手册的**安装依赖包**](manual#121-%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96%E5%8C%85)一节。


## 编译国密版FISCO BCOS


> **(1) 拉取源码**

部署FISCO BCOS之前需要安装git, dos2unix, lsof依赖软件

-  git：用于拉取最新代码
-  dos2unix && lsof: 用于处理windows shell脚本上传到linux服务器时，文件格式无法被linux正确解析的问题；

可用如下命令安装这些软件：

```shell
[centos]
sudo yum -y install git
sudo yum -y install dos2unix
sudo yum -y install lsof

[ubuntu]
sudo apt install git
sudo apt install lsof
sudo apt install tofrodos
ln -s /usr/bin/todos /usr/bin/unxi2dos
ln -s /usr/bin/fromdos /usr/bin/dos2unix
```

> 拉取源码

```bash
#====进入源码存放目录====
$ cd /mydata

#====从git拉取源码=======
$ git clone https://github.com/FISCO-BCOS/FISCO-BCOS
```


> **(2) 安装依赖包**

编译国密版FISCO BCOS前，需要调用FISCO-BCOS/scripts目录下install_deps.sh脚本安装依赖软件包：

```bash
# ====进入FISCO BCOS源码目录(设FISCO-BCOS源码位于/mydata目录)====
$ cd /mydata/FISCO-BCOS

# ==== 为了防止windows脚本上传到linux环境下引起的不兼容问题，使用dos2unix格式化所有脚本===
$ dos2unix `find . -name "*.sh"`

# ==== 调用install_deps.sh脚本安装依赖包====
$ sudo bash scripts/install_deps.sh

```

> **(3) 开启国密版FISCO BCOS编译开关，编译并安装fisco-bcos**

依赖包安装成功后，即可使用如下命令开启国密开关，并编译国密版**FISCO BCOS**：

```bash
#======调用cmake3或cmake产生编译文件Makefile(centos系统使用cmake3和ubuntu系统使用cmake)====
#======FISCO BCOS使用-DENCRYPTTYPE开关控制国密开关：-DENCRYPTTYPE=ON时，在FISCO BCOS中开启国密特性支持；-DENCRYPTTYPE=OFF，在FISCO BCOS中关闭国密特性支持
$ mkdir -p build
$ cd build/

# [centos]
$ cmake3 -DENCRYPTTYPE=ON  -DEVMJIT=OFF -DTESTS=OFF -DMINIUPNPC=OFF .. 
# [ubuntu]
$ cmake  -DENCRYPTTYPE=ON -DEVMJIT=OFF -DTESTS=OFF -DMINIUPNPC=OFF .. 

#===编译源码： 编译成功后，会在eth/目录下生成可执行程序fisco-bcos, 启动节点时，将fisco-bcos链接到该可执行程序即可=====
$ make  #注: 可根据当前主机cpu配置灵活配置编译源码的线程数，如：make -j2 , 表示用2个线程编译FISCO BCOS

# 注: 若上次编译失败，本次继续编译时可能会报错，此时需要删掉源码目录下deps/src/目录中缓存包后继续编译，一般包括如下命令:
# rm -rf deps/src/*-build
# rm -rf deps/src/*-stamp
# make

#===安装 fisco-bcos===
$ sudo make install

```
