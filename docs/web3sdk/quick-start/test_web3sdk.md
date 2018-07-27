## 测试是否配置成功

web3sdk编译配置成功后，可调用Ok合约测试web3sdk与服务器是否连接正常:

``` important:: Tips
    测试客户端与节点连接是否正常时，必须保证连接的FISCO-BCOS节点能正常出块
    FISCO-BCOS节点是否正常可参考 `FISCO BCOS入门的相关介绍<http://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/setup_nodes.html>`_

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
