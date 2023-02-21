# -*- coding: utf-8 -*-
"""
Created on Fri May 21 08:31:30 2021

@author: 63482

env: py 3.7
"""

import fiona
import pandas as pd
import numpy as np
import geopandas as gpd
from cpami import Sewer_Schema as sewer

def ReplacePartOfSHP(TargetColum, TargetVal, Schema, BaseFile, OutPath, DfBase, DfNew, ColumnExcel, OldName, NewName ):
    #
    print(">>> 比對欄位名稱 ...")
    colconvert = pd.read_excel(ColumnExcel)
    RENAME = {}
    for i in range(len(colconvert)):
        if str(colconvert[NewName][i]) not in ['nan', '']:
            RENAME[colconvert[OldName][i]] = colconvert[NewName][i]
            
    dftp = DfNew.rename(columns = RENAME)

    # check lack column
    print(">>> 檢查欄位數量 ...")
    must = list(DfBase.columns)
    for c in must:
        if c not in dftp.columns:
            print("   -> 插入缺少欄位 : ",  c)
            dftp.insert(dftp.shape[1], c, None)

    # fill target column value of new data
    dftp[TargetColum] = TargetVal

    # get column for use of new data
    dfres = dftp[must]
    
    # cut data need to be delete from base data
    print(">>> 抽換資料 ...")
    dfans = DfBase[DfBase[TargetColum] != TargetVal]

    # add new data to base data
    df_finall = pd.concat([dfans,dfres], ignore_index = True)

    # SAVE
    df_finall.to_file(filename = OutPath + "\\" + BaseFile.split("\\")[-1].split(".")[0] + ".shp",
                      driver = 'ESRI Shapefile',
                      encoding = 'utf-8',
                      schema = Schema) 
    
    print(">>> 完成 ")
    return

if __name__ == "__main__":
    print(132)
    # imformation
    DEVICE_NUM = "804020102"
    TARGET_COLUMN = "CITY_ID" 
    TARGET_VALUE = "00065" #新北    
    SCHEMA = sewer.SCHEMA804020102
    
    # 成果路徑
    OUT_PATH = r'D:\04__Project_GIS\10207__普三_營建署連線\01_DATA_online\1_圖資\99_圖資整合20230112_抽換新北\TT'
    # 原始SHP
    BASE_FILE = r"D:\04__Project_GIS\10207__普三_營建署連線\01_DATA_online\1_圖資\99_圖資整合20230112_抽換新北\前版\Sewer_{}.shp".format(DEVICE_NUM)
    DF_BASE = gpd.read_file(BASE_FILE)
    # 抽換來源
    REPLACE_FILE = r'D:\04__Project_GIS\10207__普三_營建署連線\01_DATA_online\1_圖資\99_圖資整合20230112_抽換新北\新北提供\新北市雨污水圖資.gdb'
    GDBlayername = "雨水下水道調查管線"
    DF_NEW = gpd.read_file(REPLACE_FILE, layer=GDBlayername)
    # 欄位對照表
    COLUMN_EXCEL = r'D:\04__Project_GIS\10207__普三_營建署連線\01_DATA_online\1_圖資\99_圖資整合20230112_抽換新北\欄位對照表\F{}.xlsx'.format(DEVICE_NUM)
    SOURCE_COL_NAME = "欄位名稱_新北市"
    CECI_COL_NAME = "CECI對應欄位"
    
    # start 
    ReplacePartOfSHP(TARGET_COLUMN, TARGET_VALUE, SCHEMA, BASE_FILE, OUT_PATH, DF_BASE, DF_NEW, COLUMN_EXCEL, SOURCE_COL_NAME, CECI_COL_NAME)
    
