
# Imports the Google Cloud client library
from google.cloud import speech


# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://speech-api-test-2344/Greetings and Introductions Basic.mp3"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    # encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))