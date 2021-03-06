import os,sys,urllib2
from multiprocessing import Pool,cpu_count
from datetime import datetime

mapUrl = 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer'
tileDir = r'D:/coding/imagerytile'

def Download( extent ):
    #print extent
    currentLevel = extent[0]
    dire = tileDir+'/_alllayers/L{0}/'.format(str(currentLevel).zfill(2))
    x=extent[1]
    startY=extent[2]
    endY=extent[3]
    Rdire = dire + 'R' + hex(x).split('x')[1].zfill(8)
    os.makedirs(Rdire)
    for y in range(startY,endY+1):
        trytimes=3
        for i in range(trytimes):
            Cdire = Rdire + r'/' + 'C' + '{0}.jpg'.format(hex(y).split('x')[1].zfill(8))
            try:
                response = urllib2.urlopen(mapUrl+'/tile'+'/{0}/{1}/{2}'.format(currentLevel,x,y),timeout=3)
                img=response.read()
                with open(Cdire,'wb') as f:
                    f.write(img)
                break
            except Exception as e:
                #print str(e) +':'+ Cdire
                continue


if __name__ == '__main__':
    if len(sys.argv) == 7:
        startLevel = int(sys.argv[1])
        endLevel = int(sys.argv[2])
        startX = int(sys.argv[3])
        startY = int(sys.argv[4])
        endX = int(sys.argv[5])
        endY = int(sys.argv[6])

        time1=datetime.now()
		
        for level in range(startLevel,endLevel+1):
            currentLevel = level
            GPpool = Pool(16)
            GPpool.map_async(Download, [[currentLevel,x,startY,endY] for x in range(startX,endX+1)])
            GPpool.close()
            GPpool.join()
            print 'Level {0} is complete.'.format(currentLevel)
            startX = startX*2
            startY = startY*2
            endX = endX*2+1
            endY = endY*2+1

        time2=datetime.now()
        print time2-time1
			
#Usage:
#python downloadMap.py startlevel endlevel startx starty endx endy

#Example:
#python downloadMap.py 0 4 0 0 0 0
#python downloadMap.py 8 16 54848 102528 55103 102912
