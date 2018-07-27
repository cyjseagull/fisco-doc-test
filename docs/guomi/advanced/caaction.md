# 证书注销

类似于[非国密版FISCO BCOS](manual#%E7%AC%AC%E5%85%AB%E7%AB%A0-%E8%AF%81%E4%B9%A6%E6%B3%A8%E9%94%80)，国密版FISCO BCOS也支持证书注销功能。

在节点加入网络后，节点间通过证书进行通信。FISCO BCOS区块链中的管理者，可以通过登记证书到注销证书列表，来禁止使用该证书的节点接入网络。

> 在进行注销证书登记操作前，再次请确认：
>
> （1）系统合约已经被正确的部署。
>
> （2）所有节点的config.json的systemproxyaddress字段已经配置了相应的系统代理合约地址。
>
> （3）节点在配置了systemproxyaddress字段后，已经重启使得系统合约生效。
>
> （4）/mydata/web3sdk/dist/conf/applicationContext.xml的systemProxyAddress字段已经配置了系统代理合约地址。



## 登记注销证书

<br>

每个节点data目录都保存了节点证书gmnode.ca，执行以下命令可将节点证书加入系统合约注销证书列表中，以普通节点nodeB证书注销为例：

```bash
#====进入web3sdk路径=====
$ cd /mydata/web3sdk/dist

#====将节点证书拷贝到web3sdk配置目录====
$ cp /mydata/nodedata-2/data/gmnode.ca /mydata/web3sdk/dist/conf/node2.ca

#====调用系统合约工具，将普通节点nodeB的证书加入注销证书列表====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools CAAction add node2.ca   
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
gmnode.ca=node2.ca

#====查看证书注销列表=====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools CAAction all
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
HashsLength= 1
----------CA 0---------
hash=DE96E7AFF17B29C2
serial=DE96E7AFF17B29C2
pubkey=0efc141f88d5b7e4b3fa5573a10684860950eb0d920ac9a93c5d2be5c57cf87d371507357805fb22992b2eedaaab495361068fbec9dabf8b881cce257b07465a
name=nodeB
blocknumber=31

```

> 通过证书列表输出可看出，普通节点nodeB的证书已经被加入了注销证书列表中。

<br>

[返回目录](#目录)

<br>


## 移除注销证书

<br>

```bash
#====进入web3sdk路径=====
$ cd /mydata/web3sdk/dist

#====调用系统合约工具，将普通节点nodeB的证书从证书列表中移除====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools CAAction remove node2.ca
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
gmnode.ca=node2.ca

#====查看证书注销列表====
$ java -cp 'conf/:apps/*:lib/*' org.bcos.contract.tools.SystemContractTools CAAction all
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
generate keypair data succeed
HashsLength= 0
```

> 通过输出信息可看出，普通节点nodeB的证书已经从证书注销列表中成功移除。
