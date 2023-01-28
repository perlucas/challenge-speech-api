from abc import ABC, abstractmethod
from domain.audio.audio import Audio
from domain.audio.audio_transcription import AudioTranscription
from google.cloud import speech

class AudioTranscriber(ABC):

    def __init__(self):
        self._config = {}

    def set_config(self, config):
        self._config = config

    @abstractmethod
    def transcribe(self, audio: Audio) -> AudioTranscription:
        pass


class GoogleSpeechAPITranscriber(AudioTranscriber):

    def __init__(self):
        AudioTranscriber.__init__(self)
        self.__client = speech.SpeechClient()

    def transcribe(self, audio: Audio) -> AudioTranscription:
        audio.prepare_transcriber(self)

        config = speech.RecognitionConfig(
            **self._config,
            enable_word_time_offsets=True 
        )

        audio_input = speech.RecognitionAudio(uri=audio.uri())

        response = self.__client.recognize(config=config, audio=audio_input)

        return AudioTranscription.from_speech_api_result(response)