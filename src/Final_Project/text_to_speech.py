import os
import playsound
import pyttsx3
from gtts import gTTS
from IPython.display import Audio

def text_to_speech(text, lang='pt-br'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_file = "text_to_speech.wav"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)
    except Exception as e:
        print(f"Erro ao gerar o áudio com gTTS: {e}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    
