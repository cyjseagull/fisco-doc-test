# 区块链快速扩容

对以前的已经在跑的区块链, 可以提供其创世节点的相关文件, 创建出一个非创世节点, 使其可以连接到这条区块链。
## 从创世节点的机器上拷贝下面的的3个文件，放到区块链安装包创建工具所在的机器：
  * genesis.json
  * bootstrapnodes.json : 创世节点的连接ip信息。
  * syaddress.txt : 系统合约的地址。  
- [x]   这几个文件位于创世节点所在机器的安装目录下的dependencies子目录。
- [x]   区块链安装包创建工具所在的服务器如果之前没有编译、安装FISCO BCOS时, 也可以把创世节点上的fisco-bcos文件拿下来，放入/usr/local/bin目录下, 这样就可以不用重新编译FISCO BCOS.

## 配置

配置需要扩容的节点的信息,这个配置文件在区块链安装包创建工具的安装目录的根目录：
```sh
vim specific_genesis_node_scale_config.sh
```
参考的demo配置如下：

```shell
p2p_network_ip="127.0.0.1"
listen_network_ip="127.0.0.1"
node_number=2
identity_type=1
crypto_mode=0
super_key="d4f2ba36f0434c0a8c1d01b9df1c2bce"
agency_info="agent_test"

genesis_json_file_path=/fisco-bcos/fisco-package-build-tool/build/test/dependencies/genesis.json
genesis_node_info_file_path=/fisco-bcos/fisco-package-build-tool/build/test/dependencies/bootstrapnodes.json
genesis_system_address_file_path=/fisco-bcos/fisco-package-build-tool/build/test/dependencies/syaddress.txt
genesis_ca_dir_path=/fisco-bcos/fisco-package-build-tool/build/test/dependencies/cert/
```
配置解释：
* p2p_network_ip：   p2p连接的网段ip, 根据p2p网络的网段配置。
* listen_network_ip：   监听网段ip, 用来接收rpc、channel、ssl连接请求, 建议配置为"0.0.0.0"。
* node_number：   在该服务器上面需要创建的节点数目。  
* identity_type： 节点类型, "1"：记账节点,  "0"：观察节点。 
* crypto_mode：   落盘加密开关: "0":关闭,  "1":开启。  
* super_key：     落盘加密的秘钥, 一般情况不用修改。
* agency_info：   机构名称, 如果不区分机构, 值随意。
  
* genesis_json_file_path   genesis.json的路径
* genesis_node_info_file_path   bootstrapnodes.json的路径
* genesis_system_address_file_path            syaddress.txt的路径
* genesis_ca_dir_path  链的相关证书目录

## 生成安装包

```shell
$ ./generate_installation_packages.sh expand
```
生成的安装包在`build/`目录下

## 安装启动节点
将安装包上传至服务器, 进入目录, 执行./intall_node.sh install  
依次执行 ./start_nodeN.sh启动节点  
可以通过 ps -aux | egrep fisco-bcos查看节点是否正常启动

## 添加新增节点到节点管理合约
将新节点的安装目录下dependencies/node_action_info_dir的nodeactioninfo_xxxxxxxxxxxx.json文件, 放入创世节点所在服务器的安装目录的node_action_info_dir, 然后执行node_manager.sh命令将新添加的节点注册到管理合约。

## 相关链接  
- [FISCO BCOS WIKI](https://github.com/FISCO-BCOS/Wiki)  
- [一键安装FISCO BCOS脚本](https://github.com/FISCO-BCOS/FISCO-BCOS/tree/master/sample)  
- [FISCO BCOS区块链操作手册](https://github.com/FISCO-BCOS/FISCO-BCOS/tree/master/doc/manual)

## FAQ

- 重要的目录说明   
安装完成之后FISCO-BCOS/tool FISCO-BCOS/systemcontractv对应的路径为：
dependencies/tool/  
dependencies/systemcontract

- 一定要确保安装的机器上面的各个节点的端口都没有被占用, 当前服务器上面的端口配置可以查看安装目录下的 build/nodedirN/config.json 文件, 可以使用 netstat -anp | egrep 端口号 , 查看端口是否被占用。
 	```sh
	    "rpcport":"8546",
        "p2pport":"30304",
        "channelPort":"8822",
	```

- 一定要确保各个机器之前可以连接, 端口是放开的, 可以通过ping检查各个机器之前的网络连接, 使用telnet检查端口是否开通。
- 如果构建安装包过程有出错，但不知道错误在哪里，可以这样执行构建脚本：

	```sh
	$ bash -x generate_installation_packages.sh build
	```
- 如果安装过程有出错，但不知道错误在哪里，可以这样安装脚本：

	```sh
	$ bash -x install_node.sh install
	```
	
- 执行启动脚本start_node0.sh后, ps -aux | egrep fisco发现进程不存在, 可以查看./build/nodedir0/log/log文件的内容, 里面会有具体的报错内容。  
常见的一些报错如下：  
a. 
```
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<dev::eth::DatabaseAlreadyOpen>'
  what():  DatabaseAlreadyOpen  
```
进程已经启动, 使用ps -aux | egrep fisco-bcos查看。  

b.
```
./fisco-bcos: error while loading shared libraries: libleveldb.so.1: cannot open shared object file: No such file or directory 
```

leveldb动态库缺失, 安装脚本里面默认使用 yum/apt 对依赖组件进行安装, 可能是 yum/apt 源缺失该组件。  
可以使用下面命令手动安装leveldb, 若leveldb安装不成功可以尝试替换yum/apt的源。
```
[CentOS]sudo yum -y install leveldb-devel
[Ubuntu]sudo apt-get -y install libleveldb-dev

```  
c.
```
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<dev::FileError>' what():  FileError
```

操作文件失败抛出异常, 原因可能是当前登录的用户没有安装包目录的权限, 可以通过ls -lt查看当前文件夹对应的user/group/other以及对应的权限, 一般可以将安装包的user改为当前用户或者切换登录用户为安装包的user用户即可。  

-- Not Found xx 这种打印说明, 安装工具自动安装对应的安装包失败, 可以使用对应的yum/apt工具进行手动安装, 手动安装失败则说明对应的源没有改软件, 建议更换yum/apt源。  
安装的命令列表如下：

```
 Utuntu安装命令：
        [OpenSSL] sudo apt-get -y install openssl libssl-dev libkrb5-dev
        [leveldb] sudo apt-get -y install libleveldb-dev
        [CURL]    sudo apt-get -y install libcurl4-openssl-dev
        [mhd]     sudo apt-get -y install libmicrohttpd-dev
        [gmp]     sudo apt-get -y install libgmp-dev 
        
CentOS安装命令：
        [OpenSSL] sudo yum -y install openssl openssl-devel
        [leveldb] sudo yum -y install leveldb-devel
        [CURL]    sudo yum -y install curl-devel 
        [mhd]     sudo yum -y install libmicrohttpd-devel
        [gmp]     sudo yum -y install gmp-devel
```
