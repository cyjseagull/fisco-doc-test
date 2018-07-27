# 证书生成

## 生成节点证书

<br>

FISCO BCOS网络采用面向CA的准入机制，类似于[非国密版FISCO BCOS](manual)，国密版FISCO BCOS也要生成三级证书，包括：链证书，机构证书和节点证书，且两者生成流程类似。FISCO BCOS团队提供了`gmchain.sh, gmagency.sh, gmnode.sh`三个脚本来生成这些证书，这些脚本存放于FISCO-BCOS/cert/GM目录下。

每级证书说明如下：

| 证书类型    | 生成方式                             | 功能说明                                     |
| ------- | -------------------------------- | ---------------------------------------- |
| 生成链根证书  | bash gmchain.sh                  | 生成链根证书，主要功能是颁发机构证书，用于链认证；，链私钥由链管理员拥有，对每个参与该链的机构签发机构证书 |
| 机构二级根证书 | bash gmagency.sh ${agency}       | 使用链证书生成机构二级根证书，其中${agency}是机构名，用于机构认证；机构证书私钥由机构管理员持有，并对机构下属节点签发节点证书 |
| 节点证书    | bash gmnode.sh ${agency} ${node} | 使用机构二级根证书生成节点证书，其中${agency}是节点所在的机构名, ${node}是节点名，主要用于节点认证，使用该证书与其他节点间建立SSL连接进行加密通讯 |


> 以机构agencyA的nodeA生成节点证书为例：

```bash
#进入国密版证书生成脚本所在目录
$ cd /mydata/FISCO-BCOS/cert/GM

# ======步骤1： 若没有生成过nodeA所属链的根证书，则生成链根证书，否则直接跳到步骤2=========
$ bash gmchain.sh

# ===步骤2：若nodeA节点所属机构agencyA没有生成过机构证书，则生成机构证书，否则直接跳到步骤3 ===
$ bash gmagency.sh agencyA

# ======步骤3：生成节点证书 =========
$ bash gmnode.sh agencyA nodeA
```

<br>

**注意：**

- **请链管理员妥善保存链私钥gmca.key**
- **请机构管理员妥善保存机构私钥gmagencyA.key**
- **节点私钥gmnode.key请妥善保存**




## 生成客户端证书

<br>

节点与web3sdk客户端之间通信使用openssl协议，因此必须生成一套与节点匹配的web3sdk证书，web3sdk才可与节点通信，可使用FISCO-BCOS/cert/GM目录下的gmsdk.sh生成客户端证书.

- **生成客户端证书方法：** bash gmsdk.sh ${agency} ${directory}
- **功能说明：** 生成${agency}机构下的web3sdk证书和节点访问证书; ${agency}是web3sdk客户端所属证书; ${directory}是证书相对FISCO-BCOS/cert/GM目录的存放路径;
- **注：** web3sdk applicationContext.xml文件的keystorePassWord字段需要设置为client.keystore的keystore password, clientCertPassWord需要设置为123456，若需要改成其他密码，请修改gmsdk.sh脚本;

> 例：为机构agencyA的客户端sdk1生成证书：

```bash
#====进入客户端证书生成脚本所在目录====
$ cd /mydata/FISCO-BCOS/cert/GM

#=== 运行gmsdk.sh脚本为客户端生成证书====
$ bash gmsdk.sh agencyA sdk1
```

<br> 

执行上述步骤后，在/mydata/FISCO-BCOS/cert/GM/agencyA/sdk1目录下生成server.crt, server.key, ca.crt, client.keystore证书；将server.crt, server.key, ca.crt拷贝到节点的data目录，将ca.crt, client.keystore拷贝到web3sdk的配置目录下

<br>

> 例：节点nodeA所在目录为/mydata/nodedata-1/, web3sdk所在目录为/mydata/web3sdk，则证书拷贝命令下：

```bash
#====生成节点数据目录（设节点位于/mydata/nodedata-1路径）===
$ mkdir -p /mydata/nodedata-1/data

#====进入源码目录=====
$ cd /mydata/FISCO-BCOS/cert/GM/agencyA/sdk1/

#====将证书拷贝到节点数据目录========
$ cp server.crt server.key ca.crt /mydata/nodedata-1/data

#====将证书拷贝到客户端(如使用nodejs发送国密交易该步骤忽略)======
$ cp ca.crt client.keystore /mydata/web3sdk/dist/conf/

##注：此时/mydata/web3sdk/dist/conf/applicationContext.xml文件的keystorePassWord字段设置为123456，
##    若要修改client.keystore的keystore password，请修改SDK证书生成脚本gmsdk.sh
# applicationContext.xml与口令相关的默认配置如下：
 <property name="keystorePassWord" value="123456" />
 <property name="clientCertPassWord" value="123456" />
```

**注意：请妥善保存sdk1私钥文件sdk1.key**
