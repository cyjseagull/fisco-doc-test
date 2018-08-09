# 部署系统合约

```eval_rst

.. admonition:: 注意事项
   部署系统合约前，请参考 `【编译安装】 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/compile.html#id4>`_ 配置好国密版nodejs.

```

国密版FISCO BCOS提供了nodejs工具部署系统合约：

## 配置config.js

配置web3lib/config.js中的proxy字段为【创世节点IP】:【创世节点RPC端口】，这里创世节点ip为 ``127.0.0.1`` , 端口为8545，配置如下：

```bash
# 【创世节点IP】:【创世节点RPC端口】
var proxy="http://127.0.0.1:8545";
# 国密版nodejs，配置为1
var encryptType = 1;// 0:ECDSA 1:sm2Withsm3
```

## 部署系统合约

调用 `babel-node deploy.js` 部署系统合约，若有如下输出，表明部署系统合约成功，否则请参考 *[【国密版nodejs安装方法】](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/compile.html#id4)检查nodejs环境是否有问题* 

```bash
# 进入系统合约工具所在目录(设FISCO-BCOS源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS/systemcontract

# 部署系统合约
$ babel-node deploy.js
SystemProxycomplie success！
send transaction success: 0x6be898031f91743e6dac8935e438d5ac4b2fdf854efb47e6955590dcb4791dd1
SystemProxycontract address 0xee80d7c98cb9a840b9c4df742f61336770951875
...省略若干行...
SystemProxy address :0xee80d7c98cb9a840b9c4df742f61336770951875
-----------------SystemProxy route ----------------------
0 )TransactionFilterChain=>0x08f8eeb7959660ed84b18b2daf271dc19e62aaf9,false,22
1 )ConfigAction=>0xbc2b0ca104ac0a824b05c1e055f24b1857e69b35,false,23
2 )NodeAction=>0x22af893607e84456eb5aea0b277e4dffe260fdcd,false,24
3 )CAAction=>0xa92014f1593bbaa1294be562f0dbfbc7aca0d579,false,25
4 )ContractAbiMgr=>0xe441c93f05d2d200c9e51fdac87b9851483aa341,false,26
5 )ConsensusControlMgr=>0xb53b1513c2edf88c0a27f3670385481821cc0818,false,27
6 )FileInfoManager=>0xa9e38b700f6462b21e595402e870bc51ae852768,false,28
7 )FileServerManager=>0x3eeff72da75f3a2a1a97d958142b08ca75b86b5a,false,29

# 修改创世节点和普通节点 config.json的systemproxyaddress字段为系统合约地址
# systemproxyaddress: "0xee80d7c98cb9a840b9c4df742f61336770951875"
# 更新创世节点和普通节点系统合约地址
$ bash update_syscontract.sh /mydata/node0 /mydata/node1 "0xee80d7c98cb9a840b9c4df742f61336770951875"

# --- 重启创世节点和普通节点---
# 重启创世节点和重启普通节点
$ bash start_node.sh /mydata/node0 /mydata/node1
```

