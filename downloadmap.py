import os,sys,urllib
from multiprocessing import Pool,cpu_count

mapUrl = 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile'
def Download( extent ):
    #print extent
    try:
        currentLevel = extent[0]
        dire = r'D:/3Coding/esriimagery/_alllayers/L{0}/'.format(str(currentLevel).zfill(2))
        x=extent[1]
        startY=extent[2]
        endY=extent[3]
        Rdire = dire + 'R' + hex(x).split('x')[1].zfill(8)
        os.makedirs(Rdire)
        for y in range(startY,endY+1):
            try:
                response = urllib.urlopen(mapUrl+'/{0}/{1}/{2}'.format(currentLevel,x,y))
                img=response.read()
                Cdire = Rdire + r'/' + 'C' + '{0}.png'.format(hex(y).split('x')[1].zfill(8))
                with open(Cdire,'wb') as f:
                    f.write(img)
            except Exception as e:
                print e
    except:
        print 'error'
    else:
        return
    #print '{0} done!'.format(x)

if __name__ == '__main__':
    if len(sys.argv) == 7:
        startLevel = int(sys.argv[1])
        endLevel = int(sys.argv[2])
        startX = int(sys.argv[3])
        startY = int(sys.argv[4])
        endX = int(sys.argv[5])
        endY = int(sys.argv[6])

        for level in range(startLevel,endLevel+1):
            currentLevel = level
            GPpool = Pool(25)
            GPpool.map_async(Download, [[currentLevel,x,startY,endY] for x in range(startX,endX+1)])
            GPpool.close()
            GPpool.join()
            print '{0} level is complete!'.format(currentLevel)
            startX = startX*2
            startY = startY*2
            endX = endX*2+1
            endY = endY*2+1
			
#Using:
#python get_online.py startlevel endlevel startx starty endx endy

#Example:
#python get_online.py 8 16 54848 102528 55103 102912
