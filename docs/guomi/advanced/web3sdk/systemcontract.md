# 系统合约部署

部署完适配于[国密版FISCO BCOS](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/国密操作文档.md)的web3sdk后，可调用InitSystemContract部署系统合约，系统合约部署工具InitSystemContract由`src/main/java/org/bcos/contract/tools/InitSystemContract.java`调用合约生成的java代码实现，使用如下命令部署系统合约：

```bash
##进入bin目录(设web3sdk位于/mydata目录下)
cd /mydata/web3sdk/dist/bin && chmod a+x web3sdk
####执行部署工具InitSystemContract部署系统合约: ./web3sdk InitSystemContract
[app@VM_105_81_centos bin]$ ./web3sdk InitSystemContract
===================================================================
Start deployment...
===================================================================
systemProxy getContractAddress 0xc9ed60a2ebdf22936fdc920133af2a77dd553e13
caAction getContractAddress 0x014bf33e022f78f7c4bb8dbfe1d22df5168fc9bc
nodeAction getContractAddress 0x51b25952b01a42e6f84666ed091571c7836eda34
consensusControlMgr getContractAddress 0xffda2977b8bd529dd187d226ea6600ff3c8fb716
configAction getContractAddress 0xf6677fa9594c823abf39ac67f1f34866e2843399
fileInfoManager getContractAddress 0x0f49a17d17f82da2a7d92ecf19268274150eaf5e
fileServerManager getContractAddress 0xfbe0184fe09a3554103c5a541ba052f7fa45283b
contractAbiMgr getContractAddress 0x66ec295357750ce442227a6419ada7fdf9207be2
authorityFilter getContractAddress 0x2fa1ec76f3e31d2c42d21b62960625f326a044e6
group getContractAddress 0xa172b92c85a98167d96b9fde10792eb2fd4d584c
transactionFilterChain getContractAddress 0x0b78d9be55f047fb32d6fbc2c79013c0eca5d09d
Contract Deployment Completed System Agency Contract:0xc9ed60a2ebdf22936fdc920133af2a77dd553e13
-----------------System routing table----------------------
 0)TransactionFilterChain=>0x0b78d9be55f047fb32d6fbc2c79013c0eca5d09d,false,35
       AuthorityFilter=>1.0,0x2fa1ec76f3e31d2c42d21b62960625f326a044e6
 1)ConfigAction=>0xf6677fa9594c823abf39ac67f1f34866e2843399,false,36
 2)NodeAction=>0x51b25952b01a42e6f84666ed091571c7836eda34,false,37
 3)ConsensusControlMgr=>0xffda2977b8bd529dd187d226ea6600ff3c8fb716,false,38
 4)CAAction=>0x014bf33e022f78f7c4bb8dbfe1d22df5168fc9bc,false,39
 5)ContractAbiMgr=>0x66ec295357750ce442227a6419ada7fdf9207be2,false,40
 6)FileInfoManager=>0x0f49a17d17f82da2a7d92ecf19268274150eaf5e,false,41
 7)FileServerManager=>0xfbe0184fe09a3554103c5a541ba052f7fa45283b,false,42
```

部署完毕的系统合约地址是0xc9ed60a2ebdf22936fdc920133af2a77dd553e13, 还需要进行如下两步操作：

**(1) 设置配置文件的系统合约地址：将dist/conf/applicationContext.xml的systemProxyAddress字段更新为输出的系统合约地址**

**(2) 设置私钥地址：参考 [4.生成国密秘钥对和账户](#4-生成国密秘钥对和账户) ，生成国密秘钥对和账户，将dist/conf/applicationContext.xml的privKey更新为生成的国密秘钥privateKey**

执行完上述两步操作后，按照[FISCO BCOS 国密特性文档](https://github.com/FISCO-BCOS/FISCO-BCOS/blob/master/doc/国密操作文档.md#7-多记账节点组网) **多记账节点组网**一节进行加入新节点等操作。
