# <a name="FAQ" id="FAQ">FAQ</a>
## generate_installation_packages.sh build/expand 报错提示.
- ERROR - build directory already exist, please remove it first.  
fisco-package-build-tool目录下已经存在build目录, 可以将build目录删除再执行。
- ERROR - no sudo permission, please add youself in the sudoers.  
当前登录的用户需要有sudo权限.
- ERROR - Unsupported or unidentified Linux distro.  
当前linux系统不支持, 目前FISCO-BCOS支持CentOS 7.2+、Ubuntu 16.04.
- ERROR - Unsupported Ubuntu Version. At least 16.04 is required.  
当前ubuntu版本不支持, 目前ubuntu版本仅支持ubuntu 16.04 64位操作系统.
- ERROR - Unsupported CentOS Version. At least 7.2 is required.  
当前CentOS系统不支持, 目前CentOS支持7.2+ 64位.
- ERROR - Unsupported Oracle Linux, At least 7.4 Oracle Linux is required.  
当前Oracle Linux不支持, 当前Oracle支持7.4+ 64位.
- ERROR - Unsupported Linux distribution    
不支持的linux系统.目前FISCO-BCOS支持CentOS 7.2+、Ubuntu 16.04.
- ERROR - Oracle JDK 1.8 be requied  
需要安装Oracle JDK 1.8.
- ERROR - OpenSSL 1.0.2 be requied  
openssl需要1.0.2版本.
- ERROR - XXX is not installed.  
XXX没有安装.  
- ERROR - FISCO BCOS gm version not support yet.  
物料包不支持国密版本的FISCO BCOS的安装.
- ERROR - At least FISCO-BCOS 1.3.0 is required.  
物料包工具支持的FISCO BCOS的最小版本为v1.3.0
- ERROR - Required version is xxx, now fisco bcos version is xxxx"  
当前fisco-bcos版本与配置的版本不一致, 建议手动编译自己需要的版本.
不支持国密版本的fisco-bcos环境搭建.
- ERROR - temp node rpc port check, XXX is in use.  
temp节点使用的rpc端口被占用, 可以netstat -anp | egrep XXX查看占用的进程是哪个. 
- ERROR - temp node channel port check, XXX is in use.  
temp节点使用的channel端口被占用, 可以netstat -anp | egrep XXX查看占用的进程是哪个. 
- ERROR - temp node p2p port check, XXX is in use.  
temp节点使用的p2p端口被占用, 可以netstat -anp | egrep XXX查看占用的进程是哪个. 
- ERROR - git clone FISCO-BCOS failed.  
下载FISCO-BCOS源码失败, 建议手动下载.  
- ERROR - system contract address file is not exist, web3sdk deploy system contract not success.  
temp节点部署系统合约失败.

## generate_installation_packages.sh build/expand 直接退出.
查看build/stderr.log内容, 看错误信息.


## start.sh 显示nodeIDX is not running.  
这个提示是说nodeIDX启动失败, 可以ps -aux | egrep fisco 查看是否正常启动. 可以执行`cat node/nodedirIDX/log/log`查看节点启动失败的原因. 
常见的原因:
- libleveldb.so No such file or directory.
```
./fisco-bcos: error while loading shared libraries: libleveldb.so.1: cannot open shared object file: No such file or directory 
```
leveldb动态库缺失, 安装脚本里面默认使用 yum/apt 对依赖组件进行安装, 可能是 yum/apt 源缺失该组件。  
可以使用下面命令手动安装leveldb, 若leveldb安装不成功可以尝试替换yum/apt的源。
```
[CentOS]sudo yum -y install leveldb-devel
[Ubuntu]sudo apt-get -y install libleveldb-dev

```  
如果leveldb已经安装, 则可以尝试执行`sudo ldconfig`, 然后执行start.sh, 重新启动节点.

- FileError
```
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<dev::FileError>' what():  FileError
```

操作文件失败抛出异常, 原因可能是当前登录的用户没有安装包目录的权限, 可以通过ls -lt查看当前文件夹对应的user/group/other以及对应的权限, 一般可以将安装包的user改为当前用户或者切换登录用户为安装包的user用户即.
