# web3sdk开发入门(链上转账)

```eval_rst
.. admonition:: 文档目标

   区块链系统因其开放性、不可篡改性、去中心化特性成为构建可信的去中心化应用的核心解决方案，Java是当前最主流的编程语言之一, 区块链系统支持java调用智能合约很重要。

   web3sdk实现了部署和调用智能合约的接口, 方便用户将Java系统集成到FISCO-BCOS平台中。
   
   本文档主要目标:
    - 以链上转账为蓝本，引导大家使用web3sdk将数据上链；
    - 介绍使用web3sdk调用和部署智能合约的流程。

.. admonition:: 参考资料

    - 智能合约参考文档：http://solidity.readthedocs.io/en/v0.4.24/
    - `示例合约下载 <https://github.com/FISCO-BCOS/web3sdk/tree/master/tools/Ok.sol>`_
    - FISCO dev团队提供的示例应用:
      (1) 存证Demo： https://github.com/FISCO-BCOS/evidenceSample
      (2) 群/环签名客户端Demo: https://github.com/FISCO-BCOS/sig-service-client
      (3) depotSample服务Demo: https://github.com/FISCO-BCOS/depotSample

.. admonition:: 转账小程序功能设计 

   基于web3sdk实现转账功能，并记录每笔转账的明细，转账相关的信息均存入区块链中：
    (1) 实现基本转账功能：如Alice转N元给Bob, Alice账号减少N元, Bob的账号增加N元;
    (2) 查询账户余额：Alice和Bob可查询各自账户余额
    (3) 交易明细记录：Alice和Bob间每笔转账均有日志记录

```

## 链上转账小程序开发步骤 

```eval_rst
.. important:: 
   开发转账小程序前，请确保：
    - 参考 `FISCO BCOS入门 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/index.html>`_ 完成FISCO BCOS节点环境搭建
     ( 快速搭链方法可参考 `FISCO BCOS快速搭链工具      <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/tools/index.html>`_ )
    - 参考 `web3sdk入门 <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/web3sdk/quick-start/index.html>`_ 完成web3sdk java环境的搭建
    - 已经安装正确版本的java(1.8+)和gradle(4.0+)

.. admonition:: 主要开发步骤

   使用web3sdk开发区块链java应用主要包括如下过程:
    (1) 数据结构和接口设计
    (2) 编写合约
    (3) 将合约代码转换成java代码
    (4) 编写应用程序：调用合约转换后的java代码完成数据上链逻辑
   
```


下面以编写链上转账小程序为例，step by step介绍使用web3sdk构建区块链应用过程。

## 转账小程序合约设计与实现

```eval_rst
.. admonition:: 数据结构和接口设计

   代码接口设计:
    - 转账接口(向指定账户转入num元人民币): trans(uint num)
    - 查询账户余额接口: get()

   数据结构设计:
    - 账户信息(Account): 包括账号信息(account)和余额信息(balance)
    - 转账明细(Translog): 包括每笔交易的转账时间(time), 转入地址(to), 转出地址(from)和转账金额(amount)
    - 主要数据成员
     (1) Account from: 金额转出账户信息;
     (2) Account to: 金额转入账户信息
     (3) Translog[] log数组：记录转账明细的数组

.. admonition:: 智能合约代码Ok.sol

    .. literalinclude:: Ok.cpp
       :language: cpp
       :linenos:

```     

## 将合约代码转换成java代码

```eval_rst
.. admonition:: 转换脚本compile.sh使用方法
   
   web3sdk提供了转换脚本compile.sh，可将合约代码转换成java代码:
    - 转换脚本 ``compile.sh`` 存放路径: ``web3sdk/dist/bin/compile.sh``
    - 转换脚本 ``compile.sh`` 脚本用法：( ``${package}`` 时生成的java代码import的包名)
     (1) 合约代码转换成不包含国密特性的java代码(所有版本均支持): ``bash compile.sh ${package}``
     (2) 合约代码转换成支持国密特性的java代码( `1\.2\.0版本  <https://github.com/FISCO-BCOS/web3sdk/tree/V1.2.0>`_ 后支持):``bash compile.sh ${package} 1``
    - 建议使用 `1\.2\.0版本 <https://github.com/FISCO-BCOS/web3sdk/tree/V1.2.0>`_ 后的web3sdk时，生成支持国密特性的java代码，应用有更大可扩展空间

