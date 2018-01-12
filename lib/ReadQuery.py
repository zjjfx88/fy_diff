#!/usr/bin/python
#coding=UTF-8
#author=zhangjj
from lib import SendQuery
import json

def getReqNum(query):
    query=query.strip().split('===')
    Num=query[0]
    req=query[1]


def readXmlFile(xmlreqfile,xmlresfile,testHost,testPort,isParsereq='yes',isParseres='yes'):
    xml_info=dict()
    with open(xmlreqfile,'r') as infile,open(xmlresfile,'a') as outfile:
        for line in infile.readlines():
            xmlInfo=line.strip().split('===')
            xml_info['num']=xmlInfo[0]
            if isParsereq=='yes':
                query_lst_info=ParseXml.parseXmlReq(xmlInfo[1])
                if 'wrongreq' in query_lst_info:
                    xml_info['wrongreq']=query_lst_info['wrongreq']
                    outfile.write(str(xml_info)+'\n')
                    xml_info=dict()
                    continue
                xml_info['req']= query_lst_info

            resxmlstr=SendQuery.sendreq(xmlInfo[1],'xml',testHost,testPort)

            if isParseres=='yes':
                res=ParseXml.parseXmlRes(resxmlstr)
                if 'wrongres' in res:
                    xml_info['wrongres']=res['wrongres']
                    outfile.write(str(xml_info)+'\n')
                    xml_info=dict()
                    continue
                xml_info['res']=res
            else:
                xml_info['res']=resxmlstr

            outfile.write(str(xml_info)+'\n')


def readJsonFile(jsonreqfile,jsonresfile,testHost,testPort,isParsereq='yes',isParseres='yes'):
    json_info=dict()
    with open(jsonreqfile,'r') as injsonf,open(jsonresfile,'a') as outjsonf:
        for line in injsonf.readlines():
            jsonInfo=line.strip().split('===')
            json_info['num']=jsonInfo[0]
            if isParsereq=='yes':
                temp=json.loads(jsonInfo[1])
                json_info['req_chquery']=temp['translate_struct']['chinese_query']
                json_info['req_enquery']=temp['translate_struct']['english_query']
#               print u' '.join((req_chquery,req_enquery)).encode('utf-8').strip()
#               for i in  temp['translate_struct']['docs']:
#               print i['title'].decode('utf-8')
            res=SendQuery.sendreq(jsonInfo[1],'json',testHost,testPort)
            if isParseres=='yes':
                resparse=json.loads(res)
                rep_chquery=resparse['translate_result']['chinese_query']
#               print rep_chquery.encode('utf-8').strip()
                resp_doc_lst=list()
                for doc in resparse['translate_result']['docs']:
                    resp_doc_lst.append((doc['title'],doc['abstract']))
                json_info['docs']=resp_doc_lst
            else:
                json_info['docs']=res
            outjsonf.write(str(json_info))




def readAlltjFile(alltjreqFile,alltjresFile,testHost,testPort,isParsereq='yes',isParseres='yes'):
    alltj_info=dict()
    with open(alltjreqFile,'r') as inalltjf,open(alltjresFile,'w',encoding='utf-8') as outalltjf:
        for line in inalltjf.readlines():
            alltjInfo=line.strip().split('===')
            alltj_info['num']=alltjInfo[0]
            if isParsereq=='yes':
                temp=json.loads(alltjInfo[1])
                alltj_info['req_from']=temp['from_lang']
                alltj_info['req_to']=temp['to_lang']
            res=SendQuery.sendreq(alltjInfo[1],'alltrans_json',testHost,testPort)
#            print(res)
#            print(type(res))
            if isParseres=='yes':
                resparse=json.loads(res.decode('utf-8'))
                result=resparse['trans_result']
                resp_doc_lst=list()
                for sub_res in result:
                    resp_doc_lst.append((sub_res['model'],sub_res['trans_text'],sub_res['sendback']))
                alltj_info['subres']=resp_doc_lst
            else:
                alltj_info['subres']=res.decode('utf-8')

        print(type(alltj_info))
        print(type(str(alltj_info).encode()))
        outalltjf.write(str(alltj_info))
