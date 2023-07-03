#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import img_transform as img_trans
import shp_transform as shp_trans

# /***************************/
# // MAIN
# /***************************/
if __name__ == "__main__":
    start_time = datetime.datetime.now()

    # Image coordinates transform
    # (1) Single File
    # read_path_str = "G:/geoserver_satellite_data/ndvi_wgs84/dancheng_DT_ZS_20230611.tif"
    # write_path_str = "G:/geoserver_satellite_data/ndvi_gcj02/dancheng_DT_ZS_20230611.tif"
    # img_trans.transform_imgfile(read_path_str, write_path_str, "wgs84", "gcj02")

    # (2) File Path
    # read_path_str = "G:/UAV_process/3wgs84"
    # write_path_str = "G:/UAV_process/4gcj02"
    # img_trans.transform_imgfile_batch(read_path_str, write_path_str, "wgs84", "gcj02")

    # Shp file coordinates transform
    # (1) Single File
    # read_path_str = 'F:/SHP/HeNan_DanCheng_Shp/Dancheng_LAD_wgs84.shp'
    # write_path_str = 'F:/SHP/HeNan_DanCheng_Shp/Dancheng_LAD_gcj02.shp'
    # shp_trans.transform_shpfile(read_path_str, write_path_str, "wgs84", "gcj02")

    # (2) File Path
    # read_path_str = r'G:\test\shp_wgs84'
    # write_path_str = r'G:\test\shp_gcj02'
    # shp_trans.transform_shpfile_batch(read_path_str, write_path_str, "wgs84", "gcj02")
    
    trans_dir = 'G:/geoserver_satellite_data/ndvi_gcj02'
    trans_crs = 'gcj02'
    filename = 'lingang_DT_ZS_20230702.tif'
    filepath = 'G:/geoserver_satellite_data/ndvi_wgs84/lingang_DT_ZS_20230702.tif'
    img_trans.trans_compress(trans_dir, trans_crs, filename, filepath)

    end_time = datetime.datetime.now()
    print("Elapsed Time:", end_time - start_time)  # 输出程序运行所需时间
