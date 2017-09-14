#! /user/bin/ python
# -*- coding:utf-8 -*-
import getpass
# i1=raw_input("UserName:")
# i2=getpass.getpass("Password")
#
# print (i1)
# print(i2)
import time

i=1;
j = 1;
sum=0;
# while i<=10:
#     if i==7:
#         i+=1;
#         continue;
#     print (i);
#     time.sleep(0.2);
#     i+=1;
while j<=100:
     sum=sum+j;
     j+=1;
print (sum)

n=0;
sn=0;
# while n<=100:
#     if n%2 ==0: # 求100以内所有偶数的和  ==变为 != 求100 以内所有基数的和
#         sn=sn+n;
#         n+=1;
#     else:
#         n+=1;
#         continue;
# print(sn);
while n<=100:
    if n%2==0:
        sn=sn-n;
    elif n%2 !=0:
        sn=sn+n
    n += 1;
print (sn)

