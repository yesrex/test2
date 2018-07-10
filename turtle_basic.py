# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:38:07 2018

@author: user
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
GC1 = pd.read_csv('GC1_Comdty.csv', sep='\t', index_col=0, dtype={'PX_LAST':np.float64, 'Date':str})
GC1 = GC1.reindex(index=GC1.index[::-1])
GC1.plot()

StopLoss = 0.07
GC1['high20'] = GC1.PX_LAST.rolling(20).max()
GC1['low20'] = GC1.PX_LAST.rolling(20).min()
GC1['high10'] = GC1.PX_LAST.rolling(10).max()
GC1['low10'] = GC1.PX_LAST.rolling(10).min()
GC1.PX_LAST = GC1.PX_LAST.shift(-1)
GC1.dropna(inplace=True)

Ret = []
Entries = []


for date in range(len(GC1)):
    if GC1.PX_LAST.iloc[date] > GC1.high20.iloc[date]:
        Entries.append(GC1.high20.iloc[date])
        stop = GC1.high20.iloc[date]*(1-StopLoss)
        pos = 'long'
    if GC1.PX_LAST.iloc[date] < GC1.low20.iloc[date]:
        Entries.append(GC1.low20.iloc[date])
        stop = GC1.low20.iloc[date]*(1+StopLoss)
        pos = 'short'
        
    if pos == 'long':
        if GC1.PX_LAST.iloc[date] < GC1.low10.iloc[date]:
            for entry in Entries:
                Ret.append( (GC1.low10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] < stop:
             for entry in Entries:
                Ret.append( (stop - entry)/entry )
             Entries.clear()
            
    elif pos == 'short':
        if GC1.PX_LAST.iloc[date] > GC1.high10.iloc[date]:
            for entry in Entries:
                Ret.append( -(GC1.high10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] > stop:
             for entry in Entries:
                Ret.append( -(stop - entry)/entry )
             Entries.clear()    
             
################################################# 
GC1 = pd.read_csv('GC1_Comdty.csv', sep='\t', index_col=0, dtype={'PX_LAST':np.float64, 'Date':str})
GC1 = GC1.reindex(index=GC1.index[::-1])
GC1.plot()

StopLoss = 0.07
GC1['high20'] = GC1.PX_LAST.rolling(55).max()
GC1['low20'] = GC1.PX_LAST.rolling(55).min()
GC1['high10'] = GC1.PX_LAST.rolling(20).max()
GC1['low10'] = GC1.PX_LAST.rolling(20).min()
GC1.PX_LAST = GC1.PX_LAST.shift(-1)
GC1.dropna(inplace=True)

Ret2 = []
Entries = []


for date in range(len(GC1)):
    if GC1.PX_LAST.iloc[date] > GC1.high20.iloc[date]:
        Entries.append(GC1.high20.iloc[date])
        stop = GC1.high20.iloc[date]*(1-StopLoss)
        pos = 'long'
    if GC1.PX_LAST.iloc[date] < GC1.low20.iloc[date]:
        Entries.append(GC1.low20.iloc[date])
        stop = GC1.low20.iloc[date]*(1+StopLoss)
        pos = 'short'
        
    if pos == 'long':
        if GC1.PX_LAST.iloc[date] < GC1.low10.iloc[date]:
            for entry in Entries:
                Ret2.append( (GC1.low10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] < stop:
             for entry in Entries:
                Ret2.append( (stop - entry)/entry )
             Entries.clear()
            
    elif pos == 'short':
        if GC1.PX_LAST.iloc[date] > GC1.high10.iloc[date]:
            for entry in Entries:
                Ret2.append( -(GC1.high10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] > stop:
             for entry in Entries:
                Ret2.append( -(stop - entry)/entry )
             Entries.clear()    

################################################# 
GC1 = pd.read_csv('GC1_Comdty.csv', sep='\t', index_col=0, dtype={'PX_LAST':np.float64, 'Date':str})
GC1 = GC1.reindex(index=GC1.index[::-1])
GC1.plot()

StopLoss = 0.07
GC1['high20'] = GC1.PX_LAST.rolling(10).max()
GC1['low20'] = GC1.PX_LAST.rolling(10).min()
GC1['high10'] = GC1.PX_LAST.rolling(5).max()
GC1['low10'] = GC1.PX_LAST.rolling(5).min()
GC1.PX_LAST = GC1.PX_LAST.shift(-1)
GC1.dropna(inplace=True)

Ret3 = []
Entries = []


for date in range(len(GC1)):
    if GC1.PX_LAST.iloc[date] > GC1.high20.iloc[date]:
        Entries.append(GC1.high20.iloc[date])
        stop = GC1.high20.iloc[date]*(1-StopLoss)
        pos = 'long'
    if GC1.PX_LAST.iloc[date] < GC1.low20.iloc[date]:
        Entries.append(GC1.low20.iloc[date])
        stop = GC1.low20.iloc[date]*(1+StopLoss)
        pos = 'short'
        
    if pos == 'long':
        if GC1.PX_LAST.iloc[date] < GC1.low10.iloc[date]:
            for entry in Entries:
                Ret3.append( (GC1.low10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] < stop:
             for entry in Entries:
                Ret3.append( (stop - entry)/entry )
             Entries.clear()
            
    elif pos == 'short':
        if GC1.PX_LAST.iloc[date] > GC1.high10.iloc[date]:
            for entry in Entries:
                Ret3.append( -(GC1.high10.iloc[date] - entry)/entry )
            Entries.clear()
        if GC1.PX_LAST.iloc[date] > stop:
             for entry in Entries:
                Ret3.append( -(stop - entry)/entry )
             Entries.clear()    
  

  