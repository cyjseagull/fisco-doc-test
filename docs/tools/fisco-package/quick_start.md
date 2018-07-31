# FISCO-BCOS物料包快速部署

## 安装依赖  
- 机器配置: 参考FISCO BCOS区块链操作手册：[机器配置](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/environment.html)  
  
- 安装软件依赖 
```bash
git 
dos2unix 
lsof 
java[1.8+]

[CentOS Install]
sudo yum -y install git 
sudo yum -y install dos2unix
sudo yum -y install java 
sudo yum -y install lsof

[Ubuntu Install]
sudo apt install git
sudo apt install lsof
sudo apt install openjdk-8-jre-headless
sudo apt install tofrodos
ln -s /usr/bin/todos /usr/bin/unix2dos 
ln -s /usr/bin/fromdos /usr/bin/dos2unix 
```

- 其他依赖：当前执行用户有sudo权限

## 零开始搭建区块链

### 获取fisco-package-build-tool工具包  
 
```bash
git clone https://github.com/FISCO-BCOS/fisco-package-build-tool.git 
chmod a+x format.sh ; dos2unix format.sh ; ./format.sh
```

### 配置节点信息

```bash
$ cd fisco-package-build-tool
$ vim installation_config.sh
```

下面以在三台服务器上分别启动两个节点为例子，参考配置如下：

```bash
#github path for FISCO BCOS
FISCO_BCOS_GIT="https://github.com/FISCO-BCOS/FISCO-BCOS.git"
#local FISCO BCOS path, if FICSO BSOC is not exist in the path, pull it from the github.
FISCO_BCOS_LOCAL_PATH="../"

# default config for temp block node, if the port already exist, please change the following config.
P2P_PORT_FOR_TEMP_NODE=30303
RPC_PORT_FOR_TEMP_NODE=8545
CHANNEL_PORT_FOR_TEMP_NODE=8821

# config for the blockchain node
# the first node is the genesis node
# field 0 : p2p_network_ip
# field 1 : listen_network_ip
# field 2 : node number on this host
# field 3 : identity type
# field 4 : crypto mode
# field 5 : super key
# filed 6 : agency info

weth_host_0=("172.20.245.42" "172.20.245.42" "2" "1" "0" "d4f2ba36f0434c0a8c1d01b9df1c2bce" "agent_0")
weth_host_1=("172.20.245.43" "172.20.245.43" "2" "1" "0" "d4f2ba36f0434c0a8c1d01b9df1c2bce" "agent_1")
weth_host_2=("172.20.245.44" "172.20.245.44" "2" "1" "0" "d4f2ba36f0434c0a8c1d01b9df1c2bce" "agent_2")

MAIN_ARRAY=(
weth_host_0[@]
weth_host_1[@]
weth_host_2[@]
)
```

配置的详细说明如下：

