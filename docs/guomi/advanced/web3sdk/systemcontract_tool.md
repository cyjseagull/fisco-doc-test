# 系统合约工具和测试工具的使用


## 系统合约介绍

web3sdk将系统合约部署于链上，并可通过工具调用这些系统合约，部署的系统合约如下：

| 系统合约                   | 详细说明                                     |
| ---------------------- | ---------------------------------------- |
| SystemProxy            | 系统合约代理合约                                 |
| TransactionFilterChain | 设置transaction过滤器                         |
| ConfigAction           | 设置/获取区块链系统参数，可参考[系统参数说明文档](https://github.com/FISCO-BCOS/Wiki/tree/master/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3) |
| ConsensusControlMg     | 联盟控制合约，可参考[联盟控制模板参考文档](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/%E5%BC%B9%E6%80%A7%E8%81%94%E7%9B%9F%E9%93%BE%E5%85%B1%E8%AF%86%E6%A1%86%E6%9E%B6%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3.md)             |
| CAAction               | 证书列表黑名单管理: 包括将证书加入黑名单列表，将制定证书从黑名单列表删除，获取证书黑名单列表功能              |
| ContractAbiMgr         | ABI相关合约                                  |

<br>

[返回目录](#目录)
<br>
<br>


## 系统合约工具使用方法

web3sdk使用SystemContractTools调用系统合约，主要功能如下：

**(1) 系统合约代理合约SystemProxy**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk SystemProxy
```

**功能**：遍历系统代理合约路由表，输出所有系统合约地址

<br>

[返回目录](#目录)

<br>


**(2) 权限控制合约AuthorityFilter**

**调用方法**：

```bash
./web3sdk ARPI_Model 
./web3sdk PermissionInfo 
./web3sdk FilterChain addFilter name1 version1 desc1 
./web3sdk FilterChain delFilter num 
./web3sdk FilterChain showFilter 
./web3sdk FilterChain resetFilter 
./web3sdk Filter getFilterStatus num 
./web3sdk Filter enableFilter num 
./web3sdk Filter disableFilter num 
./web3sdk Filter setUsertoNewGroup num account 
./web3sdk Filter setUsertoExistingGroup num account group 
./web3sdk Filter listUserGroup num account 
./web3sdk Group getBlackStatus num account 
./web3sdk Group enableBlack num account 
./web3sdk Group disableBlack num account 
./web3sdk Group getDeployStatus num account 
./web3sdk Group enableDeploy num account 
./web3sdk Group disableDeploy num account 
./web3sdk Group addPermission num account A.address fun(string) 
./web3sdk Group delPermission num account A.address fun(string) 
./web3sdk Group checkPermission num account A.address fun(string) 
./web3sdk Group listPermission num account 
```

<br>

[返回目录](#目录)

<br>


**(3) 节点管理合约NodeAction**

**① 加入节点**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction registerNode ${node_json_path}
```

**功能**：将${node_json_path}中指定的节点加入到FISCO BCOS区块链网络中(注: ${node_json_path}是节点配置文件相对于dist/conf的路径)

节点配置文件主要包括如下配置项：

| 配置项        | 详细说明          |
| ---------- | ------------- |
| id         | 节点的node id    |
| ip         | 节点IP          |
| port       | 节点P2P连接端口     |
| desc       | 节点描述          |
| agencyinfo | 节点所属机构信息      |
| idx        | 节点序号，按照加入顺序排序 |

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

**② 退出节点**

**调用方法**

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction cancelNode ${node_json_path}
```

**功能**：将${node_json_path}指定的节点从FISCO BCOS区块链网络中退出(注: ${node_json_path}是节点配置文件相对于dist/conf的路径，节点配置文件说明同上)

<br>

**③ 显示节点连接信息**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk NodeAction all
```

**功能**：显示FISCO BCOS区块链网络中所有节点信息，输出示例如下：

```bash
$  ./web3sdk NodeAction all
===================================================================
NodeIdsLength= 1
----------node 0---------
id=28f815c7222118adaca6dfdefdda76906a491ae4ef9de4d311f3f23bd2371ee9d15e2f26646d1641bf6391b1c1489c8a1708e35012903f041d1841f58c63e674
nodeA
agencyA
E2746FDF0B29F8A8
org.bcos.web3j.abi.datatypes.generated.Uint256@ee871267
```

<br>

[返回目录](#目录)

<br>


**(4) 节点证书管理合约CAAction**

**① 将指定节点证书加入黑名单列表**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction add ${node_ca_path}
```

**功能**：通过系统合约CAAction，将路径${node_ca_path}指定的节点证书信息添加到黑名单列表，其他节点将拒绝与此节点连接(注: ${node_ca_path}是节点配置文件相对于dist/conf的路径)

<br>

**② 从黑名单列表中删除指定节点证书信息**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction remove ${node_ca_path}
```

**功能**：通过系统合约CAAction，将${node_ca_path}指定的节点证书信息从黑名单列表中删除，其他节点恢复与该节点的连接(注: ${node_ca_path}是节点配置文件相对于dist/conf的路径)

**③ 显示区块链黑名单节点证书信息**

**调用方法**: 

```bash
##设web3sdk代码位于/mydata/目录下
#----进入bin目录---
cd /mydata/web3sdk/dist/bin
chmod a+x web3sdk
./web3sdk CAAction all
```

**功能**: 显示记录在系统合约CAAction中的所有黑名单节点证书信息

<br>

[返回目录](#目录)

<br>


**(5) 系统参数配置合约ConfigAction**


**FISCO BCOS系统合约主要配置如下:**

<br>

| 配置项        | 详细说明          |
| ---------- | ------------- |
| maxBlockTransactions| 控制一个块内允许打包的最大交易数量上限 <br>  设置范围: [0, 2000) <br> 默认值:1000|
| intervalBlockTime| 设置出块间隔时间 <br> 设置范围：大于等于1000 <br> 默认值: 1000 |
| maxBlockHeadGas| 控制一个块允许最大Gas消耗上限 <br> 取值范围: 大于等于2000,000,000 <br> 默认值: 2000,000,000|
| maxTransactionGas| 设置一笔交易允许消耗的最大gas <br> 取值范围: 大于等于30,000,000 <br> 默认值: 30,000,000 |
| maxNonceCheckBlock| 控制Nonce排重覆盖的块范围 <br> 取值范围： 大于等于1000 <br>  缺省值: 1000 |
| maxBlockLimit| 控制允许交易上链延迟的最大块范围 <br> 取值范围：大于等于1000 <br> 缺省值：1000|
| CAVerify| 控制是否打开CA验证 <br> 取值：true或者false  <br>  缺省值: false|
| omitEmptyBlock| 控制是否忽略空块 <br> 取值：true或者false  <br> 缺省值：false |

<br>

**① 获取系统参数**

**调用方法**: 在/mydata/web3sdk/dist/bin目录下执行./web3sdk ConfigAction get ${配置项}

**功能**: 从系统合约ConfigAction读取${key}对应的值(ConfigAction中记录的系统参数说明参考[系统参数说明文档](https://github.com/FISCO-BCOS/Wiki/tree/master/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3))

<br>

**② 设置系统参数信息**

**调用方法**: 在/mydata/web3sdk/dist/bin目录下执行./web3sdk ConfigAction set ${配置项} ${配置项的值}"

**功能**: 将记录在系统合约ConfigAction中${key}对应的值设置为${setted_value}(ConfigAction中记录的系统参数说明参考[系统参数说明文档](https://github.com/FISCO-BCOS/Wiki/tree/master/%E7%B3%BB%E7%BB%9F%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3))

<br>

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

<br>

[返回目录](#目录)

<br>
<br>

**(6) 联盟控制合约ConsensusControl**

**① 部署联盟共识模板合约**

**调用方法**: ./web3sdk ConsensusControl deploy

<br>

**② 列出所有联盟共识合约地址**

**调用方法**: ./web3sdk ConsensusControl list

<br>

**③ 关闭联盟共识特性**

**调用方法**:  ./web3sdk ConsensusControl list turnoff

<br>



[返回目录](#目录)

<br>
<br>

## 5.3 测试工具使用方法

web3sdk提供了一些测试工具，方便确定web3sdk与[FISCO BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/国密操作文档.md)通信是否正常，本节简要介绍这些测试工具使用方法：

**(1) Ok合约测试工具**

**调用方法:** java -cp 'conf/:apps/\*:lib/\*' org.bcos.channel.test.TestOk
**说明:** 向链上部署Ok合约，并调用Ok合约的trans接口(Ok合约可参考[Ok.sol](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol))

Ok合约调用示例如下:

```bash
[app@VM_105_81_centos dist]$ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.TestOk
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:204851937051ba3192100417a79fe3b2fe88d99aff8c861b86a5fbd6fa8a108d
generate keypair data succeed
####create credential succ, begin deploy contract
####contract address is: 0xecf79838dc5e0b4c2834f27b3dd2706d77d5f548
###callback trans success
============to balance:org.bcos.web3j.abi.datatypes.generated.Uint256@ee87126b
```

<br>
<br>

**(2) Ethereum测试工具**

**调用方法:** java -cp 'conf/:apps/\*:lib/\*' org.bcos.channel.test.Ethereum
**说明:** Ethereum功能与Ok合约测试工具类似，也是向链上部署Ok合约，并调用相关接口(Ok合约可参考[Ok.sol](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol))

Ethereum测试工具调用示例如下：

```bash
[app@VM_105_81_centos dist]$ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.Ethereum
start...
===================================================================
=====INIT GUOMI KEYPAIR from Private Key
====generate kepair from priv key:204851937051ba3192100417a79fe3b2fe88d99aff8c861b86a5fbd6fa8a108d
generate keypair data succeed
Ok getContractAddress 0xa5db78544f7970ff04be172f03b0b236e4e3befb
receipt transactionHash0xf46894ad8e6a22eb06e99d9a6f471d12c9a3158a1c0605a2473b2e9f97e2fa19
ok.get() 999
```

<br>

[返回目录](#目录)

<br>
<br>

# 6. 生成支持国密算法的java代码

`dist/bin/compile.sh`脚本调用`src/main/java/org/bcos/web3j/codegen/SolidityFunctionWrapperGenerator.java`将合约代码转换成java代码，便于开发者基于web3sdk和智能合约开发新应用。本章主要介绍了如何使用compile.sh脚本生成java代码。

compile.sh脚本将放置于`dist/contracts`目录下的sol合约转换成java代码(dist/contracts目录下合约是编译web3sdk时，从tools/contracts目录下拷贝获取的)，主要用法如下：

**(1) 生成不支持国密特性的java代码**

**调用方法**: `bash compile.sh "${package_name}"`

**说明**: 

- 使用默认fisco-solc编译器编译dist/contracts/目录下所有合约代码，并将合约代码转换成java代码，java代码包名由${package_name}指定;
- 执行成功后，在dist/output/目录下生成相应的java代码(java代码相对dist/output路径由包名${package_name}决定);
- 使用该方法生成的java代码不支持使用国密算法发交易;
- 若系统没有安装合约编译器fisco-solc，请参考[fisco-solc](https://github.com/FISCO-BCOS/fisco-solc)编译安装编译器



**(2) 生成支持国密特性的java代码**

**调用方法**: `bash compile.sh "${package_name}" "${enable_guomi}" "${fisco_solc_guomi_path}"`

**参数说明**:

- ${package_name}: 生成的java代码import的包名;
- ${enable_guomi}: 表明生成的java代码是否要求支持使用国密算法发交易；0表示不支持国密算法，1表示支持国密算法;
- ${fisco_solc_guomi_path}: [国密版本fisco-solc编译器](https://github.com/FISCO-BCOS/fisco-solc) 路径，默认在\`which fisco-solc\`-guomi路径下，如何编译国密版本编译器可参考[编译国密版fisco-solc](https://github.com/FISCO-BCOS/fisco-solc/tree/master#312-编译国密版fisco-solc);

**说明**: 

- 使用默认fisco-solc编译器编译dist/contracts目录下所有合约代码，使用[国密版本fisco-solc编译器](https://github.com/FISCO-BCOS/fisco-solc/tree/master#312-编译国密版fisco-solc)编译dist/contacts目录下所有合约代码，并将其转换成支持国密算法的java代码，java代码包名由${package_name}指定;
- 执行成功后，在dist/output/目录下生成相应的java代码(java代码相对dist/output路径由包名${package_name}决定);
- 使用该方法生成的java代码支持使用国密算法发交易;
- 开启国密算法方法可参考[2.2.3 开启国密算法，配置链上节点信息和证书](#223-开启国密算法配置链上节点信息和证书)
