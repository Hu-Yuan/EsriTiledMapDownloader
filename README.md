# EsriTiledMapDownloader

用于下载ArcGIS Server制作的切片地图。

下载完成后可部署至Web服务器（或GIS服务器）进行离线调用，或者配合服务对应的切片方案在ArcMap中进行浏览。

#Usage:
python downloadmap.py startlevel endlevel startx starty endx endy

#Example:
python downloadmap.py 0 4 0 0 0 0
python downloadmap.py 8 16 54848 102528 55103 102912