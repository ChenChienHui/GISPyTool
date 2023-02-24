# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:04:29 2022

@author: 63482

version: 3.7
"""

import numpy as np
from pyproj import CRS
from pyproj import Transformer
import json
import requests
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")


    
def ConvertXY(lonX, latY, FROM = 4326, TO = 3826 ):
    from_crs = CRS.from_epsg(FROM) 
    to_crs = CRS.from_epsg(TO) 
    
    transformer = Transformer.from_crs(from_crs,to_crs,always_xy=True)
    ans = transformer.transform(lonX, latY)
    
    if ans[0] == np.inf:
        return (0,0)
    else:
        return ans
    
def ConvertXYs(lonX, latY, FROM = 4326, TO = 3826 ):
    from_crs = CRS.from_epsg(FROM) 
    to_crs = CRS.from_epsg(TO) 
    
    transformer = Transformer.from_crs(from_crs,to_crs,always_xy=True)
    
    resX = []
    resY = []
    for x,y in zip(lonX, latY):        
        ans = transformer.transform(x, y)
        
        if ans[0] == np.inf:
            resX.append(0)
            resY.append(0)            
        else:
            resX.append(ans[0])
            resY.append(ans[1])   
    return resX, resY

def TGOS(ADDRESS, CRS, n = 1):
    '''
    4326 (WGS84)國際
    3825 (TWD97TM119)澎湖金馬
    3826 (TWD97TM121)台灣
    3827 (TWD67TM119)澎湖金馬
    3828 (TWD67TM121)台灣
    '''
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    
    URL = "https://addr.tgos.tw/addrws/v30/QueryAddr.asmx/QueryAddr"
    PARA = {"oAPPId":"prUmkAKkpXOHQsjalh1UYdO21ukzJANXNH8ePDPUMqhQY1Lr8XM+bA==",
        "oAPIKey":"cGEErDNy5yNr14zbsE/4GSfiGP5i3PuZ5b5X641QlCKckWKfmnwyromK3qE7q+mhDxebzUvIHoGFqGARSclldyBn9X321KuIhTEoq33IaOuc8dgsg5msBaOBfOjEb75CrGXEh92PNr5Nr36SWOUmpBgngQ0E4sOREdAzsibh9XXZJieacg5VGZ3+FbbOO848JT92pyuRECIg/2iaYzy0TXJb/Xeo1tCjhIZ9NNCe2oCNMA8zYQPnLTXjNqKytAmnbvwyhmtMDuYQhgYZ3UrbRCagOmpl0jv4yOWWEGOonxmHWio4ILH9zkuie4zmyRE6aNI+k8w81vqND1BZnI+WLJ6NkFCU5Rn7rzVzeqYmIgU7E0FMo8dfzCzJzIyiBuNSPH7JId2zNfWQtz0xI71dul/yWN/0/iEYq3SS0hJ0O5FVC8O0isJceOXmTWnZ2hEPJzS/5f0kxMMpo92FeFCdYMYM8Z1aUnKDfDVJcPzdaMA=",
        "oAddress": ADDRESS,
        "oSRS":"EPSG:" + str(CRS), # 4326(WGS84)國際, 3825(TWD97TM119)澎湖金馬,EPSG:3826(TWD97TM121)台灣,3827(TWD67TM119)澎湖金馬,3828(TWD67TM121)台灣
        "oFuzzyType":"2",   # 0:最近門牌號機制, 1:單雙號機制, 2:[最近門牌號機制]+[單雙號機制]
        "oResultDataType":"JSON",
        "oFuzzyBuffer":"0",  #模糊比對回傳門牌號的許可誤差範圍，輸入格式為正整數，0表不限制誤差範圍
        "oIsOnlyFullMatch":"false",
        "oIsLockCounty":"true",
        "oIsLockTown":"true",
        "oIsLockVillage":"false",
        "oIsLockRoadSection":"false",
        "oIsLockLane":"false",
        "oIsLockAlley":"false",
        "oIsLockArea":"false",
        "oIsSameNumber_SubNumber":"true",
        "oCanIgnoreVillage":"true",
        "oCanIgnoreNeighborhood":"true",
        "oReturnMaxCount": str(n) # 回傳資料筆數
        }

    HEADER = {"Content-Type": "application/x-www-form-urlencoded",
    "charset":"UTF-8"}

    response = requests.post(URL, 
                             data=PARA, 
                             verify=False,
                             headers=HEADER)

    # return list (can save multi data)
    return json.loads(BeautifulSoup(response.text).find_all("string")[0].text)['AddressList']


if __name__ == "__main__":
    # Convert
    res = ConvertXY(312074.901, 2773394.406, 3826, 4326)
    print(res)
    
    # TGOS
    Coor = TGOS("臺北市內湖區陽光接323號", 3826, n = 1) 
    X = Coor[0]["X"]
    Y = Coor[0]["Y"]
    
    