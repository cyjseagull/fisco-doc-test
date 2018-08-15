# 基本操作

本文提供了FISCO-BCOS的基本操作。包括证书操作，节点操作，链操作及信息查看。



## 证书操作

### 生成链证书 （CA）

**脚本**：generate_chain_cert.sh

**说明**：在指定位置生成链的根证书CA

**操作**：

查看用法

``` shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_chain_cert.sh -h
```

生成证书

``` shell
bash generate_chain_cert.sh -o /mydata
```

在目录下生成

``` log
#tree /mydata
/mydata
|-- ca.crt
`-- ca.key
```

### 生成机构证书

**脚本**：generate_agency_cert.sh

**说明**：用链的根证书，在指定的位置生成机构的证书

**操作**：

查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_agency_cert.sh -h
```

生成证书

``` shell
bash generate_agency_cert.sh -c /mydata -o /mydata -n test_agency
```

在目录下生成

``` log
#tree test_agency
test_agency/
|-- agency.crt
|-- agency.csr
|-- agency.key
|-- ca.crt
`-- cert.cnf
```

### 生成节点证书

**脚本**：generate_node_cert.sh

**说明**：用机构证书，在节点的data目录下生成节点证书。在使用本脚本前，请先用generate_node_basic.sh生成节点目录。

**操作**：

查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_node_cert.sh -h
```

生成证书

``` shell
bash generate_node_cert.sh -a test_agency -d /mydata/test_agency -n node0 -o /mydata/node0/data
```

节点目录下生成证书，身份，功能等文件，用*标出

``` log
node0/
|-- config.json
|-- data
|   |-- agency.crt *
|   |-- bootstrapnodes.json
|   |-- ca.crt *
|   |-- node.ca *
|   |-- node.crt *
|   |-- node.csr *
|   |-- node.json *
|   |-- node.key *
|   |-- node.nodeid *
|   |-- node.param *
|   |-- node.private *
|   |-- node.pubkey *
|   `-- node.serial *
|-- keystore
|-- log
|-- log.conf
|-- start.sh
`-- stop.sh
```

### 生成SDK证书

**脚本**：generate_sdk_cert.sh

**说明**：在指定机构的证书目录下生成机构对应的SDK证书。此脚本相对独立，只有需要使用web3sdk，才需使用此脚本。

**操作**：

查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_sdk_cert.sh -h
```

生成证书

``` shell
bash generate_sdk_cert.sh -d /mydata/test_agency
```

输入一系列密码后，在机构证书目录下生成sdk文件夹

``` log
#tree test_agency/
test_agency/
|-- agency.crt
|-- agency.csr
|-- agency.key
|-- agency.srl
|-- ca-agency.crt
|-- ca.crt
|-- cert.cnf
`-- sdk
    |-- ca.crt
    |-- client.keystore
    |-- keystore.p12
    |-- sdk.crt
    |-- sdk.csr
    |-- sdk.key
    |-- sdk.param
    |-- sdk.private
    `-- sdk.pubkey
```

## 节点操作

### 生成创世节点

**脚本**：generate_genesis_node.sh

**说明**：生成创世节点，并自动内置系统合约。其中会调用generate_node_basic.sh，generate_node_cert.sh、generate_genesis.sh和deploy_system_contract.sh生成创世节点的目录、文件、证书和系统合约。生成的创世节点是关闭状态。创世节点生成后，需启动，并注册，将其加入联盟中参与共识。

**操作**：查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_genesis_node.sh -h
```

生成创世节点

``` shell
bash generate_genesis_node.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -d /mydata/test_agency -a test_agency
```

生成创世节点所有的文件，并自动部署上了系统合约

