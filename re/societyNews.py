import urllib.request,re

class getHtml():
    def __init__(self,url,name):
        self.url=url
        self.name=name
        self.__get()
    def __get(self):
        self.html=urllib.request.urlopen(url=self.url).read()
        with open(r"{url}.html".format(url=self.name),"wb") as w:
            w.write(self.html)


class getNews():
    def __init__(self,html):
        self.html=html.decode('utf-8')
        self.__get()
    def __get(self):
        self.news1 = re.finditer(r'<span class="title">(.*?)?</span>',self.html)
        self.news2 = re.finditer(r'<span class="text-span">(.*?)?</span>',self.html)
        self.news3 = re.finditer(r'target="_blank">[^<](.*?)?</a>',self.html)
        str_news3=""
        for i in self.news3:
            if len(i.group(1))>=5:
                str_news3=str_news3+i.group()
        self.news3 = re.finditer(r'target="_blank">(.*?)?</a>',str_news3)
        self.news4 = re.finditer(r'<span class="mask">(.*?)?</span>', self.html)
        self.news5 = re.finditer(r' target="_blank" title=(.*?)?>(.*?)?</a>', self.html)
        self.news=[]
        for i in self.news1:
            self.news.append(i.group(1))
        for i in self.news2:
            self.news.append(i.group(1))
        for i in self.news3:
            self.news.append(i.group(1))
        for i in self.news4:
            self.news.append(i.group(1))
        for i in self.news5:
            self.news.append(i.group(1))

with open(r"{url}.html".format(url="社会新闻"),"rb") as r:
    html=r.read()
# html=getHtml("https://news.sina.com.cn/society/","社会新闻").html
news=getNews(html).news
# print(news)
for i in news:
    print(i)