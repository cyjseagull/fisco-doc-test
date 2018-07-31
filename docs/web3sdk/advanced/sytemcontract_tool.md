# 系统合约工具

web3sdk提供了系统合约管理工具，下表简单介绍了这些管理工具,系统合约介绍文档参考[FISCO BCOS系统合约介绍](https://github.com/FISCO-BCOS/Wiki/tree/master/FISCO-BCOS%E7%B3%BB%E7%BB%9F%E5%90%88%E7%BA%A6%E4%BB%8B%E7%BB%8D)

```eval_rst
+------------------------+-----------------------------------------------------------------------+
|  系统合约              |    详细说明                                                           |
+========================+=======================================================================+
|  SystemProxy           |    系统合约代理合约                                                   |
+------------------------+-----------------------------------------------------------------------+
|  TransactionFilterChain|    设置transaction过滤器                                              |
+------------------------+-----------------------------------------------------------------------+
|  ConfigAction          |    设置/获取区块链系统参数，可参考 `_系统参数说明文档 <TODO>`_        |
+------------------------+-----------------------------------------------------------------------+
|  ConsensusControlMg    |    联盟控制合约，可参考 `_联盟控制模板参考文档 <TODO>`_               |
+------------------------+-----------------------------------------------------------------------+
|  CAAction              |    证书列表黑名单管理: 包括将证书加入黑名单列表，                     |
|                        |    将指定证书从黑名单列表删除，获取证书黑名单列表功能                 |
+------------------------+-----------------------------------------------------------------------+
|  ContractAbiMgr        |    ABI相关合约                                                        |
+------------------------+-----------------------------------------------------------------------+

```

web3sdk/dist/bin/web3sdk是web3sdk的执行脚本, 下面介绍如何通过web3sdk脚本调用系统合约管理工具:

### 系统合约代理合约SystemProxy
 
遍历系统代理合约路由表，输出所有系统合约地址

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk SystemProxy
```


### 节点管理合约NodeAction

(1) 将节点加入记账者列表

将${node_json_path}(${node_json_path}是节点配置文件相对于dist/conf的路径)中指定的节点加入到FISCO BCOS区块链网络中:

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction registerNode ${node_json_path}
```
注: ${node_json_path}是节点配置文件相对于dist/conf的路径，节点配置文件主要包括如下配置项:


```eval_rst
+------------+--------------------------------+
| 配置项     | 详细说明                       |
+============+================================+
| id         | 节点node id                    |
+------------+--------------------------------+
| ip         | 节点IP                         |
+------------+--------------------------------+
| port       | 节点P2P连接端口                |
+------------+--------------------------------+
| desc       | 节点描述                       |
+------------+--------------------------------+
| agencyinfo | 节点所属机构信息               |
+------------+--------------------------------+
| idx        |  节点序号，按照加入顺序排序    |
+------------+--------------------------------+
```

一个简单的节点配置文件node.json示例如下:

```json
{
    "id":"2cd7a7cadf8533e5859e1de0e2ae830017a25c3295fb09bad3fae4cdf2edacc9324a4fd89cfee174b21546f93397e5ee0fb4969ec5eba654dcc9e4b8ae39a878",
    "ip":"127.0.0.1",
    "port":30501,
    "desc":"node1",
    "CAhash":"",
    "agencyinfo":"node1",
    "idx":0
}
```

(2) 退出节点

将${node_json_path}指定的节点从FISCO BCOS区块链网络中退出(${node_json_path}是节点配置文件相对于/mydata/web3sdk/dist/conf的路径，节点配置文件说明同上)

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction cancelNode ${node_json_path}
```

(3) 显示节点连接信息

可通过如下命令查询区块链网络中所有记账节点信息:

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction all
```

输出的记账节点信息如下：

```bash
$ cd /mydata/web3sdk/dist/bin
$ ./web3sdk NodeAction all
===================================================================
=====INIT ECDSA KEYPAIR From private key===
NodeIdsLength= 1
----------node 0---------
id=28f815c7222118adaca6dfdefdda76906a491ae4ef9de4d311f3f23bd2371ee9d15e2f26646d1641bf6391b1c1489c8a1708e35012903f041d1841f58c63e674
nodeA
agencyA
E2746FDF0B29F8A8
org.bcos.web3j.abi.datatypes.generated.Uint256@ee871267
```


### 节点证书管理合约CAAction

(1) 将指定节点证书加入黑名单列表

可使用如下命令将路径${node_ca_path}(${node_ca_path}是节点配置文件相对于dist/conf的路径)指定的节点证书信息添加到黑名单列表，加入成功后，其他节点将拒绝与此节点连接:

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction add ${node_ca_path}
```

(2) 从黑名单列表中删除指定节点证书信息

可使用如下命令将${node_ca_path}(${node_ca_path}是节点配置文件相对于dist/conf的路径)指定的节点证书信息从黑名单列表中删除，其他节点恢复与该节点的连接:

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction remove ${node_ca_path}
```

(3) 显示区块链黑名单节点证书信息

使用如下命令可获取记录在系统合约CAAction中的所有黑名单节点证书信息：
```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction all
```

### 系统参数配置合约ConfigAction

(1) 获取系统参数：./web3sdk ConfigAction get ${key}

从系统合约ConfigAction读取${key}对应的值(ConfigAction中记录的系统参数说明参考[系统参数说明文档](https://github.com/FISCO-BCOS/Wiki/tree/master/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3))


(2) 设置系统参数信息：./web3sdk ConfigAction set ${key} ${setted_value}

将记录在系统合约ConfigAction中${key}对应的值设置为${setted_value}(ConfigAction中记录的系统参数说明参考[系统参数说明文档](https://github.com/FISCO-BCOS/Wiki/tree/master/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3))


**FISCO BCOS系统合约主要配置如下**:

```eval_rst
+-------------------------+-------------------------------------------------------------+
| 配置项                  |     详细说明                                                |
+=========================+=============================================================+
| maxBlockTransactions    |     控制一个块内允许打包的最大交易数量上限                  |
|                         |     设置范围: [0, 2000), 默认值:1000                        |
+-------------------------+-------------------------------------------------------------+
| intervalBlockTime       |     设置出块间隔时间                                        |
|                         |     设置范围：大于等于1000, 默认值: 1000                    |
+-------------------------+-------------------------------------------------------------+
|  maxBlockHeadGas        |      控制一个块允许最大Gas消耗上限                          |
|                         |      取值范围: 大于等于2000,000,000, 默认值: 2000,000,000   |
+-------------------------+-------------------------------------------------------------+
|  maxTransactionGas      |      设置一笔交易允许消耗的最大gas                          |
|                         |      取值范围: 大于等于30,000,000, 默认值: 30,000,000       |
+-------------------------+-------------------------------------------------------------+
|  maxNonceCheckBlock     |      控制Nonce排重覆盖的块范围                              |
|                         |      取值范围： 大于等于1000, 缺省值: 1000                  |
+-------------------------+-------------------------------------------------------------+
|  maxBlockLimit          |      控制允许交易上链延迟的最大块范围                       |
|                         |      取值范围：大于等于1000, 缺省值：1000                   |
+-------------------------+-------------------------------------------------------------+
|  CAVerify               |      控制是否打开CA验证,取值：true或者false, 缺省值: false  |      
+-------------------------+-------------------------------------------------------------+
|  omitEmptyBlock         |      控制是否忽略空块                                       |
|                         |      取值：true或者false, 缺省值：false                     |
+-------------------------+-------------------------------------------------------------+
```

**通过ConfigAction配置系统参数的例子如下:**

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
$ cd /mydata/web3sdk/dist/bin
$ chmod a+x web3sdk

# =====更改出块时间为2s====
$ ./web3sdk ConfigAction set intervalBlockTime 2000

# =====允许空块落盘=====
$ ./web3sdk ConfigAction set omitEmptyBlock false

# ====调整一笔交易允许消耗的最大交易gas为40,000,000
$ ./web3sdk ConfigAction set maxTransactionGas 40000000

# ====调整一个块允许消耗的最大交易gas为3000,000,000
$ ./web3sdk ConfigAction set maxBlockHeadGas 3000000000

# ==== 打开CA认证开关====
$ ./web3sdk ConfigAction set CAVerify true

# ......
```

### 联盟控制合约ConsensusControl

(1) 部署联盟共识模板:./web3sdk ConsensusControl deploy

(2) 获取联盟共识模板合约地址:./web3sdk ConsensusControl list

(3) 关闭联盟共识特性: ./web3sdk ConsensusControl list turnoff
