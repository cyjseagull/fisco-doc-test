# 应用开发指南

## 应用开发步骤 

```eval_rst

.. admonition:: 主要开发步骤

   使用web3sdk开发区块链java应用主要包括如下过程:
    (1) 数据结构和接口设计
    (2) 编写合约
    (3) 将合约代码转换成java代码
    (4) 编写应用程序：调用合约转换后的java代码完成数据上链逻辑
   
```

## 编写合约


```eval_rst
.. admonition:: 合约功能设计：实现简单计数器

   实现一个简单的计数器，主要功能包括： 
    - 设置和读取计数器名字、增加计数、读取当前计数功能。
    - 通过receipt log的方式，把修改记录log到区块中，供客户端查询。
    
    (注: receipt log用处很大，是区块链和业务端同步交易处理过程和结果信息的有效渠道)

.. admonition:: 智能合约代码Counter.sol
    
    根据合约功能要求可实现智能合约 `Counter.sol <codes/Counter.sol>`_ ，合约代码如下：

    .. literalinclude:: codes/Counter.sol
       :language: cpp
       :linenos:


.. admonition:: 将合约代码Counter.sol转换为java代码Counter.java

    将Counter.sol放置到web3sdk/dist/contracts下，执行合约编译脚本：

       .. code-block:: bash

          # 进入合约编译脚本所在目录 (设web3sdk位于/mydata目录)
          $ cd /mydata/web3sdk/dist/bin
          # 执行合约编译脚本
          # (com是java代码所属的包，转换后可手动修改)
          $ bash compile.sh  org.bcosliteclient

    查看生成的java代码

       .. code-block:: bash
          
          $ cd /mydata/web3sdk/dist/output
          $ tree
          # ...此处省略若干输出...
          ├── Counter.abi
          ├── Counter.bin
          └── org
              └── bcosliteclient
                  ├── Counter.java
                  ├── Evidence.java
                  ├── EvidenceSignersData.java
                  └── Ok.java

    output目录生成了合约的.abi, .bin等文件，以及org/bcosliteclient/Counter.java文件。这个java文件可以复制到客户端开发环境里，后续建立的java工程的对应的包路径下。Counter.sol对应的Counter.java代码如下：

     `Counter.java <codes/Counter.java>`_ 

```


## 部署合约


```eval_rst
.. admonition:: 下载java应用bcosliteclient

   - FISCO-BCOS提供了示例应用bcosliteclient，该应用在 `CounterClient <codes/CounterClient.java>`_ 中提供Counter.sol合约部署和调用功能。应用下载链接如下:

     `bcosliteclient.zip <codes/bcosliteclient.zip>`_ 

.. admonition:: 编译bcosliteclient应用

   .. code-block:: bash
      
      # 解压应用程序(设下载的压缩包bcosliteclient.zip位于/mydata目录下)
      $ cd /mydata && unzip bcosliteclient.zip
      
      # 编译bcosliteclient应用
      $ cd bcosliteclient && gradle build
    
   此时bcosliteclient应用目录如下:
    .. code-block:: bash
    
       ├── bcosliteclient # 编译生成目录
       │   ├── bin        # 包含部署和调用Counter.sol合约的可执行脚本
       │   ├── conf       # 配置文件，包含客户端配置文件applicationContext.xml，客户端证书
       │   └── lib        # jar包目录
       ├── build          # 编译生成的临时目录
       │   ├── ...省略若干行...
       ├── build.gradle   
       ├── lib
       │   ├── fastjson-1.2.29.jar
       │   └── web3sdk.jar    # 应用引用的web3sdk jar包
       └── src
          ├── bin             # 包含可执行程序bcosclient
          ├── contract        
          |── org             # 源码目录
          └── resources       # 配置文件目录

.. admonition:: 配置java应用


```


可使用附件工程里的build.gradle配置文件，包含了基本的java库依赖，在classpath下放置附件工程里applicationContext.xml文件（基于web3sdk1.2版本）,默认的log4j2.xml配置文件默认把所有信息打印到控制台，便于观察，可以根据自己的喜好和需要修改

在项目目录下执行gradle build ，应该会自动拉取所有相关java库到项目的lib目录下。

同时也把fisco bcos的web3sdk.jar复制到项目的lib目录下。

对java项目进行必要的配置，如文本编码方式，build path等，创建一个空的带main入口的java文件，如在org.bcosclient包路径下的bcosliteclient.java，写一两行打印输出什么的，保证这个简单的java项目能正常编译跑通，避免出现开发环境问题。




## 运行应用

```eval_rst


```

## 总结


```eval_rst

.. note::
   根据以上描述，使用web3sdk开发区块链应用主要包括如下过程：
    1. 根据应用功能设计合约代码(包括数据结构和接口)
    2. 编写智能合约(必要时可以用Nodejs简单验证合约代码逻辑是否正确)
    3. 将合约代码转换成java代码
    4. 编写java应用程序，调用合约java接口完成合约部署和调用功能
    5. 应用功能测试

.. admonition:: 参考资料

    - 智能合约参考文档：http://solidity.readthedocs.io/en/v0.4.24/
    - AMOP: https://fisco-bcos-test.readthedocs.io/zh/latest/docs/features/amop/index.html
    - web3j JSON-RPC: https://github.com/ethereum/wiki/wiki/JSON-RPC
    - FISCO dev团队提供的示例应用:
      (1) 存证Demo： https://github.com/FISCO-BCOS/evidenceSample
      (2) 群/环签名客户端Demo: https://github.com/FISCO-BCOS/sig-service-client
      (3) depotSample服务Demo: https://github.com/FISCO-BCOS/depotSample

```