``` log
#tree node0/
node0/
|-- config.json
|-- data
|   |-- 4bcbbeb4
|   |   |-- 12041
|   |   |   |-- extras
|   |   |   |   |-- 000003.log
|   |   |   |   |-- CURRENT
|   |   |   |   |-- LOCK
|   |   |   |   |-- LOG
|   |   |   |   `-- MANIFEST-000002
|   |   |   `-- state
|   |   |       |-- 000003.log
|   |   |       |-- CURRENT
|   |   |       |-- LOCK
|   |   |       |-- LOG
|   |   |       `-- MANIFEST-000002
|   |   `-- blocks
|   |       |-- 000003.log
|   |       |-- CURRENT
|   |       |-- LOCK
|   |       |-- LOG
|   |       `-- MANIFEST-000002
|   |-- abiname
|   |   |-- 000003.log
|   |   |-- CURRENT
|   |   |-- LOCK
|   |   |-- LOG
|   |   `-- MANIFEST-000002
|   |-- agency.crt
|   |-- bootstrapnodes.json
|   |-- ca.crt
|   |-- event.log
|   |-- geth.ipc
|   |-- IPC_MappedFile
|   |-- keys.info
|   |-- keys.info.salt
|   |-- node.ca
|   |-- node.crt
|   |-- node.csr
|   |-- node.json
|   |-- node.key
|   |-- node.nodeid
|   |-- node.param
|   |-- node.private
|   |-- node.pubkey
|   |-- node.serial
|   |-- pbftMsgBackup
|   |   |-- 000003.log
|   |   |-- CURRENT
|   |   |-- LOCK
|   |   |-- LOG
|   |   `-- MANIFEST-000002
|   |-- RPC_MappedFile
|   `-- UTXO
|       |-- db
|       |   |-- 000003.log
|       |   |-- CURRENT
|       |   |-- LOCK
|       |   |-- LOG
|       |   `-- MANIFEST-000002
|       |-- extra
|       |   |-- 000003.log
|       |   |-- CURRENT
|       |   |-- LOCK
|       |   |-- LOG
|       |   `-- MANIFEST-000002
|       `-- vault
|           |-- 000003.log
|           |-- CURRENT
|           |-- LOCK
|           |-- LOG
|           `-- MANIFEST-000002
|-- fisco-bcos.log
|-- genesis.json
|-- keystore
|-- log
|   |-- debug_log_2018081521.log
|   |-- error_log_2018081521.log
|   |-- fatal_log_2018081521.log
|   |-- info_log_2018081521.log
|   |-- log_2018081521.log
|   |-- stat_log_2018081521.log
|   |-- trace_log_2018081521.log
|   |-- verbose_log_2018081521.log
|   `-- warn_log_2018081521.log
|-- log.conf
|-- myeasylog.log
|-- start.sh
`-- stop.sh
```

### 生成普通节点

**脚本**：generate_node.sh

**说明**：用创世节点的nodeid、系统代理合约地址、创世节点的p2p地址，生成普通节点。其中会调用generate_node_basic.sh、generate_node_cert.sh和generate_genesis.sh，生成节点的目录、文件和证书。生成的节点是关闭状态。节点启动后，会自动连接创世节点，同步系统合约。

**操作**：

查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_node.sh -h
```

生成节点

``` shell
bash generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -d /mydata/test_agency -a test_agency -x 0x919868496524eedc26dbb81915fa1547a20f8998 -i xxxxxx
```

生成节点的全部文件

``` log
tree node1
node1
|-- config.json
|-- data
|   |-- agency.crt
|   |-- bootstrapnodes.json
|   |-- ca.crt
|   |-- node.ca
|   |-- node.crt
|   |-- node.csr
|   |-- node.json
|   |-- node.key
|   |-- node.nodeid
|   |-- node.param
|   |-- node.private
|   |-- node.pubkey
|   `-- node.serial
|-- genesis.json
|-- keystore
|-- log
|-- log.conf
|-- start.sh
`-- stop.sh
```

### 生成节点基本文件

**脚本**：generate_node_basic.sh

**说明**：在指定目录下，生成节点目录，并在目录下生成节点的配置文件和操作脚本。此时，节点还缺少证书文件，功能文件和信息文件，需要继续使用generate_node_cert.sh来生成。或直接用generate_node.sh直接生成节点的所有文件。

**操作**：

查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_node_basic.sh -h
```

生成节点基本文件

``` shell
bash generate_node_basic.sh -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -e 127.0.0.1:30303,127.0.0.1:30304
```

在目录下生成

```log
#tree node0/
node0/
|-- config.json
|-- data
|   `-- bootstrapnodes.json
|-- keystore
|-- log
|-- log.conf
|-- start.sh
`-- stop.sh
```

## 链操作

### 生成god账号

**说明**：在生产条件下，需要手动生成god账号，提供给相关脚本生成节点文件。

**操作**：

到指定目录下生成god账号

``` shell
cd /mydata/FISCO-BCOS/tools/contract
node accountManager.js > godInfo.txt
cat godInfo.txt
```

