# 节点入网

```eval_rst
.. admonition:: 注意事项
   
   节点入网前，请确保：
    - 系统合约被正确的部署，参考 `部署系统合约 <>`_ 
    - 所有节点的config.json的systemproxyaddress字段已经配置了相应的系统代理合约地址
    - 节点在配置了systemproxyaddress字段后，已经重启使得系统合约生效
    - /mydata/FISCO-BCOS/web3lib/下的config.js已经正确的配置了节点的RPC端口
    - 节点入网时，必须先注册创世节点
```

## 创世节点入网

创世节点入网过程如下：

```bash
$ babel-node tool.js NodeAction registerNode /mydata/node0/data/gmnode.json 
{ HttpProvider: 'http://127.0.0.1:8545',
  Ouputpath: './output/',
  EncryptType: 1,
  privKey: 'bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd',
  account: '0x64fa644d2a694681bd6addd6c5e36cccd8dcdde3' }
Soc File :NodeAction
Func :registerNode
SystemProxy address 0xee80d7c98cb9a840b9c4df742f61336770951875
node.json=../../node0/data/gmnode.json
NodeAction address 0x22af893607e84456eb5aea0b277e4dffe260fdcd
send transaction success: 0x160a2e8b92349f891e97239d7a0e799c7b729881b9d6caf4ecd0117e50999414

# 创世节点配置/mydata/node0/data/gmnode.json如下：
$ cat /mydata/node0/data/gmnode.json
{
 "id":"730195b08dda7b027c9ba5bec8ec19420aa996c7ce72fa0954711d46c1c66ae8c2eeaa5f84d1f7766f21ba3dc822bc6d764fbee14034b19a0cf1c69c7f75e537",
 "name":"",
 "agency":"",
 "caHash":"AF33DEB4033C0D47"
}

```

## 普通节点入网

普通节点入网过程如下：

```
$ babel-node tool.js NodeAction registerNode ../../node1/data/gmnode.json  
{ HttpProvider: 'http://127.0.0.1:8545',
  Ouputpath: './output/',
  EncryptType: 1,
  privKey: 'bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd',
  account: '0x64fa644d2a694681bd6addd6c5e36cccd8dcdde3' }
Soc File :NodeAction
Func :registerNode
SystemProxy address 0xee80d7c98cb9a840b9c4df742f61336770951875
node.json=../../node1/data/gmnode.json
NodeAction address 0x22af893607e84456eb5aea0b277e4dffe260fdcd
send transaction success: 0x3ff3a0d795f8dd6c896a63890aef3d9b2e733854194fcd0556f1883a02c7a766
```

## 查看节点入网情况

使用`babel-node tool.js NodeAction all`命令查看节点入网情况：

```bash
babel-node tool.js NodeAction all
{ HttpProvider: 'http://127.0.0.1:8545',
  Ouputpath: './output/',
  EncryptType: 1,
  privKey: 'bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd',
  account: '0x64fa644d2a694681bd6addd6c5e36cccd8dcdde3' }
Soc File :NodeAction
Func :all
SystemProxy address 0xee80d7c98cb9a840b9c4df742f61336770951875
NodeAction address 0x22af893607e84456eb5aea0b277e4dffe260fdcd
NodeIdsLength= 2
----------node 0---------
id=730195b08dda7b027c9ba5bec8ec19420aa996c7ce72fa0954711d46c1c66ae8c2eeaa5f84d1f7766f21ba3dc822bc6d764fbee14034b19a0cf1c69c7f75e537
name=
agency=
caHash=AF33DEB4033C0D47
Idx=0
blocknumber=30
----------node 1---------
id=6f77e654e2a7a5487696c0b63e2433f01575c4d1d0a6a87e2a4d5f33e4d53afe3f8b479a70426918a99fde426890d88c88ed968fef90ea789c69a2866b04312b
name=
agency=
caHash=D304175CD76AF6B1
Idx=1
```

从输出信息可看出，创世节点和普通节点均成功入网。

## check节点入网情况

使用如下命令检查创世节点入网情况，若输出`+++`等打包信息，表明创世节点入网成功：

```bash
$ bash check_seal.sh /mydata/node0
INFO|2018-08-09 15:52:55:155|+++++++++++++++++++++++++++ Generating seal on4ffa4ee789a9efdeefe8c48455bbaaf39d8dfc914fba5638a1e0ade595e72cb2#32tx:0,maxtx:0,tq.num=0time:1533801175155
INFO|2018-08-09 15:52:57:175|+++++++++++++++++++++++++++ Generating seal onbf86213ea9ad2fa0d14e90404e90ccc9de2c94ae38b0d6e9f4a097fa2be85a8c#32tx:0,maxtx:0,tq.num=0time:1533801177175
```


同样地，使用如下命令检查普通节点入网情况，若输出`+++`等打包信息，表明普通节点入网成功：

```bash
$ bash check_seal.sh /mydata/node0
INFO|2018-08-09 15:53:22:461|+++++++++++++++++++++++++++ Generating seal onafd52f8bdd894b915883dd94986da0700c597d67b63484810787961e8a797007#32tx:0,maxtx:1000,tq.num=0time:1533801202461
INFO|2018-08-09 15:53:24:480|+++++++++++++++++++++++++++ Generating seal on5025fc6f1ca2ecf62418d9a19aec782829c817338942a38ca9284ff3c6dea768#32tx:0,maxtx:1000,tq.num=0time:1533801204480
```


```eval_rst

.. admonition:: congratulations ^V^

   至此，您已经成功搭建一条可用的国密版FISCO-BCOS链 
   - 更高级的使用方法请参考 `FISCO-BCOS高级特性 <TODO>`_
   - 国密版web3sdk配置和使用方法请参考 `国密版web3sdk <TODO>`_
```