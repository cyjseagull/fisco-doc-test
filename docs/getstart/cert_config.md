# 基础配置

## 配置根证书

生成链的根证书

``` shell
cd /mydata/FISCO-BCOS/tools/scripts/
#sh generate_chain_cert.sh -o 根证书生成的目录
sh generate_chain_cert.sh -o /mydata
```

## 配置机构证书

生成机构（agency）证书，假设生成两个机构test_agency

```shell
cd /mydata/FISCO-BCOS/tools/scripts/
#sh generate_agency_cert.sh -c 根证书所在目录 -o 机构证书生成目录 -n 机构名
sh generate_agency_cert.sh -c /mydata -o /mydata -n test_agency
```
