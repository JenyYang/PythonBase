#! /user/bin/ python
# -*- coding:utf-8 -*-

goods=[{"name":"电脑","price":1999},{"name":"鼠标","price":10},{"name":"游艇","price":20},{"name":"帅哥","price":100}]
inp=input("请输入总资产:")
#定义购物车字典
shoppingcart={}
total=int(inp)
for good in goods:
    print(good["name"],good["price"])
selectstr=input("请输入商品（Y/y结算）:")
while True:
    for item in goods:
        if item["name"] == selectstr:
            name=item["name"]
            #购物车已经存在 只改变其数量
            if name in shoppingcart.keys():
                shoppingcart[name]["num"]+=1
            else:#购物车新增商品
                shoppingcart[name]={"single_price":item["price"],"num":1}
    print(shoppingcart)
    if selectstr.upper() == "Y":
        break
    else:
        selectstr = input("请输入商品（Y/y结算）:")

#结算
total_pay=0#总价
for pay_item in shoppingcart.values():
    total_pay+=pay_item["single_price"]*pay_item["num"]
print(total_pay)
if total_pay > total:#总价超过总资产
    print("资产不足，不能购买")
else:
    print("购买成功！")
#附加功能 充值 删除购物车



