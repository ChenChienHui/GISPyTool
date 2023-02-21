# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:04:29 2022

@author: 63482

version: 3.7
"""
import datetime
import geopandas as gpd
import pandas as pd
import numpy as np
import fiona
import os

from shapely.geometry import mapping, shape, Point, LineString, Polygon, MultiLineString

def SHPorGDB_2DPoint_to3DShp(_path, _zcolumn, _layername = ""):
    ''' GDB 必須給 layer name , SHP 可不給(同檔名)'''      
    if _path.split(".")[-1] == "shp":
        _layername = fiona.listlayers(_path)[0]
        print('Convert 2D point to 3D : {}.shp'.format(_layername) )    
    else:
        print('Convert 2D point to 3D : (GDB) {}'.format(_layername))
    
    # creat result path
    outpath = _path.split('.')[0] + '_convert3D'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    
    savename = outpath + '\\{}.shp'.format(_layername)   
    with fiona.open(_path, layer = _layername, encoding = 'utf-8' ) as source:
        # shpfile can not support 'datetime' column type ---> so convert to 'str'
        for ty in source.schema['properties']:
            if source.schema['properties'][ty] =='datetime':
                source.schema['properties'][ty] = 'str:100'
        # convert 2D to 3D
        source.schema['geometry'] = '3D Point'
        # wtite shp
        with fiona.open(savename, 'w', driver='ESRI Shapefile', crs=source.crs,
                            schema = source.schema,encoding = 'utf-8') as ouput:
            for elem in source:
                x, y = elem['geometry']['coordinates']
                z = elem['properties'][_zcolumn]
                elem['geometry']['coordinates'] = (x,y,z)
                
                ouput.write({'geometry':elem['geometry'], 'properties':elem['properties']}) 
    return savename

def SHPorGDB_2DLine_to3DShp(_path, _z1column, _z2column, _layername = ""):
    '''
    ckeck mutiline & convert2D to 3D
    GDB 必須給 layer name , SHP 可不給(同檔名)'''      
    if _path.split(".")[-1] == "shp":
        _layername = fiona.listlayers(_path)[0]
        print('Convert 2D line to 3D : {}.shp'.format(_layername) )    
    else:
        print('Convert 2D linne to 3D : (GDB) {}'.format(_layername))
    
    
    # creat result path
    outpath = _path.split('.')[0] + '_convert3D'
    if not os.path.exists(outpath):
        os.makedirs(outpath)

    savename = outpath + '\\{}.shp'.format(_layername)   
    with fiona.open(_path, layer = _layername, encoding = 'utf-8' ) as source:
        # shpfile can not support 'datetime' column type ---> so convert to 'str'
        for ty in source.schema['properties']:
            if source.schema['properties'][ty] =='datetime':
                source.schema['properties'][ty] = 'str:100' ###        
        # convert 2D to 3D
        source.schema['geometry'] = '3D LineString'   
                 
        df = gpd.read_file(_path)
        with fiona.open(savename, 'w', driver='ESRI Shapefile', crs=source.crs,
                            schema = source.schema,encoding = 'utf-8') as ouput:            
            # iter each line
            for n, elem in enumerate(source):       
                alldist = float(df[n:n+1].length)
            
                # after modify all line to single 
                # -> find line type is mutiline -> modify to single
                if elem['geometry']['type'] == 'MultiLineString': 
                    elem['geometry']['type'] = 'LineString'
                    elem['geometry']['coordinates'] = elem['geometry']['coordinates'][0]
                # type is singleline
                else:
                    pass
                
                # get z
                z1, z2 = float(elem['properties'][_z1column]), float(elem['properties'][_z2column])
                # first point
                x1, y1 = elem['geometry']['coordinates'][0]
                elem['geometry']['coordinates'][0] = (x1, y1, z1)  
                # other point
                datumn = float(z1)
                for pn in range(len(elem['geometry']['coordinates'])-1):
                    x1, y1, ztemp = elem['geometry']['coordinates'][pn]
                    x2, y2 = elem['geometry']['coordinates'][pn+1]
                    
                    dist = np.sqrt( (x1-x2)**2 + (y1-y2)**2)

                    zz = datumn + (z2-z1)*(dist/alldist)
                    elem['geometry']['coordinates'][pn+1] = (x2, y2, zz)
                    
                    datumn = zz                          
                # write
                ouput.write({'geometry':elem['geometry'], 'properties':elem['properties']})
    return savename

def Line_3Dto3D(_SHPpath, _layername, _z1column, _z2column):
    '''convert3D to 3D'''
    print('Convert to 3D : {} (line)'.format(_layername) )

    savename = _SHPpath.split(".")[0] + '_update3D.shp'
    with fiona.open(_SHPpath, layer = _layername, encoding = 'utf-8' ) as source:
        # shpfile can not support 'datetime' column type ---> so convert to 'str'
        for ty in source.schema['properties']:
            if source.schema['properties'][ty] =='datetime':
                source.schema['properties'][ty] = 'str:100' ###        
        # convert 2D to 3D
        source.schema['geometry'] = '3D LineString'   
                 
        df = gpd.read_file(_SHPpath, layer = _layername)
        with fiona.open(savename, 'w', driver='ESRI Shapefile', crs=source.crs,
                            schema = source.schema,encoding = 'utf-8') as ouput:            
            # iter each line
            for n, elem in enumerate(source):       
                alldist = float(df[n:n+1].length)
            
                # after modify all line to single 
                # -> find line type is mutiline -> modify to single
                if elem['geometry']['type'] == 'MultiLineString': 
                    elem['geometry']['type'] = 'LineString'
                    elem['geometry']['coordinates'] = elem['geometry']['coordinates'][0]
                # type is singleline
                else:
                    pass
                
                # get z
                z1, z2 = elem['properties'][_z1column] or 0, elem['properties'][_z2column] or 0
                # first point
                x1, y1, z = elem['geometry']['coordinates'][0]
                elem['geometry']['coordinates'][0] = (x1, y1, z1)  
                # other point
                datumn = float(z1)
                for pn in range(len(elem['geometry']['coordinates'])-1):
                    x1, y1, ztemp = elem['geometry']['coordinates'][pn]
                    x2, y2, ztemp2 = elem['geometry']['coordinates'][pn+1]
                    
                    dist = np.sqrt( (x1-x2)**2 + (y1-y2)**2)
                    zz = datumn + (z2-z1)*(dist/alldist)
                    elem['geometry']['coordinates'][pn+1] = (x2, y2, zz)
                    
                    datumn = zz                          
                # write
                ouput.write({'geometry':elem['geometry'], 'properties':elem['properties']})
    return savename

def Check_GDB_Or_SHP_MutiLine(_path, _layername = ""):    
    ''' GDB 必須給 layer name , SHP 可不給(同檔名)'''      
    if _path.split(".")[-1] == "shp":
        _layername = fiona.listlayers(_path)[0]
        print('Check MutiLine : {}.shp'.format(_layername) )    
    else:
        print('Check MutiLine : (GDB) {} '.format(_layername) )
    
    with fiona.open(_path, layer = _layername, encoding = 'utf-8' ) as source:         
        # iter each line
        count = 0
        for n, elem in enumerate(source):
            # mutiline
            if elem['geometry']['type'] == 'MultiLineString' and len(elem['geometry']['coordinates']) != 1:
                print ('   --> MutiLine FID : {} '.format(n+1))
                count +=1
        if count == 0:
            print( '   -->  no mutiline')                
    return count