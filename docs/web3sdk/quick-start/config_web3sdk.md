# web3sdk配置运行

## 生成客户端证书

参考[FISCO-BCOS Quick Start的客户端证书生成部分](https://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/chain_setting.html#id3)

## 配置applicationContext.xml

web3sdk编译成功后，在web3sdk的dist/conf目录下生成applicationContext.xml文件，主要配置包括：

```eval_rst
+----------------------+---------------------------------------------------------------------+
| **encryptType**      |  配置国密算法开启/关闭开关(默认为0)                                 |
|                      |   - 0: 不使用国密算法发交易                                         |
|                      |   - 1: 使用国密算法发交易                                           |
+----------------------+---------------------------------------------------------------------+
|**systemProxyAddress**|  配置FISCO BCOS区块链的系统合约地址                                 |
+----------------------+---------------------------------------------------------------------+
| **privKey**          |  向FISCO BCOS节点发交易或发消息的账户私钥(使用默认配置即可)         |
+----------------------+---------------------------------------------------------------------+
|**ChannelConnections**|- caCertPath: CA证书路径，默认为dist/conf/ca.crt                     |
|                      |- clientKeystorePath: 客户端证书路径，默认为dist/conf/client.keystore|
|                      |- keystorePassWord: 客户端证书文件访问口令, 默认为123456             | 
|                      |- clientCertPassWord: 客户端证书验证口令, 默认为123456               |
+----------------------+---------------------------------------------------------------------+

```

以下为web3sdk的applicationContext.xml配置案例<br />

```xml 
<?xml version="1.0" encoding="UTF-8" ?>
	<beans xmlns="http://www.springframework.org/schema/beans"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p"
		xmlns:tx="http://www.springframework.org/schema/tx" xmlns:aop="http://www.springframework.org/schema/aop"
		xmlns:context="http://www.springframework.org/schema/context"
		xsi:schemaLocation="http://www.springframework.org/schema/beans   
	    http://www.springframework.org/schema/beans/spring-beans-2.5.xsd  
	         http://www.springframework.org/schema/tx   
	    http://www.springframework.org/schema/tx/spring-tx-2.5.xsd  
	         http://www.springframework.org/schema/aop   
	    http://www.springframework.org/schema/aop/spring-aop-2.5.xsd">
	    
	<!-- AMOP消息处理线程池配置，根据实际需要配置 -->
	<bean id="pool" class="org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor">
		<property name="corePoolSize" value="50" />
		<property name="maxPoolSize" value="100" />
		<property name="queueCapacity" value="500" />
		<property name="keepAliveSeconds" value="60" />
		<property name="rejectedExecutionHandler">
			<bean class="java.util.concurrent.ThreadPoolExecutor.AbortPolicy" />
		</property>
	</bean> 
	    
	    <bean id="encryptType" class="org.bcos.web3j.crypto.EncryptType">
                <constructor-arg value="0"/>
        </bean>
	
	<!-- 系统合约地址配置，在使用./web3sdk SystemProxy|AuthorityFilter等系统合约工具时需要配置 -->
	<bean id="toolConf" class="org.bcos.contract.tools.ToolConf">
		<property name="systemProxyAddress" value="0x919868496524eedc26dbb81915fa1547a20f8998" />
		<!--GOD账户的私钥（注意去掉“0x”）-->
		<property name="privKey" value="bcec428d5205abe0f0cc8a734083908d9eb8563e31f943d760786edf42ad67dd" />
		<!--GOD账户-->
		<property name="account" value="0x776bd5cf9a88e9437dc783d6414bccc603015cf0" />
		<property name="outPutpath" value="./output/" />
	</bean>

	<!-- 区块链节点信息配置 -->
	<bean id="channelService" class="org.bcos.channel.client.Service">
		<property name="orgID" value="WB" /> <!-- 配置本机构名称 -->
			<property name="allChannelConnections">
				<map>
					<entry key="WB"> <!-- 配置本机构的区块链节点列表（如有DMZ，则为区块链前置）-->
						<bean class="org.bcos.channel.handler.ChannelConnections">
						    <property name="caCertPath" value="classpath:ca.crt" />
						    <property name="clientKeystorePath" value="classpath:client.keystore" />
						    <property name="keystorePassWord" value="123456" />
						    <property name="clientCertPassWord" value="123456" />
							<property name="connectionsStr">
								<list>
									<value>NodeA@127.0.0.1:30333</value><!-- 格式：节点名@IP地址:channelport，节点名可以为任意名称 -->
								</list>
							</property>
						</bean>
					</entry>
				</map>
			</property>
		</bean>
	</bean>
```


## 测试是否配置成功

调用Ok合约测试web3sdk与服务器是否连接正常:

``` important::
    测试客户端与节点连接是否正常时，必须保证连接的FISCO-BCOS节点能正常出块
    FISCO-BCOS节点是否正常可参考 `FISCO BCOS入门的相关介绍 <http://fisco-bcos-test.readthedocs.io/zh/latest/docs/getstart/setup_nodes.html>`_

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
