#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from osgeo import gdal
    from osgeo import osr
except ImportError:
    import gdal
    import osr
import glob
import os


# 读入image
def read_img(filename):
    dataset = gdal.Open(filename)
    im_width = dataset.RasterXSize
    im_height = dataset.RasterYSize
    im_geotrans = dataset.GetGeoTransform()
    im_proj = dataset.GetProjection()
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)

    im_band = dataset.GetRasterBand(2)
    nodata = im_band.GetNoDataValue()
    im_data[im_data == nodata] = 0

    del dataset
    return im_proj, im_geotrans, im_data


# 写入image
def write_img(filename, im_proj, im_geotrans, im_data):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_Int16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    else:
        im_bands, (im_height, im_width) = 1, im_data.shape

    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)

    dataset.SetGeoTransform(im_geotrans)
    dataset.SetProjection(im_proj)

    if im_bands == 1:
        dataset.GetRasterBand(1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i + 1).WriteArray(im_data[i])

    del dataset


# 生成tfw和prj文件
def generate_tfw(file_path, gen_prj):
    src = gdal.Open(file_path)
    xform = src.GetGeoTransform()

    if gen_prj == 'prj':
        src_srs = osr.SpatialReference()
        src_srs.ImportFromWkt(src.GetProjection())
        src_srs.MorphToESRI()
        src_wkt = src_srs.ExportToWkt()

        prj = open(os.path.splitext(file_path)[0] + '.prj', 'wt')
        prj.write(src_wkt)
        prj.close()

    src = None
    edit1 = xform[0] + xform[1] / 2
    edit2 = xform[3] + xform[5] / 2

    tfw = open(os.path.splitext(file_path)[0] + '.tfw', 'wt')
    tfw.write("%0.14f\n" % xform[1])
    tfw.write("%0.14f\n" % xform[2])
    tfw.write("%0.14f\n" % xform[4])
    tfw.write("%0.14f\n" % xform[5])
    tfw.write("%0.14f\n" % edit1)
    tfw.write("%0.14f\n" % edit2)
    tfw.close()


# 删除tfw和prj文件
def delete_tfw(path):
    for infile in glob.glob(os.path.join(path, '*.tfw')):
        if os.path.isfile(infile):
            os.remove(infile)
    for infile in glob.glob(os.path.join(path, '*.prj')):
        if os.path.isfile(infile):
            os.remove(infile)


# 清空文件夹下文件
def del_file(path_data):
    for i in os.listdir(path_data):
        file_data = path_data + "\\" + i
        if os.path.isfile(file_data):
            os.remove(file_data)
        else:
            del_file(file_data)
