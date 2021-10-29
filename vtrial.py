# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 22:10:23 2021

@author: sreem
"""

import numpy as np
import random
from random import seed
from random import randint
import datetime
from datetime import date
import csv

filename = 'Vehicleinfo.csv'

Vlist = ['TS08HE6446', 'AP28AN8619','TS08ER2494'] 
#Ebatlist = ['15','125','276','124','40', '125', '276','180','255']
#Mbatlist = ['1.2','2.2','3.0','4.6','1.2','3.7','2.2','1.2','4.6','4.6','3.4','3.7','3.0','2.2','40','3.7','2.1','40','40','70','124','4.6','300']
Nbatlist = ['15','125','276','124','276','125','124']
#array = [10, 20, 30, 40, 50, 20, 40]
bike = random.uniform(1.0, 4.7)
riks = random.uniform(3.7,10)
l4w = random.uniform(30.0,76.4)
truck = random.uniform(100.0,400.0)
bus = random.uniform(72.0,324.0)
cur = base = datetime.datetime (2019,1,1,hour=12,minute=0,second=0)
#cur = base = datetime.datetime.now() 
end  = base + datetime.timedelta(days=365)
delta  = datetime.timedelta(minutes=30)
earlyhours = datetime.time(hour=0,minute=0,second=0)
MorningH = datetime.time(hour=5,minute=0,second=0)
eveningH = datetime.time(hour=22,minute=0,second=0)
vtype = 0
battery = 0
power_con = 0
with open(filename, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    header = ['VID','type','battery', 'iSoC','finalcharge ','charged amount','start time','stop time','duration','power_con','year','month','day', 'hour','minute']
    writer.writerow(header)
seed(1)

for j in range(10000000):
    for i in range(len(Vlist)):
        intialcharge = x  = randint(20, 50)
        
        finalcharge = randint(x,100)
        charge_total = finalcharge-intialcharge
        hour = t = base.hour
        start_time = float(t)
             
        duration = (charge_total*5)/100
        stop_time = start_time + duration
        #battery = randint(1,100)
        #battery =  np.random.choice(Mbatlist)
        
        #print("base hour:" + str(z))
        
        
        if (hour>0 and hour<=5):
        
           battery = random.uniform(80.0, 225.0)
           if (battery>80 and battery<150):
              vtype = 'TruckL/Dcm'
              power_con = 0.125*duration
           if (battery>151 and battery<200):
              vtype = 'TruckM'
              power_con = 1.18*duration
           if (battery>201 and battery<225):    
              vtype = 'TruckH'
              power_con = 2.5*duration
           
        if (hour>5 and hour<=21):
           battery = random.uniform(1.0, 80.0)
           if (battery>0.9 and battery<4.7):
              vtype = 'bike'
              power_con = 0.22*duration
           if (battery>4.8 and battery<10):
              vtype = 'rickshaw'
              power_con = 0.32*duration
           if  (battery>10 and battery<40):
              vtype = 'car'
              power_con = 0.33*duration
           if  (battery>40 and battery<79):
              vtype = 'bus'
              power_con = 0.75*duration
        
        if (hour>21 and hour<=0):
        #else:
            battery = random.uniform(10,250)
            if (battery>10 and battery<100):
                vtype = 'car'
                power_con = 0.33*duration
            if (battery>100 and battery<200):
                vtype = 'bus'
                power_con = 0.75*duration
            if (battery>200):
                vtype  = 'TruckH'
                power_con = 2.5*duration            
                          
                         
        data = [Vlist[i], vtype, battery, intialcharge, finalcharge, charge_total, start_time, stop_time, duration,power_con,base.year, base.month, base.day, base.hour, base.minute ]
        
       
        
        with open(filename, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)      
            # write the data
            writer.writerow(data)
            print("Data written to file")
   
    base = base+delta
    if(base > end):
        print('Generated data')
        break
#x = np.random.choice(array, size=1)


