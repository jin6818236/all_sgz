import requests
import parsel
import re
def download_one_url(url):
    ws_url = url
    ws_html = requests.get(ws_url)
    ws_html.encoding = ws_html.apparent_encoding
    ws_text = parsel.Selector(ws_html.text)
    ws_biaoti = ws_text.css('body > div.wrap > div.mod.mod-news-info > div > div.title > p > span::text').extract()
    ws_name = ws_text.css('body > div.wrap > div.mod.mod-news-info > div > div.title > h2::text').extract_first()
    ws_neirong = ws_text.css('body > div.wrap > div.mod.mod-news-info > div > div.content::text').extract()
    #print(ws_name)
    ws_mingzi = ws_name
    ws_xiaoshuo = open(ws_mingzi + '.txt','a', encoding='utf-8')
    for ws_bt in ws_biaoti:
        ws_xiaoshuo.write(ws_bt)
        #print(ws_bt)
        for ws_yi in ws_neirong:
            ws_xiaoshuo.write(ws_yi)
        ws_xiaoshuo.close()
    ws_xiaoshuo.close()
#download_one_url('https://m.wanshi.net/book/2677/797472.html')
def download_zhang_BU(BU, name):
    ws_html = requests.get(BU)
    ws_html.encoding = ws_html.apparent_encoding
    ws_text = parsel.Selector(ws_html.text)
    ws_biaoti = ws_text.css('body > div.wrap > div.mod.mod-news-info > div > div.title > p > span::text').extract_first()
    ws_qbt = re.sub(name,'',ws_biaoti)
    ws_sh = re.sub('\D','',ws_qbt)[1:]
    ws_over = int(ws_sh)
    ws_a = 0
    while ws_a < ws_over:
        ws_a += 1
        ws_xia = ws_text.css('body > div.wrap > div.mod.mod-news-info > div > div:nth-child(2) > a:nth-child(3)::attr(href)').extract_first()[0:18]
        ws_xyy = 'https://m.wanshi.net' + ws_xia + str(ws_a) + '.html'
        download_one_url(ws_xyy)
        #print(ws_xyy + '下载完成。')
#download_zhang_BU('https://m.wanshi.net/book/3079/908737.html')
def download_zhang_book(book):
    ws_html = requests.get(book)
    ws_html.encoding = ws_html.apparent_encoding
    ws_text = parsel.Selector(ws_html.text)
    ws_mul = ws_text.css('#allchapter > div.attentions > ul > li > a::attr(href)').extract()
    name_1 = ws_text.css('#allchapter > div.attentions > ul > li > a::text').extract()
    shuzi = 0
    for mul in ws_mul:
        name = name_1[shuzi]
        shuzi +=1
        ws_ul = 'https://m.wanshi.net'+mul
        print(name+'......已下载')
        download_zhang_BU(ws_ul, name)
        #print(ws_ul + '.....')
#download_zhang_book('https://m.wanshi.net/chapterlist/3079/')

def download_book_one(one):
    ws_quanbu_url = one
    ws_html = requests.get(ws_quanbu_url)
    ws_html.encoding = ws_html.apparent_encoding
    ws_html_one = parsel.Selector(ws_html.text)
    ws_biaoge = ws_html_one.css('#allchapter > div:nth-child(2) > span.middle > select > option::attr(value)').extract()[-1]
    ws_shuming = ws_html_one.css('body > div.header > h1::text').extract_first()
    print(ws_shuming+'开始下载！......')
    tin = one.replace('https://m.wanshi.net','')
    ws_zhang = ws_biaoge.replace(tin,'')[:-1]
    ws_zhangjie = int(ws_zhang)
    ws_u = tin
    #print(ws_u)
    shuzi = 0
    while shuzi < ws_zhangjie:
        shuzi += 1
        ws_quanben = 'https://m.wanshi.net' + ws_u + str(shuzi) + '/'
        download_zhang_book(ws_quanben)
        print('已下载' + str(int(shuzi/ws_zhangjie*100))+'%')
    print(ws_shuming+'.txt下载完成.')
#download_book_one('https://m.wanshi.net/chapterlist/2677/')
def download_quan_ben(ben):
    ws_qbzj_url = ben
    ws_quanbu_url = ws_qbzj_url
    ws_html = requests.get(ws_quanbu_url)
    ws_html.encoding = ws_html.apparent_encoding
    ws_html = parsel.Selector(ws_html.text)
    ws_qbzj = ws_html.css('body > div.wrap.wrap-info > div.mod.mod-attentions > div.attentions > ul > li > a::attr(href)').extract()[-1]
    ws_qben = 'https://m.wanshi.net' + ws_qbzj
    download_book_one(ws_qben)
#download_quan_ben('https://m.wanshi.net/book/2677/')

def download_qz_yiye(yiye):
    ws_quanzhan = yiye
    ws_html = requests.get(ws_quanzhan)
    ws_html.encoding = ws_html.apparent_encoding
    ws_html = parsel.Selector(ws_html.text)
    ws_qz = ws_html.css('body > div.wrap > div.mod.mod-book > div.book-list > ul > li > a.tit::attr(href)').extract()
    for quanben in ws_qz:
        ws_all = 'https://m.wanshi.net' + quanben
        download_quan_ben(ws_all)
        #print(ws_all)
#download_qz_yiye('https://m.wanshi.net/sort/1/')
def download_qz_quanbu(quanbu):
    ws_quanzhan = quanbu
    ws_qbzj_url = ws_quanzhan
    ws_quanbu_url = ws_qbzj_url
    ws_html = requests.get(ws_quanbu_url)
    ws_html.encoding = ws_html.apparent_encoding
    ws_html = parsel.Selector(ws_html.text)
    ws_qz = ws_html.css('body > div.wrap > div.mod.mod-book > div.book-list > ul > li > a.tit::attr(href)').extract()
    ws_qye = ws_html.css('body > div.wrap > div.mod.mod-book > div.pages > a::attr(href)').extract()[-1]
    ws_quanbu = ws_qye[:-8]
    shuzi = 0
    ws_xye = int(ws_qye[-8:-5])
    while shuzi < ws_xye:
        shuzi += 1
        ws_allhtml = 'https://m.wanshi.net' + ws_quanbu + str(shuzi) + '.html'
        download_qz_yiye(ws_allhtml)
        #print(ws_allhtml)
download_qz_quanbu('https://m.wanshi.net/sort/')


