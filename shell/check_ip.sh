#!/bin/bash

count=0
while (($count<=255))
do
    ip=192.168.$count.1
    res=`ping -c 3 -t 1 $ip`
    echo $res
    count=$[count+1]
done

