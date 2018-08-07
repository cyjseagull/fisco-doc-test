# 搭建创世节点 

```eval

.. admonition:: 注意事项
   
   创建创世节点配置genesis.json前，必须确保已在创世节点data目录生成了节点证书，参考 `证书生成 <TODO>`_ 
   
```

## 创世节点配置生成

FISCO BCOS提供generate_genesis.sh 脚本创建创世节点配置genesis.json:

```bash
# 进入脚本所在目录(设FISCO-BCOS位于/mydata目录)
$ cd /mydata/FISCO-BCOS/scripts

# 生成god账号：
$ fisco-bcos --newaccount
address:0x363a7fc65a054738e5332b2db97d63474421afe6 # god账号
publicKey:61c1012bffa671aa0a816b3919038b5ed6572b68da5e62acd92ad3f6ab52ab28ffd4a17a08dd9613e1b2495e62bc84e18fddd206283efb0c97b3ca845c466a85  #god账号公钥
privateKey:d16b5fd854d668256c7ec76aad344c84b22fdbbecc46a0a8ba8f3de32b8017fd #god账号私钥

# 初始化创世节点配置genesis.json
$ ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g 0x363a7fc65a054738e5332b2db97d63474421afe6
God account address: 0x3b5b68db7502424007c6e6567fa690c5afd71721
/mydata/node0/genesis.json is generated

# 此时在/mydata/node0/目录下生成genesis.json，内容如下:
$ cat /mydata/node0/genesis.json
{
     "nonce": "0x0",
     "difficulty": "0x0",
     "mixhash": "0x0",
     "coinbase": "0x0",
     "timestamp": "0x0",
     "parentHash": "0x0",
     "extraData": "0x0",
     "gasLimit": "0x13880000000000",
     "god":"0x3b5b68db7502424007c6e6567fa690c5afd71721",
     "alloc": {}, 
     "initMinerNodes":["08eff55799d66d7426e64e44384c8e3eb5d849b4b5dbf21a32e5b954d787cc6c2500b8d25e14bf90e327940b0a2d3eeecb26ab2ea43b076f67af75d8cb3fbcf0"]
}

# 若使用默认god账号0x3b5b68db7502424007c6e6567fa690c5afd71721生成创世节点配置，可使用如下命令：
# ./generate_genesis.sh -d /mydata/node0 -o /mydata/node0 -g # 生成/mydata/genesis.json
# god账号信息存储在/mydata/node0/guomiGodInfo.txt中

# generate_genesis.sh 脚本功能


```

## 创世节点环境初始化

FISCO-BCOS提供generate_node.sh脚本初始化节点环境

## 启动创世节点

## check创世节点环境

