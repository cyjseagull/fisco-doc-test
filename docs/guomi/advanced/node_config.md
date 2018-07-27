# 注册/移除记账节点

## 注册记账节点

所有的节点注册流程都相同。**在注册节点时，被注册节点必须处于运行状态**。

**注册前，请确认已注册的所有节点，都已经启动。**

系统合约使用方法可参考[适配于国密的web3sdk对系统合约工具的使用方法](https://github.com/FISCO-BCOS/web3sdk/blob/master/doc/guomi_support_manual.md#52-%E7%B3%BB%E7%BB%9F%E5%90%88%E7%BA%A6%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

**（1）注册创世节点**


```
#====进入web3sdk路径=====
$ cd /mydata/web3sdk/dist

#====将创世节点nodeA配置文件gmnode.json拷贝到web3sdk配置目录下====
$ cp /mydata/FISCO-BCOS/cert/GM/agencyA/nodeA/gmnode.json /mydata/web3sdk/dist/conf/node1.json

#====注册创世节点=====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction registerNode node1.json  
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
gmnode.json=node1.json

#====查看记账节点信息====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction all 
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
NodeIdsLength= 1
----------node 0---------
id=7a645ed6fe21df8455de30316b2c2180925acbde7e1831dda6192b9e37b7bfa1168df5f6de54c9753292075a8bccce735a64a4ef9c6c3896aef325396b3ea2bb
name=nodeA
agency=agencyA
caHash=A6EFE350CAE21137
Idx=0
blocknumber=26
[app@VM_105_81_centos dist]$ 

```

> 从上述输出信息可看出，创世节点已经被注册到系统合约中


**（2） 注册普通节点**

```
#====将普通节点nodeB配置文件gmnode.json拷贝到web3sdk配置目录下====
$ cp /mydata/FISCO-BCOS/cert/GM/agencyA/nodeB/gmnode.json /mydata/web3sdk/dist/conf/node2.json

#====注册普通节点========
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction registerNode node2.json
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
gmnode.json=node2.json

#====查看记账节点信息====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction all
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
NodeIdsLength= 2
----------node 0---------
id=7a645ed6fe21df8455de30316b2c2180925acbde7e1831dda6192b9e37b7bfa1168df5f6de54c9753292075a8bccce735a64a4ef9c6c3896aef325396b3ea2bb
name=nodeA
agency=agencyA
caHash=A6EFE350CAE21137
Idx=0
blocknumber=26
----------node 1---------
id=0efc141f88d5b7e4b3fa5573a10684860950eb0d920ac9a93c5d2be5c57cf87d371507357805fb22992b2eedaaab495361068fbec9dabf8b881cce257b07465a
name=nodeB
agency=agencyA
caHash=DE96E7AFF17B29C2
Idx=1
blocknumber=27

#====节点重启后，普通节点能正常出块====
$ cd /mydata/nodedata-2/log

#====查看日志，不断刷出打包信息=============
$ tail -f log_2018052521.log  | grep "+++"
INFO|2018-05-25 21:01:40:460|+++++++++++++++++++++++++++ Generating seal onfeff6d25d83774b022abd4eaf7b66095577ce4dcdf3d3b43789ff317d06cbb1b#35tx:0,maxtx:1000,tq.num=0time:1527253300460
INFO|2018-05-25 21:01:42:484|+++++++++++++++++++++++++++ Generating seal one79e4d52b6178de12b767cd8cf977e63f45b79e59d7fa1c32f09f2a3240b03e6#35tx:0,maxtx:1000,tq.num=0time:1527253302484
```

> 通过输出信息可看出，普通节点成功注册到系统合约中

### 节点退出

> 若将某节点退出记账列表，执行以下操作：

```bash
#=====进入web3sdk目录==========
$ cd /mydata/web3sdk/dist

#=====调用系统合约工具退出普通节点nodeB(注：退出前，必须保证/mydata/web3sdk/dist/conf目录下存在nodeB的配置文件node2.json)===
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction cancelNode node2.json
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
gmnode.json=node2.json

#====查看记账节点列表信息：此时仅剩nodeA信息，说明nodeB退出记账节点成功=====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools NodeAction all
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
NodeIdsLength= 1
----------node 0---------
id=7a645ed6fe21df8455de30316b2c2180925acbde7e1831dda6192b9e37b7bfa1168df5f6de54c9753292075a8bccce735a64a4ef9c6c3896aef325396b3ea2bb
name=nodeA
agency=agencyA
caHash=A6EFE350CAE21137
Idx=0
blocknumber=26

```
