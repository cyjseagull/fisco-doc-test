## 客户端证书生成原理

web3sdk客户端证书ca.crt, client.keystore生成方法请参考[FISCO-BCOS区块链操作手册的生成sdk证书](https://github.com/FISCO-BCOS/FISCO-BCOS/tree/master/doc/manual#24-生成sdk证书)一节。<br>
具体步骤可以参考[sdk.sh](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/cert/sdk.sh)



,详细解释如下：<br>
(1)将链的根ca证书ca.crt和次级的机构ca证书agency.crt合成证书链ca证书ca.crt。此证书用来验证sdk连接节点的节点证书的合法性。具体步骤为：<br>

```shell
cp ca.crt ca-agency.crt
more agency.crt | cat >>ca-agency.crt
mv ca-agency.crt ca.crt
```

(2)生成client.keystore。其中的client证书有三种用途：1、用作和节点连接是sdk的身份证书，由节点的ca.crt和agency.crt来验证合法性。2、用作和其他sdk（前置）连接的身份证书，由其他sdk的ca.crt来验证合法性。3、用作sdk发交易的私钥证书。<br>
先用openssl生成一张secp256k1的证书sdk.crt。<br>

```shell
    openssl ecparam -out sdk.param -name secp256k1
    openssl ecparam -out sdk.param -name secp256k1
    openssl genpkey -paramfile sdk.param -out sdk.key
    openssl pkey -in sdk.key -pubout -out sdk.pubkey
    openssl req -new -key sdk.key -config cert.cnf  -out sdk.csr
    openssl x509 -req -days 3650 -in sdk.csr -CAkey agency.key -CA agency.crt -force_pubkey sdk.pubkey -out sdk.crt -CAcreateserial -extensions v3_req -extfile cert.cnf
```

再将生成的sdk证书导入到client.keystore中。下面步骤中的第一步是中间步骤，用于生成导入keystore的p12文件。<br>

```shell
    openssl pkcs12 -export -name client -in sdk.crt -inkey sdk.key -out keystore.p12
    keytool -importkeystore -destkeystore client.keystore -srckeystore keystore.p12 -srcstoretype pkcs12 -alias client
```

(3)加载client.keystore中私钥作为交易私钥的示例代码<br>

```
   KeyStore ks = KeyStore.getInstance("JKS");
   ksInputStream =  Ethereum.class.getClassLoader().getResourceAsStream(keyStoreFileName);
   ks.load(ksInputStream, keyStorePassword.toCharArray());
   Key key = ks.getKey("client", keyPassword.toCharArray());
   ECKeyPair keyPair = ECKeyPair.create(((ECPrivateKey) key).getS());
   Credentials credentials = Credentials.create(keyPair);
```


<table border="1"; padding="3px 7px 2px 7px">
    <tr>
		<td  bgcolor="DeepSkyBlue">applicationContext.xml</td>
		<td>主要包括三项配置: <br> 1. encryptType: 配置国密算法开启/关闭开关，0表示不使用国密算法发交易，1表示开启国密算法发交易，默认为0(即不使用国密算法发交易，web3sdk支持国密算法的具体方法可参考文档[web3sdk对国密版FISCO BCOS的支持](https://github.com/FISCO-BCOS/web3sdk/blob/master/doc/guomi_support_manual.md));  <br>  2. systemProxyAddress: 配置FISCO BCOS系统合约地址, 部署系统合约成功后，要将systemProxyAddress对应的值改为部署的系统合约地址;  <br> - privKey: 向FISCO BCOS节点发交易或发消息的账户私钥，使用默认配置即可 <br> 3. ChannelConnections：配置FISCO BCOS节点信息和证书，证书相关配置如下:  <br>  (1) caCertPath: CA证书路径，默认为dist/conf/ca.crt; <br> (2) clientKeystorePath: 客户端证书路径，默认为dist/conf/client.keystore; <br> (3)keystorePassWord: 客户端证书文件访问口令, 默认为123456; <br> (4) clientCertPassWord: 客户端证书验证口令, 默认为123456</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">ca.crt</td>
		<td>用来验证节点或者前置的CA证书，必须与链上FISCO BCOS节点CA证书保持一致</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">client.keystore</td>
		<td>用来做sdk的ssl身份证书， 里面需要包含一个由节点CA证书颁发的，别名为client的身份证书，默认访问口令和验证口令均为123456</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">日志配置文件</td>
		<td>- commons-logging.properties： 配置日志类, 默认为org.apache.commons.logging.impl.SimpleLog;  <br>  - log4j2.xml：日志常见配置，包括路径、格式、缓存大小等; <br> - simplelog.properties: 日志级别设置，默认为WARN</td>
	</tr>
</table>
