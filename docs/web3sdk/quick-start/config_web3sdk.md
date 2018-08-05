# web3sdk配置运行

```eval_rst

.. admonition:: 文档目标
   ``applicationContext.xml`` 是web3sdk的配置文件，主要用于配置日志、证书、系统合约地址、FISCO-BCOS节点连接信息等，本文档详细介绍如何配置 ``applicationContext.xml`` 

.. important::
   - 配置web3sdk前，请确保参考 `web3sdk编译文档 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/web3sdk/quick-start/compile.html#>`_ 成功编译web3sdk
   - 配置web3sdk前，请参考 `FISCO-BCOS Quick Start的客户端证书生成 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/chain_setting.html#id3>`_ 生成客户端证书，并将证书拷贝到web3sdk/dist/conf目录
```

## 配置applicationContext.xml

```eval_rst
.. admonition:: applicationContext.xml配置项详细说明
   
   applicationContext.xml主要包括如下配置选项：

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


```eval_rst
.. admonition:: applicationContext.xml配置示例
   
   以下为web3sdk的applicationContext.xml配置案例:
```

```eval_rst
   .. literalinclude:: applicationContext.xml
      :language: xml
      :linenos:
```

## 测试是否配置成功



```eval_rst

.. important::

   - 测试客户端与节点连接是否正常时，必须保证连接的FISCO-BCOS节点能正常出块
   -  FISCO-BCOS节点是否正常可参考 `FISCO BCOS入门的相关介绍 <http://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/setup_nodes.html>`_

.. admonition:: 测试web3sdk与节点连接是否正常
   
   使用以下命令，调用TestOk测试web3sdk与节点连接是否正常：

    .. code-block:: bash

       #-----------进入dist目录
       $ cd /mydata/web3sdk/dist
       
       #-----------调用测试合约TestOk
       $ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.TestOk
       ===================================================================
       =====INIT ECDSA KEYPAIR From private key===
       ============to balance:4
       ============to balance:8

   (Ok合约详细代码可参考 `Ok.sol  <https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol>`_ )
```
