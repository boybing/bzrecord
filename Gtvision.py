# encoding:utf-8

import datetime
import os
import re
import time
import requests

def mktsfile(address):
    global visTime
    url = address
    all_content = requests.get(url).text
    print(all_content)
    err = re.findall(r'ErrTS.*?ts',all_content)
    t = re.findall(r'http:.*?.ts', all_content)
    # s1 = re.findall(r'C71904961_1_1/.*?.ts', all_content)
    print(err)
    print(t)
    # s1=s1[0].replace("C71904961_1_1/","")
    # print(s1)
    if len(err)>0:
        pass
    else:
        if len(t)==1:
            res = requests.get(t[0])
            with open(str(getNum()) + '.ts', 'ab') as f:
                f.write(res.content)
                f.flush()
        else:
            #排序
            t=changeOrder(t)
            for i in range(0,len(t)):
                global count
                fres = t[i]
                print(fres)
                arr=fres.split('-')
                nameChangedOrNot(arr[0])
                rr=arr[1].replace(".ts","")
                print(type(rr))
                intv=int(rr)
                if intv >count:
                    count=int(rr)
                    print(fres)
                    res = requests.get(t[i])
                    listNum=str(getNum())
                    with open(os.getcwd() + "/"+listNum + '.ts', 'ab') as f:
                        f.write(res.content)
                        f.flush()
                    time.sleep(2)
                    crontabMovie(os.getcwd(),listNum, visTime)
                    timeDid()
                else:
                    pass

def OsDelete():
    ls = os.listdir(os.getcwd())
    print(os.getcwd())

    for name in ls:
        filename,type=os.path.splitext(name)
        print(filename)
        print(type)
        if type==".ts":
            print(os.path.join(os.getcwd(),filename+type))
            os.remove(os.path.join(os.getcwd(), filename+type))

def getNum():
    global num
    print(num)
    num=num+1
    return num

def changeOrder(t):
    for x in range(0,len(t)):
        for y in  range(0,len(t)):
            if t[x]<t[y]:
                tmp=t[x];
                t[x]=t[y];
                t[y]=tmp;
    return t

def timeDid():
    global visTime
    if visTime == 0:
        visTime = timeformat()
    elif visTime == timeformat():
        pass
    else:
        # OsDid.OsMove(visTime)
        OsDelete()
        global num
        num=0
        visTime=timeformat()

def nameChangedOrNot(nn):
    global name
    global count
    if count==0:
        name=nn
    else:
        if nn==name:
            pass
        else:
            count=0

def timeformat():
    return datetime.datetime.now().strftime('%Y%m%d%H%M')

def timedelay():
    return (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime('%Y-%m-%d-%H-%M')

def crontabMovie(pa,ls,name):
    try:
        os.system("cat " + pa +"/"+ str(ls) + ".ts >> " + pa + "/" + name + ".mp4")
    except:
        pass
num=0
count=0
visTime=0
name=''
os.chdir("tsdir")
while 1:
    try:
        try:
            if os.environ['ADDRESS']=="":
                print("empty")
                break
        except:
            print("erro")
            break
        mktsfile(address=os.environ['ADDRESS'])
        time.sleep(3)
    except Exception as e:
        time.sleep(2)
        print(e)

# print(timeformat())
# print(timedelay())
