# FAQ

**1. 使用工具包生成合约Java Wrap代码时会报错**

从 https://github.com/FISCO-BCOS/web3sdk 下载代码（Download ZIP），解压之后，目录名称将为：web3sdk-master，运行gradle命令后生成的工具包中，/dist/apps目录下生成的jar包名称为web3sdk-master.jar，导致和/dist/bin/web3sdk中配置的CLASSPATH中的配置项$APP_HOME/apps/web3sdk.jar名称不一致，从而导致使用工具包生成合约Java Wrap代码时会报错。

**2. 工具目录下，dist/bin/web3sdk运行会出错**

可能是权限问题，请尝试手动执行命令：chmod +x  dist/bin/web3sdk。

- java.util.concurrent.ExecutionException: com.fasterxml.jackson.databind.JsonMappingException: No content to map due to end-of-input

> 出现此问题请按顺序尝试来排查：

(1) 检查配置是否连接的是channelPort，需要配置成channelPort。<br />
(2) 节点listen ip是否正确，最好直接监听0.0.0.0。<br />
(3) 检查channelPort是否能telnet通，需要能telnet通。如果不通检查网络策略，检查服务是否启动。<br />
(4) 服务端和客户端ca.crt是否一致，需要一致。<br />
(5) [FISCO-BCOS中client.keystore 的生成方法](https://github.com/FISCO-BCOS/web3sdk/issues/20)
