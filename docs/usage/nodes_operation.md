# 区块链节点

节点是区块链上的执行单元。多个节点彼此连接，构成一个P2P网络，承载了区块链上的通信，计算和存储。节点入网后（加入联盟），成为区块链上的一个共识单位。多个节点参与共识，确保了区块链上交易的一致。

## 节点的文件

FISCO-BCOS的节点包含了下列文件

其中[]是必须文件

``` log
node0
|-- config.json    #节点总配置文件（IP，端口，共识算法）
|-- log.conf       #节点日志配置文件（日志格式，优先级）
|-- genesis.json   #创世块文件（创世块信息，god账号，创世节点）
|-- start.sh       #节点启动脚本
|-- stop.sh        #节点停止脚本
|-- data
|   |-- bootstrapnodes.json    #节点启动时需访问的peers列表
|   |-- ca.crt                 #链根证书私钥
|   |-- agency.crt             #机构证书私钥
|   |-- node.crt               #节点证书私钥
|   |-- node.ca          
|   |-- node.csr
|   |-- node.json
|   |-- node.key
|   |-- node.nodeid
|   |-- node.param
|   |-- node.private
|   |-- node.pubkey
|   |-- node.serial
|   `-- geth.ipc
|-- keystore
|-- fisco-bcos.log   #节点启动日志
`-- log  #节点运行日志目录
```





