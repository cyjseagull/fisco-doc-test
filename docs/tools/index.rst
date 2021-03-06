################################################################################
FISCO BCOS物料包
################################################################################


.. 什么是FISCO BCOS物料包

通过简单配置 ,可以在指定服务器上构建FISCO BCOS的区块链, 构成FISCO BCOS的节点既可以直接运行于服务器, 也可以是docker节点。 可以非常快速的搭建临时使用的测试环境, 又能满足生产环境的需求。  
例如：  

配置三台服务器, 每台启动两个FISCO BCOS节点, 则将生成三个安装包, 对应三台服务器, 将安装包上传到对应的服务器上, 继续按照指引安装, 在每台服务器上启动节点, 就可以组成一个区块链网络。

* **一键部署工具**: 降低FISCO BCOS部署难度
* **区块链扩容支持**: 提供FISCO BCOS区块链快速扩容支持
* **JAVA安装**：FISCO BCOS中需要使用Oracle JDK 1.8(java 1.8)环境，提供FISCO BCOS支持的JAVA组件
* **物料包搭建FISCO BCOS环境CheckList**：检查系统是否满足搭建FISCO BCOS的条件

术语简介  

* 两种节点类型：**创世节点, 非创世节点**。
* **创世节点**：搭建一条新链时, 配置文件的第一台服务器上的第一个节点为创世节点, 创世节点是需要第一个启动的节点, 其他节点需要主动连接创世节点, 通过与创世节点的连接, 所有节点同步连接信息, 最终构建正常的网络。
* **非创世节点**：除去创世节点的其它节点。



版本支持

物料包与FISCO BCOS之间存在版本对应关系:

* 物料包1.2.X版本对应支持FISCO BCOS的版本为: 1.3.X，即物料包1.2的版本兼容支持FISCO BCOS1.3的版本

物料包的相关流程如下:

.. toctree::
   :maxdepth: 1

   environment.md
   build_blockchain.md
   expand_blockchain.md
   sample.md
   appendix.md
   oracle_java.md
   web3sdk.md
   check_list.md
   FAQ.md
