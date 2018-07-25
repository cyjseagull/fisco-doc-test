# 配置区块链

## 配置创世节点

生成创世块

``` shell
sh generate_genesis.sh /mydata 
```

## 证书配置
**生成链证书**

``` shell
sh generate_chain_cert.sh /mydata ca
```

**生成机构证书**

生成机构证书，假设机构名为WB

```shell
sh generate_agency_cert.sh /mydata /mydata/ca WB
```
**生成节点证书**

编写节点模板文件

``` shell
vim node_xxx.sample
```

生成节点

``` shell
sh generate_node.sh node_xxx.sample
```