#!/usr/bin/python
#coding=UTF-8
#author=zhangjj
import requests
def sendreq(query,mode,testHost,testPort):
    try:
#        encoded = unicode(query,'utf-8').encode("utf8")
        encoded=query.encode('utf-8')
#        print(type(encoded))
        headers = {'User-agent': 'Mozilla/5.0', "Content-type":"text/xml"}
        resp = requests.post("http://"+testHost+":"+testPort+"/"+mode, headers=headers, data=encoded)
        resp_str = resp.text.encode('utf-8')
        return resp_str
    except Exception as e:
        print('request failed',e)
