from melody_analysis import analyze_melody
from lyrics_generator import generate_lyrics

# Input file
audio_file = "audio/song.mp3"

# Step 1: Analyze the melody
melody_data = analyze_melody(audio_file)
print("Melody Analysis Complete:", melody_data)

# Step 2: Generate lyrics
generated_lyrics = generate_lyrics(melody_data)
print("\nGenerated Lyrics:")
print(generated_lyrics)

# Save lyrics to a file
with open("output/generated_lyrics.txt", "w") as f:
    f.write(generated_lyrics)
