from selenium import webdriver
import time
from gtts import gTTS
import os


urlEn = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/"
urlFr = "https://www.elle.fr/Astro/Horoscope/Quotidien/"
urlEs = "https://www.lecturas.com/horoscopo/"
astrologicalSignsEn = {"aries":"","taurus":"","gemini":"","cancer":"","leo":"","virgo":"","libra":"","scorpio":"","sagittarius":"","capricorn":"","aquarius":"","pisces":""}
astrologicalSignsFr = {"Belier":"","Taureau":"","Gemeaux":"","Cancer":"","Lion":"","Vierge":"","Balance":"","Scorpion":"","Sagittaire":"","Capricorne":"","Verseau":"","Poissons":""}
astrologicalSignsEs = {"Aries": "", "Tauro": "","geminis":"","cancer":"","Leo":"","Virgo":"","Libra":"","Escorpio":"","Sagitario":"","Capricornio":"","Acuario":"","Piscis ":""}


browser = webdriver.Chrome('D:\projects\py app\chromedriver\chromedriver.exe')

for sign in astrologicalSignsEs:
    browser.get(urlEs + sign)
    time.sleep(1)
    astrologicalSignsEs[sign] = browser.find_element_by_xpath("/html/body/form/main/div[1]/section/div/div[2]/div/div[2]/p").text

for sign in astrologicalSignsEn:
    browser.get(urlEn+sign)
    time.sleep(1)
    astrologicalSignsEn[sign]=browser.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/p").text

for sign in astrologicalSignsFr:
    browser.get(urlFr+sign)
    time.sleep(1)
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[2]/button[2]').click()
    except:
        pass
    time.sleep(1)
    astrologicalSignsFr[sign]=browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[1]").text+ browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[2]").text + browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[3]").text + browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[4]").text + browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[5]").text + browser.find_element_by_xpath("/html/body/section/div/div/div[3]/div[1]/div[2]/div/p[6]").text


for sign in astrologicalSignsEn:
    myobj = gTTS(text=astrologicalSignsEn[sign], lang='en', slow=False)
    myobj.save("%s.mp3" % os.path.join("D:\projects\py app\horoscope\sounds\en",sign))

for sign in astrologicalSignsFr:
    myobj = gTTS(text=astrologicalSignsFr[sign], lang='fr', slow=False)
    myobj.save("%s.mp3" % os.path.join("D:\projects\py app\horoscope\sounds\\fr",sign))

for sign in astrologicalSignsEs:
    myobj = gTTS(text=astrologicalSignsEs[sign], lang='es', slow=False)
    myobj.save("%s.mp3" % os.path.join("D:\projects\py app\horoscope\sounds\\es",sign))

print(astrologicalSignsEn)
print(astrologicalSignsFr)
print(astrologicalSignsEs)
