# 创世节点

## 生成创世节点

生成节点的目录、配置文件、启动脚本、身份文件、证书文件。并自动部署系统合约。

``` shell
cd /mydata/FISCO-BCOS/tools/scripts/

#sh generate_genesis_node -o 节点文件夹生成位置 -n 节点名 -l 节点监听的IP -r 节点的RPC端口 -p 节点的P2P端口 -c 节点的Channel Port端口 -d 机构证书存放目录 -a 机构证书名
#创世节点
sh generate_genesis_node.sh  -o /mydata -n node0 -l 127.0.0.1 -r 8545 -p 30303 -c 8891 -d /mydata/test_agency/ -a test_agency
```

若成功，得到创世节点信息

``` log
Genesis node generate success!
-----------------------------------------------------------------
Name:   node0
Agency:   test_agency
CA hash:  B33BDF6F9E4B3703
Node ID:  cd9992e71c1a68fba0a5d3fd61b94a61a12da859e279231fc747c0016867795a38eebaacb608032b59d9516b093186aed34ccd5015444b679df50c2b3b99e643
RPC address:  127.0.0.1:8545
P2P address:  127.0.0.1:30303
Channel address: 127.0.0.1:8891
SystemProxy address: 0x919868496524eedc26dbb81915fa1547a20f8998
Node dir:  /mydata/node0
State:   Stop
-----------------------------------------------------------------
```

记录下创世节点的RPC address，之后会用到

``` log
RPC address:  127.0.0.1:8545
```



## 启动创世节点

直接到创世节点文件目录下启动

``` shell
cd /mydata/node0
sh start.sh
#关闭用 sh stop.sh
```



## 创世节点加入联盟

让创世节点成为参与共识的第一个成员

``` shell
cd /mydata/FISCO-BCOS/tools/scripts/
```

将tools下的脚本操作对象指向链上某个节点（此链上只有一个创世节点）

``` shell
#sh set_proxy_address.sh -o 节点的RPC address
sh set_proxy_address.sh -o 127.0.0.1:8545 
```

将创世节点注册如联盟中，参与共识

``` shell
#sh register_node.sh -d 要注册节点的文件目录
sh register_node.sh -d /mydata/node0/
```



## 验证创世节点启动

### 验证进程

查看创世节点进程

``` shell
ps -ef |grep fisco-bcos
```

若看到创世节点进程，表示创世节点启动成功

``` log
root  6227  6224  3 17:22 pts/2    00:00:02 fisco-bcos --genesis /mydata/node0/genesis.json --config /bcos-data/node0/config.json
```

### 验证已加入联盟

查看联盟成员

``` shell
babel-node XXXX
```

若看到节点在列表中，表示此节点已加入联盟，已参与共识

``` log

```



### 验证可共识

查看日志，查看打包信息

``` shell
tail -f /mydata/node0/log/info* |grep +++
```

可看到周期性的出现如下日志，表示节点间在周期性的进行共识，节点运行正确

``` log
INFO|2017-11-23 15:04:12|+++++++++++++++++++++++++++ Generating seal onc04e60aa22d6348f323de53031744120206f317d3abcb8b3a90be060284b8a5b#1tx:0time:1511420652136
INFO|2017-11-23 15:04:14|+++++++++++++++++++++++++++ Generating seal on08679a397f9a2d100e0c63bfd33a7c7311401e282406b87fd6c607cfb2dde2c6#1tx:0time:1511420654148
```
