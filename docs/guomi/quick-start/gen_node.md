# 创建普通节点

类似于[非国密版FISCO BCOS](manual#%E7%AC%AC%E5%85%AD%E7%AB%A0-%E5%88%9B%E5%BB%BA%E6%99%AE%E9%80%9A%E8%8A%82%E7%82%B9)，若实现多节点互连，还需要创建普通节点。

## 创建节点环境

<br>

> 参考[非国密版FISCO BCOS创建节点环境](manual#61-%E5%88%9B%E5%BB%BA%E8%8A%82%E7%82%B9%E7%8E%AF%E5%A2%83)步骤

<br>

## 生成普通节点证书文件

<br>

> 参考[3.1 生成节点证书](#31-生成节点证书)为普通节点nodeB生成证书，设nodeB也属于agencyA, 主要操作步骤如下：

```
#===注：由于生成创世节点时，已经生成了链证书和机构agencyA证书，因此普通节点不需要重新生成链证书====
#===进入源码cert/GM目录===
$ cd /mydata/FISCO-BCOS/cert/GM

#===为隶属于agencyA的nodeB生成节点证书====
$  bash gmnode.sh agencyA nodeB

#====此时会在agencyA/nodeB目录下生成一套国密版节点证书====
$ ls agencyA/nodeB/
gmagency.crt  gmca.crt  gmennode.crt  gmennode.key  gmnode.crt  gmnode.key  gmnode.nodeid  gmnode.private  gmnode.serial  gmnode.ca  gmnode.json

#====将节点证书拷贝到nodeB节点目录/mydata/nodedata-2/data目录下
$ cp /mydata/FISCO-BCOS/cert/GM/agencyA/nodeB/* /mydata/nodedata-2/data

#====将3.2节生成的客户端证书拷贝到节点数据目录/mydata/nodedata-2/data下
$ cp /mydata/FISCO-BCOS/cert/GM/agencyA/sdk1/* /mydata/nodedata-2/data
```

<br>

## 其他配置

<br>

> 参考[非国密版FISCO BCOS的第6.3节到第6.6节](manual#63-%E9%85%8D%E7%BD%AE%E8%BF%9E%E6%8E%A5%E6%96%87%E4%BB%B6bootstrapnodesjson)

- [配置连接文件bootstrapnodes.json](manual#63-%E9%85%8D%E7%BD%AE%E8%BF%9E%E6%8E%A5%E6%96%87%E4%BB%B6bootstrapnodesjson)
- [配置节点配置文件config.json](manual#64--%E9%85%8D%E7%BD%AE%E8%8A%82%E7%82%B9%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6configjson)
- [配置日志文件log.conf](manual#65-%E9%85%8D%E7%BD%AE%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6logconf)
- [启用落盘加密](#44-数据落盘加密): 普通节点也可开启落盘加密功能，具体步骤可参考4.4节
- [启动节点](manual#66-%E5%90%AF%E5%8A%A8%E8%8A%82%E7%82%B9)



# 多记账节点组网

类似于[国密版FISCO BCOS](manual#%E7%AC%AC%E4%B8%83%E7%AB%A0-%E5%A4%9A%E8%AE%B0%E8%B4%A6%E8%8A%82%E7%82%B9%E7%BB%84%E7%BD%91),非国密版FISCO BCOS同样将节点注册到系统合约记账列表中，才能参与记账。

> 进行多节点记账组网前，请确认：

> （1）[系统合约](#53-部署系统合约)已经被正确的部署

> （2）所有节点的config.json的systemproxyaddress字段已经[配置系统代理合约地址](##54-配置系统代理合约地址) 

> （3）节点在配置了systemproxyaddress字段后，已经重启使得系统合约生效


<br>

## 注册记账节点

<br>

所有的节点注册流程都相同。**在注册节点时，被注册节点必须处于运行状态**。

**注册前，请确认已注册的所有节点，都已经启动。**

系统合约使用方法可参考[适配于国密的web3sdk对系统合约工具的使用方法](https://github.com/FISCO-BCOS/web3sdk/blob/master/doc/guomi_support_manual.md#52-%E7%B3%BB%E7%BB%9F%E5%90%88%E7%BA%A6%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

**（1）注册创世节点**

<br>

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

<br>

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
