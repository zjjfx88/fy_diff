#!/usr/bin/python
#coding=UTF-8
from lib import ConfReader
from lib import ParseXml
from lib import ReadQuery
import requests,sys

def getdiff():
    test_lst=dict()
    with open('alltj_result','r') as testfile:
        for line in testfile.readlines():
            test=eval(line)
            num=test['num']
            test_lst[num]=test
    with open('alltj_result1','r') as resfile,open('diff','a') as diffres:
        for line in resfile.readlines():
            base=eval(line)
            num=base['num']
            if num in test_lst:
                if base!=test_lst[num]:
                    diffres.write('base:'+str(base)+'\ntest:' +str(test_lst[num])+'\n')

if __name__ == "__main__":
    readconf=ConfReader.ConfReader('fy_diff.cfg')
    globalcfg=readconf.getItem('global')
    isParsereq=globalcfg['parse_req']
    isParseres=globalcfg['parse_res']
    runmode=globalcfg['run']
    print runmode
    if runmode=='all':
        testcfg=readconf.getItem('test')
        testHost=testcfg['test_host']
        testPort=testcfg['test_port']
        basecfg=readconf.getItem('base')
        baseHost=basecfg['base_host']
        basePort=basecfg['base_port']
        
    elif runmode=='test':
        testcfg=readconf.getItem('test')
        testHost=testcfg['test_host']
        testPort=testcfg['test_port']
    elif runmode=='base':
        basecfg=readconf.getItem('base')
        baseHost=basecfg['base_host']
        basePort=basecfg['base_port']
#    getdiff()
#    print globalcfg
    if globalcfg['query_alljson_file']!='':
       alltjreqFile=globalcfg['query_alljson_file']
       alltjresFile=alltjreqFile+'_result'
       ReadQuery.readAlltjFile(alltjreqFile,alltjresFile,testHost,testPort,isParsereq,isParseres)
#    if globalcfg['query_xml_file']!='' and globalcfg['xml_result_file']!='':
#        xmlreqfile=globalcfg['query_xml_file']
#        xmlresfile=globalcfg['xml_result_file']
#        readXmlFile(xmlreqfile,xmlresfile,isParsereq,isParseres)
#    if globalcfg['query_json_file']!='' and globalcfg['json_result_file']!='':
#        jsonreqfile=globalcfg['query_json_file']
#        jsonresfile=globalcfg['json_result_file']
#        readJsonFile(jsonreqfile,jsonresfile,isParsereq,isParseres)
#	readXmlFile()
#	getdiff()
#	conf=ConfReader.ConfReader('fy_diff.cfg')
#	print conf.getAllItem()	
#	print conf.getKey('test','svn')
