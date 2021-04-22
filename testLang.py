import os

from gtts import gTTS

myobj = gTTS(text='hola soy un skander', lang='es', slow=False)
myobj.save("%s.mp3" % os.path.join("D:\projects\py app\horoscope\sounds",'testesp'))

myobj = gTTS(text='你好，我是溜冰者', lang='zh-CN', slow=False)
myobj.save("%s.mp3" % os.path.join("D:\projects\py app\horoscope\sounds",'testch'))