```eval

FISCO_BCOS_GIT               FISCO-BCOS git源码路径，默认为https://github.com/FISCO-BCOS/FISCO-BCOS.git
FISCO_BCOS_LOCAL_PATH        FISCO-BCOS源码存放路径(若源码已在该路径存在，不会从git拉源码)
                             (注: 由于国内git访问速度慢，建议手动下载FISCO-BCOS到该目录)

P2P_PORT_FOR_TEMP_NODE       构建安装包时创建的temp节点的p2p端口, rpc端口, channel端口
RPC_PORT_FOR_TEMP_NODE       (注: 一般不需改动,但要确定这些端口没被占用)
CHANNEL_PORT_FOR_TEMP_NODE

weth_host_n                  第n台服务器的配置，配置包括:
			     (1) p2p_network_ip(第一个字段):  p2p连接ip
                             (2) listen_network_ip(第二个字段): 监听ip,填写实际的网络的ip, 不要填写0.0.0.0
                             (3) node number on this host(第三个字段): 创建的节点数目
                             (4) identity type(第四个字段):
                             (5) crypto mode(第五个字段):
                             (6) super key(第六个字段):
                             (7) agency info(第七个字段):

```
* weth\_host\_n是第n台服务器的配置。  
* field 0(p2p_network_ip)： p2p连接的网段ip, 根据p2p网络的网段配置。
* field 1(listen_network_ip)： 监听网段, 用来接收rpc、channel连接请求, 注意这里填写实际的网段的ip, 不要填写0.0.0.0。
* field 2(node number on this host)：在该服务器上面需要创建的节点数目。  
* field 3(identity type)：节点类型, "1"：记账节点,  "0"：观察节点 , 推荐默认值：1。 
* field 4(crypto mode)： 落盘加密开关: "0":关闭,  "1":开启 , 推荐默认值 0。  
* field 5(super key)： 落盘加密相关, 无特殊情况不用修改。  
* field 6(agency info)： 机构名称, 不关心机构则可以随意值, 但不能为空。  
比如：weth_host_0=("172.20.245.42" "172.20.245.42" "2" "1" "0" "d4f2ba36f0434c0a8c1d01b9df1c2bce" "agent_0") 是第一台服务器上面的配置, 说明需要在172.20.245.42这台服务器上面启动两个节点。

**配置说明：**  
1. 工具在构建安装包(非扩容流程)过程中会启动一个temp节点, 用于系统合约的部署, 注册创世节点信息到节点管理合约, 生成genesis.json文件。  
2. 每个节点需要占用三个端口:p2p port、rpc port、channel port, 对于单台服务器上的节点端口使用规则, 默认从temp节点的端口+1开始, 依次增长。例如temp节点的端口配置为了p2p port 30303、rpc port 8545、channel port 8821, 则每台服务器上的第0个节点默认使用p2p port 30304、rpc port 8546、channel port 8822，第1个节点默认使用p2p port 30305、rpc port 8547、channel port 8823, 以此类推, 要确保这些端口没有被占用。  
3. 工具构建安装包过程中会涉及到从github上面拉取FISCO BCOS、编译FISCO BCOS流程, 具体规则如下：  
  a、首先检查/usr/local/bin目录下是否存在fisco-bcos文件,  若存在则说明fisco-bcos已经被编译安装, 不存在则继续流程b 。   
  b、判断配置文件中FISCO_BCOS_LOCAL_PATH的路径是否存在名为FISCO-BCOS的文件夹, 存在则说明FISCO-BCOS源码已经存在, 直接进入FISCO-BCOS目录进行编译、安装流程, 否则进行流程c。  
  c、从FISCO_BCOS_GIT配置的github地址拉取FISCO-BCOS源码, 拉取完成之后进入FISCO-BCOS目录, 进行FISCO BCOS的编译安装流程, 编译生成的文件为fisco-bcos, 安装目录为/usr/local/bin。  

### 创建安装包

```bash
$ ./generate_installation_packages.sh build
```

* 执行完脚本以后在当前目录会自动生成**build**目录, 在build目录下生成每台机器的安装包, 其中带有**genesis**字样的为创世节点所在服务器的安装包。  
按照示例配置, 会生成下面的四个文件：
```
ls build/
172.20.245.44_with_172.20.245.44_installation_package
172.20.245.43_with_172.20.245.43_installation_package
172.20.245.42_with_172.20.245.42_genesis_installation_package
temp
```
其中temp目录为临时节点的目录,不需要关心, 其余的几个包分别为对应服务器上节点的安装包。  
安装包的目录结构：

