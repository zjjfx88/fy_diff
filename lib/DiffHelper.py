#!/usr/bin/python
#coding=UTF-8
#author=zhangjj
import subprocess
import difflib
from bs4 import BeautifulSoup
def getdiff():
    test_lst=dict()
    with open('../alltj_result','r') as testfile:
        for line in testfile.readlines():
            test=eval(line)
            num=test['num']
            test_lst[num]=test
    with open('../alltj_result1','r') as resfile,open('diff','a') as diffres:
        for line in resfile.readlines():
            base=eval(line)
            num=base['num']
            if num in test_lst:
                if base!=test_lst[num]:
                    diffres.write('base:'+str(base)+'\ntest:' +str(test_lst[num])+'\n')

def getDiff():
    #with open('../alltj_result','r') as str1,open('../alltj_result1','r') as str2:
    str1='abcdaf ghda12314 24325'
    str2='abcdef ghdaa12314 2325'
    diff=difflib.HtmlDiff.make_file(difflib.HtmlDiff(),str1,str2)
#    print diff
#    diff=BeautifulSoup(diff)
#    diff=diff.prettify()
    k = BeautifulSoup(diff, "html.parser")
    
    with open('aaa.html','w') as test:
        test.write(diff)
#    print diff
#    diffres.write(diff)
    res1=list()
    res2=list()
    i='0'
    for sub in k.descendants:
#        #print k.descendants
#        print sub
        if sub.name=='td':
            try:
                if sub['nowrap']=='nowrap':
                    print sub
                    if i=='0':
                        res1.append(sub.contents)
                        i='1'
                        continue
                    if i=='1':
                        res2.append(sub.contends)
                        i='0'
                        continue
            except Exception,e:
                #print e
                pass
    print res1
    print res2    

def getHtmlDiff():
    parent='/search/odin/daemon/zhangjj/tools/diff/lib'
#   subprocess.Popen('rm -f diff.html',cwd=parent,stdout = None,stderr = None, shell = True)
    with open('../alltj_result','r') as testfile,open('../alltj_result1','r') as resfile,open('diff.html','w') as diffres: 
        #wrapcolumn=100
        diff=difflib.HtmlDiff.make_file(difflib.HtmlDiff(),testfile,resfile )
        k = BeautifulSoup(diff, "html.parser")
        #print k
        #diffres.write(diff)
        res1=list()
        res2=list()
        i='0'
        for sub in k.descendants:
        #print k.descendants
            if sub.name=='td':
                try:
                    if sub['nowrap']=='nowrap':
                        if i=='0':
                            print sub.contents
                except Exception,e:
                    print e
    subprocess.Popen('cp -f diff.html /search/odin/nginx/html/fy/',cwd=parent,stdout = None,stderr = None, shell = True)
if __name__ == '__main__':
#    a='abcdefg hello word'
#    b='abccefg hEllo Worf'
#    s=difflib.SequenceMatcher(None,a,b)
#    print(s.get_matching_blocks())
#    print a,'\n',b
#    print(s.get_opcodes())
#    print(list(difflib.Differ().compare(a,b)))
    getDiff()
