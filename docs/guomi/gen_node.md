# 普通节点环境搭建

## 生成节点证书

证书生成可参考[创世节点证书生成](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/gen_cert.html) ,若普通节点与创世节点属于同一机构，只需生成节点证书即可。

```bash
# 进入脚本所在目录(设源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools/scripts
# 在/mydata/node1/data目录下生成普通节点证书
$ ./generate_node_cert.sh -a test_agency -d /mydata/test_agency/ -n node1 -o /mydata/node1/data -s sdk1 -g

# /mydata/node1/data目录下生成的证书如下:
$ ls /mydata/node1/data/ -1
ca.crt
ca.key
client.keystore
gmagency.crt
gmca.crt
gmennode.crt
gmennode.key
gmnode.ca
gmnode.crt
gmnode.json
gmnode.key
gmnode.nodeid
gmnode.private
gmnode.serial
sdk1
server.crt
server.key

```

## 初始化普通节点环境

类似于 [创世节点环境初始化](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/genesis_node.html#id2)`_ ,普通节点使用generate_node.sh脚本初始化普通节点环境。

```bash
# 进入脚本所在目录(设源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools/scripts

# 查看创世节点信息:
# -d: 指定创世节点目录
# -g: 指定节点类型是国密版FISCO-BCOS
$ ./node_info.sh -d /mydata/node0 -g
-----------------------------------------------------------------
Name:
Node dir:               /mydata/node0
Agency:
CA hash:                D14983471F0AC975
Node ID:                3d4fe4c876cac411d4c7180b5794198fb3b4f3e0814156410ae4184e0a51097a01bf63e431293f30af0c01a57f24477ad1704d8f676bc7e345526ba1735db6a7
RPC address:            127.0.0.1:8545
P2P address:            127.0.0.1:30303
Channel address:        127.0.0.1:8891
SystemProxy address:    0xee80d7c98cb9a840b9c4df742f61336770951875
God address:            0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad
State:                  Running (pid: 11524)
-----------------------------------------------------------------


# 创建普通节点环境:
# 节点目录: /mydata/node1, 监听端口: 127.0.0.1
# rpc端口: 8546, p2p端口: 30304
# channel prot: 8892
# bootstrapnodes.json: 127.0.0.1:30303,127.0.0.1:3030
# 系统合约地址: 0xee80d7c98cb9a840b9c4df742f61336770951875
# 创世节点目录: /mydata/node0
$ ./generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -x 0xee80d7c98cb9a840b9c4df742f61336770951875 -i 3d4fe4c876cac411d4c7180b5794198fb3b4f3e0814156410ae4184e0a51097a01bf63e431293f30af0c01a57f24477ad1704d8f676bc7e345526ba1735db6a7 -s 0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad -g
# 创建节点环境
---------- Generate node basic files ----------
RUN: sh generate_node_basic.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -x 0xee80d7c98cb9a840b9c4df742f61336770951875 -g
#...此处省略若干行....
SUCCESS execution of command: sh generate_node_basic.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -x 0xee80d7c98cb9a840b9c4df742f61336770951875 -g
# 创建普通节点genesis.json
---------- Generate node genesis file ----------
# ... 此处省略若干行...
# 输出普通节点信息
-----------------------------------------------------------------
Name:
Node dir:               /mydata/node1
Agency:
CA hash:                F4AC757508FF6AB2
Node ID:                9940c84c1964095c7a3e0daa37c5cbe718dfb2a20def6df19ffd84438e307fa63427920fbf76550e13b318ed0464b6832d44f87b6a515e9f3616f58d51c81739
RPC address:            127.0.0.1:8546
P2P address:            127.0.0.1:30304
Channel address:        127.0.0.1:8892
SystemProxy address:    0xee80d7c98cb9a840b9c4df742f61336770951875
God address:            0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad
State:                  Stop
-----------------------------------------------------------------

## generate_node.sh用法
$ ./generate_node.sh -h

Usage:
 -o <output dir> Where node files generate  #普通节点所在目录
 -n <node name> Name of node  #普通节点名称
 -l <listen ip> Node\'s listen IP #普通节点监听IP(推荐填外网IP) 
 -r <RPC port> Node\'s RPC port #普通节点RPC端口
 -p <P2P port> Node\'s P2P port #普通节点P2P端口
 -c <channel port> Node\'s channel port #普通节点channel port
 -e <bootstrapnodes> Node\'s bootstrap nodes    #普通节点bootstrapnode.json配置，主要包括要连接节点的IP和端口
 -a <agency name> The agency name that the node belongs to #普通节点所属机构(国密版搭建过程忽略该参数)
 -d <agency dir> The agency cert dir that the node belongs to #普通节点机构证书目录(国密版搭建过程忽略该参数)
 -i <genesis node id> Genesis node id   #普通节点所属链的创世节点node id
 -s <god address> God address # 普通节点所属链的god账号
 -x <system proxy address> System proxy address of the blockchain # 普通节点所属链的系统合约地址
Optional:
 -m Input agency information manually #手动输入机构证书信息(国密版搭建过程忽略该参数)
 -g Create guomi node #生成国密版普通节点
 -h This help
Example: #非国密版generate_node.sh使用示例
 bash ./generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -d /mydata/test_agency -a test_agency -x 0x919868496524eedc26dbb81915fa1547a20f8998 -i xxxxxx -s xxxxxx
GuomiExample: #国密版generate_node.sh使用示例
 bash ./generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -x 0x919868496524eedc26dbb81915fa1547a20f8998 -i xxxxxx -s xxxxxx -g
```

## 启动节点进程

FISCO BCOS在节点目录下提供 `start.sh`和`stop.sh`来启停节点：

```bash
# 进入节点目录
$ cd /mydata/node1

# 调用start.sh脚本启动进程
$ ./start.sh
```

## check节点环境

启动普通节点后，check普通节点进程和error日志：

```bash
# 查看普通节点进程状态：创世节点和普通节点进程均启动
$ ps aux | grep fisco
root     20995  0.2  0.1 2171448 13316 pts/3   Sl   09:15   0:05 ./fisco-bcos --genesis /mydata/node0/genesis.json --config /mydata/node0/config.json
root     21727  0.7  0.1 2023984 14092 pts/4   Sl   09:52   0:01 ./fisco-bcos --genesis /mydata/node1/genesis.json --config /mydata/node1/config.json

# 通过最新日志check节点连接: 刷出"topics send"日志，表明节点连接正常
$ tail -f /mydata/node1/log_2018081219.log | grep "Send topic"
DEBUG|2018-08-12 19:34:13:659| Send topic Req:0 type:0
DEBUG|2018-08-12 19:34:14:659| Send topic Req:0 type:0
DEBUG|2018-08-12 19:34:15:659| Send topic Req:0 type:0
DEBUG|2018-08-12 19:34:16:659| Send topic Req:0 type:0
DEBUG|2018-08-12 19:34:17:660| Send topic Req:0 type:0
```