from googletrans import Translator

astrologicalSignsFr = ["Belier","Taureau","Gemeaux","Cancer","Lion","Vierge","Balance","Scorpion","Sagittaire","Capricorne","Verseau","Poissons"]
translator = Translator()

for a in astrologicalSignsFr:
    print(translator.translate(a,src='fr', dest='es'))
    print(translator.translate(a,src='fr', dest='pt'))
    print(translator.translate(a,src='fr', dest='zh-CN'))
