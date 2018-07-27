# web3j API说明

## 常用API
> web3j API接口命令参考如下，--后为参数说明：

```bash
./web3sdk web3_clientVersion 
./web3sdk eth_accounts
./web3sdk eth_blockNumber
./web3sdk eth_pbftView
./web3sdk eth_getCode address blockNumber  --地址 存储位置整数
./web3sdk eth_getBlockTransactionCountByHash blockHash   --区块hash
./web3sdk eth_getTransactionCount address blockNumber   --区块号
./web3sdk eth_getBlockTransactionCountByNumber blockNumber  --区块号
./web3sdk eth_sendRawTransaction signTransactionData  --签名的交易数据
./web3sdk eth_getBlockByHash blockHash true|false   --区块hash true|false
./web3sdk eth_getBlockByNumber blockNumber  --区块号
./web3sdk eth_getTransactionByBlockNumberAndIndex blockNumber transactionPosition  --区块号 交易位置
./web3sdk eth_getTransactionByBlockHashAndIndex blockHash transactionPosition  --区块hash 交易位置
./web3sdk eth_getTransactionReceipt transactionHash  --交易hash
```

web3j API接口代码参照：

org.bcos.web3j.console.Web3RpcApi


# 权限控制API

在SDK工具包/dist/bin目录下，compile.sh为合约编译脚本，web3sdk为SDK的的执行脚本。web3sdk脚本中将权限相关的接口进行暴露，使用相关命令执行即可。权限控制介绍文档请参看[FISCO BCOS权限模型（ARPI）介绍](https://github.com/FISCO-BCOS/Wiki/tree/master/FISCO%20BCOS%E6%9D%83%E9%99%90%E6%A8%A1%E5%9E%8B) 、[联盟链的权限体系](https://github.com/FISCO-BCOS/Wiki/tree/master/%E5%8C%BA%E5%9D%97%E9%93%BE%E7%9A%84%E6%9D%83%E9%99%90%E4%BD%93%E7%B3%BB) 。

```java
org.bcos.contract.tools.ARPI_Model    #一键执行类
org.bcos.contract.tools.AuthorityManagerTools
```

在使用时，需要在applicationContext.xml文件中配置相关参数：

```xml
	<!-- 系统合约地址配置置-->
	<bean id="toolConf" class="org.bcos.contract.tools.ToolConf">
		<!--系统合约-->
		<property name="systemProxyAddress" value="0x919868496524eedc26dbb81915fa1547a20f8998" />
		<!--GOD账户的私钥-->（注意去掉“0x”）
		<property name="privKey" value="bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd" />
		<!--God账户-->
		<property name="account" value="0x776bd5cf9a88e9437dc783d6414bccc603015cf0" />
		<property name="outPutpath" value="./output/" />
	</bean>
```

> 权限控制接口命令参考如下

```bash
./web3sdk ARPI_Model 
./web3sdk PermissionInfo 
./web3sdk FilterChain addFilter name1 version1 desc1 
./web3sdk FilterChain delFilter num 
./web3sdk FilterChain showFilter 
./web3sdk FilterChain resetFilter 
./web3sdk Filter getFilterStatus num 
./web3sdk Filter enableFilter num 
./web3sdk Filter disableFilter num 
./web3sdk Filter setUsertoNewGroup num account 
./web3sdk Filter setUsertoExistingGroup num account group 
./web3sdk Filter listUserGroup num account 
./web3sdk Group getBlackStatus num account 
./web3sdk Group enableBlack num account 
./web3sdk Group disableBlack num account 
./web3sdk Group getDeployStatus num account 
./web3sdk Group enableDeploy num account 
./web3sdk Group disableDeploy num account 
./web3sdk Group addPermission num account A.address fun(string) 
./web3sdk Group delPermission num account A.address fun(string) 
./web3sdk Group checkPermission num account A.address fun(string) 
./web3sdk Group listPermission num account 
```

