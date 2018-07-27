# 部署合约-nodejs客户端
## 配置

> 安装依赖环境

```shell
cd /mydata/FISCO-BCOS/web3lib
cnpm install
chmod +x guomi.sh
dos2unix guomi.sh
./guomi.sh
#安装nodejs依赖, 在执行nodejs脚本之前该目录下面需要执行一次, 如果已经执行过, 则忽略。
```

```shell
cd /mydata/FISCO-BCOS/tool
cnpm install
chmod +x guomi.sh
dos2unix guomi.sh
./guomi.sh
#安装nodejs依赖, 在执行nodejs脚本之前该目录下面需要执行一次, 如果已经执行过, 则忽略。
```

```shell
cd /mydata/FISCO-BCOS/systemcontract
cnpm install
chmod +x guomi.sh
dos2unix guomi.sh
./guomi.sh
#安装nodejs依赖, 在执行nodejs脚本之前该目录下面需要执行一次, 如果已经执行过, 则忽略。
```

> 开启国密开关

```shell
vim /mydata/FISCO-BCOS/web3lib/config.js
```

```javascript
var encryptType = 1;// 0:ECDSA版本 1:国密版本
```

> 设置区块链节点RPC端口，仅需将proxy指向区块链节点的RPC端口即可。RPC端口在节点的config.json中查看rpcport。

```shell
vim /mydata/FISCO-BCOS/web3lib/config.js
```

```javascript
var proxy="http://127.0.0.1:8545";
```

## 部署测试合约

```shell
cd /mydata/FISCO-BCOS/tool
```

国密版FISCO BCOS部署测试合约流程与[非国密版FISCO BCOS部署测试合约](manual#42-%E9%83%A8%E7%BD%B2%E5%90%88%E7%BA%A6)流程相似
    
## 部署系统合约

```shell
cd /mydata/FISCO-BCOS/systemcontract
```
国密版FISCO BCOS部署系统合约流程与[非国密版FISCO BCOS部署系统合约](manual#52-%E9%83%A8%E7%BD%B2%E7%B3%BB%E7%BB%9F%E5%90%88%E7%BA%A6)流程相似

## 配置系统代理合约地址

国密版FISCO BCOS配置系统代理合约地址与[非国密版FISCO BCOS配置系统代理合约地址](manual#53-%E9%85%8D%E7%BD%AE%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%90%86%E5%90%88%E7%BA%A6%E5%9C%B0%E5%9D%80)流程相似