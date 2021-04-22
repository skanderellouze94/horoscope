import cv2
import glob
x=0
astrologicalSigns = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
img_array = []
for sign in astrologicalSigns:
    img_array = []
    for filename in glob.glob('D:\projects\py app\horoscope\photos\\'+sign+'.jpg'):
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        x=size
        img_array.append(img)

    out = cv2.VideoWriter('D:\projects\py app\horoscope\\videos\en\\'+sign+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 200.0, x)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
