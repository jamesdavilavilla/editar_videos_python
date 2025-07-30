from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import os

def create_video(audio_path, sentences, idx):
    bg_path = "gameplay/minecraft_sample.mp4"
    if not os.path.exists(bg_path):
        print(" No hay gameplay en /gameplay/. Añade un video .mp4 llamado 'minecraft_sample.mp4'")
        return

    audio = AudioFileClip(audio_path)
    video = VideoFileClip(bg_path).subclip(0, audio.duration).resize((1080, 1920))
    video = video.set_audio(audio)

    clips = []
    dur = audio.duration / len(sentences)
    for i, sentence in enumerate(sentences):
        txt = TextClip(sentence, fontsize=48, color='white', size=(1000, None)).set_position("center")
        txt = txt.set_start(i * dur).set_duration(dur)
        clips.append(txt)

    final = CompositeVideoClip([video] + clips)
    final.write_videofile(f"output/video_{idx}.mp4", fps=24)
