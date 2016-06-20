
# -*- coding: utf-8 -*-
from urllib import request
import threading
import datetime
import os
from time import sleep,ctime
from html import parser

# 历史信息
#
#http://table.finance.yahoo.com/table.csv?s=600000.ss    
#http://table.finance.yahoo.com/table.csv?s=000001.sz


def download(load_url,save_url):
    webopen = request.urlopen(load_url)
    web_file = webopen.read()
    local_file = open(save_url,"wb")
    local_file.write(web_file)
    local_file.close()
    
def downloads(codeList,save_url,load_url):
    task_threads = [] #存储线程
    count = 1
    for code in codeList:
        t_url = load_url.replace("#",code)
        file_url = save_url.replace("#",code)
        t = threading.Thread(target=download,args=(t_url,file_url))
        count = count + 1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()  #等待所有线程结束


# 当天信息
# test thread download now 
#now = datetime.datetime.now().strftime('%Y-%m-%d')        
#codeList = ["sh600399","sz002142"]
#load_url = "http://market.finance.sina.com.cn/downxls.php?date=#d#&symbol=#c#"
#folder = "E:\\Cloud\\finance\\lianghua\\F4838\\data\\#c#\\"
#save_url = "E:\\Cloud\\finance\\lianghua\\F4838\\data\\#c#\\#d#.csv"  
#downloads_now(codeList,save_url,load_url,now,folder)

def download_now(load_url,save_url):
    webopen = request.urlopen(load_url)
    web_file = webopen.read()
    local_file = open(save_url,"wb")
    local_file.write(web_file)
    local_file.close()
    
def downloads_now(codeList,save_url,load_url,now,folder):
    task_threads = [] #存储线程
    count = 1
    for code in codeList:
        print(code)
        print(folder)
        t_url = load_url.replace("#c#",code).replace("#d#",now)
        file_url = save_url.replace("#c#",code).replace("#d#",now)
        local_folder = folder.replace("#c#",code)
        is_folder = os.path.exists(local_folder)
        print(local_folder)
        print(is_folder)
        if is_folder== False:
            os.makedirs(local_folder)
        t = threading.Thread(target=download_now,args=(t_url,file_url))
        count = count + 1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()  #等待所有线程结束
# test #
#save_url = "E:\\Cloud\\finance\\lianghua\\F4838\\data\\#.csv"
#load_url = "http://table.finance.yahoo.com/table.csv?s=#"
#download(load_url,save_url)    
# test end ...
        
#test thread download history#
#save_url = "E:\\Cloud\\finance\\lianghua\\F4838\\data\\#.csv"
#load_url = "http://table.finance.yahoo.com/table.csv?s=#"     
#codeList = [
#    "600399.ss","002142.sz"
#]
#downloads(codeList,save_url,load_url)
        

    