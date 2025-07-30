from gtts import gTTS
import os

def generate_voice(sentences, idx):
    text = " ".join(sentences)
    tts = gTTS(text=text, lang='es')
    filename = f"output/audio_{idx}.mp3"
    tts.save(filename)
    return filename, sentences
