from abc import ABC

from collections.abc import Iterable

# from .word_scan_result import WordScanResult


class Scanner(ABC):
    

    def scan_audio(self, words: Iterable[str]) -> Iterable[WordScanResult]:
        pass