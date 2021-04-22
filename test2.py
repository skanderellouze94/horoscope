import moviepy.editor as mp

astrologicalSigns = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
astrologicalSignsFr = ["Belier","Taureau","Gemeaux","Cancer","Lion","Vierge","Balance","Scorpion","Sagittaire","Capricorne","Verseau","Poissons"]
astrologicalSignsEs = ["Aries", "Tauro","geminis","cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]

for sign in astrologicalSigns:
    audio = mp.AudioFileClip('D:\projects\py app\horoscope\sounds\en\\'+sign+'.mp3')
    video1 = mp.VideoFileClip('D:\projects\py app\horoscope\Galaxy.mp4')
    final = video1.set_audio(audio)
    final.write_videofile('D:\projects\py app\horoscope\\result\en\\'+sign+'.mp4',codec= 'mpeg4' ,audio_codec='libvorbis')

for sign in astrologicalSignsFr:
    audio = mp.AudioFileClip('D:\projects\py app\horoscope\sounds\\fr\\'+sign+'.mp3')
    video1 = mp.VideoFileClip('D:\projects\py app\horoscope\Galaxy.mp4')
    final = video1.set_audio(audio)
    final.write_videofile('D:\projects\py app\horoscope\\result\\fr\\'+sign+'.mp4',codec= 'mpeg4' ,audio_codec='libvorbis')

for sign in astrologicalSignsEs:
    audio = mp.AudioFileClip('D:\projects\py app\horoscope\sounds\\es\\'+sign+'.mp3')
    video1 = mp.VideoFileClip('D:\projects\py app\horoscope\Galaxy.mp4')
    final = video1.set_audio(audio)
    final.write_videofile('D:\projects\py app\horoscope\\result\\es\\'+sign+'.mp4',codec= 'mpeg4' ,audio_codec='libvorbis')
