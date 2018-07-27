# 创建创世节点

国密版FISCO BCOS 创建创世节点流程与[非国密版FISCO BCOS](manual#%E7%AC%AC%E4%B8%89%E7%AB%A0-%E5%88%9B%E5%BB%BA%E5%88%9B%E4%B8%96%E8%8A%82%E7%82%B9)流程相似，但**配置god账号**和**配置节点身份**有所不同；

## 创建节点环境

<br>

参考[非国密版FISCO BCOS的**创建节点环境**](manual#31-%E5%88%9B%E5%BB%BA%E8%8A%82%E7%82%B9%E7%8E%AF%E5%A2%83)一节。

<br>

## 配置国密版god账号

<br>

god账号是拥有区块链最高权限的账号，类似于[非国密版FISCO BCOS](manual#32-%E9%85%8D%E7%BD%AEgod%E8%B4%A6%E5%8F%B7)，国密版FISCO BCOS节点启动前必须配置god账号。

<br>

### 生成国密版god账号

<br>

国密版FISCO BCOS提供了国密版账号生成功能，用如下命令生成god账号：

```bash
#====使用--newaccount选项生成国密版god账号====
$ fisco-bcos --newaccount
address:0xf77f6c849d579748678fa31e329b6ef504369b3f
publicKey:f62c3d7db6c0d7fe7761adca9bc74d7fc16a5dcbef38270fdda15dd4e24840ba900e39f73795342589703e9b8d225fe24e2f980d1cfa6368bbe461a2627fc17e
privateKey:c1a591ceead51029756cddf89f4c9a40b4253bc53000ec15c320bf8ed516a473
```
<br>

### 配置国密版god账号

<br>

将上步生成的god的address配置填入创世节点的genesis.json的god字段：

```bash
#====从源码目录拷贝genesis.json配置文件 ====
$ cp /mydata/FISCO-BCOS/genesis.json /mydata/nodedata-1/

#====打开节点的genesis.json配置 ====
$ vim /mydata/nodedata-1/genesis.json

#====将生成的god账号address账号填入genesis.json的god字段====
"god": "0xf77f6c849d579748678fa31e329b6ef504369b3f"
```


## 配置节点身份

<br>

类似于[非国密版FISCO BCOS](manual#33-%E9%85%8D%E7%BD%AE%E8%8A%82%E7%82%B9%E8%BA%AB%E4%BB%BD)，国密版FISCO BCOS启动创世节点前，要将创世节点的身份信息NodeId配置如genesis.json文件。

<br>

### 获取节点身份信息

<br>

将[3.1节](#31-生成节点证书)生成的节点证书等信息拷贝到节点数据目录下，并查看节点NodeId：

```bash
#====将生成的证书拷贝到节点数据目录=====
# --- (设nodedata-1目录下运行机构agencyA的节点nodeA) ----
$ cp /mydata/FISCO-BCOS/cert/GM/agencyA/nodeA/* /mydata/nodedata-1/data/

#====查看节点NodeId =====
$ cat /mydata/nodedata-1/data/gmnode.nodeid
7a645ed6fe21df8455de30316b2c2180925acbde7e1831dda6192b9e37b7bfa1168df5f6de54c9753292075a8bccce735a64a4ef9c6c3896aef325396b3ea2bb
```

<br>

### 配置创世节点NodeId

<br>

> 将上步获取的节点NodeId信息填入创世节点配置文件genesis.json的initMinerNodes字段，指定创世节点为初始出块节点：

```bash
$ vim /mydata/nodedata-1/genesis.json

#====修改后genesis.json的initMinerNodes字段如下: ====
"initMinerNodes":["7a645ed6fe21df8455de30316b2c2180925acbde7e1831dda6192b9e37b7bfa1168df5f6de54c9753292075a8bccce735a64a4ef9c6c3896aef325396
b3ea2bb"]

```
