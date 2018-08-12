# 搭建创世节点 

```eval_rst
.. admonition:: 注意事项
   
   创建创世节点配置genesis.json前，必须确保已在创世节点data目录生成了节点证书，参考 `证书生成 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/gen_cert.html>`_ 
   
```

## 创世节点配置生成

FISCO BCOS提供generate_genesis.sh 脚本创建创世节点配置genesis.json:

```bash
# 进入脚本所在目录(设FISCO-BCOS位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools/scripts

# 生成god账号：
$ fisco-bcos --newaccount
address:0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad # god账号
publicKey:9c39ff254a673ec069c5aec56d206531ec45a2165f97df0b7259ad393dbde90b3f6896925060006ff6a43191dfabf93941de4e42bd54dea88c2f373e1f8db252 #god账号公钥
privateKey:f5474c4c9b1a3d922bc583b261c4ec45cd2bacb19030c82f9ad20d64acd431a8 #god账号私钥

# 配置rpc端口：(设创世节点P2P端口是8545)
$ bash config_rpc_address.sh -o 127.0.0.1:8545
Attention! This operation will change the target <rpcport url> of all tools under tools/. Continue?
[Y/n]: ]y

# 初始化创世节点配置genesis.json
$ ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g -r 0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad
God account address: 0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad
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
     "god":"0xf02a10f685a90c3bfc2eccd906b75fe3feeec9ad",
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

FISCO-BCOS提供generate_genesis_node.sh脚本初始化节点环境并部署系统合约，下面使用该脚本初始化创世节点：

```bash
# 进入脚本所在目录(设FISCO-BCOS位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools/scripts

#---调用generate_genesis_node.sh生成创世节点环境并部署系统合约
#---节点位于/mydata目录，节点名为mydata，监听IP是127.0.0.1, rpc端口是8545, 
#---p2p端口是30303, channelport是8891
$ ./generate_genesis_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -g
---------- Generate node basic files ---------- #初始化创世节点配置信息
RUN: sh generate_node_basic.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -e 127.0.0.1:30303 -g
#... 此处省略若干行 ...
SUCCESS execution of command: sh generate_node_basic.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -e 127.0.0.1:30303 -g
---------- Deploy system contract ----------  # 部署系统合约
RUN: sh deploy_systemcontract.sh -d /mydata/node0 -g
Pre-start genesis node
Deploy System Contract
Start depoly system contract
RUN: babel-node deploy_systemcontract.js /data/chenyujie/guomi/FISCO-BCOS/tools/web3lib/tmp_config_deploy_system_contract.js
SystemProxycomplie success！
#... 此处省略若干行 ...
### 显示系统合约信息
-----------------SystemProxy route ----------------------
0 )TransactionFilterChain=>0x08f8eeb7959660ed84b18b2daf271dc19e62aaf9,false,22
1 )ConfigAction=>0xbc2b0ca104ac0a824b05c1e055f24b1857e69b35,false,23
2 )NodeAction=>0x22af893607e84456eb5aea0b277e4dffe260fdcd,false,24
3 )CAAction=>0xa92014f1593bbaa1294be562f0dbfbc7aca0d579,false,25
4 )ContractAbiMgr=>0xe441c93f05d2d200c9e51fdac87b9851483aa341,false,26
5 )ConsensusControlMgr=>0xb53b1513c2edf88c0a27f3670385481821cc0818,false,27
6 )FileInfoManager=>0xa9e38b700f6462b21e595402e870bc51ae852768,false,28
7 )FileServerManager=>0x3eeff72da75f3a2a1a97d958142b08ca75b86b5a,false,29
SUCCESS execution of command: babel-node deploy_systemcontract.js /data/chenyujie/guomi/FISCO-BCOS/tools/web3lib/tmp_config_deploy_system_contract.js
/data/chenyujie/guomi/FISCO-BCOS/tools/scripts
Stop genesis node
Reconfig genesis node
SystemProxy address: 0xee80d7c98cb9a840b9c4df742f61336770951875
Deploy System Contract Success!
SUCCESS execution of command: sh deploy_systemcontract.sh -d /mydata/node0 -g
#... 此处省略若干行 ...
# 显示节点信息
-----------------------------------------------------------------
Name:
Node dir:               /mydata/node0 #创世节点名
Agency:
CA hash:                D14983471F0AC975
Node ID:                3d4fe4c876cac411d4c7180b5794198fb3b4f3e0814156410ae4184e0a51097a01bf63e431293f30af0c01a57f24477ad1704d8f676bc7e345526ba1735db6a7 #node id
RPC address:            127.0.0.1:8545
P2P address:            127.0.0.1:30303
Channel address:        127.0.0.1:8891
SystemProxy address:    0xee80d7c98cb9a840b9c4df742f61336770951875 #系统代理合约地址
State:                  Running (pid: 11524)  #节点运行状态
-----------------------------------------------------------------

# generate_node.sh脚本功能
$ ./generate_genesis_node.sh -h
Usage:
 -o <output dir> Where node files generate # 节点所处目录
 -n <node name> Name of node # 节点名
 -l <listen ip> Node\'s listen IP # 监听IP
 -r <RPC port> Node\'s RPC port  # RPC端口
 -p <P2P port> Node\'s P2P port # P2P端口
 -c <channel port> Node\'s channel port # channel port
 -a <agency name> The agency name that the node belongs to #国密版FISCO-BCOS不需关注
 -d <agency dir> The agency cert dir that the node belongs to #国密版FISCO-BCOS不需关注
Optional:
 -m Input agency information manually #手动输入证书信息，国密版FISCO-BCOS不需关注
 -g Generate guomi genesis node # 国密版FISCO-BCOS加该选项
 -h This help
Example: #非国密版FISCO-BCOS使用示例
 ./generate_genesis_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -d /mydata/test_agency -a test_agency 
guomi Example: #国密版FISCO-BCOS使用示例
 ./generate_genesis_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -g
```

## check创世节点环境

创世节点部署成功后，需要check创世节点进程和是否正常出块：

```bash
# check创世节点是否正常出块
$ tail -f log_2018080809.log | grep +++
INFO|2018-08-08 09:21:18:109|+++++++++++++++++++++++++++ Generating seal onff05d8b4386fc1a058b9c9da7816fa1e340d0bffcd008424104b2ed48740ace4#1tx:0,maxtx:1000,tq.num=0time:1533691278109
INFO|2018-08-08 09:21:19:138|+++++++++++++++++++++++++++ Generating seal on7e78c3a28b652a243ec2d2ffe2c3c927469bddef53cfaf9cab9128b7930f3c50#1tx:0,maxtx:1000,tq.num=0time:1533691279138

```
通过以上输出可看出，创世节点进程已启动，且出块正常。

