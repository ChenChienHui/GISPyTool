# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:18:30 2022
@author: 63482

set schema for cpami(10207) sewer
"""
from collections import OrderedDict
"""
str
date
float:10.2
str:255
"""

# ================================================================================
# 污水設計管線 804010102
SCHEMA804010102 = {"geometry": "3D LineString",
          "properties":OrderedDict({"PI_NUM":"str:50", 
                                    "US_MH":"str:50",
                                    "DS_MH": "str:50",
                                    "SEW_CAT":"str:10",
                                    "PI_TYP":"str:10",
                                    "PI_LENG":"float:6.2", 
                                    "PI_MAT":"str",
                                    "PI_CAT":"str:10",
                                    "PI_INR":"str:10",
                                    "PI_LIF": "int",
                                    "DIA": "int",
                                    "PI_THICK":"int",
                                    "SLOP":"float",
                                    "US_BLE":"float:6.2",
                                    "DS_BLE":"float:6.2",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }  

# 污水設計人孔 804010202
SCHEMA804010202 = {"geometry": "3D Point",
          "properties":OrderedDict({"MH_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "MH_TYP":"str:10",
                                    "MH_TYPE":"str:10",
                                    "MH_TLE":"float:6.2",
                                    "MH_DEP":"float:6.2",
                                    "MH_LENG":"int",
                                    "MH_WIDTH":"int",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }   

# 污水竣工管線 804010103
SCHEMA804010103 = {"geometry": "3D LineString",
          "properties":OrderedDict({"PI_NUM":"str:50",
                                    "US_MH":"str:50",
                                    "DS_MH":"str:50",
                                    "SEW_CAT":"str:10",
                                    "PI_TYP":"str:10",
                                    "PI_LENG":"float:6.2",
                                    "PI_MAT":"str",
                                    "PI_CAT":"str:10",
                                    "PI_CURV":"str:10",
                                    "PI_INR":"str:10",
                                    "PI_LIF":"int",
                                    "DIA":"int",
                                    "PI_THICK":"int",
                                    "SLOP":"int",
                                    "US_BLE":"float:6.2",
                                    "DS_BLE":"float:6.2",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }

# 污水竣工人孔 804010203
SCHEMA804010203 = {"geometry": "3D Point",
          "properties":OrderedDict({"MH_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "MH_CLASS":"str:10",
                                    "MH_TYP":"str:10",
                                    "MH_TLE":"float:6.2",
                                    "MH_DEP":"float:6.2",
                                    "MH_LENG":"int",
                                    "MH_WIDTH":"int",
                                    "MH_GRD":"int",
                                    "MH_GRD_DEP":"int",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "PIC":"str:100",
                                    "MH_EXVIEW":"str:100",
                                    "MH_MARK":"str:100",
                                    "NOTE":"str",
                                    "Theta":"int",
                                    "TR_WID":"int",
                                    "TR_HGT":"int",
                                    "TH_HGT":"int",
                                    "TH_MDiA":"int",
                                    "AP_HGT":"int",
                                    "BPBS_HGT":"int",
                                    "BB_IDiA":"int",
                                    "BB_ODiA":"int"
                                    })
          }   

# 巷道連接管 804010104
SCHEMA804010104 = {"geometry": "3D LineString",
          "properties":OrderedDict({"CPI_NUM":"str:50",
                                    "US_CB":"str:50",
                                    "DS_CB":"str:50",
                                    "PI_TYP":"str:10",
                                    "PI_MAT":"str",
                                    "PI_CAT":"str:10",
                                    "PI_INR":"str:10",
                                    "PI_LIF":"int",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "DIA":"int",
                                    "PI_LENG":"float:8.2",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }

# 陰井 804010204
SCHEMA804010204 = {"geometry": "3D Point",
          "properties":OrderedDict({"CB_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "DS_CB_NUM":"str:50",
                                    "CB_TYP":"str:10",
                                    "G_LE":"float:6.2",
                                    "CB_DEP":"float:6.2",
                                    "CB_WID":"int",
                                    "CB_LENG":"int",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }   

# 污水抽(揚)水站(井) 804010301
SCHEMA804010301 = {"geometry": "3D Point",
          "properties":OrderedDict({"PUMP_NAME":"str",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "ADD":"str",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "STAFF":"str:50",
                                    "STAFF_TEL":"str:50",
                                    "TPUMP_VOL":"float:9.2",
                                    "MACHINE":"int",
                                    "POWER":"int",
                                    "GRD_ELEV":"float:7.3",
                                    "IN_ELEV":"float:7.3",
                                    "WELL_H":"float:7.3",
                                    "OUT_ELEV":"float:7.3",
                                    "START_WL":"float:7.3",
                                    "STOP_WL":"float:7.3",
                                    "METHOD":"str:10",
                                    "PIMH_ID":"str:50",
                                    "NOTE":"str"
                                    })
          } 

# 截流站\井設施 804010302
SCHEMA804010302 = {"geometry": "3D Point",
          "properties":OrderedDict({"PUMP_NAME":"str",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "ADD":"str",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "STAFF":"str:50",
                                    "STAFF_TEL":"str:50",
                                    "VOLUME":"int",
                                    "METHOD":"str:10",
                                    "PIMH_ID":"str:50",
                                    "NOTE":"str"
                                    })
          } 

# 用戶接管資料 804010508
SCHEMA804010508 = {"geometry": "3D Point",
          "properties":OrderedDict({"CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "DIST":"str:20",
                                    "VILLAGE":"str:20",
                                    "ROAD":"str:50",
                                    "LANE":"str:20",
                                    "ALLEY":"str:20",
                                    "NUM":"str:10",
                                    "FLOOR":"str:10",
                                    "OF":"str:10",
                                    "BD_USAGE":"str:10",
                                    "BD_FLOW":"str:50",
                                    "FLOORS":"str:10",
                                    "HOUSEHOLDS":"str:10",
                                    "CARD_NUM":"str:50",
                                    "CARD":"str",
                                    "BD_NAME":"str",
                                    "WATER_NUM":"str:100",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "CB_NUM":"str:10",
                                    "BD_NUM":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          } 

# ================================================================================
# 雨水規劃管線 804020101
SCHEMA804020101 = {"geometry": "3D LineString",
          "properties":OrderedDict({"SSEW_CAT":"str:10",
                                    "PI_NUM":"str:50",
                                    "US_MH":"str:50",
                                    "DS_MH":"str:50",
                                    "PI_TYP":"str:10",
                                    "PI_WID":"float:4.2", 
                                    "PI_HEI":"float:4.2", 
                                    "PI_LENG":"float:6.2", 
                                    "ROAD_WID":"float:4.2", 
                                    "PI_MAT":"str",
                                    "PI_THICK":"int", 
                                    "PI_SLOP":"float:6.5", 
                                    "DES_FLOW":"float:9.2", 
                                    "DES_VELO":"float:9.2", 
                                    "US_BLE":"float:6.2", 
                                    "DS_BLE":"float:6.2", 
                                    "CATCH_NUM":"str:100",
                                    "KEYIN_DATE":"str:10",
                                    "PLAN_ID":"str:100",
                                    "NOTE":"str"
                                    })
          }  

# 雨水規劃人孔 804020201
SCHEMA804020201 = {"geometry": "3D Point",
          "properties":OrderedDict({"MH_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "ROAD_NAME":"str:100",
                                    "MH_DEP":"float:4.2", 
                                    "MH_TYP":"str:10",
                                    "MH_LENG":"int", 
                                    "MH_WIDTH":"int", 
                                    "FALL_MAX":"float:6.2", 
                                    "MH_TLE":"float:6.2", 
                                    "KEYIN_DATE":"str:10",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "PLAN_ID":"str",
                                    "NOTE":"str"
                                    })
          }   

#雨水竣工管線 804020102
SCHEMA804020102 = {"geometry": "3D LineString",
          "properties":OrderedDict({"SSEW_CAT":"str:10",
                                    "PI_NUM":"str:50",
                                    "US_MH":"str:50",
                                    "DS_MH":"str:50",
                                    "PI_TYP":"str:10",
                                    "PI_WIDT":"float:4.2", 
                                    "PI_WIDB":"float:4.2", 
                                    "PI_HEI":"float:4.2", 
                                    "PI_LENG":"float:6.2", 
                                    "PI_MAT":"str",
                                    "PI_THICK":"int", 
                                    "PI_SLOP":"float:6.2",
                                    "DES_FLOW":"float:9.2", 
                                    "DES_VELO":"float:9.2", 
                                    "US_BLE":"float:6.2", 
                                    "DS_BLE":"float:6.2", 
                                    "CATCH_NUM":"str:100",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_DEPT":"str",
                                    "CONS_NAME":"str:100",
                                    "CONS_DATE":"str:10",
                                    "KEYIN_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }  

# 雨水竣工人孔 804020202
SCHEMA804020202 = {"geometry": "3D Point",
          "properties":OrderedDict({"MH_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "ROAD_NAME":"str:100",
                                    "MH_DEP":"float:4.2", 
                                    "MH_TYP":"str:10",
                                    "MH_LENG":"int", 
                                    "MH_WIDTH":"int", 
                                    "ROAD_WID":"float:4.2", 
                                    "FALL_MAX":"float:6.2", 
                                    "MH_TLE":"float:6.2", 
                                    "CONS_DATE":"str:10",
                                    "MH_GRD":"int",
                                    "MH_GRD_DEP":"int",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "CONS_ID":"str:50",
                                    "CONS_TIT":"str",
                                    "CONS_DEPT":"str:100",
                                    "CONS_NAME":"str:100",
                                    "KEYIN_DATE":"str:10",
                                    "MH_PIC":"str:100",
                                    "MH_EXVIEW":"str:100",
                                    "MH_MARK":"str:100",
                                    "NOTE":"str",
                                    "Theta":"int", 
                                    "Model":"int",
                                    "MHN_TYP":"str:10",
                                    "MHN_LENG":"int", 
                                    "MHN_WID":"int", 
                                    "BH_LENG":"int",
                                    "BH_WID":"int",
                                    "BH_HGT":"int"
                                    })
          }   

#連接管 804020103
SCHEMA804020103 = {"geometry": "3D LineString",
          "properties":OrderedDict({"CPI_NUM":"str:50",
                                    "IN_MHNUM":"str:50",
                                    "IN_PINUM":"str:50",
                                    "CPI_WID":"float:4.2", 
                                    "CPI_HEI":"float:4.2", 
                                    "CPI_LENG":"float:4.2", 
                                    "PI_MAT":"str",
                                    "US_BLE":"float:6.2",
                                    "IN_TDIS":"float:6.2",
                                    "CONS_ID":"str:50",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "NOTE":"str"
                                    })
          }  

# 集水井 804020204
SCHEMA804020204 = {"geometry": "3D Point",
          "properties":OrderedDict({"CP_NUM":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "CP_BLE":"float:6.2",
                                    "CP_DEP":"float:4.2",
                                    "CP_LENG":"int",
                                    "CP_WID":"int",
                                    "IN_CPNUM":"str:50",
                                    "CONS_ID":"str:50",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "NOTE":"str"
                                    })
          }   

#抽水站設施 804020302
SCHEMA804020302 = {"geometry": "3D Point",
          "properties":OrderedDict({"PUMP_NAME":"str:100",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "CATCH_NUM":"str:50",
                                    "CATCH_AREA":"float:9.2",
                                    "PRO_AREA":"float:9.2",
                                    "TPUMP_VOL":"float:9.2",
                                    "TPUMP_NUM":"str:50",
                                    "TYPH_VOL":"float:9.2",
                                    "STORM_VOL":"float:9.2",
                                    "WARN_WL":"float:9.2",
                                    "START_WL":"float:9.2",
                                    "STOP_WL":"float:9.2",
                                    "TDES_HEAD":"float:9.2",
                                    "PW_TLE":"float:9.2",
                                    "PUMP_CUR":"str",
                                    "OUT_LE":"float:9.2",
                                    "COUT_LE":"float:9.2",
                                    "DES_RWL":"float:9.2",
                                    "GROUND_LE":"float:9.2",
                                    "TIDE_LE":"float:9.2",
                                    "BANK_LE":"float:9.2",
                                    "BANK_NAME":"str:100",
                                    "RIVER":"str:100",
                                    "SET_DATE":"str:10",
                                    "PICS":"str:100",
                                    "CROSS_SEC":"str:100",
                                    "LONG_SEC":"str:100",
                                    "ADD":"str",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10",
                                    "STAFF":"str:50",
                                    "STAFF_TEL":"str:50",
                                    "GATE_NUM":"str:50",
                                    "NOTE":"str"
                                    })
          }   

# 大排水分區 804020401
SCHEMA804020401 = {"geometry": "3D Polygon",
          "properties":OrderedDict({"CATCH_NUM":"str:50",
                                    "CATCH_NAME":"str:100",
                                    "CATCH_AREA":"float:9.2",
                                    "CATCH_SLOP":"float:6.5",
                                    "CATCH_RIV":"str:100",
                                    "CATCH_SRT":"float:9.2",
                                    "DES_FORM":"str",
                                    "CITY_ID":"str:10",
                                    "TOWN_ID":"str:10"
                                    })
          }   

# 貯留設施/滯洪池 804020501
SCHEMA804020501 = {"geometry": "3D Point",
          "properties":OrderedDict({"DTP_NAME":"str:100",
                                    "CATCH_NAME":"str:50",
                                    "X":"float:9.3",
                                    "Y":"float:10.3",
                                    "DTP_AREA":"float:6.2",
                                    "DTP_VOL":"float:6.2",
                                    "DTP_DEP":"float:6.2",
                                    "IN_LE":"float:6.2",
                                    "OUT_LE":"float:6.2",
                                    "IPI_NAME":"str:100",
                                    "OPI_NAME":"str:100",
                                    "OUT_TYPE":"str:100",
                                    "BLE":"float:6.2",
                                    "MAX_WL":"float:6.2",
                                    "PUMP_NAME":"str:100"
                                    })
          }   

# 雨水側溝 804020601
SCHEMA804020601 = {"geometry": "3D LineString",
          "properties":OrderedDict({"SPI_TYP":"str:10",
                                    "SPI_NUM":"str:50",
                                    "STR_X":"float:9.3",
                                    "STR_Y":"float:10.3",
                                    "STR_LE":"float:6.2",
                                    "END_X":"float:9.3",
                                    "END_Y":"float:10.3",
                                    "END_LE":"float:6.2",
                                    "STR_DEP":"int",
                                    "END_DEP":"int",
                                    "STR_WID":"int",
                                    "END_WID":"int",
                                    "LENG":"float:5.2",
                                    "SLOP":"float:6.5",
                                    "CATCH_NUM":"str:100",
                                    "KEYIN_DATE":"str:10",
                                    "CONS_DATE":"str:10",
                                    "NOTE":"str"
                                    })
          }  
