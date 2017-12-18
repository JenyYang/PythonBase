#! /user/bin/python/
# -*-coding:utf-8 -*-

import select

import socket

sk1 = socket.socket()
sk1.bind(("127.0.0.1", 8002))
sk1.listen(5)
# sk2=socket.socket()
# sk2.bind(("127.0.0.1",8003))
# sk2.listen(5)

# inputs=[sk1,sk2]
inputs = [sk1]
while True:
    s_list, w_list, e_list = select.select(inputs, [], inputs, 1)
    # for sk in s_list:
    #     conn,address=sk.accept()
    #     print(address,conn)
    print (s_list)
    for sk_or_conn in s_list:

        if sk_or_conn == sk1:
            conn, address = sk_or_conn.accept()
            inputs.append(conn)
            conn.sendall("欢迎致电")
        else:
            # while True:
                try:
                    data = sk_or_conn.recv(1024)
                except Exception as e:
                    print(e.message)
                    inputs.remove(sk_or_conn)
                else:
                    print(data)
                    inp=raw_input("输入>>")
                    sk_or_conn.sendall(inp)
