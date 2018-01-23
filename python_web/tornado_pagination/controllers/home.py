#! /user/bin/python/
# -*-coding:utf-8 -*-

import tornado.web
from views import home

LIST_INFO = []

for i in range(100):
    temp={"name":"alex"+str(i),"email":str(i)+"3443@qq.com"}
    LIST_INFO.append(temp)
class HomeHandler(tornado.web.RequestHandler):
    def get(self, page):
        try:
            page = int(page)
        except Exception as e:
            print(e)
            page = 1

        start = (page - 1) * 5
        end = page * 5

        # print(start, end)
        list = LIST_INFO[start: end]

        ret, r = divmod(len(LIST_INFO), 5)
        if r==0:
            total_page=ret
        else:
            total_page=ret+1
        # print(total_page)
        page_str=[]
        # 控制显示10个页码
        """
            r_start=page-5 页码开始
            r_end=page+5   页码结束
        """
        if page<6:
            r_start=1
            r_end=11
        else:
            if page+5>=total_page:
                r_start=total_page-9
                r_end=total_page+1
            else:
                r_start=page-5
                r_end=page+5
        # print(r_start,r_end)
        #添加首页
        temp='<a href="%s%s">%s</a>'%("/index/","1","首页")
        page_str.append(temp)
        # 添加上一页
        if page>1:
            pre=page-1
        else:
            pre=page
        temp = '<a href="%s%s">%s</a>' % ("/index/", str(pre), "上一页")
        page_str.append(temp)
        for line in range(r_start,r_end):
            if line==page:
                temp = '<a class="click_style" href="%s%s">%s</a>' % ("/index/", line, line)
            else:
                 temp='<a href="%s%s">%s</a>'%("/index/",line,line)
            page_str.append(temp)
        # 添加下一页
        if page<total_page:
            next=page+1
        else:
            next=total_page
        temp = '<a href="%s%s">%s</a>' % ("/index/", str(next), "下一页")
        page_str.append(temp)
        # 添加尾页
        temp = '<a href="%s%s">%s</a>' % ("/index/", str(total_page), "尾页")
        page_str.append(temp)

        #跳转
        jump="""<input type="number" /><a onclick="Jump('%s',this,%d);">Go</a>"""%("/index/",total_page,)
        script="""
        <script>
                function Jump(base_url,ths,total_page){
                    var p=ths.previousElementSibling.value
                    if (p.trim().length>0){
                        if(p>total_page)
                            p=total_page
                        else if(p<1)
                            p=1
                        location.href=base_url+p
                    }
                }
        </script>
        """
        page_str.append(jump)
        page_str.append(script)
        page_html="".join(page_str)

        self.render("home/index.html", list_info=list, current_page=page,page_str=page_html)

    def post(self, page):
        print(page)
        name = self.get_argument("name")
        email = self.get_argument("email")
        temp = {"name": name, "email": email}
        LIST_INFO.append(temp)
        self.redirect('/index/' + page)
