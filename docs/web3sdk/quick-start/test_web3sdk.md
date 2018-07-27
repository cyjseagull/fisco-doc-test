# 测试是否配置成功

web3sdk提供了一些测试工具，方便确定web3sdk与[FISCO BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS)通信是否正常，本节简要介绍这些测试工具使用方法：

**(1) Ok合约测试工具**

**调用方法:** java -cp 'conf/:apps/\*:lib/\*' org.bcos.channel.test.TestOk
**说明:** 向链上部署Ok合约，并调用Ok合约的trans接口(Ok合约可参考[Ok.sol](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol))

Ok合约调用示例如下:

```bash
#进入dist目录
$ cd /mydata/web3sdk/dist
#调用测试合约TestOk
$ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.TestOk
===================================================================
=====INIT ECDSA KEYPAIR From private key===
contract address is: 0xecf79838dc5e0b4c2834f27b3dd2706d77d5f548
callback trans success
============to balance: 2000
....
```

<br>
<br>

**(2) Ethereum测试工具**

**调用方法:** java -cp 'conf/:apps/\*:lib/\*' org.bcos.channel.test.Ethereum
**说明:** Ethereum功能与Ok合约测试工具类似，也是向链上部署Ok合约，并调用相关接口(Ok合约可参考[Ok.sol](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/tool/Ok.sol))

Ethereum测试工具调用示例如下：

```bash
#进入dist目录
$ cd /mydata/web3sdk/dist
#调用测试合约Ethereum
$ java -cp 'conf/:apps/*:lib/*' org.bcos.channel.test.Ethereum
start...
===================================================================
=====INIT ECDSA KEYPAIR From private key===
Ok getContractAddress 0xa5db78544f7970ff04be172f03b0b236e4e3befb
receipt transactionHash0xf46894ad8e6a22eb06e99d9a6f471d12c9a3158a1c0605a2473b2e9f97e2fa19
ok.get() 999
```
