import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Generate speech
text = "Bharath is crazy. he puts lot of scene and is not understanding of your kashtam kaalam"
engine.save_to_file(text, 'lyrics_audio.mp3')
engine.runAndWait()