```

```eval_rst
.. admonition:: 将合约代码Ok.sol转换为java代码Ok.java操作步骤

    查看web3sdk提供的测试合约

     .. code-block:: bash

        $ cd /mydata/web3sdk/tool/contracts
        $ ls
        EvidenceSignersData.sol  Evidence.sol  Ok.sol
        #----进入compile.sh脚本所在路径(设web3sdk代码路径是/mydata/web3sdk)
        $ cd /mydata/web3sdk/dist/bin
    
    Ok.sol转换成不支持国密特性的Ok.java

       .. code-block:: bash

          #执行compile.sh脚本，将/mydata/web3sdk/dist/contract目录下所有合约代码转换成java代码
          $ bash compile.sh com

    查看生成的java代码(位于/mydata/web3sdk/dist/output)

       .. code-block:: bash

          $ tree
          # ...此处省略若干输出...
          ├── Ok.abi
          ├── Ok.bin
          └── com
              ├── Evidence.java
              ├── EvidenceSignersData.java
              └── Ok.java

    高版本可选项：将合约转换成支持国密特性java代码(web3sdk版本号>= 1.2.0时,推荐使用)
     .. code-block:: bash

        $ bash compile.sh com 1

```

```eval_rst
.. admonition:: 转换后的java代码Ok.java
   
   以上步骤执行完毕后，生成了Ok.sol对应的java代码Ok.java(将包名改为org.bcos.channel.test)，具体代码如下：

.. literalinclude:: Ok.java
   :language: java
   :linenos:

```

## 编写java程序调用合约代码

```eval_rst
.. admonition:: 参考资料

   - AMOP: https://fisco-bcos-test.readthedocs.io/zh/latest/docs/features/amop/index.html
   - web3j JSON-RPC: https://github.com/ethereum/wiki/wiki/JSON-RPC

