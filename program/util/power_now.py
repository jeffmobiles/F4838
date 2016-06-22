# -*- coding: utf-8 -*-

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import os

folder = "E:\\python\\F4838\\data\\all_temp\\"
#folder = "E:\\python\\F4838\\data\\sh600399\\"
filelist = os.listdir(folder)
print(filelist)

for file in filelist:
    df = pd.read_csv(folder+file,encoding="gbk",sep="\t")
    #print (df.columns)
    #Index(['成交时间', '成交价', '价格变动', '成交量(手)', '成交额(元)', '性质'], dtype='object')
    power = 0
    small_bill_buy = 0;
    small_bill_sell = 0
    small_bill_cha = 0;
    p_index = 0;
    p_all_vol = 0;
    if (df.size > 10):
        for index,row in df.iterrows():
            v_date = row['成交时间']
            open_date = v_date.split(":")[0]+v_date.split(":")[1]
            v_price = row['成交价']
            v_change = row['价格变动']
            if v_change == "--" :
                v_change = "0" 
            v_vol = row['成交量(手)']
            v_amount = row['成交额(元)']
            v_type = row['性质']
            
            p_all_vol += v_vol;
            #1-------------power--------------------
            this_power = float(v_change) * v_vol
            if open_date != "0925":
                power +=this_power
                
           #2------------小单差--------------------    
            if v_amount <= 40000 :
                if v_type == "买盘" :
                   small_bill_buy +=v_vol
                if v_type == "卖盘" :
                   small_bill_sell +=v_vol
           #3------------总笔数--------------------
            p_index = p_index + 1
        small_bill_cha = small_bill_buy - small_bill_sell           
        small_rate = (small_bill_buy + small_bill_sell )/p_all_vol
        #print (small_bill_cha)  
        if power > 0 and small_bill_cha < 0:         
            print (file,str(power) + "\t"+ str(p_index) + "\t"+str(small_bill_cha) +"\t"+str(small_rate))
        