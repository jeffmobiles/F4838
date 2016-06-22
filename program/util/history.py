
# -*- coding: utf-8 -*-
from urllib import request
import threading
import datetime
import os
from time import sleep,ctime
from html import parser
import queue  
# 历史信息
#
#http://table.finance.yahoo.com/table.csv?s=600000.ss    
#http://table.finance.yahoo.com/table.csv?s=000001.sz
  
#test thread download history#
#save_url = "E:\\Cloud\\finance\\lianghua\\F4838\\data\\#.csv"
#load_url = "http://table.finance.yahoo.com/table.csv?s=#"     
#codeList = [
#    "600399.ss","002142.sz"
#]
#downloads(codeList,save_url,load_url)

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

      
# 历史成交明细  
def downloads_daily(codeList,save_url,load_url,date_from,date_to,folder):
    task_threads = [] #存储线程
    count = 1
    d1 =  datetime.datetime.strptime(date_from, '%Y-%m-%d')
    d2 =  datetime.datetime.strptime(date_to, '%Y-%m-%d')
    deld = d2 -d1
    d = 0;
    for code in codeList:
        #print(code)
        #print(folder)
        while d < deld.days+1:
            ddeld = datetime.timedelta(days=d)
            one_day = d1 + ddeld
            code_date = one_day.strftime("%Y-%m-%d")
            t_url = load_url.replace("#c#",code).replace("#d#",code_date)
            file_url = save_url.replace("#c#",code).replace("#d#",code_date)
            local_folder = folder.replace("#c#",code)
            is_folder = os.path.exists(local_folder)
            print(is_folder)
            print(file_url)
            print(t_url)
            if is_folder== False:
                os.makedirs(local_folder)
            t = threading.Thread(target=download_now,args=(t_url,file_url))
            count = count + 1
            task_threads.append(t)
            d = d + 1
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()  #等待所有线程结束  
        
        
d_load_url = "http://market.finance.sina.com.cn/downxls.php?date=#d#&symbol=#c#"
d_save_url = "E:\\python\\F4838\\data\\all_temp\\#c#___#d#.csv" 
class download(threading.Thread):
     def __init__(self,que):  
        threading.Thread.__init__(self)  
        self.que=que  
     def run(self):  
        while True:  
            if not self.que.empty():  
                print('-----%s------'%(self.name))  
                code = self.que.get().split("&&")[0]
                code_date = self.que.get().split("&&")[1]
                t_url = d_load_url.replace("#c#",code).replace("#d#",code_date)
                file_url = d_save_url.replace("#c#",code).replace("#d#",code_date)
                download_now(t_url,file_url)
                #os.system('wget '+self.que.get())  
            else:  
                break  
#下载当天的数据
                
  
def downloads_daily_single(codeList,save_url,load_url,date_from,date_to,folder):
    count = 1
    que=queue.Queue()
    d1 =  datetime.datetime.strptime(date_from, '%Y-%m-%d')
    d2 =  datetime.datetime.strptime(date_to, '%Y-%m-%d')
    deld = d2 -d1
    d = 0;
    for code in codeList:
        #print(code)
        #print(folder)
        ddeld = datetime.timedelta(days=0)
        one_day = d1 + ddeld
        code_date = one_day.strftime("%Y-%m-%d")
        #print(code_date)
        que.put(code+"&&"+code_date)
    for task in range(5):
        d = download(que)
        d.start()

codeList = ["sh600399"]
load_url = "http://market.finance.sina.com.cn/downxls.php?date=#d#&symbol=#c#"
folder = "E:\\python\\F4838\\data\\#c#\\"
save_url = "E:\\python\\F4838\\data\\#c#\\#d#.csv"  
downloads_daily(codeList,save_url,load_url,"2016-6-15","2016-6-22",folder)  
    