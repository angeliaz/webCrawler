# #coding=utf-8
# from bs4 import BeautifulSoup
# import re

# doc = ['<html><head><title>测试文件</title></head>',
#        '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.</p>',
#        '<p id="secondpara" align="blah">This is paragraph <b>two</b>.</p>',
#        '</html>']
# soup = BeautifulSoup(''.join(doc))
# head = soup.contents[0].contents[0]
# # print soup.prettify()

# print soup.title.name
# print soup.title.string
# print soup.p

# # print soup.contents[0].name
# # print soup.contents[0].contents[0].name
# # print head.nextSibling.name                            

# import codecs
# import urllib2
# import sys
# reload(sys)
# url = 'http://www.sina.com.cn'
# content= urllib2.urlopen(url).read()
# typeEncode=sys.getfilesystemencoding()
# infoencode=chardet.detect(u).get('encoding','utf-8')
# html = content.decode(infoencode,'ignore').encode(typeEncode)#{'confidence': 0.0, 'encoding': None}
# # soup = BeautifulSoup(content, from_encoding="gb2312")

# # print content.decode('gb2312').encode('utf8')
import urllib2
from StringIO import StringIO
import gzip
import re
 
hdr = {
    'Accept-Language' : 'zh-CN',
    'Accept-Charset' : 'gb2312',
    'User-Agent' : 'Mozilla/5.0 (MSIE 9.0; qdesk 2.5.1277.202; Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
}
 
rq = urllib2.Request('http://www.163.com', headers=hdr)
op = urllib2.urlopen(rq)
pg = None
if op.info().get('Content-Encoding') == 'gzip':
    buf = StringIO(op.read())
    f = gzip.GzipFile(fileobj = buf)
    pg = f.read()
else:
    pg = op.read()
m = re.findall('<a.*?href="([^"]+)"[^>]*>([^<]*)</a>', pg)
for l, i in m:
    print l, i