# web3sdk配置修改

## 生成客户端证书

<br>

> 国密版客户端证书ca.crt, client.keystore生成方法请参考[国密操作文档的生成客户端证书](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/%E5%9B%BD%E5%AF%86%E6%93%8D%E4%BD%9C%E6%96%87%E6%A1%A3.md#32-%E7%94%9F%E6%88%90%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%AF%81%E4%B9%A6)一节

<br>

## 更新applicationContext.xml

<br>

编译成功后, web3sdk主要配置文件存放于dist/conf目录下，主要包括如下设置（详细配置方法可参考[web3sdk使用指南]( https://github.com/FISCO-BCOS/web3sdk) 第(三)部分）：<br> 

<br>

| 配置文件                   | 详细说明                                     |
| ---------------------- | ---------------------------------------- |
| applicationContext.xml | 主要包括三项配置: <br> - encryptType: 配置国密算法开启/关闭开关，0表示不使用国密算法发交易，1表示开启国密算法发交易，默认为0(即不使用国密算法发交易) ;  <br>  - systemProxyAddress: 配置FISCO BCOS系统合约地址, 部署系统合约成功后，要将systemProxyAddress对应的值改为部署的系统合约地址;  <br> - privKey: 向FISCO BCOS节点发交易或发消息的账户私钥，**国密版用户公私钥对和账户的生成方法请参考[生成国密秘钥对和账户一章](#4-生成国密秘钥对和账户)** <br> - ChannelConnections：配置FISCO BCOS节点信息和证书，证书相关配置如下:  <br>  (1) caCertPath: CA证书路径，默认为dist/conf/ca.crt; <br> (2) clientKeystorePath: 客户端证书路径，默认为dist/conf/client.keystore; <br> (3)keystorePassWord: 客户端证书文件访问口令, 默认为123456; <br> (4) clientCertPassWord: 客户端证书验证口令, 默认为123456 |
| ca.crt                 | CA证书，必须与链上FISCO BCOS节点CA证书保持一致           |
| client.keystore        | 客户端证书(默认访问口令和验证口令均为123456)               |
| 日志配置文件                 | - commons-logging.properties： 配置日志类, 默认为org.apache.commons.logging.impl.SimpleLog;  <br>  - log4j2.xml：日志常见配置，包括路径、格式、缓存大小等; <br> - simplelog.properties: 日志级别设置，默认为WARN |

开启国密算法时，applicationContext.xml配置如下(将encryptType设置为1)：(注：web3sdk端开启国密算法用于发交易时，其连接的链上节点必须是国密版本的FISCO BCOS，否则交易无法被验证) <br>

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
                <constructor-arg value="1"/> <!--### encyptType设置为1，web3sdk端开启国密验证，使用国密签名算法和hash算法向FISCO BCOS发交易-->
        </bean>

        <bean id="toolConf" class="org.bcos.contract.tools.ToolConf"> <!--===系统合约部署成功后，将systemProxyAddress设置为系统合约地址====-->
                <property name="systemProxyAddress" value="0x919868496524eedc26dbb81915fa1547a20f8998" />
                <property name="privKey" value="204851937051ba3192100417a79fe3b2fe88d99aff8c861b86a5fbd6fa8a108d" /> <!--====向FISCO BCOS节点发消息或交易的账户私钥===-->
                <property name="account" value="0xe519346a02b88cac6f91b52acf7c3951ed6cdb1e" /> <!--权限控制部分配置-->
                <property name="outPutpath" value="./output/" />
        </bean>

        <bean id="channelService" class="org.bcos.channel.client.Service">
                <property name="orgID" value="WB" /> <!--机构名称-->
                <property name="connectSeconds" value="10" />
                <property name="connectSleepPerMillis" value="10" />
                <property name="allChannelConnections">
                        <map>
                                <entry key="WB"> <!--机构节点配置，key与"orgID"配置值一致-->
                                        <bean class="org.bcos.channel.handler.ChannelConnections">
                                                <property name="caCertPath" value="classpath:ca.crt" />  <!--###CA证书路径, 默认是dist/conf/ca.crt, 必须与连接节点CA证书保持一致-->
                                                <property name="clientKeystorePath" value="classpath:client.keystore" /> <!--客户端证书路径, 默认是dist/conf/client.keystore-->
                                                <property name="keystorePassWord" value="123456" /> <!--访问客户端keystore证书的口令,默认是123456-->
                                                <property name="clientCertPassWord" value="123456" /> <!--客户端证书验证口令, 默认是123456-->
                        <property name="connectionsStr">
                                                        <list> <!--##连接信息，包括要连接节点的IP和channelPort, 节点名称可任意填，无限制##-->
                                                                <value>node1@10.107.105.81:7703</value>  
                                                        </list>
                                                </property>
                    </bean>
                                </entry>
                        </map>
                </property>
        </bean>
</beans>
```
