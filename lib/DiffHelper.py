#!/usr/bin/python
#coding=UTF-8
#author=zhangjj
import subprocess
import difflib,os,sys,re
from bs4 import BeautifulSoup
difflist=[]

def getAllDiff(diffbase,difftest):
    diff=difflib.HtmlDiff.make_file(difflib.HtmlDiff(),diffbase.splitlines(keepends=True),difftest.splitlines(keepends=True))
    soup = BeautifulSoup(diff, "html.parser")
    alltd=soup.tr.find_all('td')
    for line in alltd:
        if "nowrap" in str(line):
            difflist.append("<tr>"+str(line)+"</tr>")


def gethtmlDiff(diffbase,difftest):
    diff=difflib.HtmlDiff.make_file(difflib.HtmlDiff(),diffbase.splitlines(keepends=True),difftest.splitlines(keepends=True))
    with open('diff_test.html','w',encoding='utf-8') as r:
        r.write(diff) 
    

def getHtmlDiff(base):
    base_dic=dict()
    test_dic=dict()
    global lentest
    global lenbase
    global diffbase
    global difftest
    #read base file and transfer to a dict
    with open('../alltj_result','r',encoding='utf-8') as basef:
        try:
            while True:
                baseline=basef.readline().strip()
                if baseline:
                    base=eval(baseline)
                    num=base['num']
                    base_dic[num]=base
                else:
                    lenbase=len(base_dic)
                    break
        except Exceptions as e:
            print(e)

    #read test file and transfer to a dict
    with open('../alltj_result1','r',encoding='utf-8') as testf:
        try:
            while True:
                testline=testf.readline()
                if testline:
                    test=eval(testline)
                    num=test['num']
                    test_dic[num]=test
                else:
                    lentest=len(test_dic)
                    break
        except Exceptions as e:
            print(e)
    diffcount=0
    samecount=0
    if lentest>=lenbase:
        for key in test_dic:
            if key in base_dic:
                if test_dic[key]!=base_dic[key]:
                    diffcount+=1
                    diffbase=str(base_dic[key])
                    difftest=str(test_dic[key])
                    getAllDiff(diffbase,difftest)
                else:
                    samecount+=1
            else:
                diffcount+=1
                diffbase='have no result'
                difftest=str(test_dic[key])
                getAllDiff(diffbase,difftest)
    else:
        for key in base_dic: 
            if key in test_dic:
                if test_dic[key]!=base_dic[key]:
                    diffcount+=1
                    diffbase=str(base_dic[key])
                    difftest=str(test_dic[key])
                    getAllDiff(diffbase,difftest)
                else:
                    samecount+=1
            else:
                diffcount+=1
                difftest='have no result'
                diffbase=str(test_dic[key])
                getAllDiff(diffbase,difftest)
    genReport()

    
def genReport():
    parent=os.getcwd()
    with open('diffreport.html','w',encoding='utf-8') as report:
        report.write(header)
    with open('diffreport.html','a',encoding='utf-8') as diffreport:
        for line in difflist:
            diffreport.write(line)
        diffreport.write(ender)
    subprocess.Popen('cp -f diffreport.html /search/nginx/html/fy/',cwd=parent,stdout = None,stderr = None, shell = True)


global header
global ender

header='''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title></title>
<style type="text/css">
table.diff {font-family:Courier; border:medium;}
.diff_header {background-color:#e0e0e0}
td.diff_header {text-align:right}
.diff_next {background-color:#c0c0c0}
.diff_add {background-color:#aaffaa}
.diff_chg {background-color:#ffff77}
.diff_sub {background-color:#ffaaaa}
</style>
</head>
<body>
<table class="diff" summary="Legends">
<tbody>
<tr> <td> <table border="" summary="Colors">
<tbody>
<tr><td class="diff_add">&nbsp;Added&nbsp;</td><td>(f)irst change</td><td class="diff_chg">Changed</td><td>(n)ext change</td><td class="diff_sub">Deleted</td><td>(t)op</td></tr>
</tbody></table></td>
</tr>
</tbody></table><table class="diff" id="difflib_chg_to0__top" cellspacing="0" cellpadding="0" rules="groups">
<tbody>
'''
ender='''
</tbody>
</table>
</body></html>
'''

if __name__ == '__main__':
#    getHtmlDiff()
#    parent=os.getcwd()
#    str1='''<document expiretime="600000" location="0" request_id="000000000021848e">'''
#    str2='''<document expiretime="600000" location="0" request_id="0000000000d3f01d">'''
#    gethtmlDiff(str1,str2) 
#    subprocess.Popen('cp -f diff_test.html /search/nginx/html/fy/',cwd=parent,stdout = None,stderr = None, shell = True)
