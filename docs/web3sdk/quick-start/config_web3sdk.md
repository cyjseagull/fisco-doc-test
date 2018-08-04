# web3sdk配置运行

## 生成客户端证书

参考[FISCO-BCOS Quick Start的客户端证书生成部分](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/chain_setting.html#id3)

## 配置applicationContext.xml

web3sdk编译成功后，在web3sdk的dist/conf目录下生成applicationContext.xml文件，主要配置包括：

```eval_rst
+----------------------+---------------------------------------------------------------------+
| **encryptType**      |  配置国密算法开启/关闭开关(默认为0)                                 |
|                      |   - 0: 不使用国密算法发交易                                         |
|                      |   - 1: 使用国密算法发交易                                           |
+----------------------+---------------------------------------------------------------------+
|**systemProxyAddress**|  配置FISCO BCOS区块链的系统合约地址                                 |
+----------------------+---------------------------------------------------------------------+
| **privKey**          |  向FISCO BCOS节点发交易或发消息的账户私钥(使用默认配置即可)         |
+----------------------+---------------------------------------------------------------------+
|**ChannelConnections**|- caCertPath: CA证书路径，默认为dist/conf/ca.crt                     |
|                      |- clientKeystorePath: 客户端证书路径，默认为dist/conf/client.keystore|
|                      |- keystorePassWord: 客户端证书文件访问口令, 默认为123456             | 
|                      |- clientCertPassWord: 客户端证书验证口令, 默认为123456               |
+----------------------+---------------------------------------------------------------------+

```

以下为web3sdk的applicationContext.xml配置案例:
```eval_rst

.. literalinclude:: applicationContext.xml
   :language: xml
   :linenos:

```


## 测试是否配置成功

调用Ok合约测试web3sdk与服务器是否连接正常:

```eval_rst
.. important::

   - 测试客户端与节点连接是否正常时，必须保证连接的FISCO-BCOS节点能正常出块
   -  FISCO-BCOS节点是否正常可参考 `FISCO BCOS入门的相关介绍 <http://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/setup_nodes.html>`_

```

```bash
#-----------进入dist目录
$ cd /mydata/web3sdk/dist

#-----------调用测试合约TestOk
$ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.TestOk
===================================================================
=====INIT ECDSA KEYPAIR From private key===
contract address is: 0xecf79838dc5e0b4c2834f27b3dd2706d77d5f548
callback trans success
============to balance: 2000
....
```

(**说明**:Ok合约详细代码可参考[Ok.sol](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol))
