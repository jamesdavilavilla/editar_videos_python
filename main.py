from story_generator import generate_stories
from voice_generator import generate_voice
from video_editor import create_video

print("🔄 Generando historias...")
stories = generate_stories(3)

for idx, story in enumerate(stories):
    print(f"🎙️  Procesando historia {idx + 1}")
    audio_path, sentences = generate_voice(story, idx)
    create_video(audio_path, sentences, idx)

print("✅ 3 videos generados en la carpeta 'output'")
