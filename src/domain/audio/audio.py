from abc import ABC, abstractmethod

class Audio(ABC):

    def __init__(self, uri: str):
        self.__uri = uri

    def uri(self) -> str:
        return self.__uri

    @abstractmethod
    def prepare_transcriber(self, transcriber):
        pass




class GoogleBucketAudio(Audio):

    def __init__(self, uri: str, rate_hertz=16000, language="en-US"):
        Audio.__init__(self, uri)
        self.__rate_hertz = rate_hertz
        self.__language_code = language

    def prepare_transcriber(self, transcriber):
        transcriber.set_config({
            "sample_rate_hertz": 16000,
            "language_code": "en-US",
        })