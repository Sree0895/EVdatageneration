# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:17:44 2021

@author: sreem
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
YearList=[]
TypeList=[]
MonthList = ["Jan", "Feb", "Mar", "Apr", "May","Jun", "Jul", "Aug", "Sep","Oct","Nov","Dec"]
WeekDayList = ["Sun", "Mon", "Tue", "Wed", "Thu","Fri", "Sat"]

RegionList = []
ChargePointList = [] 
HourList = range(0,24)
DateList = range(0,32)

YearWise = []
TypeWise = []
MonthWise = []
SensorWise = []
HourWise = []
DateWise =[]
WeekDayWise =[]
RegionWise = []
ChargePointWise = []

filename='Vehicleinfo2.csv'

def plotBar(xData,yData,plot_title,x_label,y_label):
    plt.figure(figsize = (20,10))
       
    df = pd.DataFrame(list(zip(xData, yData)),
                   columns =[x_label, y_label])
    
    plots = sns.barplot(x=x_label, y=y_label, data=df)
     
    # Iterating over the bars one-by-one
    for bar in plots.patches:
       
      # Using Matplotlib's annotate function and
      # passing the coordinates where the annotation shall be done
      # x-coordinate: bar.get_x() + bar.get_width() / 2
      # y-coordinate: bar.get_height()
      # free space to be left to make graph pleasing: (0, 8)
      # ha and va stand for the horizontal and vertical alignment
        plots.annotate(format(bar.get_height()),
                       (bar.get_x() + bar.get_width() / 3,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
    
    plt.title(plot_title)
    
    # giving X and Y labels
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    
def getYearWise():
    
    for i in range(len(YearList)):
        Total_power=dataset_power_con.loc[dataset_power_con['Year'] == YearList[i], 'power_con'].sum()
        Total_power=round(Total_power,2)
        YearWise.append(Total_power)
        print('Power consumption in year ' + str(YearList[i]) +  " = " + str(Total_power))
    plotBar(YearList,YearWise,"Overall Year wise Power Consumption","Year","Power consumption") 

def getTypeWise():
    # This part of code gets the total number of intrusions in a given region
    for i in range(len(TypeList)):
        Total_power=dataset_power_con.loc[dataset_power_con['type'] == TypeList[i], 'power_con'].sum()
        Total_power=round(Total_power,2)
        TypeWise.append(Total_power)
        print('power consumption in region ' + str(TypeList[i]) +  " = " + str(Total_power))
    plotBar(TypeList,TypeWise,"Overall type wise Power consumption","type","Power consumption") 
    
def getMonthWise():
    for i in range(len(MonthList)):
        Total_power=dataset_power_con.loc[dataset_power_con['Month'] == i+1, 'power_con'].sum()
        Total_power=round(Total_power,2)
        MonthWise.append(Total_power)
        print( "Power Consumption in Month " + str(i) + " = " + str(Total_power) )
    plotBar(MonthList,MonthWise,"Overall Month wise Power Consumption","Month","Power Consumption")    

def getHourWise():

    for i in range(len(HourList)):
        Total_power=dataset_power_con.loc[dataset_power_con['Hour'] == i+1, 'power_con'].sum()
        Total_power=round(Total_power,2)
        HourWise.append(Total_power)
        print( "Power Consumption in Hr " + str(i) + " = " + str(Total_power) )
    plotBar(HourList,HourWise,"Overall Hour wise Power Consumption","Time in hours","Power Consumption")
    
def getRegionWise():

    for i in range(len(RegionList)):
        Total_power=dataset_power_con.loc[dataset_power_con['Region'] == RegionList[i], 'power_con'].sum()
        Total_power=round(Total_power,2)
        RegionWise.append(Total_power)
        print( "Power Consumption in Region " + str(i) + " = " + str(Total_power) )
    plotBar(RegionList,RegionWise,"Overall Region wise Power Consumption","Region","Power Consumption")
    
def getChargePointWise():

    for i in range(len(ChargePointList)):
        Total_power=dataset_power_con.loc[dataset_power_con['ChargePoint'] == ChargePointList[i], 'power_con'].sum()
        Total_power=round(Total_power,2)
        ChargePointWise.append(Total_power)
        print( "Power Consumption in ChargePoint " + str(i) + " = " + str(Total_power) )
    plotBar(ChargePointList,ChargePointWise,"Overall ChargePoint wise Power Consumption","ChargePoint","Power Consumption")


def getRegionMonthWise():
    
    for i in range(len(RegionList)):
        Total_power = 0
        MonthWise.clear()
        for j in range(len(MonthList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Month'] == j+1) & (dataset_power_con['Region'] == RegionList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            MonthWise.append(Total_power)
            print( "Power Consumption in Month " + str(MonthList[j])  +" in Region" + RegionList[i] + " = " + str(Total_power) )
        plotBar(MonthList,MonthWise,"Region wise Power Consumption per month in "+RegionList[i],"Month","PC")

def getTypeMonthWise():
    
    for i in range(len(TypeList)):
        Total_power = 0
        MonthWise.clear()
        for j in range(len(MonthList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Month'] == j+1) & (dataset_power_con['type'] == TypeList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            MonthWise.append(Total_power)
            print( "Power Consumption in Month " + str(MonthList[j])  +" of type" + TypeList[i] + " = " + str(Total_power) )
        plotBar(MonthList,MonthWise,"Month wise Power Consumption in "+TypeList[i],"Month","PC") 

def getRegionHourWise():
            
    for i in range(len(RegionList)):
        Total_power = 0
        HourWise.clear()
        for j in range(len(HourList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Hour'] == j) & (dataset_power_con['Region'] == RegionList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            HourWise.append(Total_power)
            print( "Power Consumption in hour " + str(HourList[j])  +" in Region " + RegionList[i] + " = " + str(Total_power) )
        plotBar(HourList,HourWise,"Region wise Power Consumption per hour in "+ RegionList[i],"Region","Power Consumption")
        
def getTypeHourWise():
            
    for i in range(len(TypeList)):
        Total_power = 0
        HourWise.clear()
        for j in range(len(HourList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Hour'] == j) & (dataset_power_con['type'] == TypeList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            HourWise.append(Total_power)
            print( "Power Consumption in hour " + str(HourList[j])  +" of type " + TypeList[i] + " = " + str(Total_power) )
        plotBar(HourList,HourWise,"Hour wise Power Consumption in "+ TypeList[i],"Time in hours","Power Consumption")     

def getChargePointHourWise():
            
    for i in range(len(ChargePointList)):
        Total_power = 0
        HourWise.clear()
        for j in range(len(HourList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Hour'] == j) & (dataset_power_con['ChargePoint'] == ChargePointList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            HourWise.append(Total_power)
            print( "Power Consumption in hour " + str(HourList[j])  +" of charge Point " + ChargePointList[i] + " = " + str(Total_power) )
        plotBar(HourList,HourWise,"Charge Point wise Power Consumption per hour in "+ ChargePointList[i],"Time in hours","Power Consumption")     


def getTypeDateWise():        
        
    for i in range(len(TypeList)):
        Total_power = 0
        DateWise.clear()
        for j in range(len(DateList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['Day'] == j+1) & (dataset_power_con['type'] == TypeList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            DateWise.append(Total_power)
            print( "Power Consumption in datawise " + str(DateList[j])  +" of type " + TypeList[i] + " = " + str(Total_power) )
        plotBar(DateList,DateWise,"Date wise Power Consumption in "+ TypeList[i],"Dates","Power Consumption")  

def getTypeDayWise():
    
    for i in range(len(TypeList)):
        Total_power = 0
        WeekDayWise.clear()
        for j in range(len(WeekDayList)):
            Total_power=dataset_power_con.loc[(dataset_power_con['WeekDay'] == j) & (dataset_power_con['type'] == TypeList[i]), 'power_con'].sum()
            Total_power=round(Total_power,2)
            WeekDayWise.append(Total_power)
            print( "Power Consumption in WeekDayWise " + str(WeekDayList[j])  +" of type " + TypeList[i] + " = " + str(Total_power) )
        plotBar(WeekDayList,WeekDayWise,"Week Day wise Power Consumption in "+ TypeList[i],"Days","Number of Power Consumption")     



    
plt.close('all') 

# Importing the dataset
dataset = pd.read_csv(filename)

# Get the Regions from the table
RegionList=dataset.Region.unique()
YearList=dataset.Year.unique()
TypeList=dataset.type.unique()
ChargePointList=dataset.ChargePoint.unique()

# Get the Regions from the table
dataset_power_con=dataset[dataset.power_con >0]

getYearWise()
getTypeWise()
getMonthWise()
getHourWise()
getChargePointWise()
getRegionWise()
getTypeMonthWise()
#getTypeHourWise()
#getTypeDateWise()
getTypeDayWise()
getRegionMonthWise()
getRegionHourWise()
getChargePointHourWise()
