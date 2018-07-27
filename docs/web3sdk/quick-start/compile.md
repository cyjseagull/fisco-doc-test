# web3sdk编译

## 环境检查

- **FISCO BCOS节点环境搭建完成**：参考[FISCO-BCOS入门](#./../getstart/setup.md)
- **java**: 要求[jdk1.8+](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html);推荐使用jdk8u141
- **网络连通性检查**：检查web3sdk要连接的FISCO BCOS节点channelPort是否能telnent通，若telnet不通，需要检查网络连通性和安全策略。


## 安装依赖软件 

部署web3sdk之前需要安装git, dos2unix, lsof依赖软件

-  **git**：用于拉取最新代码
-  **dos2unix && lsof**: 用于处理windows文件上传到linux服务器时，文件格式无法被linux正确解析的问题；

可使用如下命令安装这些软件：

```shell
[centos]
bash deploy_
sudo yum -y install git
sudo yum -y install dos2unix
sudo yum -y install lsof
[ubuntu]
sudo apt install git
sudo apt install lsof
sudo apt install tofrodos
ln -s /usr/bin/todos /usr/bin/unxi2dos
ln -s /usr/bin/fromdos /usr/
```

## 获取并编译源码

依赖软件部署完毕后，可拉取并编译web3sdk代码：

- 从git上拉取代码
- 编译web3sdk源码，生成jar包

```bash
#=== 进入web3sdk源码放置目录（假设为/mydata/）=====
$ mkdir -p /mydata
$ cd /mydata

#==== 拉取git代码 ====
$ git clone https://github.com/FISCO-BCOS/web3sdk

#===编译we3bsdk源码，生成dist目录 ===
$ cd web3sdk
$ dos2unix *.sh
$ bash compile.sh

#===编译成功后，web3sdk目录下生成dist文件夹，目录结构如下==========
```

dist目录下各个目录包含的内容如下：

<table border="1"; padding="3px 7px 2px 7px">
    <tr bgcolor="DeepSkyBlue">
        <td color="red">目录</td>
        <td>说明</td>
    </tr>
    <tr>
        <td bgcolor="DeepSkyBlue">dist/apps</td>
         <td>存放web3sdk项目编译生成的jar包web3sdk.jar</td>
    </tr>
    <tr>
        <td bgcolor="DeepSkyBlue">dist/bin</td>
         <td> 主要包括两个可执行文件：<br> (1) web3sdk: 可执行脚本，调用web3sdk.jar执行web3sdk内方法(如部署系统合约、调用合约工具方法等) <br>  (2) compile.sh:
 调用该脚本可将dist/contracts目录下的合约代码转换成java代码，该功能便于用户基于web3sdk开发更多应用</td>
    </tr>
    <tr>
        <td bgcolor="DeepSkyBlue">dist/conf</td>
         <td>配置目录, 用于配置节点信息、证书信息、日志目录等</td>
    </tr>
    <tr>
        <td bgcolor="DeepSkyBlue">dist/contracts</td>
         <td>合约存放目录，调用compile.sh脚本可将存放于该目录下的.sol格式合约代码转换成java代码</td>
    </tr>
    <tr>
        <td bgcolor="DeepSkyBlue">dist/lib</td>
        <td>存放web3sdk依赖库的jar包 </td>
    </tr>
</table>


