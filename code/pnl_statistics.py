#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:16:19 2019

@author: yawen
"""

import pandas as pd 
import numpy as np 
from scipy.stats import skew 
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
import seaborn as sns, numpy as np


def f_pnl_statistics(rtn,spy_r=None):
    '''
    parameters:
        rtn is dataframe of daily return , with index of date and columns of daily return 
        
    return:
        df_pnl_ana : with columns of 'Cumulative_Return', 'Daily_Mean_Arith', 'Daily_Mean_Geom', 'Max_Drawdown', 'Volatility', 'Skewness', 'Kurtosis', 'Modified_Var', 'Conditional_VaR', 'Sharpe_Ratio', 'Min_Daily_Return'
                    all indicator are annualized assuming that 250 business day in one year
        fig: graph of annualized return 
    '''
    
    
    
    #Cumulative(rtn)
    rtn_array = rtn.values.flatten()
    
    #number of trade days
    N = rtn_array.shape[0]

    try:
        spy_array = spy_r.values.flatten()
    except:
        spy_array=np.full(N,0)
        
    
    
    
    #cumulative return 
    Cumulative_Pnl = (rtn_array+1).cumprod()-1
    Cumulative_spy = (spy_array+1).cumprod()-1
    
    #plot cumulative return 
    fig1 = plt.figure(figsize=(10,6))
    plt.plot(Cumulative_Pnl, label = 'Cumulative_Pnl of Portfolio')
    plt.plot(Cumulative_spy, label = 'Cumulative_Pbl of SPY500')
    plt.legend()
    plt.title('Cumulative Return')
    plt.close(fig1)
    
    # plot daliy return distribution
    fig2 = plt.figure(figsize=(10,6))
    sns.distplot(rtn)
    plt.title("Distributon of Daliy Return")
    plt.close(fig2)
    
    #cumulative return
    Cumulative_Return = Cumulative_Pnl[-1]*250/N
    
    #arithmetic average return
    Daily_Mean_Arith = np.nanmean(rtn_array)*250
    
    # Geometric Mean Return
    Daily_Mean_Geom = (np.power((rtn_array+1).cumprod()[-1],1/N)-1)*250
    
    # Min_Daily_Return
    Min_Daily_Return = np.min(rtn_array)
    
    #Max Drawdown 
    df_max_dd = pd.DataFrame(Cumulative_Pnl+1,columns=['Rtn'])
    df_max_dd['max_pnl']=df_max_dd.rolling(10).max()
    df_max_dd['drawdown']=df_max_dd.max_pnl-df_max_dd.Rtn
    Max_Drawdown = np.nanmax(df_max_dd.drawdown)
    
    #Volatility of daily return 
    Volatility = np.std(rtn_array)*np.sqrt(250)
    
    #Skewness and Kurtosis
    Skewness = skew(rtn_array)
    Kurtosis = kurtosis(rtn_array)
    
    #Modified_VaR
    g = (0.95+Skewness*(0.95**2-1)/6+Kurtosis*(0.95**3-3*0.95)/24-Skewness**2*(0.95**3*2-5*0.95)/36)
    Modified_VaR=( Daily_Mean_Arith+g*Volatility)
    
    #Conditional_VaR 
    Conditional_VaR = - np.mean(np.sort(rtn_array)[:int(0.05*len(rtn_array))])*np.sqrt(250)
    
    #sharp_ration 
    #risk_free=pd.read_csv('risk_free.csv',index_col=0).dropna()
    #risk_free.index=pd.to_datetime(risk_free.index)
    #risk_free_mu=risk_free.mean()[0]
    risk_free_mu=0.01
    
    
    Sharpe_Ratio = (Daily_Mean_Arith-risk_free_mu)/Volatility
    
    rst = {'Cumulative_Return':Cumulative_Return,
                  'Daily_Mean_Arith':Daily_Mean_Arith,
                  'Daily_Mean_Geom':Daily_Mean_Geom,
                  'Max_Drawdown':Max_Drawdown,
                  'Volatility':Volatility,
                  'Skewness':Skewness,
                  'Kurtosis':Kurtosis,
                  'Modified_Var':Modified_VaR,
                  'Conditional_VaR':Conditional_VaR,
                  'Sharpe_Ratio':Sharpe_Ratio,
                  'Min_Daily_Return':Min_Daily_Return}
    
    return rst,fig1,fig2

