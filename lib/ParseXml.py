#!/usr/bin/python
#encoding=UTF-8
from xml.etree import ElementTree


def parseXmlReq(xml_str):
    query_lst_info=dict()
    if xml_str=="":
        return query_lst_info
    xmlns={'soapenv':'http://schemas.xmlsoap.org/soap/envelope/',
         'v2':'http://api.microsofttranslator.com/V2'}
    try:
        root=ElementTree.fromstring(xml_str)
    except Exception,e:
        query_lst_info['wrongreq']='wrong request,reson:'+str(e)
        return query_lst_info
    for node in root.findall('soapenv:Body',xmlns):
        for Translate in node.findall('v2:Translate',xmlns):
            if Translate.find('v2:text',xmlns) is not None:
                query_lst_info['text']=Translate.find('v2:text',xmlns).text.encode('utf-8')
            else:
                query_lst_info['qtext']=''
            if Translate.find('v2:from',xmlns) is not None:
                query_lst_info['qfrom']=Translate.find('v2:from',xmlns).text.encode('utf-8')
            else:
                query_lst_info['qfrom']=''
            if Translate.find('v2:to',xmlns) is not None:
                query_lst_info['qto']=Translate.find('v2:to',xmlns).text.encode('utf-8')
            else:
                query_lst_info['qto']=''
    return query_lst_info

def parseXmlRes(xml_str):
    result_dic=dict()
    ns={'parent':'http://schemas.xmlsoap.org/soap/envelope/','child':'http://fanyi.sogou.com/'}
    try:
        root=ElementTree.fromstring(xml_str)
    except Exception,e:
        result_dic['wrongres']='wrongres:'+str(e)
        return result_dic
    for node in root.findall('parent:Body',ns):
        for body in node.findall('child:TranslateResponse',ns):
            if body.find('child:TranslateResult',ns) is not None:
                result_dic['transRes']=body.find('child:TranslateResult',ns).text.encode('utf-8')
            else:
                result_dic['transRes']=''
            if body.find('child:orig_text',ns) is not None:
                result_dic['transText']=body.find('child:orig_text',ns).text.encode('utf-8')
    return result_dic
