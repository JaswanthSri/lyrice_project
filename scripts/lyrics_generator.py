from transformers import pipeline

# Load pre-trained model
generator = pipeline('text-generation', model='gpt2')

# Generate lyrics
seed_text = "I am dreaming of the stars tonight"
generated_lyrics = generator(seed_text, max_length=100, num_return_sequences=1)

print("Generated Lyrics:\n", generated_lyrics[0]['generated_text'])
#testing 
#new line
#this is srivatchan testing 