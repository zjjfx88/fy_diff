#!/usr/bin/python
#encoding=UTF-8
import os,subprocess













if __name__ == '__main__':
    parent='/search/odin/daemon/zhangjj/trans_server/dl_kernel.20171213.branch/server_frame/translate_server'
    startShell='start_uniq_trans_server1.sh'
    print 'sh '+os.path.join(parent,startShell)
    startInfo=subprocess.Popen('sh '+os.path.join(parent,startShell),cwd=parent,stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)
    print startInfo.wait()
    print startInfo.stdout.read()
    print startInfo.stderr.read()
