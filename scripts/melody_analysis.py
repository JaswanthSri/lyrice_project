import librosa
import librosa.display
import numpy as np
from lyrics_generator import generated_lyrics

def analyze_melody(audio_file):
    try:
        # Check if the audio file exists
        import os
        if not os.path.exists(audio_file):
            print(f"Error: The file {audio_file} was not found.")
            return None

        # Load the audio file
        y, sr = librosa.load(audio_file)
        print("Audio file successfully loaded.")

        # Analyze tempo
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        print(f"Detected Tempo: {tempo} BPM")

        # Analyze key (approximation using chroma)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = np.argmax(np.sum(chroma, axis=1))
        key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        detected_key = key_names[key_index]
        print(f"Detected Key: {detected_key}")

        # Analyze rhythm (approximation using onset strength)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        rhythm_complexity = np.mean(onset_env)
        print(f"Estimated Rhythm Complexity: {rhythm_complexity}")

        # Package melody analysis results
        melody_data = {
            "tempo": tempo,
            "key": detected_key,
            "rhythm_complexity": rhythm_complexity
        }

        return melody_data

    except Exception as e:
        print(f"An error occurred while analyzing the melody: {e}")
        return None


if __name__ == "__main__":
    # Specify the audio file
    audio_file = r"D:\\Jaswanth\\lyrics_project\\audio\\song.mp3"

    # Step 1: Analyze the melody
    melody_data = analyze_melody(audio_file)
    if melody_data:
        print("Melody Analysis Complete:")
        print(melody_data)

        # Step 2: Generate lyrics based on melody
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM

            # Initialize tokenizer and model
            tokenizer = AutoTokenizer.from_pretrained("gpt2")
            model = AutoModelForCausalLM.from_pretrained("gpt2")

            # Convert melody data into a prompt for lyrics generation
            melody_prompt = f"Generate lyrics for a melody with tempo {melody_data['tempo']} BPM, key {melody_data['key']}, and rhythm complexity {melody_data['rhythm_complexity']:.2f}:"

            # Tokenize input with truncation enabled
            inputs = tokenizer(melody_prompt, return_tensors="pt", max_length=50, truncation=True)

            # Generate lyrics
            outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)
            generated_lyrics = tokenizer.decode(outputs[0], skip_special_tokens=True)

            print("\nGenerated Lyrics:")
            print(generated_lyrics)

            # Save the generated lyrics to a file
            with open("output/generated_lyrics.txt", "w") as f:
                f.write(generated_lyrics)
            print("\nLyrics saved to output/generated_lyrics.txt")

        except Exception as e:
            print(f"An error occurred during lyrics generation: {e}")