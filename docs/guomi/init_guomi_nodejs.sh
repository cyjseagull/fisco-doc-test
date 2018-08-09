#!/bin/bash
function LOG_ERROR()
{
    local content=${1}
    echo -e "\033[31m"${content}"\033[0m"
}

function LOG_INFO()
{
    local content=${1}
    echo -e "\033[32m"${content}"\033[0m"
}

function execute_cmd()
{
    local command="${1}"
    eval ${command}
    local ret=$?
    if [ $ret -ne 0 ];then
        LOG_ERROR "execute command ${command} FAILED"
        exit 1
    else
        LOG_INFO "execute command ${command} SUCCESS"
    fi
}

current_dir=`pwd`

LOG_INFO "[web3lib]: init guomi nodejs..."
execute_cmd "cd ../web3lib/ && cnpm install && chmod a+x guomi.sh && ./guomi.sh"

LOG_INFO "[tool]: init guomi nodejs..."
execute_cmd "cd ../tool/ && cnpm install && chmod a+x guomi.sh && ./guomi.sh"

LOG_info "[systemcontract]: init guomi nodejs..."
execute_cmd "cd ../systemcontract && cnpm install && chmod a+x guomi.sh && ./guomi.sh"
