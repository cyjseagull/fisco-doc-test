# 客户端证书生成原理

FISCO-BCOS提供了客户端证书生成脚本[sdk](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/cert/sdk.sh),该脚本生成客户端证书`ca.crt`和`client.keystore`, 本节详细介绍客户端证书生成原理。

## ca.crt根证书生成原理

FISCO-BCOS区块链系统中，web3sdk与所连接的FISCO-BCOS节点必须属于同一机构，节点通过web3sdk的ca.crt进行此项验证。为了使客户端能连上FISCO-BCOS节点，web3sdk的根证书必须同时包含FISCO-BCOS区块链的根证书(ca.crt)和机构证书(agency.crt), 因此web3sdk的根证书ca.crt由链根证书和机构证书合成:

```shell
#*******设链证书为ca.crt,机构证书为agency.crt; 最终输出的web3sdk根证书为ca.crt

#------将链证书拷贝到web3sdk根证书
$ cp ca.crt ca-agency.crt

#------追加机构证书到web3sdk根证书
$ more agency.crt | cat >>ca-agency.crt

#------重命名web3sdk根证书为ca.crt
$ mv ca-agency.crt ca.crt
```


## 生成web3sdk证书client.keystore

和其他sdk(前置)连接时, client.keystore是web3sdk的连接证书; 在[存证案例中](https://github.com/FISCO-BCOS/evidenceSample), client.keystore中包含的私钥还可用于为交易签名.


 client.keystore生成过程如下：

**(1) web3sdk所属机构颁发sdk证书sdk.crt**

```shell
    # 使用ECDSA算法,生成公私钥对(sdk.pubkey, sdk.key)
    $ openssl ecparam -out sdk.param -name secp256k1
    $ openssl genpkey -paramfile sdk.param -out sdk.key
    $ openssl pkey -in sdk.key -pubout -out sdk.pubkey

    # 生成证书sdk.crt
    $ openssl req -new -key sdk.key -config cert.cnf  -out sdk.csr
    $ openssl x509 -req -days 3650 -in sdk.csr -CAkey agency.key -CA agency.crt -force_pubkey sdk.pubkey -out sdk.crt -CAcreateserial -extensions v3_req -extfile cert.cnf
```

**(2) 将生成的sdk证书导入client.keystore**

```shell
    # 生成临时文件keystore.p12
    $ openssl pkcs12 -export -name client -in sdk.crt -inkey sdk.key -out keystore.p12
    
    # 将keystore.p12导入client.keystore
    $ keytool -importkeystore -destkeystore client.keystore -srckeystore keystore.p12 -srcstoretype pkcs12 -alias client
```
