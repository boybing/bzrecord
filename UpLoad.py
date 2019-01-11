# encoding:utf-8

from bypy import ByPy
import os
import time

def upLoad(t):
    bp=ByPy()
    for l in range(0,len(t)-1):
        print(os.path.join(os.getcwd(),"tsdir",t[l]))
        try:
            bp.upload(localpath=os.path.join(os.getcwd(), "tsdir",t[l]), remotepath='bypy')
            print('上传完毕！')
            documentDelete(os.path.join(os.getcwd(),"tsdir",t[l]))
        except Exception as e:
            print(e)

def changeOrder(t):
    for x in range(0,len(t)):
        for y in range(0,len(t)):
            if t[x]<t[y]:
                tmp=t[x];
                t[x]=t[y];
                t[y]=tmp;
    return t

def documentDelete(path):
    print(path)
    os.remove(path)

while 1:
    try:
        ls = os.listdir(os.path.join(os.getcwd(),"tsdir"))
        print(os.path.join(os.getcwd(),"tsdir"))

        arr = []
        for name in ls:
            filename,type=os.path.splitext(name)
            print(filename)
            print(type)
            if type == ".mp4":
                arr.append(int(filename))
        cg=changeOrder(arr)
        print(cg)
        if len(cg)>1:
            tmp=[]
            for c in cg:
                tmp.append(str(c)+".mp4")
            print(tmp)
            upLoad(tmp)
        time.sleep(10)
    except Exception as e:
        print(e)
        time.sleep(10)