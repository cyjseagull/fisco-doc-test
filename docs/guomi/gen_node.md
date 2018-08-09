# 普通节点环境搭建

## 生成节点证书

证书生成可参考[创世节点证书生成](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/gen_cert.html) ,若普通节点与创世节点属于同一机构，只需生成节点证书即可。

```bash
# 进入脚本所在目录(设源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools
# 在/mydata/node1/data目录下生成普通节点证书
$ bash ./generate_node_cert.sh -a fisco-dev -d /mydata/fisco-dev/ -n node1 -o /mydata/node1/data -m -s sdk1 -g

# /mydata/node1/data目录下生成的证书如下:
$ ls /mydata/node1/data/ -1
ca.crt
ca.key
client.keystore
gmagency.crt
gmca.crt
gmennode.crt
gmennode.key
gmnode.ca
gmnode.crt
gmnode.json
gmnode.key
gmnode.nodeid
gmnode.private
gmnode.serial
sdk1
server.crt
server.key

```

## 初始化普通节点环境

类似于 [创世节点环境初始化](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/genesis_node.html#id3)`_ ,普通节点使用generate_node.sh脚本初始化普通节点环境。

```bash
# 进入脚本所在目录(设源码位于/mydata目录)
$ cd /mydata/FISCO-BCOS/tools

# 创建普通节点环境:
# 节点目录: /mydata/node1, 监听端口: 127.0.0.1
# rpc端口: 8546, p2p端口: 30304
# channel prot: 8892
# bootstrapnodes.json: 127.0.0.1:30303,127.0.0.1:3030
$ ./generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304

# 从创世节点拷贝配置
$  cp /mydata/node0/genesis.json /mydata/node1/

# 此时/mydata/node1目录下已初始化所有配置
$ ls /mydata/node1/                           
config.json  data  genesis.json  keystore  log  log.conf  start.sh  stop.sh

```

## 启动节点进程

类似于[创世节点启动进程](<https://fisco-bcos-test.readthedocs.io/zh/latest/docs/guomi/genesis_node.html#id4>)方法，普通节点使用start.sh脚本启动节点

```bash
# 进入节点目录
$ cd /mydata/node1

# 调用start.sh脚本启动进程
$ ./start.sh
```

## check节点环境

启动普通节点后，check普通节点进程和error日志：

```bash
# 查看普通节点进程状态：创世节点和普通节点进程均启动
$ ps aux | grep fisco
root     20995  0.2  0.1 2171448 13316 pts/3   Sl   09:15   0:05 ./fisco-bcos --genesis /mydata/node0/genesis.json --config /mydata/node0/config.json
root     21727  0.7  0.1 2023984 14092 pts/4   Sl   09:52   0:01 ./fisco-bcos --genesis /mydata/node1/genesis.json --config /mydata/node1/config.json

# 通过最新日志check节点连接: 刷出"topics send"日志，表明节点连接正常
$ tail -f log_2018080911.log 
DEBUG|2018-08-09 11:36:21:251| Send topic Req:0 type:0
DEBUG|2018-08-09 11:36:21:251|topics Send to730195b08dda7b027c9ba5bec8ec19420aa996c7ce72fa0954711d46c1c66ae8c2eeaa5f84d1f7766f21ba3dc822bc6d764fbee14034b19a0cf1c69c7f75e537@10.107.105.81:30303

```