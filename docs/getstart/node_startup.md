# 增加节点

## 准备

查看创世节点信息

``` shell
cd /mydata/FISCO-BCOS/tools/scripts/

#sh node_info.sh -d 要查看信息的节点目录
sh node_info.sh -d /mydata/node0/
```

得到创世节点信息

``` shell
Name:   node0
Agency:   test_agency
CA hash:  B33BDF6F9E4B3703
Node ID:  cd9992e71c1a68fba0a5d3fd61b94a61a12da859e279231fc747c0016867795a38eebaacb608032b59d9516b093186aed34ccd5015444b679df50c2b3b99e643
RPC address:  127.0.0.1:8545
P2P address:  127.0.0.1:30303
Channel address: 127.0.0.1:8891
SystemProxy address: 0x919868496524eedc26dbb81915fa1547a20f8998
Node dir:  /mydata/node0/
State:   Running (pid: 45162)
```

记录关键信息

``` log
Node ID:  cd9992e71c1a68fba0a5d3fd61b94a61a12da859e279231fc747c0016867795a38eebaacb608032b59d9516b093186aed34ccd5015444b679df50c2b3b99e643
P2P address:  127.0.0.1:30303
SystemProxy address: 0x919868496524eedc26dbb81915fa1547a20f8998
```



## 生成节点

生成节点的目录、配置文件、启动脚本、身份文件、证书文件.

**注意：端口不要和其它节点重复**

``` shell
#sh generate_node -o 节点文件生成位置 -n 节点名 -l 节点监听的IP -r 节点的RPC端口 -p 节点的P2P端口 -c 节点的Channel Port端口 -e 链上现有节点的P2P端口列表，用“,”隔开（如指向创世节点和自己 127.0.0.1:30303,127.0.0.1:30304） -d 机构证书存放目录 -a 机构证书名 -x SystemProxy address（链上的所有节点都一样） -i 创世节点的Node ID
sh generate_node.sh -o /mydata -n node1 -l 127.0.0.1 -r 8546 -p 30304 -c 8892 -e 127.0.0.1:30303,127.0.0.1:30304 -d /mydata/test_agency -a test_agency -x 0x919868496524eedc26dbb81915fa1547a20f8998 -i cd9992e71c1a68fba0a5d3fd61b94a61a12da859e279231fc747c0016867795a38eebaacb608032b59d9516b093186aed34ccd5015444b679df50c2b3b99e643
```

若成功，得到节点信息

``` log
Node generate success!
-----------------------------------------------------------------
Name:   node1
Agency:   test_agency
CA hash:  B33BDF6F9E4B3704
Node ID:  0883cf560536cd75a8cbb8afc1eb1314c297d7e94e85bbad829307f9eb0dfac8873c8f6f5717b8855eddc2ca935ed5b3b21a9cee5e04a7b3d2b2f2fe39c77e9a
RPC address:  127.0.0.1:8546
P2P address:  127.0.0.1:30304
Channel address: 127.0.0.1:8892
SystemProxy address: 0x0
Node dir:  /mydata/node1
State:   Stop
-----------------------------------------------------------------
```



## 启动节点

直接到节点文件目录下启动

``` shell
cd /mydata/node1
sh start.sh
#关闭用 sh stop.sh
```



## 节点加入联盟

让节点成为参与共识的成员

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
```

若已正确设置，则无需重复设置：将tools下的脚本操作对象指向链上某个节点（此链上只有一个创世节点）

```shell
#sh set_proxy_address.sh -o 节点的RPC address
sh set_proxy_address.sh -o 127.0.0.1:8545 
```

将节点注册如联盟中，参与共识

```shell
#sh register_node.sh -d 要注册节点的文件目录
sh register_node.sh -d /mydata/node1/
```



## 验证节点启动

### 验证进程

查看节点进程

```shell
ps -ef |grep fisco-bcos
```

若看到节点进程，表示创世节点启动成功

```log
root  6227  6224  3 17:22 pts/2    00:00:02 fisco-bcos --genesis /mydata/node1/genesis.json --config /bcos-data/node1/config.json
```

### 验证已连接

查看日志

``` shell
cat /mydata/node1/log/* | grep "topics Send to"
```

看到发送topic的日志，表示节点已经连接了相应的另一个节点

``` log
DEBUG|2018-05-25 21:14:39|topics Send to6a9b9d071fa1e52a12c215ec0f469668f177af4817823e71277f36cbe3e020ff8cbe953c967fbc4d7467cd0eadd7443212d87c99ad38976b2150eccbc1aaa739@127.0.0.1:30304
```

### 验证已加入联盟

查看联盟成员

```shell
babel-node XXXX
```

若看到节点在列表中，表示此节点已加入联盟，已参与共识

```log

```



### 验证可共识

查看日志，查看打包信息

```shell
tail -f /mydata/node1/log/* |grep +++
```

可看到周期性的出现如下日志，表示节点间在周期性的进行共识，节点运行正确

```log
INFO|2017-11-23 15:04:12|+++++++++++++++++++++++++++ Generating seal onc04e60aa22d6348f323de53031744120206f317d3abcb8b3a90be060284b8a5b#1tx:0time:1511420652136
INFO|2017-11-23 15:04:14|+++++++++++++++++++++++++++ Generating seal on08679a397f9a2d100e0c63bfd33a7c7311401e282406b87fd6c607cfb2dde2c6#1tx:0time:1511420654148
```


