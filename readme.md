# Install Python and GDAL (1 time)

This is a Python (v3.7*) script for rasterizing shapefiles in a directory.

## Install Python 3.7 for Windows
Download the executable installer from [Python windows downloads](https://www.python.org/downloads/windows/). Then execute the installer. 
<img src="/images/python_windows.png" width="300" title="Proj4 link">

## Add the following items to 'path' variable in windows.
c:\python37;c:\python37\Scripts;c:\python37\Lib;

Click environmental variables |  Click Path and Append to existing values
:-------------------------:|:-------------------------:
<img src="/images/path1.png" width="300" title="Proj4 link"> | <img src="/images/path2.png" width="300" title="Proj4 link">


## Install gdal from [GIS Internals](https://www.gisinternals.com/query.html?content=filelist&file=release-1911-x64-gdal-2-4-4-mapserver-7-4-3.zip).
<img src="/images/gdal1.png" width="300" title="Proj4 link">

## Add the following gdal items to 'path' variable in windows.
C:\Program Files\GDAL;C:\Program Files\GDAL\gdal-data

# Execute script

## Place input shapefile in DATA folder.
1) Place shapefile in data folder (min 4 files: *.shp, *.dbf, *.shx, *.prj)

## Add variable values to script.
1) Take note of the EPSG code of the input data. If unknown can be found with the following gdal cmd. Adjusting file and layer name accordingly.
```bash
ogrinfo layer.shp layer -so 
``` 
<img src="/images/epsg.png" width="300" title="Proj4 link">
1) Set the mySRS variable to the EPSG code of the shapefile data (line 5 in script).

## Execute from cmd line.
1) Open cmd prompt.
2) 'cd' to project folder (ie. - cd c:\gdal_rasterize) 
3) Run script
```bash
python scripts\script.py
```