.. admonition:: 链上转账小程序关键代码

   1. 加载 `applicationContext.xml <https://github.com/FISCO-BCOS/web3sdk/blob/master/src/test/resources/applicationContext.xml>`_ 配置
    
    .. code-block:: java
       :linenos:

       //import相关包
       import org.springframework.context.support.ClassPathXmlApplicationContext;
       import org.springframework.context.ApplicationContext;
       import org.bcos.channel.client.Service;
       
       //加载配置
       ApplicationContext context = new ClassPathXmlApplicationContext("classpath:applicationContext.xml");


   2. 初始化AMOP服务
   
    .. code-block:: java
       :linenos:

       //import相关包
       import org.bcos.channel.client.Service;
       import org.bcos.web3j.protocol.Web3j;
       import org.bcos.web3j.protocol.channel.ChannelEthereumService;
       
       //初始化客户端channel服务
       Service service = context.getBean(Service.class);
       service.run();
       //初始化AMOP服务
       ChannelEthereumService channelEthereumService = new ChannelEthereumService();
       channelEthereumService.setChannelService(service);


   3. web3j对象初始化

      .. code-block:: java
         :linenos:
         
         //import相关包
         import org.bcos.web3j.protocol.Web3j;
         //用AMOP服务初始化web3j对象
         Web3j web3 = Web3j.build(channelEthereumService);
   
   4. 加载签名密钥对

    .. code-block:: java
       :linenos:

       //import相关包
       import org.bcos.web3j.crypto.ECKeyPair;
       import org.bcos.web3j.crypto.Credentials;
       import java.math.BigInteger;
       //加载签名密钥对
       BigInteger bigPrivKey = new BigInteger(privKey, 16);
       //通过私钥bigPrivKey推导公钥，并生成ECKeyPair密钥对
       ECKeyPair keyPair = ECKeyPair.create(bigPrivKey); 
       if (keyPair == null)
            return null;
       //根据签名密钥对加载Credentials对象 
       Credentials credentials = Credentials.create(keyPair);


   5. 调用Ok.java接口部署链上转账合约功能

    .. code-block:: java
       :linenos:
       
       //import相关包
       package org.bcos.channel.test; //import转账合约代码所在的java包
       import java.math.BigInteger;
       import org.bcos.web3j.abi.datatypes.Address; 
       
       //初始化交易参数
       // gasPrice: 每gas对应的wei数目(wei是以太坊最小计价单位), FISCO BCOS剔除以太坊价值的概念，gasPrice用于保证虚拟机evm被拒绝服务攻击
       //gasLimit: 交易的gas限制
       //initialWeiValue: FISCO BCOS平台剔除wei的价值概念，填写默认值"0"即可
       java.math.BigInteger gasPrice = new BigInteger("30000000");
       java.math.BigInteger gasLimit = new BigInteger("30000000");
       java.math.BigInteger initialWeiValue = new BigInteger("0");
       
       //调用Ok.java合约代码部署合约，并返回合约对象
       Ok okDemo = Ok.deploy(web3, credentials, gasPrice, gasLimit, initialWeiValue).get();
       //使用合约对象的getContractAddress接口获取合约地址
       System.out.println("Ok getContractAddress " + ok.getContractAddress());

   6. 调用转账合约接口，实现链上转账

    .. code-block:: java
       :linenos:
       
       //import相关包
       import java.math.BigInteger;
       import org.bcos.web3j.protocol.core.methods.response.TransactionReceipt;
       import org.bcos.web3j.tx.RawTransactionManager;
       import org.bcos.web3j.abi.datatypes.generated.Uint256;
       
       //调用转账接口，给0x01账号循环给0x02账号转账4
       //(合约调用逻辑可根据实际需求设置，这里仅是示例)
       if (okDemo != null) {
           while (true) {
               TransactionReceipt receipt = okDemo.trans(new Uint256(4)).get();
               //查询0x2账户余额信息
               Uint256 toBalance = okDemo.get().get();
               System.out.println("============to balance:" + toBalance.getValue());
               Thread.sleep(1000);
            }
        } 
    
  `1\.2\.0版本的web3sdk <https://github.com/FISCO-BCOS/web3sdk/tree/V1.2.0>`_ 支持使用国密算法发交易，使用如下方法加载公私钥对可同时兼容国密算法和非国密算法：
    .. code-block:: java
       :linenos:

       //import相关包
       import org.bcos.web3j.crypto.GenCredential;
       //调用GenCredential类加载公私钥对
       ToolConf toolConf=context.getBean(ToolConf.class);
       Credentials credentials = GenCredential.create(toolConf.getPrivKey()); 


.. important::
   `链上转账小程序TestOk.java完整代码下载 <https://github.com/FISCO-BCOS/web3sdk/blob/master/src/test/java/org/bcos/channel/test/TestOk.java>`_
```

## 运行链上转账小程序

```eval_rst
.. admonition:: 编译并运行链上转账小程序
   
   编译链上转账小程序
    .. code-block:: bash
       
       # 进入web3sdk源码目录(设web3sdk源码位于/mydata/目录下)
       cd /mydata/web3sdk
       # 使用gradle编译源码(编译成功后会生成/mydata/web3sdk/dist目录)
       gradle build
   
   运行链上转账小程序
    .. code-block:: bash

       # 进入/mydata/web3sdk/dist目录，运行测试程序
       $ cd /mydata/web3sdk/dist
       $ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.TestOk
       ===================================================================
       =====INIT ECDSA KEYPAIR From private key===
       ####create credential succ, begin deploy contract
       ============to balance:4
       ============to balance:8

    通过应用程序执行结果可看出，链上转账小程序运行结果符合代码逻辑，即完成了0x01账户到0x02账户的链上转账功能。

```

## 总结

``` eval_rst
.. note::
   根据以上描述，使用web3sdk开发区块链应用主要包括如下过程：
    1. 根据应用功能设计合约代码(包括数据结构和接口)
    2. 编写智能合约(必要时可以用Nodejs简单验证合约代码逻辑是否正确)
    3. 将合约代码转换成java代码
    4. 编写java应用程序，调用合约java接口完成合约部署和调用功能
    5. 应用功能测试
```