```shell
创世节点服务器安装包目录内容：
dependencies  fisco-bcos  install_node.sh  node_action_info_dir  node_manager.sh  

非创世节点服务器安装包目录内容：
dependencies  fisco-bcos  install_node.sh   
```
创世节点跟非创世节点相比多了node_manager.sh脚本跟node_action_info_dir目录。  
* node_manager.sh用来执行节点信息注册、取消、查询功能, 即操作节点管理合约。  
* node_action_info_dir目录保存了本次创建的所有节点的信息(包括创世节点与非创世节点)。按照示例中的配置node_action_info_dir目录下的内容为:  
```shell
nodeactioninfo_172.20.245.42_0.json  nodeactioninfo_172.20.245.42_1.json 
nodeactioninfo_172.20.245.43_0.json  nodeactioninfo_172.20.245.43_1.json 
nodeactioninfo_172.20.245.44_0.json  nodeactioninfo_172.20.245.44_1.json 
```
* 节点信息文件名的格式为nodeactioninfo_IP_IDX, IDX从0开始, 表示该服务器生成的第几个节点。

* install_node.sh脚本用来生成本机的数据目录、启动、停止脚本, 每个目录下都存在。

**注意**：
- [x]  1. 执行./generate_installation_packages.sh build 如果出错, 解决问题重新执行之前, 需要将错误执行生成的build目录删除, 才能重新执行。
- [x]  2. 生成的安装包最好不要部署在build目录内, 部署在build目录时, 启动的fisco-bcos进程也会在build目录下启动, 会导致build目录无法删除, 下次想重新生成其他安装包时可能引发一些问题。

### 上传安装包  
将安装包上传到对应的服务器, 注意上传的安装包必须与服务器相对应, 否则搭链过程会出错。


