# 编译安装

## 拉取源码

```eval_rst

.. admonition:: 安装依赖软件

   .. code-block:: bash

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

.. admonition:: 安装国密版智能合约编译器
   
   .. code-block:: bash
   
      [ubuntu]:
      wget https://github.com/FISCO-BCOS/fisco-solc/raw/master/fisco-solc-guomi-ubuntu
      sudo cp fisco-solc-guomi-ubuntu  /usr/bin/fisco-solc-guomi
      sudo chmod +x /usr/bin/fisco-solc-guomi
      [centos]:
      wget https://github.com/FISCO-BCOS/fisco-solc/raw/master/fisco-solc-guomi-centos
      sudo cp fisco-solc-guomi-centos  /usr/bin/fisco-solc-guomi
      sudo chmod +x /usr/bin/fisco-solc-guomi

.. admonition:: 拉取源码
   
   .. code-block:: bash

      # 进入源码存放目录
      $ cd /mydata
      
      # 从git拉取源码
      $ git clone https://github.com/FISCO-BCOS/FISCO-BCOS

```

## 编译源码

```eval_rst

.. admonition:: 编译国密版FISCO BCOS

   安装依赖包(执行scripts/install_deps.sh脚本)：
     .. code-block:: bash

        # 进入FISCO BCOS源码目录(设FISCO-BCOS源码位于/mydata目录)
        $ cd /mydata/FISCO-BCOS
        
        # 为了防止windows脚本上传到linux环境下引起的不兼容问题，使用dos2unix格式化所有脚本
        $ dos2unix `find . -name "*.sh"`
        
        # 调用install_deps.sh脚本安装依赖包
        $ sudo bash scripts/install_deps.sh
   
   编译国密版FISCO-BCOS(-DENCRYPTTYPE=ON)：
     .. code-block:: bash
        
        # 进入源码目录(设位于/mydata目录)
        $ cd /mydata/FISCO-BCOS

        # 调用build.sh脚本编译国密版fisco-bcos
        $ sudo bash build.sh guomi


        # 注: 若上次编译失败，本次继续编译时可能会报错，此时需要删掉源码目录下deps/src/目录中缓存包后重新使用build.sh编译，一般包括如下命令:
        # rm -rf deps/src/*-build
        # rm -rf deps/src/*-stamp
```

## 国密版nodejs环境配置

FISCO BCOS提供init_guomi_nodejs.sh脚本配置nodejs环境：

```bash

# 进入FISCO BCOS源码目录(设FISCO-BCOS源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS

# 调用init_guomi_nodejs.sh脚本初始化nodejs环境
$ cd scripts && bash init_guomi_nodejs.sh
[web3lib]: init guomi nodejs...
[tool]: init guomi nodejs...
[systemcontract]: init guomi nodejs...

# 开启国密开关，设置config.js的encryptType为1
$ vim /mydata/FISCO-BCOS/web3lib/config.js
  var encryptType = 1;// 0:ECDSA 1:sm2Withsm3  

```



