from domain.audio.word_match_result import WordMatchResult

def format_zeros(number: int) -> str:
    template = "0{}" if number < 10 else "{}"
    return template.format(number)

def second_timestamp_to_string(ts: float) -> str:
    hours, minutes, seconds = 0, 0, 0
    milliseconds = int((ts * 10) % 10)
    while ts >= 3600:
        hours += 1
        ts -= 3600
    while ts >= 60:
        minutes += 1
        ts -= 60
    seconds = int(ts)
    return "{}:{}:{}.{}".format(
        format_zeros(hours),
        format_zeros(minutes),
        format_zeros(seconds),
        milliseconds
    )


class WordTimestamp:
    
    def __init__(self, word: str, seconds: float):
        self.__word = word
        self.__ts = seconds

    def word(self) -> str:
        return self.__word

    def timestamp(self) -> str:
        return second_timestamp_to_string(self.__ts)


class AudioTranscription:
    
    def __init__(self, word_timestamps: list):
        self.__timestamps = word_timestamps

    def from_speech_api_result(speech_result):
        word_timestamps = []

        for result in speech_result.results:
            alternative = result.alternatives[0]
            for word_info in alternative.words:
                word_timestamps.append(
                    WordTimestamp(word=word_info.word, seconds=word_info.start_time.total_seconds())
                )
        return AudioTranscription(word_timestamps)

    
    def compute_word_matches(self, words: list):
        result = WordMatchResult(words)
        for ts in self.__timestamps:
            result.add_word_timestamp(ts)
        return result

