# 合约代码转换为java代码

(1) 智能合约语法及细节参考 <a href="https://solidity.readthedocs.io/en/develop/solidity-in-depth.html">solidity官方文档</a>。

(2) 安装fisco-solc,fisco-solc为solidity编译器,[下载fisco-solc](https://github.com/FISCO-BCOS/fisco-solc)。

  将下载下来的fisco-solc，将fisco-solc拷贝到/usr/bin目录下，执行命令chmod +x fisco-solc。如此fisco-solc即安装完成。

(3) 设web3sdk存放于/mydata路径下，则工具包中/mydata/web3sdk/dist/bin文件夹下为合约编译的执行脚本，/mydata/web3sdk/dist/contracts为合约存放文件夹,将自己的合约复制进/mydata/web3sdk/dist/contracts文件夹中（建议删除文件夹中其他无关的合约)，/mydata/web3sdk/dist/apps为sdk jar包，/mydata/web3sdk/dist/lib为sdk依赖jar包，/mydata/web3sdk/dist/output（不需要新建，脚本会创建）为编译后输出的abi、bin及java文件目录。

(4) 在/mydata/web3sdk/dist/bin文件夹下compile.sh为编译合约的脚本，执行命令sh compile.sh [参数1：java包名]：

- 执行成功后将在output目录生成所有合约对应的abi,bin,java文件，其文件名类似：合约名字.[abi|bin|java]
	
- compile.sh首先将sol源文件编译成abi和bin文件，依赖solc工具；然后将bin和abi文件编译java Wrap代码，依赖web3sdk.
	
- 例如：在以上工作都以完成,在/dist/bin文件夹下输入命令`sh compile.sh com`,会在/dist/output目录下生成abi、bin文件，在/dist/output/com目录下生成java Wrap代码
	
- 生成兼容国密版FISCO-BCOS的java代码具体方法可参考[web3sdk对国密版FISCO BCOS的支持的生成支持国密算法的java代码](https://github.com/FISCO-BCOS/web3sdk/blob/master/doc/guomi_support_manual.md#6-%E7%94%9F%E6%88%90%E6%94%AF%E6%8C%81%E5%9B%BD%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84java%E4%BB%A3%E7%A0%81)一节

