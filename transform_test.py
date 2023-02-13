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
    read_path_str = "G:/test/wgs84/20230120T023019_20230120T023711_T51RUQ.tif"
    write_path_str = "G:/test/gcj02/img_transform.tif"
    img_trans.transform_imgfile(read_path_str, write_path_str, "wgs84", "gcj02")

    # (2) File Path
    read_path_str = "G:/test/wgs84"
    write_path_str = "G:/test/gcj02"
    img_trans.transform_imgfile_batch(read_path_str, write_path_str, "wgs84", "gcj02")

    # Shp file coordinates transform
    # (1) Single File
    read_path_str = r'G:\test\shp_wgs84\lingang_field_wgs84.shp'
    write_path_str = r'G:\test\shp_gcj02\shp_transform.shp'
    shp_trans.transform_shpfile(read_path_str, write_path_str, "wgs84", "gcj02")

    # (2) File Path
    read_path_str = r'G:\test\shp_wgs84'
    write_path_str = r'G:\test\shp_gcj02'
    shp_trans.transform_shpfile_batch(read_path_str, write_path_str, "wgs84", "gcj02")

    end_time = datetime.datetime.now()
    print("Elapsed Time:", end_time - start_time)  # 输出程序运行所需时间
