pragma solidity ^0.4.2;
contract Ok{
    //账户信息 
    struct Account{
        address account; //账户地址
        uint balance;  //账户余额
    }
    //交易明细信息 
    struct  Translog {
        string time;
        address from;
        address to;
        uint amount;
    }
    
    Account from; //转账账户
    Account to;  //收款账户
     
    Translog[] log; //账户交易明细日志

    //构造函数,该示例在构造函数中预先指定账户和余额
    function Ok(){
        from.account=0x1;
        from.balance=10000000000;
        to.account=0x2;
        to.balance=0;

    }
    //收款账户余额获取接口实现
    function get()constant returns(uint){
        return to.balance;
    }
    //转账接口实现
    function trans(uint num){
    	from.balance=from.balance-num; //转账账户扣款
    	to.balance+=num;   //收款账户增加账户金额
    	log.push(Translog("20170413",from.account,to.account,num));
    }

}
