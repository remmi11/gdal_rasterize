import os

os.environ['PROJ_LIB'] = 'C:\\Program Files\\GDAL\\projlib'

# mySRS = 'EPSG:32617'
mySRS = 'EPSG:4326'
myValue = 'altitude'

def point_to_raster(shapefile):

    #gdal_cmd = "gdal_rasterize -a_nodata 0 -a %s -a_srs %s -ot INTEGER -tr 0.01 0.01 -l %s data/%s %s1.tif" 
    gdal_cmd = "gdal_rasterize -a_nodata 0 -burn 1 -a_srs %s -ot INTEGER -tr 0.01 0.01 -l %s data/%s %s1.tif" \
    % (mySRS, shapefile[:-4], shapefile, shapefile[:-4])
    os.system(gdal_cmd)


def main():
    files = [f for f in os.listdir('data') if f.endswith('.shp')]
    for _file in files:
        print (_file)
        point_to_raster(_file)


if __name__ == '__main__':
    main()