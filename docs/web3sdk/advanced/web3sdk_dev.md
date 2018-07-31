# web3SDK开发示例

## 开发合约代码

## 将合约代码转换成java代码

## web3sdk部署合约

## web3sdk调用合约


下面代码演示了通过web3sdk调用合约向FISCO-BCOS发交易的主要流程：

```java
	package org.bcos.channel.test;
	import org.bcos.web3j.abi.datatypes.generated.Uint256;
	import org.bcos.web3j.crypto.Credentials;
	import org.bcos.web3j.crypto.ECKeyPair;
	import org.bcos.web3j.crypto.Keys;
	import org.bcos.web3j.protocol.core.methods.response.EthBlockNumber;
	import org.bcos.web3j.protocol.core.methods.response.TransactionReceipt;
	import org.slf4j.Logger;
	import org.slf4j.LoggerFactory;
	import org.springframework.context.ApplicationContext;
	import org.springframework.context.support.ClassPathXmlApplicationContext;
	import org.bcos.channel.client.Service;
	import org.bcos.web3j.protocol.Web3j;
	import org.bcos.web3j.protocol.channel.ChannelEthereumService;

	import java.math.BigInteger;

	public class Ethereum {
		static Logger logger = LoggerFactory.getLogger(Ethereum.class);
		
		public static void main(String[] args) throws Exception {
			
			//初始化Service
			ApplicationContext context = new ClassPathXmlApplicationContext("classpath:applicationContext.xml");
			Service service = context.getBean(Service.class);
			service.run();
			
			System.out.println("开始测试...");			System.out.println("===================================================================");
			
			logger.info("初始化AOMP的ChannelEthereumService");
			ChannelEthereumService channelEthereumService = new ChannelEthereumService();
			channelEthereumService.setChannelService(service);
			
			//使用AMOP消息信道初始化web3j
			Web3j web3 = Web3j.build(channelEthereumService);

			logger.info("调用web3的getBlockNumber接口");
			EthBlockNumber ethBlockNumber = web3.ethBlockNumber().sendAsync().get();
			logger.info("获取ethBlockNumber:{}", ethBlockNumber);

			//初始化交易签名私钥
			ECKeyPair keyPair = Keys.createEcKeyPair();
			Credentials credentials = Credentials.create(keyPair);

			//初始化交易参数
			java.math.BigInteger gasPrice = new BigInteger("30000000");
			java.math.BigInteger gasLimit = new BigInteger("30000000");
			java.math.BigInteger initialWeiValue = new BigInteger("0");

			//部署合约
			Ok ok = Ok.deploy(web3,credentials,gasPrice,gasLimit,initialWeiValue).get();
			System.out.println("Ok getContractAddress " + ok.getContractAddress());
			
			//调用合约接口
			java.math.BigInteger Num = new BigInteger("999");
			Uint256 num = new Uint256(Num);
			TransactionReceipt receipt = ok.trans(num).get();
			System.out.println("receipt transactionHash" + receipt.getTransactionHash());

			//查询合约数据
			num = ok.get().get();
			System.out.println("ok.get() " + num.getValue());
		}
	}
```

以上代码主要包括如下流程：

**(1) 初始化web3j对象，连接到FISCO-BCOS节点**

web3sdk使用AMOP（链上链下）连接fisco-bcos节点：

```java
	//初始化AMOP的service，初始化函数详见配置文件，sleep(3000)是确保AMOP网络连接初始化完成。注意：org.bcos.channel.client.Service在Java Client端须为单实例，否则与链上节点连接会有问题
    Service service = context.getBean(Service.class);
    service.run();
    Thread.sleep(3000);
```

**(2) 初始化AMOP的ChannelEthereumService**

ChannelEthereumService通过AMOP的网络连接支持web3j的Ethereum JSON RPC协议。（JSON RPC 参考[JSON RPC API](https://github.com/ethereum/wiki/blob/master/JSON-RPC.md)

```java
    ChannelEthereumService channelEthereumService = new ChannelEthereumService();
    channelEthereumService.setChannelService(service);
```

**(3) 使用ChannelEthereumService初始化web3j对象**

> web3sdk也支持通过http和ipc来初始化web3j对象，但在fisc-bcos中推荐使用AMOP

```java
    Web3j web3 = Web3j.build(channelEthereumService);
```

**(4) 调用web3j的rpc接口**

> 样例给出的是获取块高例子，web3j还支持sendRawTransaction、getCode、getTransactionReceipt等等。部分API参看5.3 web3j API说明（ 参考[JSON RPC API](https://github.com/ethereum/wiki/blob/master/JSON-RPC.md)）

```java
    EthBlockNumber ethBlockNumber = web3.ethBlockNumber().sendAsync().get();
```
**(5)初始化交易签名私钥（加载钱包）**

> 样例给出的是新构建一个私钥文件。web3sdk也可以用证书来初始化交易签名私钥，对交易进行签可参考[存证sample](https://github.com/FISCO-BCOS/evidenceSample)。

```java
import org.bcos.web3j.crypto.GenCredential;

//...省略若干行...

BigInteger bigPrivKey = new BigInteger(privKey, 16);
ECKeyPair keyPair = ECKeyPair.create(bigPrivKey);
if (keyPair == null)
    return null;
Credentials credentials = Credentials.create(keyPair);
```

**(6) 部署合约**
 
Ok合约代码如下：

```
pragma solidity ^0.4.2;
contract Ok{
    
    struct Account{
        address account;
        uint balance;
    }
    
    struct  Translog {
        string time;
        address from;
        address to;
        uint amount;
    }
    
    Account from;
    Account to;
    
    Translog[] log;

    function Ok(){
        from.account=0x1;
        from.balance=10000000000;
        to.account=0x2;
        to.balance=0;

    }
    function get()constant returns(uint){
        return to.balance;
    }
    function trans(uint num){
    	from.balance=from.balance-num;
    	to.balance+=num;
    	log.push(Translog("20170413",from.account,to.account,num));
    }
}
```

在部署合约前，首先要将合约代码转换成java代码，可参考（5.1）合约编译及java Wrap代码生成。
web3sdk部署合约的代码如下：

```java
	//初始化部署合约交易相关参数，正常情况采用demo给出值即可
    java.math.BigInteger gasPrice = new BigInteger("30000000");
	java.math.BigInteger gasLimit = new BigInteger("30000000");
	java.math.BigInteger initialWeiValue = new BigInteger("0");

	//部署合约
	Ok ok = Ok.deploy(web3,credentials,gasPrice,gasLimit,initialWeiValue).get();

	//更新智能合约成员的值
	TransactionReceipt receipt = ok.trans(num).get();

	//查询智能合约成员的值
	num = ok.get().get();

	//交易回调通知:
	//交易回调通知是指针对合约的交易接口（非constant function和构造函数），通过web3j生成的java代码后，会在原来的java函数基础上，新增了同名的重载函数，与原来的区别在于多了一个TransactionSucCallback的参数。原有接口web3j在底层实现的机制是通过轮训机制来获取交易回执结果的，而TransactionSucCallback是通过服务端，也就是区块链节点来主动push通知，相比之下，会更有效率和时效性。当触发到onResponse的时候，代表这笔交易已经成功上链。使用例子：
	ObjectMapper objectMapper = ObjectMapperFactory.getObjectMapper();
	Uint256 num = new Uint256(Num);
	ok.trans(num, new TransactionSucCallback() {
	@Override
    public void onResponse(EthereumResponse response) {
              TransactionReceipt transactionReceipt = objectMapper.readValue(ethereumResponse.getContent(), TransactionReceipt.class);
              //解析event log
   	}
});
```
