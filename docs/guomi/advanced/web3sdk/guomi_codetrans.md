# 将合约代码转换成支持国密的java代码

`dist/bin/compile.sh`脚本调用`src/main/java/org/bcos/web3j/codegen/SolidityFunctionWrapperGenerator.java`将合约代码转换成java代码，便于开发者基于web3sdk和智能合约开发新应用。本章主要介绍了如何使用compile.sh脚本生成java代码。

compile.sh脚本将放置于`dist/contracts`目录下的sol合约转换成java代码(dist/contracts目录下合约是编译web3sdk时，从tools/contracts目录下拷贝获取的)，主要用法如下：

**(1) 生成不支持国密特性的java代码**

**调用方法**: `bash compile.sh "${package_name}"`

**说明**: 

- 使用默认fisco-solc编译器编译dist/contracts/目录下所有合约代码，并将合约代码转换成java代码，java代码包名由${package_name}指定;
- 执行成功后，在dist/output/目录下生成相应的java代码(java代码相对dist/output路径由包名${package_name}决定);
- 使用该方法生成的java代码不支持使用国密算法发交易;
- 若系统没有安装合约编译器fisco-solc，请参考[fisco-solc](https://github.com/FISCO-BCOS/fisco-solc)编译安装编译器



**(2) 生成支持国密特性的java代码**

**调用方法**: `bash compile.sh "${package_name}" "${enable_guomi}" "${fisco_solc_guomi_path}"`

**参数说明**:

- ${package_name}: 生成的java代码import的包名;
- ${enable_guomi}: 表明生成的java代码是否要求支持使用国密算法发交易；0表示不支持国密算法，1表示支持国密算法;
- ${fisco_solc_guomi_path}: [国密版本fisco-solc编译器](https://github.com/FISCO-BCOS/fisco-solc) 路径，默认在\`which fisco-solc\`-guomi路径下，如何编译国密版本编译器可参考[编译国密版fisco-solc](https://github.com/FISCO-BCOS/fisco-solc/tree/master#312-编译国密版fisco-solc);

**说明**: 

- 使用默认fisco-solc编译器编译dist/contracts目录下所有合约代码，使用[国密版本fisco-solc编译器](https://github.com/FISCO-BCOS/fisco-solc/tree/master#312-编译国密版fisco-solc)编译dist/contacts目录下所有合约代码，并将其转换成支持国密算法的java代码，java代码包名由${package_name}指定;
- 执行成功后，在dist/output/目录下生成相应的java代码(java代码相对dist/output路径由包名${package_name}决定);
- 使用该方法生成的java代码支持使用国密算法发交易;
- 开启国密算法方法可参考[2.2.3 开启国密算法，配置链上节点信息和证书](#223-开启国密算法配置链上节点信息和证书)

# 注意事项（关于Credentials对象初始化）

web3sdk向链上发交易时，必须初始化Crendentials对象，为了便于用户调用，web3sdk在`package org.bcos.web3j.crypto`内抽象了`GenCredential`对象，用户可调用`public static Credentials create(String privKey)`接口初始化Credential对象：

使用示例如下（摘选自src/test/java/org/bcos/channel/test/TestOk.java）：

<br>

```java
import org.bcos.web3j.crypto.GenCredential;

//...省略若干行...

ToolConf toolConf=context.getBean(ToolConf.class);
//调用GenCredential的create接口初始化Crendentials对象
Credentials credentials = GenCredential.create(toolConf.getPrivKey()); 
if (credentials != null) {
	System.out.println("####create credential succ, begin deploy contract");
	java.math.BigInteger gasPrice = new BigInteger("300000000");
	java.math.BigInteger gasLimit = new BigInteger("300000000");
	java.math.BigInteger initialWeiValue = new BigInteger("0");
	Ok okDemo = Ok.deploy(web3, credentials, gasPrice, gasLimit, initialWeiValue).get();
	if (okDemo != null) {
		System.out.println("####contract address is: " + okDemo.getContractAddress());
		TransactionReceipt receipt = okDemo.trans(new Uint256(4)).get();
		System.out.println("###callback trans success");
		String toBalance = okDemo.get().get().toString();
		System.out.println("============to balance:" + toBalance);
	} else {
		System.out.println("deploy Ok contract failed");
		System.exit(1);
	}
	} else {
		System.out.println("create Credentials failed");
		System.exit(1);
	}
```

<br>

**当web3sdk与[国密版本的FISCO BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/国密操作文档.md)节点通信时，必须使用上述方法初始化Credentials对象**

老版web3sdk使用如下方法初始化Credentials对象，**但用该方法初始化的web3sdk不能与[国密版本的FISCO BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/国密操作文档.md)通信**：

<br>

```java
BigInteger bigPrivKey = new BigInteger(privKey, 16);
ECKeyPair keyPair = ECKeyPair.create(bigPrivKey);
if (keyPair == null)
    return null;
Credentials credentials = Credentials.create(keyPair);
```

