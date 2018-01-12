#coding=utf-8
import difflib,subprocess,os
from bs4 import BeautifulSoup
str1='''{'req_to': 'zh-CHS', 'subres': [('abstract_sum', '业余的亚洲混蛋-什么', 'text'), ('abstract_sum','7 : 20', 'text'), ('abstract_sum', '如此奇妙的世界', 'alt')], 'num': '1', 'req_from': 'en'}'''
str2='''{'req_to': 'zh-CHS', 'subres': [('abstract_sum', '业余亚洲混蛋-什么', 'text'), ('abstraact_sum','7 : 20', 'text'), ('abstract_sum', '如此奇妙的世界', 'alt')], 'num': '1', 'req_from': 'en'}'''

diff=difflib.HtmlDiff.make_file(difflib.HtmlDiff(),str1.splitlines(keepends=True),str2.splitlines(keepends=True))
#with open('testbs4.html','w',encoding='utf-8') as result:
#    result.write(diff)
soup=BeautifulSoup(diff,'html.parser')
#bettersoup=soup.prettify()
alltd=soup.tr.find_all('td')










with open('testbs4.html','w',encoding='utf-8') as result:
    for line in alltd:
#        result.write(str(line)+'\n')
        if "nowrap" in str(line):
            result.write(str(line)+'\n')
#            pass
parent=os.getcwd()
subprocess.Popen('cp -f testbs4.html /search/nginx/html/fy/',cwd=parent,stdout = None,stderr = None, shell = True)
