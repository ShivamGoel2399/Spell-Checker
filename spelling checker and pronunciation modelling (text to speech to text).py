from gtts import gTTS
import os
#from textblob import TextBlob
mylist = "ni10"
corrected_list = ""

language = 'en' 
myobj = gTTS(text=mylist, lang=language, slow=False)
myobj.save("welcome.mp3") 
os.system("mpg321 welcome.mp3")

'''corrected_list=TextBlob(mylist)
print("Corrected list of words are :")
print(corrected_list.correct())'''

from pydub import AudioSegment
sound = AudioSegment.from_mp3("welcome.mp3")
sound.export("welcome.wav", format="wav")

import speech_recognition as sr
filename = "welcome.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language='en-US', show_all=True)
    print(text)

assumed_words=[]
for i in range(len(text['alternative'])):
    assumed_words.append(text['alternative'][i]['transcript'])
print(assumed_words)

with open("names.txt","r+") as f:
    x=f.readlines()
    original_words=[]
    for i in x:
        original_words.append(i.strip())
for a in assumed_words:
    #print(a)
    #print(original_words)
    if a in original_words:
        print(a)
        break;
else:
    print("Not Found")
