# 编译web3sdk

``` important:: **使用web3sdk之前，请进行如下环境检查**

     FISCO BCOS节点环境搭建完成：
       参考 `FISCO-BCOS入门 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/index.html>`_
     java: 
       要求 `jdk1.8+ <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_，推荐使用jdk8u141
     网络连通性检查: 
       检查web3sdk要连接的FISCO BCOS节点channelPort是否能telnent通，若telnet不通，需要检查网络连通性和安全策略
```

## 安装依赖软件 

部署web3sdk之前需要安装git, dos2unix依赖软件:
-  **git**：用于拉取最新代码
-  **dos2unix**: 用于处理windows文件上传到linux服务器时，文件格式无法被linux正确解析的问题；
可使用如下命令安装这些软件：
```shell
[centos]
sudo yum -y install git
sudo yum -y install dos2unix
[ubuntu]
sudo apt install git
sudo apt install tofrodos
ln -s /usr/bin/todos /usr/bin/unxi2dos
ln -s /usr/bin/fromdos /usr/
```

## 拉取并编译源码

执行如下命令拉取并编译源码：
```bash
#=== 创建并进入web3sdk源码放置目录（假设为/mydata/）=====
$ mkdir -p /mydata
$ cd /mydata

#==== 拉取git代码 ====
$ git clone https://github.com/FISCO-BCOS/web3sdk

#===编译we3bsdk源码，生成dist目录 ===
$ cd web3sdk
$ dos2unix *.sh
$ bash compile.sh

#===编译成功后，web3sdk目录下生成dist文件夹，目录结构如下==========
$ tree -L 2
.
├── build
│   ├── classes
│   ├── reports
│   ├── resources
│   ├── test-results
│   └── tmp
├── build.gradle
├── ca.crt
├── client.keystore
├── dist
│   ├── apps
│   ├── bin
│   ├── contracts
│   └── lib
├── README.md
├── src
│   ├── main
│   └── test
└── tools
    ├── bin
    └── contracts

```
dist目录下各个目录包含的内容如下：

```eval_rst
+---------------+-------------------------------------------------------------------------------------+
|目录           | 说明                                                                                |
+===============+=====================================================================================+
|dist/apps      | 存放web3sdk编译生成的jar包web3sdk.jar                                               |
+---------------+-------------------------------------------------------------------------------------+
|               |  - web3sdk: 调用web3sdk.jar执行web3sdk内方法(如部署系统合约、调用合约工具方法等)    |
|dist/bin       |  - compile.sh: 将dist/contracts目录下的合约代码转换成java代码，供开发者使用         |
+---------------+-------------------------------------------------------------------------------------+
|dist/conf      | 配置目录, 用于配置节点信息、证书信息、日志目录等                                    |
+---------------+-------------------------------------------------------------------------------------+
|dist/contracts | 合约存放目录，compile.sh脚本可将存放于该目录下的合约代码转换成java代码              |
+---------------+-------------------------------------------------------------------------------------+
|dist/lib       | 存放web3sdk依赖库的jar包                                                            |
+---------------+-------------------------------------------------------------------------------------+

