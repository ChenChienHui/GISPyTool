# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:42:51 2022

@author: 63482

version: 3.7
"""
import pyodbc
import numpy as np
import pandas as pd
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

class sqlTable:
    def __init__(self, SEVER , USER, PASSWORD, DATABASE, TABLE, DRIVER = '{ODBC Driver 17 for SQL Server}'):
        self.severname = SEVER
        self.username = USER
        self.password = PASSWORD
        self.dbname = DATABASE
        self.tablename = TABLE        
        
        '''
        DRIVER
        {ODBC Driver 11 for SQL Server} ---------SQL Server 2005 到 2014
        {ODBC Driver 13 for SQL Server} ---------SQL Server 2005 到 2016
        {ODBC Driver 13.1 for SQL Server} -------SQL Server 2008 到 2016
        {ODBC Driver 17 for SQL Server} ---------SQL Server 2008 到 2019（取決於次要版本）
        {ODBC Driver 18 for SQL Server} ---------SQL Server 2012 到 2019
        '''        
        connect_key = 'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(DRIVER,
                                                                             self.severname,
                                                                             self.dbname,
                                                                             self.username,
                                                                             self.password)
        self.dbcnxn = pyodbc.connect(connect_key)
        self.dbcursor = self.dbcnxn.cursor()
        return
    
    def getData_row_col_df(self):    
        ''' datatype : list( tuple )'''
        command = "SELECT * FROM {}.dbo.{}".format(self.dbname, self.tablename)
        self.dbcursor.execute(command)        
        
        rowdata = self.dbcursor.fetchall()
        column = np.array(rowdata[0].cursor_description)
        datadf = pd.DataFrame(np.array(rowdata), columns = column[:,0])   
        return rowdata, datadf, column
    
    def getDataByCondition_row_col_df(self, conditon, where = ""):    
        ''' datatype : list( tuple )
        
        select = "*, CONCAT([City], '巷', [Alley], '弄', [AdsNum]) AS [add]"
        where = "ApplyType='2'"
        rowdata, dftt, columninfo = cpc.getDataByCondition_row_col_df(select, where) 
        '''
        command = "SELECT {} FROM {}.dbo.{}".format(conditon, self.dbname, self.tablename)
        if where != "":
            command = command + " WHERE " + where
        print(command)
        self.dbcursor.execute(command)        
        
        rowdata = self.dbcursor.fetchall()
        column = np.array(rowdata[0].cursor_description)
        datadf = pd.DataFrame(np.array(rowdata), columns = column[:,0])   
        return rowdata, datadf, column

    def createTable(self,COLUMN_SET = ('數值	int NOT NULL,小數	numeric(12, 8) NOT NULL,最長字串	nvarchar(MAX),時間	datetime2(7)')):
        '''
        if table is exist
        delete it and recreate new one
        input column format (tuple)
            ('數值	int NOT NULL,'
             '小數	numeric(12, 8) NOT NULL,'
             '非零字串	nvarchar(50) NOT NULL,'
             '最長字串	nvarchar(MAX),'
             '字串	nvarchar(50),'
             '日期時間	datetime2(7),'
             '日期  date')
        '''
        try:
            command = 'DROP TABLE {}.dbo.{}'.format(self.dbname, self.tablename)
            self.dbcursor.execute(command) #exe
            self.dbcnxn.commit()
            
            print("Table[{}] already exist -> delete it and create new".format(self.tablename))
        except:
            pass

        command = "CREATE TABLE {}.dbo.{} ({})".format(self.dbname, self.tablename, COLUMN_SET)
        self.dbcursor.execute(command) #exe
        self.dbcnxn.commit()
        return

    def deleteTable(self):
        try:
            command = 'DROP TABLE {}.dbo.{}'.format(self.dbname, self.tablename)
            self.dbcursor.execute(command) #exe
            self.dbcnxn.commit()
            
            print("Already delete Table[{}] in Database[{}]".format(self.tablename, self.dbname))
        except:
            print("Can not find Table[{}] in Database[{}]".format(self.tablename, self.dbname))

        return

    def insert_single(self, ADDDATA):
        '''
        ADDDATA = dict(np.array( [ ['city',  'name',  'X',     'Y',   'id'], 
                                   ['00063', '臺北市', 999.366, 999.01, 11] ] ).T)   
        '''
        
        NEWCOLUMN = str(tuple(ADDDATA.keys())).replace("'",'')
        NEWVALUE = str(tuple(ADDDATA.values())).replace('None','NULL').replace("\'NULL\'",'NULL') # none datatime
        
        command = "INSERT INTO {}.dbo.{} {} VALUES {}".format(self.dbname, 
                                                              self.tablename, 
                                                              NEWCOLUMN, 
                                                              NEWVALUE)
        self.dbcursor.execute(command)
        self.dbcnxn.commit()
        return
    
    def insert_df(self, DATAFRAME):
        NEWCOLUMN = str(tuple(DATAFRAME.columns)).replace("'",'')
        print("Write input dataframe in ", self.tablename)
        progress = tqdm(total = len(DATAFRAME), position = 0, leave = True)
        for i,row in DATAFRAME.iterrows():
            NEWVALUE = (str(tuple(row))
                        .replace('None','NULL')
                        .replace("\'NULL\'",'NULL')
                        .replace("nan",'NULL')
                        .replace("' '",'NULL')
                        .replace("''",'NULL')
                        )
            command = "INSERT INTO {}.dbo.{} {} VALUES {}".format(self.dbname, 
                                                                  self.tablename, 
                                                                  NEWCOLUMN, 
                                                                  NEWVALUE)
            self.dbcursor.execute(command)
            
            progress.update(1)            
        progress.close()       
        
        self.dbcnxn.commit()             
        return
    
    def insert_geodata(self, PRIMARYVALUE, NEWCOLUMN, NEWVALUE, WKT, CRS):
        """
        Sample :
            NEWCOLUMN = ["OBJECTID", "City","X","Y"]
            NEWVALUE = [23,'測試',22222,33333]
            WKT = 'POINT (309509.909 2606266.02)'
            CRS = "3826"
        Note :
            INSERT INTO CPAMISewerSystem.dbo.A_TEST_PYTHONREAD (OBJECTID, City,Shape,X,Y)
            Values (23,'測試',geometry::STGeomFromText('POINT (309509.909 2606266.02)', 3825),22222,33333)
        """ 
        _NEWCOLUMN = "OBJECTID," + ",".join(NEWCOLUMN) + ",Shape"
        _VALUE = str(tuple([PRIMARYVALUE] + NEWVALUE))[:-1] + ",geometry::STGeomFromText('" + str(WKT) + "',"
        _CRS = str(int(CRS))
        command = ("INSERT INTO {}.dbo.{} ({}) Values {}").format(self.dbname, 
                                                                  self.tablename, 
                                                                  _NEWCOLUMN, 
                                                                  _VALUE + _CRS + "))")
        self.dbcursor.execute(command)
        self.dbcnxn.commit()
        return
    
    def closeWork(self):
        if self.dbcnxn != None:
            self.dbcnxn.close()        
        self.dbcnxn = None
        self.dbcursor = None


if __name__ == "__main__":
    SEVER = r'10.110.190.203\SQL2017EXPR'
    USER = 'cpamirs' 
    PASSWORD = r'b-7VY79BMAv.sL/\nkf)UCFkV' 
    DATABASE = 'CPAMISewerSystem' 
    TABLE = "DistrictAdministrative"

 #=============================================================================
 #    # read all table
 #=============================================================================
    #ResumeClass = sqlTable(SEVER , USER, PASSWORD, DATABASE, TABLE)
    #rowdata, df, columninfo = ResumeClass.getData_row_col_df()    
    #ResumeClass.closeWork()    
    
# =============================================================================
#     # read select table
# =============================================================================    
    # cpc = sqlTable(SEVER , USER, PASSWORD, DATABASE, TABLE)
    # select = "[SewerNo] ,[WaterNo], [City], [CityArea], [ApplyType],\
    #             CONCAT([City], [CityArea], [AreaLoad], [Village]) AS [add]"
    # rowdata, df, columninfo = cpc.getDataByCondition_row_col_df(select, where="ApplyType='1'")
    # cpc.closeWork()

# =============================================================================
#     # new table
# =============================================================================
    #NEWTABLE = "A新創資料表"
    #NEWCOLUMN =('CITY_ID	nvarchar(MAX) NOT NULL,'
    #            'Name	nvarchar(MAX) NOT NULL,'
    #            'WGS84_X	numeric(12, 6) NOT NULL,'
    #            'WGS84_Y	numeric(12, 6) NOT NULL,'
    #            'Zoom	int')    
    # new = sqlTable(SEVER , USER, PASSWORD, DATABASE, NEWTABLE)   
    # new.createTable(NEWCOLUMN)
    
    
    
# =============================================================================
#     # add single data
# =============================================================================
    # ADDDATA = dict(np.array(  [list( columninfo[:,0] ), 
    #                            list( ['00063', '臺北市', 999.366, 999.01, 11]  )] ).T)    
    # new.insert_single(ADDDATA)
  
    
    
# =============================================================================
#     # add many
# =============================================================================
    # df["WGS84_X"] = df["WGS84_X"].astype(float)
    # df["WGS84_Y"] = df["WGS84_Y"].astype(float)
    # new.insert_df(df)
    
    # new.closeWork() 
    
# =============================================================================
#     # use
# =============================================================================
    # a = 1
    # while True:
    #     try:
    #         PRIMARYVALUE = a
    #         NEWCOLUMN = ["City","X","Y"]
    #         NEWVALUE = ['測試' + str(a),123,123]
    #         WKT ='POINT (309509.909 2606266.02)'
    #         CRS = "3825"
            
    #         ResumeClass.insert_geodata(PRIMARYVALUE,NEWCOLUMN, NEWVALUE, WKT, CRS)
    #         break
    #     except:
    #         pass
    #     a += 1

