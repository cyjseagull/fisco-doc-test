# 启动节点

## 启动节点进程

所有节点都进行相同操作

``` shell
cd node_xxx
sh start.sh
#stop.sh #关闭节点
```

## 查看节点是否正常运行

**查看进程**

``` shell
ps -ef |grep fisco-bcos
```

可看到节点进程

``` log
XXX
XXX
```

**查看节点连接**

``` shell
cat /bcos-data/node0/log/* | grep "topics Send to"
```

可以看到如下日志，表示日志对应的节点已经与另一个节点连接（Connected to 1 peers），连接正常：

``` log
XXXX
XXXX
```

**查看启动日志**

``` shell
cat node_xxx/fisco-bcos.log
```



