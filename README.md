# EsriTiledMapDownloader

## 简介
高速下载ArcGIS Server制作的切片地图。

## 用途
* 部署至Web服务器（或GIS服务器）进行离线调用。
* 配合服务对应的切片方案在ArcMap中进行浏览，示例见imagerytile文件夹。

## 运行环境
此脚本在python 2.7.16版本下开发运行，未在其他版本做过测试。

## 注意事项
用于商业用途时，请遵守相应的法律法规。

## Usage
### 下载地图
* python downloadMap.py startlevel endlevel startx starty endx endy
### 补充下载地图时可能因网络不稳定或其他原因未能下载完全的切片
* python completeMissingTiles.py startlevel endlevel startx starty endx endy

## Example
* python downloadMap.py 0 4 0 0 0 0
* python downloadMap.py 8 16 54848 102528 55103 102912
* python completeMissingTiles.py 0 4 0 0 0 0