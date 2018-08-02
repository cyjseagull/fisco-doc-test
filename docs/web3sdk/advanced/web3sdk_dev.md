```eval_rst
==============================
 web3sdk开发示例
=============================
```

下面提供了web3sdk开发示例，从合约编写、合约代码转换成java代码、客户端使用web3sdk部署和调用合约方面简单介绍了基于web3sdk的客户端小程序开发过程。

```eval_rst
开发合约代码
---------------------------------
```

### 合约功能和代码设计

```eval_rst
.. important::

   - 智能合约参考文档：http://solidity.readthedocs.io/en/v0.4.24/
   - `示例合约下载路径 <https://github.com/FISCO-BCOS/web3sdk/tree/master/tools/Ok.sol>`_

```

```eval_rst
.. note::    
   场景设计
    - 场景：使用智能合约实现转账功能，并记录每笔转账的明细
    - 主要功能: (1) 转账; (2)查询账户余额

   代码接口设计:
    - 转账接口(向指定账户转入num元人民币): trans(uint num)
    - 查询账户余额接口: get()

   数据结构设计:
    - 账户信息Account: 包括账号信息account和余额信息balance
    - 转账明细Translog: 包括每笔交易的转账时间time, 转入地址to, 转出地址from和转账金额amount
    - 主要数据成员
     (1) Account from: 金额转出账户信息;
     (2) Account to: 金额转入账户信息
     (3) Translog[] log数组：记录转账明细的数组   
```
**根据以上设计，可实现智能合约代码Demo如下：**

```eval_rst

.. literalinclude:: Ok.cpp
   :language: cpp
   :linenos:

```

## 将合约代码转换成java代码

```eval_rst
.. important::
    将合约代码转换成java代码前，请确保已经参考 `web3sdk入门  <https://fisco-bcos-test.readthedocs.io/zh/latest/docs/web3sdk/quick-start/index.html>`_  成功搭建了web3sdk环境

```

**web3sdk提供了转换脚本compile.sh，可将合约代码转换成java代码**

```eval_rst
.. note::
   - 转换脚本 ``compile.sh`` 存放路径: ``web3sdk/dist/bin/compile.sh``
   - 转换脚本 ``compile.sh`` 脚本用法：(``${package}``时生成的java代码import的包名)
    (1) 合约代码转换成不包含国密特性的java代码(所有版本均支持): ``bash compile.sh ${package}``
    (2) 合约代码转换成支持国密特性的java代码( `1\.2\.0版本 <https://github.com/FISCO-BCOS/web3sdk/tree/V1.2.0>`_ 后支持):``bash compile.sh ${package} 1``
   - 建议使用 `1\.2\.0版本 <https://github.com/FISCO-BCOS/web3sdk/tree/V1.2.0>`_ 后的web3sdk时，生成支持国密特性的java代码，应用有更大可扩展空间

```

**下面给出代码转换操作示例：**

```bash
#查看web3sdk提供的测试合约
#(EvidenceSignersData.sol和Evidence.sol是web3sdk提供的存证示例合约)
# Ok.sol是上节提到的测试合约
$ cd /mydata/web3sdk/tool/contracts
$ ls
EvidenceSignersData.sol  Evidence.sol  Ok.sol

#进入compile.sh脚本所在路径(设web3sdk代码路径是/mydata/web3sdk)
$ cd /mydata/web3sdk/dist/bin

#执行compile.sh脚本，将/mydata/web3sdk/dist/contract目录下所有合约代码转换成java代码
#1. 转换成不支持国密特性的java代码，包名为org.bcos.channel.test
$ bash compile.sh org.bcos.channel.test
#2. 转换成支持国密特性的java代码(使用版本号 >= 1.2.0的web3sdk时，推荐使用)
$ bash compile.sh org.bcos.channel.test 1

#执行以上命令后,编译生成的代码位于/mydata/web3sdk/dist/output目录
#查看生成的代码文件(Ok.sol编译后的java代码位于org/bcos/channel/test/目录下)
#([abi](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI)和[bin](http://solidity.readthedocs.io/en/v0.4.24/using-the-compiler.html)文件是编译过程中产生的临时文件)
$ tree
.
├── Evidence.abi
├── Evidence.bin
├── EvidenceSignersData.abi
├── EvidenceSignersDataABI.abi
├── EvidenceSignersDataABI.bin
├── EvidenceSignersData.bin
├── Ok.abi
├── Ok.bin
└── org
    └── bcos
        └── channel
            └── test
                ├── Evidence.java
                ├── EvidenceSignersData.java
                └── Ok.java
```

通过以上操作，将示例合约Ok.sol转化成了java代码Ok.java:
```eval_rst

.. literalinclude:: Ok.java
   :language: java
   :linenos:

```




## 编写java程序调用合约代码

```eval_rst

.. literalinclude:: TestOk.java
   :language: java
   :linenos:

```

## web3sdk部署合约

## web3sdk调用合约