得到生成的god账号信息

``` log
privKey : 0xc8a92524ac634721a9eac94c9d8c09ea719f3a01e0ed1f576f673af6eb90aeea
pubKey : 0xb2795b4000981fb56f386a00e5064bd66b7754db6532bb17f9df1975ca884fc7b3b3291f9f3b20ee0278e610b8814ff62fa7dfbbcda959766c0555eb5f48147d
address : 0xb862b65912e0857a49458346fcf578d199dba024
```

其中god账号地址是需要作为参数提供给其它脚本的

``` log
address : 0xb862b65912e0857a49458346fcf578d199dba024
```

### 生成创世块文件

脚本：generate_genesis.sh

说明：用god账号地址，创世节点的nodeid，生成创世块文件，若不指定god账号地址，用默认的god账号地址。

操作：查看用法

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
generate_genesis.sh -h
```

生成创世块文件

``` shell
bash generate_genesis.sh -i 4af70363e2266e62aaca5870d660cc4ced35deae83b67f3dffebd0dcfa3b16d96d8fe726f9fea0def06a3bbde47261b9722ddbb9461af131c9645eb660644842 -o /mydata/node1 -r 0xb862b65912e0857a49458346fcf578d199dba024
```

生成的创世块文件genesis.json

``` json
{
     "nonce": "0x0",
     "difficulty": "0x0",
     "mixhash": "0x0",
     "coinbase": "0x0",
     "timestamp": "0x0",
     "parentHash": "0x0",
     "extraData": "0x0",
     "gasLimit": "0x13880000000000",
     "god":"0xb862b65912e0857a49458346fcf578d199dba024",
     "alloc": {}, 	
     "initMinerNodes":["4af70363e2266e62aaca5870d660cc4ced35deae83b67f3dffebd0dcfa3b16d96d8fe726f9fea0def06a3bbde47261b9722ddbb9461af131c9645eb660644842"]
}
```



### 配置待操作链的端口

**脚本**：config_rpc_address.sh

**说明**：对正在运行中的链进行操作（如：注册节点，部署合约，调用合约）时，需先将全局proxy变量指向待操作的链。具体的，是将全局proxy变量设置为链上某个节点的RPC端口，即设置/mydata/FISCO-BCOS/tools/web3sdk/config.js的proxy为相应的节点RPC的URL。设置一次即可永久生效，无需重复设置。

**操作**：

查看用法

``` shell
cd /data/jimmyshi/feature-step-by-step/FISCO-BCOS/tools/scripts
sh set_proxy_address.sh -h
```

设置RPC的URL（节点的RPC的URL用node_info.sh获取）

``` shell
bash set_proxy_address.sh -o 127.0.0.1:8545
```

yes回车确认后，写入全局的proxy变量中

``` nodejs
proxy="http://127.0.0.1:8545"
```

### 部署系统合约

**脚本**：deploy_system_contract.sh

**说明**：在使用此脚本前，需调set_proxy_address.sh设置全局proxy地址。用在生成创世节点时（generate_generate_node.sh），已经自动调用此脚本部署了系统合约。若需要重新手动部署系统合约，则调用此脚本。并同时将链上其它节点的config.json修改为与创世节点相同的systemproxyaddress，并重启节点使其生效。一般来说，不推荐重新部署系统合约。重新部署系统合约意味着对链管理的重置，需要链上所有机构都同意，且需要重启链上所有的节点。

**操作**：

查看用法

``` shell
cd /data/jimmyshi/feature-step-by-step/FISCO-BCOS/tools/scripts
sh set_proxy_address.sh -h
```

部署系统合约

``` shell
bash deploy_systemcontract.sh -d /mydata/node0
```

得到系统代理合约地址

``` log
SystemProxy address: 0xbac830dee59a0f2a33beddcf53b329a4e1787ce2
```

将链上其它节点的systemproxyaddress也修改为相同的地址

``` shell
sed -i '/systemproxyaddress/c  \\t\"systemproxyaddress\":\"0xbac830dee59a0f2a33beddcf53b329a4e1787ce2\",'  /mydata/node1/config.json
sed -i '/systemproxyaddress/c  \\t\"systemproxyaddress\":\"0xbac830dee59a0f2a33beddcf53b329a4e1787ce2\",'  /mydata/node2/config.json
```



register_node.sh

## 信息查看

node_info.sh

node_all.sh



