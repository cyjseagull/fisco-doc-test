# 配置文件

```eval_rst

.. important::
   - 配置web3sdk前，请确保参考 `web3sdk编译文档 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/web3sdk/quick-start/compile.html#>`_ 成功编译web3sdk
   - 配置web3sdk前，请参考 `FISCO-BCOS Quick Start的客户端证书生成 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/chain_setting.html#id3>`_ 生成客户端证书，并将证书拷贝到web3sdk/dist/conf目录
```

## 配置java客户端相关信息 

```eval_rst
.. admonition:: web3sdk客户端配置

   打开web3sdk/dist/conf目录的applicationContext.xml文件,部分信息可以先用默认的, **先关注这些配置项** ：

   .. image:: imgs/javaconfig.png
      :align: center
   

   
   找到 `web3sdk/dist/conf/applicationContext.xml文件的【区块链节点信息配置】 <https://github.com/FISCO-BCOS/web3sdk/blob/master/src/test/resources/applicationContext.xml>`_ 一节，配置keystore密码
     .. code-block:: xml

         <property name="keystorePassWord" value="【生成client.keystore时对应的密码】" />
         <property name="clientCertPassWord" value="【生成client.keystore时对应的密码】" />
    
   **配置节点信息，请务必注意：节点id、ip、端口，和连接的FISCO-BCOS节点必须一致** 
     .. code-block:: xml

        <property name="connectionsStr">
            <list>
                <value>【节点id】@【IP】:【端口】</value>
            </list>
        </property>
    
    .. important::

       -  **节点id查询方法** ：若节点服务器上，节点数据目录所在路径为/mydata/nodedata-1/，则节点id可以在/mydata/nodedata-1/data/node.nodeid文件里查到，其他信息在/mydata/nodedata-1/config.json里可查到；
       - **这里的端口是对应config.json里的channelPort，而不是rpcport或p2pport** 
       - **list段里可以配置多个value，对应多个节点的信息，实现客户端多活通信** 
   
   其他配置
    另外，调用SystemProxy|AuthorityFilter等系统合约工具时需要配置系统合约地址SystemProxyAddress和GOD账户私钥信息，GOD账号默认为0x776bd5cf9a88e9437dc783d6414bccc603015cf0,GOD账号私钥默认为bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd

     .. code-block:: xml

        <bean id="toolConf" class="org.bcos.contract.tools.ToolConf">
            <property name="systemProxyAddress" value="【系统合约代理地址,对应节点config.json里的systemproxyaddress】" />
            <!--GOD账户的私钥-->
            <property name="privKey" value="【对应搭链创建god帐号环境$fiscobcos/tool/godInfo.txt里的privKey】" />
            <!--GOD账户-->
            <property name="account" value="【对应搭链创建god帐号环境$fiscobcos/tool/godInfo.txt里的address】" />
            <property name="outPutpath" value="./output/" />
        </bean>
```

## 测试是否配置成功

```eval_rst
.. admonition:: 测试web3sdk与节点连接是否正常
   
   在web3sdk/dist目录下调用TestOk，输出 ``=====INIT ECDSA KEYPAIR From private key===`` 等提示，说明web3sdk与节点连接正常，否则请参考 `faq【dist/bin/web3sdk运行出错】 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/web3sdk/faq.html#id1>`_ .
   
   具体测试过程如下：
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

## applicationContext.xml详细介绍

```eval_rst
.. admonition:: applicationContext.xml配置项详细说明

   applicationContext.xml主要包括如下配置选项：

+----------------------+---------------------------------------------------------------------+
| **encryptType**      |  配置国密算法开启/关闭开关(默认为0)                                 |
|                      |   - 0: 不使用国密算法发交易                                         |
|                      |   - 1: 使用国密算法发交易                                           |
+----------------------+---------------------------------------------------------------------+
|**systemProxyAddress**|  系统代理合约地址，对应节点config.json中的systemproxyaddress值      |
+----------------------+---------------------------------------------------------------------+
| **privKey**          |  GOD账号私钥,对应 `搭链GOD账号环境 <>`_ 产生godInfo.txt的privKey    |
+----------------------+---------------------------------------------------------------------+
| **account**          |  GOD账号, 对应 `搭建GOD账号环境<>`_ 产生的godInfo.txt的address      |
+----------------------+---------------------------------------------------------------------+
|**ChannelConnections**|- caCertPath: ca.crt证书路径，默认为classpath:ca.crt                 |
|                      |- clientKeystorePath: client.keystore证书路径，                      |
|                      |  默认为classpath:client.keystore                                    | 
|                      |- keystorePassWord: 生成client.keystore时对应的密码                  | 
|                      |- clientCertPassWord: 生成client.keystore时对应的密码                |
|                      |- nodeid:SDK连接的FISCO BCOS节点ID，从节点data/node.nodeid文件获取   | 
|                      |- ip: SDK连接的FISCO BCOS节点外网ip                                  |
|                      |- channelPort: SDK连接的FISCO BCOS节点channelPort,                   |
|                      |  对应config.json的channelPort                                       | 
+----------------------+---------------------------------------------------------------------+
```

