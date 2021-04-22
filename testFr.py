import cv2
import glob
x=0
astrologicalSignsFr = ["Belier","Taureau","Gemeaux","Cancer","Lion","Vierge","Balance","Scorpion","Sagittaire","Capricorne","Verseau","Poissons"]
img_array = []
for sign in astrologicalSignsFr:
    img_array = []
    for filename in glob.glob('D:\projects\py app\horoscope\photos\\'+sign+'.jpg'):
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        x=size
        img_array.append(img)

    out = cv2.VideoWriter('D:\projects\py app\horoscope\\videos\\fr\\'+sign+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 200.0, x)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()