from pydub import AudioSegment
import speech_recognition as sr

# Load the audio file
audio_path = "C:/Users/ROBERT MBOGNI/Downloads/WhatsApp Ptt 2024-08-27 at 10.01.52 AM.ogg"

audio = AudioSegment.from_ogg(audio_path)

# Save the audio in WAV format for processing
wav_path = "C:/Users/ROBERT MBOGNI/Downloads/WhatsApp_Ptt.wav"
audio.export(wav_path, format="wav")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio into the recognizer
with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)

# Transcribe the audio to text
text = recognizer.recognize_google(audio_data)
text
