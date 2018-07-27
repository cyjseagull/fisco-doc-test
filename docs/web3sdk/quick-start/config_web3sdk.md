# web3sdk配置

## 生成客户端证书

参考[FISCO-BCOS区块链操作手册的生成sdk证书](https://github.com/FISCO-BCOS/FISCO-BCOS/tree/master/doc/manual#24-生成sdk证书)一节;

## 配置applicationContext.xml

编译成功后，在web3sdk/dist/conf目录下生成applicationContext.xml配置文件，主要包括如下配置：
 <table border="1"; padding="3px 7px 2px 7px">
    <tr>
		<td  bgcolor="DeepSkyBlue">encryptType</td>
		<td>配置国密算法开启/关闭开关，0表示不使用国密算法发交易，1表示开启国密算法发交易，默认为0(即不使用国密算法发交易，web3sdk支持国密算法的具体方法可参考文档[web3sdk对国密版FISCO BCOS的支持](https://github.com/FISCO-BCOS/web3sdk/blob/master/doc/guomi_support_manual.md))</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">systemProxyAddress</td>
		<td>配置FISCO BCOS系统合约地址, 部署系统合约成功后，要将systemProxyAddress对应的值改为部署的系统合约地址</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">privKey</td>
		<td>向FISCO BCOS节点发交易或发消息的账户私钥，使用默认配置即可</td>
	</tr>
	<tr>
		<td  bgcolor="DeepSkyBlue">ChannelConnections</td>
		<td>- 配置FISCO BCOS节点信息和证书，证书相关配置如下:  <br>  (1) caCertPath: CA证书路径，默认为dist/conf/ca.crt; <br> (2) clientKeystorePath: 客户端证书路径，默认为dist/conf/client.keystore; <br> (3)keystorePassWord: 客户端证书文件访问口令, 默认为123456; <br> (4) clientCertPassWord: 客户端证书验证口令, 默认为123456</td>
	</tr>
</table>

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