### 准备
* 需要先部署创世节点的安装包，再部署非创世节点的安装包。
* 创世节点和非创世节点的部署步骤完全一致。只是非创世节点需要多做一步“添加节点”的操作(参考FISCO-BCOS使用手册[[多节点组网]](https://github.com/FISCO-BCOS/FISCO-BCOS/tree/master/doc/manual#第六章-多节点组网))。

### 执行安装脚本

```bash
$ ./install_node.sh install
```

执行完脚本以后会在当前目录自动生成： 
* build目录
* 启动脚本start_nodeN.sh：服务器上面配置生成多少个节点, 就会生成多少个启动脚本, N从0开始。
* 停止脚本stop_nodeN.sh：服务器上面配置生成多少个节点, 就会生成多少个停止脚本, N从0开始。  
上面配置的172.20.245.42服务器执行./install_node install后目录如下：
```
build         fisco-bcos       monitor.sh            node_manager.sh  start_node1.sh  stop_node0.sh
dependencies  install_node.sh  node_action_info_dir  start_node0.sh   stop_node1.sh
```

### 启动节点

```sh
$ ./start_nodeN.sh
```
* 启动第N个节点, 启动后可以使用```ps -ef|egrep fisco-bcos```查看进程是否存在
* 如果需要停止这台机器上的对应节点，可以运行同一个目录下的```
./stop_nodeN.sh```

### 添加节点到节点管理合约

节点组网
* 添加节点的操作只能在创世节点所在的服务器的安装目录进行，所有节点信息文件都会自动保存到<span style="color:red">创世节点安装目录根目录下的`node_action_info_dir`</span>目录。  
 以上述示例中的配置为例, 创世节点所在的
  `node_action_info_dir`中的内容如下：
  
```
$ ls
nodeactioninfo_172_20_245_42_0.json  nodeactioninfo_172_20_245_43_0.json  nodeactioninfo_172_20_245_44_0.json
nodeactioninfo_172_20_245_42_1.json  nodeactioninfo_172_20_245_43_1.json  nodeactioninfo_172_20_245_44_1.json
```

  使用`node_manager.sh`脚本进行添加, 格式为 ：   ./node_manager.sh registerNode 节点信息文件路径（绝对路径）
  例如,如果需要添加这台服务器上的第0个节点：

  ```sh
  $ ./node_manager.sh registerNode /root/172.20.245.42_with_172.20.245.42_genesis_installation_package/node_action_info_dir/nodeactioninfo_172_20_245_42_0.json
  ```

* 每个节点的节点信息文件的文件名都包含了ip信息和index信息, 用于区分, 例如`nodeactioninfo_172_20_245_42_0.json`, 最后的那个"0"字符就是表示这是172_20_245_42这台服务器上面的第0个节点node0的节点信息文件。
* 建议每个节点在启动之后, 然后再执行node_manager.sh进行添加。 
* ./node_manager.sh registerNode xxx 过程中如果命令被卡主, 一直不返回, 说明链可能出现错误, 参考FAQ里面的内容解决。

验证  
    每注册一个节点可以在对应服务器的安装目录下执行：
```shell
tail -f build/nodedir0/log/info*log | egrep "Generating seal"
INFO|2018-04-03 14:16:42:588|+++++++++++++++++++++++++++ Generating seal on8e5add00c337398ac5e9058432037aa646c20fb0d1d0fb7ddb4c6092c9d654fe#1tx:0,maxtx:1000,tq.num=0time:1522736202588
INFO|2018-04-03 14:16:43:595|+++++++++++++++++++++++++++ Generating seal ona98781aaa737b483c0eb24e845d7f352a943b9a5de77491c0cb6fd212c2fa7a4#1tx:0,maxtx:1000,tq.num=0time:1522736203595
```
    可看到周期性的出现上面的日志，表示节点间在周期性的进行共识，节点注册正常。

### 重新登录  
每个安装服务器都会安装nodejs、babel-node、ethconsole, 环境变量写入当前安装用户的.bashrc文件, 使用这些工具需要重新退出当前登录用户, 重新登录一次。

### 部署成功
可以通过发送交易是否成功判断链是否搭建成功。 
在创世节点安装根目录下执行 ：  
cd dependencies/tool/   
然后测试合约部署是否正常： 
babel-node deploy.js Ok  

```
babel-node deploy.js Ok
RPC=http://0.0.0.0:8546
Ouputpath=./output/
deploy.js  ........................Start........................
Soc File :Ok
Ok
Ok编译成功！
发送交易成功: 0x30cbf34f57386c3d435dcdb4b15e03e6370f52eecef307664eed16fd806dd4d9
Ok合约地址 0xa40c864c28ee8b07dc2eeab4711e3161fc87e1e2
Ok部署成功！
cns add operation => cns_name = Ok
         cns_name =>Ok
         contract =>Ok
         version  =>
         address  =>0xa40c864c28ee8b07dc2eeab4711e3161fc87e1e2
         abi      =>[{"constant":false,"inputs":[{"name":"num","type":"uint256"}],"name":"trans","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]
===>> namecall params = {"contract":"ContractAbiMgr","func":"addAbi","version":"","params":["Ok","Ok","","[{\"constant\":false,\"inputs\":[{\"name\":\"num\",\"type\":\"uint256\"}],\"name\":\"trans\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"get\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"}]","0xa40c864c28ee8b07dc2eeab4711e3161fc87e1e2"]}
发送交易成功: 0x268daabbf8591c4ee93c59ea0e881b6dcdf56316ebae5f4078279f6859c39ffb
```

## 物料包生成的证书文件说明

```eval_rst
+----------------------+---------------------------------------------------------------------+
| god账号公钥信息目录  | 创世节点的dependencies/cert/godInfo.txt                             |
|		       | (在项目根目录下执行`find . -name godInfo.txt` 可找到具体路径)       |
+----------------------+---------------------------------------------------------------------+
| 链的根证书           | 创世节点的dependencies/cert/ca.crt	                             |
| 机构证书             | 创世节点的dependencies/cert/${agency_name}/agency.crt               | 
|		       | (${agency_name}是机构名，如agent_0, agent_1等)                      |
|		       | (在项目根目录下执行`find . -name agency.crt`可找到全部机构证书路径) |
+----------------------+---------------------------------------------------------------------+
```
