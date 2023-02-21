# -*- coding: utf-8 -*-

"""
Created on Feb Tue 21 2023
@author: 63482
env: py 3.9
"""
import geopandas as gpd
from cpami import Sewer_Schema as sewer
from cpami.work_ReplacePartOfSHP import *


# replace data base on cityid column
if False:
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
    

