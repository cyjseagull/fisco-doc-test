# 搭建创世节点 

```eval_rst
.. admonition:: 注意事项
   
   创建创世节点配置genesis.json前，必须确保已在创世节点data目录生成了节点证书，参考 `证书生成 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/gen_cert.html>`_ 
   
```

## 创世节点配置生成

FISCO BCOS提供generate_genesis.sh 脚本创建创世节点配置genesis.json:

```bash
# 进入脚本所在目录(设FISCO-BCOS位于/mydata目录)
$ cd /mydata/FISCO-BCOS/scripts

# 生成god账号：
$ fisco-bcos --newaccount
address:0x363a7fc65a054738e5332b2db97d63474421afe6 # god账号
publicKey:61c1012bffa671aa0a816b3919038b5ed6572b68da5e62acd92ad3f6ab52ab28ffd4a17a08dd9613e1b2495e62bc84e18fddd206283efb0c97b3ca845c466a85  #god账号公钥
privateKey:d16b5fd854d668256c7ec76aad344c84b22fdbbecc46a0a8ba8f3de32b8017fd #god账号私钥

# 初始化创世节点配置genesis.json
$ ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g 0x363a7fc65a054738e5332b2db97d63474421afe6
God account address: 0x3b5b68db7502424007c6e6567fa690c5afd71721
/mydata/node0/genesis.json is generated

# 此时在/mydata/node0/目录下生成genesis.json，内容如下:
$ cat /mydata/node0/genesis.json
{
     "nonce": "0x0",
     "difficulty": "0x0",
     "mixhash": "0x0",
     "coinbase": "0x0",
     "timestamp": "0x0",
     "parentHash": "0x0",
     "extraData": "0x0",
     "gasLimit": "0x13880000000000",
     "god":"0x3b5b68db7502424007c6e6567fa690c5afd71721",
     "alloc": {}, 
     "initMinerNodes":["08eff55799d66d7426e64e44384c8e3eb5d849b4b5dbf21a32e5b954d787cc6c2500b8d25e14bf90e327940b0a2d3eeecb26ab2ea43b076f67af75d8cb3fbcf0"]
}

# 若使用默认god账号0x3b5b68db7502424007c6e6567fa690c5afd71721生成创世节点配置，可使用如下命令：
# ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g # 生成/mydata/genesis.json
# god账号信息存储在/mydata/node0/guomiGodInfo.txt中

# generate_genesis.sh 脚本功能
$ ./generate_genesis.sh -h
Usage:
 -d <genesis node dir> Genesis node dir of the blockchain #创世节点所在目录
 -o <output dir> Where genesis.json generate  #创世块配置文件genesis.json所在目录
 -r <god account> Address of god account
    (default: 0xf78451eb46e20bc5336e279c52bda3a3e92c09b6) # 非国密版默认GOD账号
    (guomi default: 0x3b5b68db7502424007c6e6567fa690c5afd71721) # 国密版默认GOD账号
 -d The Path of Guomi Directory
 -g Generate genesis node for guomi-FISCO-BCOS  # 为国密版FISCO BCOS产生genesis.json
 -h This help
Example: # 生成非国密版FISCO BCOS genesis.json示例
 ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0
./generate_genesis.sh -d /mydata/node0 -o /mydata/node0  0xf78451eb46e20bc5336e279c52bda3a3e92c09b6
Guomi Example：# 生成国密版FISCO BCOS genesis.json示例
./generate_genesis.sh -d /mydata/node0 -o /mydata/node0
 ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g 0x3b5b68db7502424007c6e6567fa690c5afd71721

```

## 创世节点环境初始化

FISCO-BCOS提供generate_node.sh脚本初始化节点环境，下面使用该脚本初始化创世节点：

```bash
# 进入脚本所在目录(设FISCO-BCOS位于/mydata目录)
$ cd /mydata/FISCO-BCOS/scripts

# 调用generate_node.sh生成创世节点环境
# 节点位于/mydata目录，节点名为mydata，监听IP是127.0.0.1, rpc端口是8545, 
# p2p端口是30303, channelport是8891
# bootstrapnode.json记录的peer信息是: 127.0.0.1:30303和127.0.0.1:30304
$ bash ./generate_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -e 127.0.0.1:30303,127.0.0.1:30304

# 执行以上命令后，创世节点环境初始化完成，具体包括如下文件:
$ ls /mydata/node0/
config.json  data  genesis.json  keystore  log  log.conf  start.sh  stop.sh

# generate_node.sh脚本功能
$ ./generate_node.sh -h  
Usage:
    -o  <output dir>        Where node files generate # 节点所处目录
    -n  <node name>         Name of node    # 节点名
    -l  <listen ip>         Node\'s listen IP  # 监听IP
    -r  <RPC port>          Node\'s RPC port   # RPC端口
    -p  <P2P port>          Node\'s P2P port   # P2P端口
    -c  <channel port>      Node\'s channel port  # channel port
    -e  <bootstrapnodes>    Node\'s bootstrap nodes # bootstrapnodes.json相关配置
    -h                      This help
Example: #使用示例
    bash ./generate_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -e 127.0.0.1:30303,127.0.0.1:30304

```

## 启动创世节点

节点目录下提供start.sh启动创世节点：

```bash
# 进入创世节点目录
$ cd /mydata/node0

# 确认fisco-bcos是国密版本
$ fisco-bcos --version
FISCO-BCOS version 1.3.1-gm # 有-gm表明是国密版本
FISCO-BCOS network protocol version: 63
Client database version: 12041
Build: ETH_BUILD_PLATFORM/ETH_BUILD_TYPE

# 启动创世节点
$ ./start.sh
```


## check创世节点环境

启动创世节点后，需要check创世节点进程和是否正常出块：

```bash
# 进入创世节点目录
$ cd /mydata/node0

# check进程状态
$ ps aux | grep fisco
root     20995  0.6  0.1 2171448 14280 pts/3   Sl   09:15   0:01 ./fisco-bcos --genesis /mydata/node0/genesis.json --config /mydata/node0/config.json

# check创世节点是否正常出块
$ tail -f log_2018080809.log | grep +++
INFO|2018-08-08 09:21:18:109|+++++++++++++++++++++++++++ Generating seal onff05d8b4386fc1a058b9c9da7816fa1e340d0bffcd008424104b2ed48740ace4#1tx:0,maxtx:1000,tq.num=0time:1533691278109
INFO|2018-08-08 09:21:19:138|+++++++++++++++++++++++++++ Generating seal on7e78c3a28b652a243ec2d2ffe2c3c927469bddef53cfaf9cab9128b7930f3c50#1tx:0,maxtx:1000,tq.num=0time:1533691279138

```
通过以上输出可看出，创世节点进程已启动，且出块正常。


